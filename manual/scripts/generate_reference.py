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
from migrate_from_sphinx import rst_title, rst_toctree_index, title_of  # noqa: E402
from myst_to_vitepress import convert  # noqa: E402

# HTML the API Markdown may contain on purpose; any other "<" outside code is text (e.g. Robot<T>).
ALLOWED_TAG = re.compile(r"<(?:a\s|/a>|br\s*/?>|/?(?:sub|sup|code|em|strong|span|div|img|table|thead|tbody|tr|td|th)[\s>/])")
FENCE = re.compile(r"^\s*(```|~~~)")
DOCSTRING_SECTION = re.compile(
    r"(?m)^#{3,6} (Examples?|Notes?|Parameters|Returns?|Raises|Yields|See Also|Warnings?|References|Attributes)\s*$")


def _escape_text(segment: str) -> str:
    out, i = [], 0
    while i < len(segment):
        if segment[i] == "<" and not ALLOWED_TAG.match(segment, i):
            out.append("&lt;")
        else:
            out.append(segment[i])
        i += 1
    return "".join(out)


def vue_safe(markdown: str) -> str:
    """Escape text that the Vue template compiler would read as elements; mark the page v-pre."""
    lines, in_fence = [], False
    for line in markdown.splitlines():
        if FENCE.match(line):
            in_fence = not in_fence
            lines.append(line)
            continue
        if in_fence:
            lines.append(line)
            continue
        if line.startswith("#"):
            # Links inside headings (e.g. template arguments) confuse heading anchors and the
            # search index (duplicate ids); keep only the link text there.
            line = re.sub(r"\[([^\]]+)\]\(#[^)]*\)", r"\1", line)
        parts = re.split(r"(`+[^`]*`+)", line)  # keep inline code untouched (markdown-it escapes it)
        lines.append("".join(p if p.startswith("`") else _escape_text(p) for p in parts))
    body = "\n".join(lines)
    # Docstring sections (Examples, Notes, ...) are headings in the export; as headings they would fill
    # the page outline with repeated entries, so they become bold paragraphs.
    body = DOCSTRING_SECTION.sub(r"**\1**", body)
    # `{{ }}` would be evaluated by Vue; v-pre turns interpolation off for the whole page.
    # Outline: classes (###) and their members (####).
    return f"---\noutline: [2, 4]\n---\n\n::: v-pre\n{body}\n:::\n"


def export_api(tmp: Path) -> None:
    out = tmp / "md"
    cmd = [sys.executable, "-m", "sphinx", "-b", "markdown", "-q", "-j", "auto",
           "-d", str(tmp / "doctrees"), str(DOC / "source"), str(out)]
    print("[api]", " ".join(cmd))
    subprocess.run(cmd, check=True)
    for lang in ("python", "cpp"):
        dst = MANUAL / "sdk" / lang
        if dst.exists():
            shutil.rmtree(dst)
        for md in (out / "sdk" / lang).rglob("*.md"):
            target = dst / md.relative_to(out / "sdk" / lang)
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(vue_safe(md.read_text()))
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
        target.write_text(convert(md.read_text()))
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
