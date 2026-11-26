#!/usr/bin/env python3
"""Generate the reference pages of the VitePress site from the SDK.

Outputs (all git-ignored, rebuilt on every site build):
  manual/sdk/python/, manual/sdk/cpp/   API pages: Sphinx (autodoc + breathe) exported as Markdown
  manual/public/sdk/cpp/raw-api/        Doxygen HTML, linked from the C++ "Full API" page
  manual/sdk/protos/generated/          proto pages converted from doc/source/sdk/protos/generated
  manual/hardware/generated/            joint range / speed tables from the SDK URDF models

Needs: the SDK installed in the Python environment (`pip install rby1-sdk==<tag>`) and the Doxygen
XML in doc/build/doxygen/xml (`make -C doc doxygen-doc`).

Usage: python3 manual/scripts/generate_reference.py [--skip-api]
"""
from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
MANUAL = HERE.parent
REPO = MANUAL.parent
DOC = REPO / "doc"
sys.path.insert(0, str(HERE))
from rst_index import rst_toctree_index, title_of  # noqa: E402
from myst_to_vitepress import convert  # noqa: E402

# HTML the API Markdown may contain on purpose; any other "<" outside code is text (e.g. Robot<T>).
ALLOWED_TAG = re.compile(r"<(?:a\s|/a>|br\s*/?>|/?(?:sub|sup|code|em|strong|span|div|img|table|thead|tbody|tr|td|th)[\s>/])")
FENCE = re.compile(r"^\s*(```|~~~)")
DOCSTRING_SECTION = re.compile(
    r"(?m)^#{3,6} (Examples?|Notes?|Parameters|Returns?|Raises|Yields|See Also|Warnings?|References|Attributes)\s*$")


SPHINX_ADMONITION = {"NOTE": ("info", "Note"), "SEE ALSO": ("info", "See also"), "TIP": ("tip", "Tip"),
                     "WARNING": ("warning", ""), "IMPORTANT": ("warning", "Important"),
                     "CAUTION": ("warning", "Caution"), "DEPRECATED": ("danger", "Deprecated"),
                     "DANGER": ("danger", "Danger")}
SPHINX_ADMONITION_HEADING = re.compile(r"^#{3,6} (NOTE|SEE ALSO|TIP|WARNING|IMPORTANT|CAUTION|DANGER|Deprecated.*)\s*$", re.I)
MATH = re.compile(r"(\$\$.+?\$\$|\$[^$\s][^$]*?\$)")


def _escape_text(segment: str) -> str:
    out, i = [], 0
    while i < len(segment):
        if segment[i] == "<" and not ALLOWED_TAG.match(segment, i):
            out.append("&lt;")
        else:
            out.append(segment[i])
        i += 1
    return "".join(out)


def _unescape_math(math: str) -> str:
    """The Markdown export escapes "*", "_" and "\\" inside formulas (q^\\*, ^\\\\top); MathJax needs them raw."""
    return re.sub(r"\\([*_\\])", r"\1", math)


def _escape_line(line: str) -> str:
    """Escape "<" in text, leaving inline code and $math$ untouched."""
    parts = re.split(r"(`+[^`]*`+)", line)
    out = []
    for p in parts:
        if p.startswith("`"):
            out.append(p)
        else:
            out.append("".join(_unescape_math(q) if MATH.fullmatch(q) else _escape_text(q) for q in MATH.split(p)))
    return "".join(out)


def _admonitions(lines: list[str]) -> list[str]:
    """Sphinx note/warning boxes come out as "#### NOTE" + paragraphs; make them VitePress containers."""
    out, open_box, has_text = [], False, False
    for line in lines:
        m = SPHINX_ADMONITION_HEADING.match(line)
        # The box holds one paragraph: it ends at the first blank line after its text,
        # or earlier at a heading/anchor.
        ends_box = open_box and (line.startswith(("#", "<a id=", "**")) or (has_text and not line.strip()))
        if ends_box or (open_box and m):
            out.extend([":::", ""])
            open_box = False
        if m:
            key = m.group(1).upper()
            kind, title = SPHINX_ADMONITION.get(key, ("danger", m.group(1)))
            out.append(f"::: {kind}{(' ' + title) if title else ''}")
            open_box, has_text = True, False
            continue
        if open_box and line.strip():
            has_text = True
        out.append(line)
    if open_box:
        out.append(":::")
    return out


