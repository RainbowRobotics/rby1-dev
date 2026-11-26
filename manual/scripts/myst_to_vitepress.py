#!/usr/bin/env python3
"""Convert a MyST (Sphinx) Markdown page to VitePress Markdown.

Handles the MyST constructs used in the RB-Y1 manual (directive names in any case):
  ```{image}/{figure} path + options     -> ![alt](/images/...), or <img> when width/class/align matter
  ```{note|tip|important|warning|...}    -> ::: info|tip|warning ... (original kind kept as the title)
  :::{admonition} Title + :class: x      -> ::: info Title
  `````{grid} + ````{grid-item-card} :link: -> card list (<div class="link-cards">)
  `````{grid} N + grid-item/card (media)  -> <div class="media-grid" style="--cols:N">
  :::{card} Title                         -> titled block
  ```{include} file                       -> <!--@include: file-->
  ```{math}, ```{raw} html, ```{mermaid}  -> $$ ... $$, raw HTML, ```mermaid
  ```{toctree}                            -> removed (VitePress uses the sidebar config)
  {doc}`text <path>`, (label)=            -> [text](path), <a id="label"></a>
Images under _static/images/ are referenced from /images/ (copy them to manual/public/images/).
Unknown directives are kept as they are and reported on stderr.

Usage: myst_to_vitepress.py SRC.md DST.md
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

# MyST admonition -> (VitePress container, title shown when the MyST kind is not the container's own).
ADMONITION = {
    "note": ("info", "Note"), "seealso": ("info", "See also"), "tip": ("tip", "Tip"), "hint": ("tip", "Hint"),
    "important": ("warning", "Important"), "caution": ("warning", "Caution"), "attention": ("warning", "Attention"),
    "warning": ("warning", ""), "danger": ("danger", "Danger"), "error": ("danger", "Error"),
}
FENCE_OPEN = re.compile(r"^(\s*)(`{3,}|:{3,})\s*\{([A-Za-z-]+)\}\s*(.*)$")


def _image_path(path: str) -> str:
    m = re.search(r"_static/images/(.+)$", path)
    return f"/images/{m.group(1)}" if m else path


def _split_options(lines: list[str]) -> tuple[dict[str, str], list[str]]:
    opts, i = {}, 0
    while i < len(lines) and re.match(r"^\s*:[\w-]+:", lines[i]):
        key, _, val = lines[i].strip()[1:].partition(":")
        opts[key] = val.strip()
        i += 1
    return opts, lines[i:]


def _image(arg: str, opts: dict[str, str], in_grid: bool) -> str:
    """Markdown image when no presentation option matters; otherwise <img> that keeps them."""
    path, alt = _image_path(arg), opts.get("alt", "").replace('"', "&quot;")
    classes = {c.replace("_", "-") for c in opts.get("class", "").split()} & {"white-bg", "rounded-img"}
    width = opts.get("width", "")
    style = f"width:{width}" if width and not (in_grid and width == "100%") else ""
    if opts.get("align") == "center" and not in_grid:
        classes.add("center")
    if not classes and not style:
        return f"![{alt}]({path})"
    attrs = [f":src=\"$withBase('{path}')\"", f'alt="{alt}"']
    if classes:
        attrs.append(f'class="{" ".join(sorted(classes))}"')
    if style:
        attrs.append(f'style="{style}"')
    return f"<img {' '.join(attrs)}>"


def _grid_columns(arg: str) -> int:
    nums = [int(n) for n in re.findall(r"\d+", arg)]
    return max(1, nums[-1] if nums else 2)


def convert(text: str, in_grid: bool = False) -> str:
    out: list[str] = []
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        m = FENCE_OPEN.match(lines[i])
        if not m:
            out.append(lines[i])
            i += 1
            continue
        indent, fence, name, arg = m.groups()
        name = name.lower()
        # Find the matching closing fence (same characters, same or longer run).
        j = i + 1
        close = re.compile(rf"^\s*{re.escape(fence[0])}{{{len(fence)},}}\s*$")
        depth = 0
        while j < len(lines):
            inner_open = FENCE_OPEN.match(lines[j])
            if inner_open and inner_open.group(2) == fence:
                depth += 1
            elif close.match(lines[j]):
                if depth == 0:
                    break
                depth -= 1
            j += 1
        body = [l[len(indent):] if l.startswith(indent) else l for l in lines[i + 1:j]]
        opts, content = _split_options(body)
        i = j + 1

        def emit(block: list[str]) -> None:
            out.extend(f"{indent}{l}" if l else "" for l in block)

        if name in ("image", "figure"):
            out.append(f"{indent}{_image(arg, opts, in_grid)}")
            caption = "\n".join(content).strip()
            if name == "figure" and caption:
                out.append("")
                out.append(f"{indent}*{caption}*")
            out.append("")  # an image is a paragraph of its own
        elif name in ADMONITION or name == "admonition":
            if name == "admonition":
                kind = ADMONITION.get(opts.get("class", "note").split()[0], ("info", ""))[0]
                title, first = arg, []
            else:
                kind, title = ADMONITION[name]
                first = [arg] if arg else []  # MyST: text on the fence line is the first body line
            inner = convert("\n".join(first + content)).splitlines()
            out.append(f"{indent}::: {kind}{(' ' + title) if title else ''}")
            emit(inner)
            out.append(f"{indent}:::")
            out.append("")
        elif name == "grid-item-card" and opts.get("link"):
            # Linked card -> one item of a card list (styled as a grid by .link-cards in the theme).
            link = opts["link"] + (".md" if opts.get("link-type") == "doc" else "")
            text = " ".join(l.strip() for l in content if l.strip())
            out.append(f"{indent}- [**{arg}**]({link})<br>{text}")
        elif name == "grid":
            inner = convert("\n".join(content), in_grid=True).splitlines()
            if any(l.lstrip().startswith("- [**") for l in inner):
                out.extend([f'{indent}<div class="link-cards">', ""])
                emit(inner)
                out.extend(["", f"{indent}</div>", ""])
            else:
                out.extend([f'{indent}<div class="media-grid" style="--cols:{_grid_columns(arg)}">', ""])
                emit(inner)
                out.extend(["", f"{indent}</div>", ""])
        elif name in ("grid-item", "grid-item-card", "card"):
            # One cell: a <div> so that its title and media stay together in the grid.
            inner = convert("\n".join(content), in_grid=in_grid).splitlines()
            out.extend([f"{indent}<div>", ""])
            if arg:
                out.extend([f"{indent}**{arg}**", ""])
            emit(inner)
            out.extend(["", f"{indent}</div>", ""])
        elif name == "math":
            # Rendered by VitePress markdown.math (MathJax); MyST allows the formula on the fence line.
            formula = "\n".join(l for l in ([arg] + content) if l.strip())
            out.extend([f"{indent}$$", *(f"{indent}{l}" for l in formula.splitlines()), f"{indent}$$", ""])
        elif name == "raw":
            emit(content)
        elif name == "mermaid":
            out.append(f"{indent}```mermaid")
            emit(content)
            out.append(f"{indent}```")
        elif name == "include":
            out.append(f"{indent}<!--@include: {arg}-->")
        elif name == "toctree":
            continue
        else:
            print(f"[myst→vitepress] unknown directive {{{name}}} kept as is", file=sys.stderr)
            out.append(f"{indent}{fence}{name} {arg}".rstrip())
            out.extend(f"{indent}{l}" for l in body)
            out.append(f"{indent}{fence}")
    result = "\n".join(out)
    result = re.sub(r"\{doc\}`([^<`]+?)\s*<([^>]+)>`", r"[\1](\2)", result)
    # "<br>" lines were used as paragraph spacers.
    result = re.sub(r"(?m)^<br>\s*$", "", result)
    # MyST target labels "(name)=" become HTML anchors.
    result = re.sub(r"(?m)^\(([A-Za-z0-9_.-]+)\)=\s*$", r'<a id="\1"></a>', result)
    # Links to reStructuredText pages: the VitePress site has a Markdown page at the same path.
    result = re.sub(r"\]\(([^)#\s]+)\.rst(#[^)]*)?\)", r"](\1.md\2)", result)
    # Plain Markdown images/links into _static: served from the public folder.
    result = re.sub(r"\]\((?:\.\./)*/?_static/((?:images|videos)/[^)\s]+)\)", r"](/\1)", result)
    # Media in raw HTML: public files need the site base, which only $withBase knows.
    result = re.sub(r'\b(src|href)="(?:\.\./)*_static/((?:images|videos)/[^"]+)"',
                    lambda m: f":{m.group(1)}=\"$withBase('/{m.group(2)}')\"", result)
    # E-mail addresses written as plain href values.
    result = re.sub(r'href="([\w.+-]+@[\w-]+\.[\w.-]+)"', r'href="mailto:\1"', result)
    result = re.sub(r"(/images/[^)\"'\s]*?)//+", r"\1/", result)
    result = re.sub(r"\n{3,}", "\n\n", result)
    return result.strip() + "\n"


def main() -> None:
    src, dst = Path(sys.argv[1]), Path(sys.argv[2])
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(convert(src.read_text()))
    print(f"[myst→vitepress] {src} -> {dst}")


if __name__ == "__main__":
    main()
