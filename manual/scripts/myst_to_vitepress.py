#!/usr/bin/env python3
"""Convert a MyST (Sphinx) Markdown page to VitePress Markdown.

Handles the MyST constructs used in the RB-Y1 manual:
  ```{image}/{figure} path + options     -> ![alt](/images/...)
  ```{note|tip|important|warning|caution} -> ::: info|tip|warning|warning|warning
  :::{admonition} Title + :class: x      -> ::: info Title
  `````{grid} / ````{grid-item}          -> contents kept, wrappers dropped
  ```{include} file                       -> <!--@include: file-->
  ```{toctree}                            -> removed (VitePress uses the sidebar config)
  {doc}`text <path>`                      -> [text](path)
Images under _static/images/ are referenced from /images/ (copy them to manual/public/images/).

Usage: myst_to_vitepress.py SRC.md DST.md
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ADMONITION = {"note": "info", "tip": "tip", "important": "warning", "warning": "warning",
              "caution": "warning", "danger": "danger", "hint": "tip", "seealso": "info"}
FENCE_OPEN = re.compile(r"^(\s*)(`{3,}|:{3,}) ?\{([a-z-]+)\}\s*(.*)$")


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


def convert(text: str) -> str:
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
        # Find the matching closing fence (same characters, same or longer run).
        j = i + 1
        close = re.compile(rf"^\s*{re.escape(fence[0])}{{{len(fence)},}}\s*$")
        depth = 0
        while j < len(lines):
            if FENCE_OPEN.match(lines[j]) and FENCE_OPEN.match(lines[j]).group(2) == fence:
                depth += 1
            elif close.match(lines[j]):
                if depth == 0:
                    break
                depth -= 1
            j += 1
        body = [l[len(indent):] if l.startswith(indent) else l for l in lines[i + 1:j]]
        opts, content = _split_options(body)
        i = j + 1

        if name in ("image", "figure"):
            alt = opts.get("alt", "")
            out.append(f"{indent}![{alt}]({_image_path(arg)})")
            caption = "\n".join(content).strip()
            if name == "figure" and caption:
                out.append(f"{indent}*{caption}*")
        elif name in ADMONITION or name == "admonition":
            kind = ADMONITION.get(name) or ADMONITION.get(opts.get("class", "note"), "info")
            title = arg if name == "admonition" else arg
            inner = convert("\n".join(content)).splitlines()
            out.append(f"{indent}::: {kind}{(' ' + title) if title else ''}")
            out.extend(f"{indent}{l}" if l else "" for l in inner)
            out.append(f"{indent}:::")
        elif name == "grid-item-card" and opts.get("link"):
            # Linked card -> one item of a card list (styled as a grid by .link-cards in the theme).
            link = opts["link"] + (".md" if opts.get("link-type") == "doc" else "")
            text = " ".join(l.strip() for l in content if l.strip())
            out.append(f"{indent}- [**{arg}**]({link})<br>{text}")
        elif name == "grid":
            inner = convert("\n".join(content)).splitlines()
            cards = any(l.lstrip().startswith("- [**") for l in inner)
            if cards:
                out.append(f'{indent}<div class="link-cards">')
                out.append("")
            out.extend(f"{indent}{l}" if l else "" for l in inner)
            if cards:
                out.append("")
                out.append(f"{indent}</div>")
        elif name in ("grid-item", "grid-item-card"):
            if name == "grid-item-card" and arg:
                out.append(f"{indent}**{arg}**")
            out.extend(f"{indent}{l}" if l else "" for l in convert("\n".join(content)).splitlines())
        elif name == "math":
            # Rendered by VitePress markdown.math (MathJax); MyST allows the formula on the fence line.
            formula = "\n".join(l for l in ([arg] + content) if l.strip())
            out.extend([f"{indent}$$", *(f"{indent}{l}" for l in formula.splitlines()), f"{indent}$$"])
        elif name == "raw":
            out.extend(f"{indent}{l}" for l in content)
        elif name == "include":
            out.append(f"{indent}<!--@include: {arg}-->")
        elif name == "toctree":
            continue
        else:
            out.append(f"{indent}{fence}{name} {arg}".rstrip())
            out.extend(f"{indent}{l}" for l in body)
            out.append(f"{indent}{fence}")
    result = "\n".join(out)
    result = re.sub(r"\{doc\}`([^<`]+?)\s*<([^>]+)>`", r"[\1](\2)", result)
    result = re.sub(r"\n<br>\n", "\n", result)
    # MyST target labels "(name)=" become HTML anchors.
    result = re.sub(r"(?m)^\(([A-Za-z0-9_.-]+)\)=\s*$", r'<a id="\1"></a>', result)
    # Links to reStructuredText pages: the VitePress site has a Markdown page at the same path.
    result = re.sub(r"\]\(([^)#\s]+)\.rst(#[^)]*)?\)", r"](\1.md\2)", result)
    # Plain Markdown images/links into _static: served from the public folder.
    result = re.sub(r"\]\((?:\.\./)*/?_static/((?:images|videos)/[^)\s]+)\)", r"](/\1)", result)
    # Media in raw HTML: public files need the site base, which only $withBase knows.
    result = re.sub(r'\b(src|href)="(?:\.\./)*_static/((?:images|videos)/[^"]+)"',
                    lambda m: f":{m.group(1)}=\"$withBase('/{m.group(2)}')\"", result)
    result = re.sub(r"\n{3,}", "\n\n", result)
    return result.strip() + "\n"


def main() -> None:
    src, dst = Path(sys.argv[1]), Path(sys.argv[2])
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(convert(src.read_text()))
    print(f"[myst→vitepress] {src} -> {dst}")


if __name__ == "__main__":
    main()