def _summary_table_headers(lines: list[str]) -> list[str]:
    """Autosummary tables have no header row; the first member would become the header."""
    out, i = [], 0
    while i < len(lines):
        line = lines[i]
        out.append(line)
        if re.match(r"^#{2,6} (Methods|Attributes)\s*$", line) or line in ("**Attributes**",):
            j = i + 1
            while j < len(lines) and not lines[j].strip():
                out.append(lines[j])
                j += 1
            if j + 1 < len(lines) and lines[j].startswith("|") and re.match(r"^\|[-| :]+\|$", lines[j + 1]):
                out.extend(["| Member | Description |", lines[j + 1], lines[j]])
                i = j + 2
                continue
            i = j
            continue
        i += 1
    return out


def tidy_python(markdown: str) -> str:
    """Fix two artifacts of the Markdown export of the Python docstrings."""
    # ":pyattr:`X`" wrongly written roles come out as one-line code blocks inside a sentence.
    markdown = re.sub(r"\n*```\n:py\w+:`([^`]+)`\n```\n*", r" `\1`", markdown)
    markdown = re.sub(r":py\w+:`([^`]+)`", r"`\1`", markdown)
    # Types like "*shape* *(**N* *,* *)*" (one emphasis per token) -> "*shape (N, )*".
    def merge(m: re.Match) -> str:
        text = re.sub(r"\s+", " ", m.group(0).replace("*", "")).replace(" ,", ",").replace("( ", "(").strip()
        return f"*{text}*"
    return re.sub(r"(?:\*{1,2}[^*\n]+?\*{1,2}[ ]?){3,}", merge, markdown)


def tidy_cpp(markdown: str) -> str:
    """C++ pages: member declarations one level below the class and section headings."""
    out, prev = [], ""
    for line in markdown.splitlines():
        if line.startswith("### ") and prev.startswith("<a id="):
            decl = line[4:]
            if not re.match(r"^(template\s*<.*?>\s*)?(class|struct)\s+[\w:]+(\s*[:{]|\s*$|\s+final)", decl) or decl == "struct timestamp":
                line = "#" + line
            # Breathe drops the type of `struct timespec` members (Log::timestamp, RobotState::timestamp).
            if decl == "struct timestamp":
                line = "#### struct timespec timestamp"
        out.append(line)
        if line.strip():
            prev = line
    return "\n".join(out)


def vue_safe(markdown: str) -> str:
    """Escape text that the Vue template compiler would read as elements; mark the page v-pre."""
    lines, in_fence, in_math = [], False, False
    for line in markdown.splitlines():
        if FENCE.match(line):
            in_fence = not in_fence
            lines.append(line)
            continue
        if line.strip() == "$$":
            in_math = not in_math
        if in_fence or in_math or line.strip() == "$$":
            lines.append(line)
            continue
        if line.startswith("#"):
            # Links inside headings (e.g. template arguments) confuse heading anchors and the
            # search index (duplicate ids); keep only the link text there.
            line = re.sub(r"\[([^\]]+)\]\(#[^)]*\)", r"\1", line)
            # "{...}" at the end of a heading would be read as attributes (markdown-it-attrs).
            line = line.replace("{", "&#123;")
            # template<...>class  ->  template<...> class
            line = re.sub(r">(class|struct|static|inline|constexpr|virtual|explicit)\b", r"> \1", line)
        lines.append(_escape_line(line))
    lines = _summary_table_headers(_admonitions(lines))
    body = "\n".join(lines)
    # Docstring sections (Examples, Notes, ...) are headings in the export; as headings they would fill
    # the page outline with repeated entries, so they become bold paragraphs.
    body = DOCSTRING_SECTION.sub(r"**\1**", body)
    # `{{ }}` would be evaluated by Vue; v-pre turns interpolation off for the whole page.
    # Five colons so that the ::: containers inside do not close it. Outline: classes and members.
    # Generated pages have no git history of their own.
    return f"---\noutline: [2, 4]\nlastUpdated: false\n---\n\n::::: v-pre\n{body}\n:::::\n"


def constexpr_members() -> set[str]:
    """Qualified names of constexpr members (the Markdown export drops the keyword)."""
    names = set()
    for xml in (DOC / "build" / "doxygen" / "xml").glob("*.xml"):
        text = xml.read_text(errors="ignore")
        for m in re.finditer(r'<memberdef [^>]*constexpr="yes"[^>]*>.*?<qualifiedname>([^<]+)</qualifiedname>', text, re.S):
            names.add(m.group(1))
    return names


def restore_constexpr(markdown: str, names: set[str]) -> str:
    out, current = [], None
    for line in markdown.splitlines():
        m = re.match(r'<a id="((?:[A-Za-z_]\w*::)+[A-Za-z_]\w*)(?:__[^"]*)?"></a>', line)
        if m:
            current = m.group(1)
        elif line.startswith("#") and current in names and "constexpr" not in line:
            head, sep, rest = line.partition(" ")
            rest = re.sub(r"^((?:template&lt;.*?>\s*|template<.*?>\s*)?(?:static\s+)?)", r"\1constexpr ", rest, count=1)
            line = f"{head}{sep}{rest}"
            current = None
        out.append(line)
    return "\n".join(out)


