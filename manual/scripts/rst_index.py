"""Helpers shared by the page scripts: titles of Markdown/rst pages and rst toctree index pages as Markdown."""
from __future__ import annotations

import re
from pathlib import Path


def title_of(md: Path) -> str:
    for line in md.read_text().splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return md.stem


def rst_title(rst: Path) -> str:
    lines = rst.read_text().splitlines()
    for i in range(len(lines) - 1):
        if lines[i].strip() and re.fullmatch(r"[=\-~^]{3,}", lines[i + 1].strip()):
            return lines[i].strip()
    return rst.stem


def rst_toctree_index(rst: Path, src_root: Path) -> str:
    """Title, intro paragraphs and toctree of a simple .rst index page -> Markdown with a link list."""
    lines = rst.read_text().splitlines()
    title = rst_title(rst)
    intro, entries, in_toc, seen_title = [], [], False, False
    for i, line in enumerate(lines):
        s = line.strip()
        if s.startswith(".. toctree::"):
            in_toc = True
            continue
        if in_toc:
            if not s or s.startswith(":"):
                continue
            if line.startswith(" "):
                entries.append(s)
                continue
            in_toc = False
        if s == title:
            seen_title = True
            continue
        if not seen_title or re.fullmatch(r"[=\-~^]{3,}", s) or s.startswith(".. "):
            continue
        intro.append(line)
    out = [f"# {title}", ""] + [l for l in "\n".join(intro).strip().splitlines()] + ([""] if intro else [])
    for e in entries:
        target = rst.parent / e
        md, rs = target.with_suffix(".md"), target.with_suffix(".rst")
        label = title_of(md) if md.exists() else rst_title(rs) if rs.exists() else e
        out.append(f"- [{label}](./{e}.md)")
    return "\n".join(out).rstrip() + "\n"
