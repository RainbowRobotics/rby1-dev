#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
GENERATED_DIR = ROOT / "source" / "sdk" / "protos" / "generated"
PROTOS_MD = GENERATED_DIR / "protos.md"
OUT_DIR = ROOT / "source" / "sdk" / "protos"

FILE_LINE = re.compile(r"^- \[rb/api/([^\]]+\.proto)\]\([^)]+\)\s*$")


def parse_toc(src: str) -> list[str]:
    files: list[str] = []
    for line in src.splitlines():
        m_file = FILE_LINE.match(line)
        if m_file:
            files.append(m_file.group(1))
    return files


def write_index(proto_dirs: list[str]) -> None:
    lines = [
        ".. _proto_api:",
        "",
        "Protobuf API Reference",
        "======================",
        "",
        "Pick a proto module to see its message groups.",
        "",
        ".. toctree::",
        # "   :hidden:",
        "   :maxdepth: 2",
        "",
    ]
    for d in proto_dirs:
        lines.append(f"   generated/{d}/index")
    lines.append("   generated/scalar-value-types")
    lines.append("")
    (OUT_DIR / "index.rst").write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    if not PROTOS_MD.exists():
        raise FileNotFoundError(f"Cannot find {PROTOS_MD}")

    toc_files = parse_toc(PROTOS_MD.read_text(encoding="utf-8"))
    proto_dirs = sorted({f.replace(".proto", "") for f in toc_files})
    write_index(proto_dirs)


if __name__ == "__main__":
    main()