def export_api(tmp: Path) -> None:
    out = tmp / "md"
    cmd = [sys.executable, "-m", "sphinx", "-b", "markdown", "-q", "-j", "auto",
           "-d", str(tmp / "doctrees"), str(DOC / "source"), str(out)]
    print("[api]", " ".join(cmd))
    subprocess.run(cmd, check=True)
    constexpr = constexpr_members()
    for lang in ("python", "cpp"):
        dst = MANUAL / "sdk" / lang
        if dst.exists():
            shutil.rmtree(dst)
        for md in (out / "sdk" / lang).rglob("*.md"):
            target = dst / md.relative_to(out / "sdk" / lang)
            target.parent.mkdir(parents=True, exist_ok=True)
            text = md.read_text()
            # Breathe target ids (#rby1-sdkclass...) are not exported; link to the page instead.
            text = re.sub(r"\]\(([^)#\s]*)#rby1-sdk[^)]*\)", lambda m: f"]({m.group(1) or '#'})", text)
            if lang == "python":
                text = tidy_python(text)
            if lang == "cpp":
                text = tidy_cpp(restore_constexpr(text, constexpr))
                # The Doxygen HTML is a static folder: load it as a normal page, not through the router.
                text = re.sub(r"\]\((raw-api/[^)]+)\)", r'](\1){target="_self"}', text)
            target.write_text(vue_safe(text))
        print(f"[api] {lang}: {sum(1 for _ in dst.rglob('*.md'))} pages")

    raw = DOC / "build" / "doxygen" / "html"
    raw_dst = MANUAL / "public" / "sdk" / "cpp" / "raw-api"
    if raw_dst.exists():
        shutil.rmtree(raw_dst)
    if raw.is_dir():
        shutil.copytree(raw, raw_dst)
        print(f"[api] Doxygen HTML -> {raw_dst.relative_to(REPO)}")
    else:
        print("[api] no Doxygen HTML (run `make -C doc doxygen-doc`); raw API links will be dead")


def import_protos() -> None:
    src_root = DOC / "source"
    src = src_root / "sdk" / "protos" / "generated"
    dst = MANUAL / "sdk" / "protos" / "generated"
    if dst.exists():
        shutil.rmtree(dst)
    pages = 0
    for md in src.rglob("*.md"):
        target = dst / md.relative_to(src)
        target.parent.mkdir(parents=True, exist_ok=True)
        # Proto anchors are lower case; links in the generated tables use the type's case.
        text = re.sub(r"\(#(rb-api-[^)]+)\)", lambda m: f"(#{m.group(1).lower()})", convert(md.read_text()))
        # Well-known protobuf types are documented on protobuf.dev, not in these pages.
        text = re.sub(r"\(#google-protobuf-(\w+)\)",
                      lambda m: f"(https://protobuf.dev/reference/protobuf/google.protobuf/#{m.group(1).lower()})", text)
        target.write_text(text)
        pages += 1
    for rst in src.rglob("*.rst"):
        if rst.name == "proto_types.rst":
            continue
        target = (dst / rst.relative_to(src)).with_suffix(".md")
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(rst_toctree_index(rst, src_root))
    # proto_types.rst lists every type page, one per line (not a valid toctree).
    entries = [l.strip() for l in (src / "proto_types.rst").read_text().splitlines()
               if l.strip() and not l.startswith((" ", ".", "=")) and "/" in l]
    lines = ["# Protobuf Types", "", "All message and service types, by proto module.", ""]
    for e in entries:
        page = src / f"{e}.md"
        lines.append(f"- [{title_of(page) if page.exists() else e}](./{e}.md)")
    (dst / "proto_types.md").write_text("\n".join(lines) + "\n")
    print(f"[protos] {pages} pages, {len(entries)} types")


def joint_limits() -> None:
    subprocess.run([sys.executable, str(DOC / "scripts" / "generate_joint_limit_tables.py"),
                    "--sdk", str(REPO / "external" / "rby1-sdk"),
                    "--out", str(MANUAL / "hardware" / "generated")], check=True)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--skip-api", action="store_true", help="only protos and joint tables (no Sphinx run)")
    args = parser.parse_args()
    import_protos()
    joint_limits()
    if not args.skip_api:
        with tempfile.TemporaryDirectory() as tmp:
            export_api(Path(tmp))


if __name__ == "__main__":
    main()
