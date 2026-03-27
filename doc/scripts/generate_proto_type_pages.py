#!/usr/bin/env python3
from __future__ import annotations

import re
import shutil
from pathlib import Path
import os
import json
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
GENERATED_DIR = ROOT / "source" / "sdk" / "protos" / "generated"
PROTOS_MD = GENERATED_DIR / "protos.md"
TYPE_INDEX_RST = GENERATED_DIR / "proto_types.rst"
SCALAR_FILE_SLUG = "scalar-value-types"
DESCRIPTION_PATH = ROOT / "source" / "sdk" / "protos" / "command_descriptions.json"

LABEL_LINE = re.compile(r"^\(([^)]+)\)=\s*$")
PROTO_HEADING = re.compile(r"^##\s+(rb/api/[^\s]+\.proto)\s*$")
TYPE_HEADING = re.compile(r"^###\s+(.+?)\s*$")
LOCAL_ANCHOR_LINK = re.compile(
    r"\[(?P<text>[^\]]+)\]\(#(?P<anchor>rb-api-[^)#\s]+|rb_api-[^)#\s]+)\)"
)
SCALAR_LINK = re.compile(r"\[(?P<text>[^\]]+)\]\(#(?P<anchor>scalar-value-types)\)")
GOOGLE_PROTO_LINK = re.compile(r"\[google\.protobuf\.([A-Za-z0-9_]+)\]\([^)]+\)")


def slugify(name: str) -> str:
    slug = name.strip().lower()
    slug = slug.replace(".", "-")
    slug = re.sub(r"[^a-z0-9_-]+", "-", slug)
    slug = re.sub(r"-{2,}", "-", slug).strip("-")
    return slug or "type"


def normalize_anchor(anchor: str) -> str:
    return anchor.strip().lower()


def _proto_dir_from_path(proto_path: str) -> str:
    # proto_path is like rb/api/arm_command.proto
    name = proto_path.rsplit("/", 1)[-1]
    return name.replace(".proto", "")


def _rel_link(from_dir: Path, to_path: Path, anchor: str) -> str:
    rel = Path(os.path.relpath(to_path, from_dir))
    return f"{rel.as_posix()}#{anchor}"


def rewrite_local_links(
    text: str,
    anchor_to_target: dict[str, dict[str, str]],
    current_proto_dir: Path,
) -> str:
    def _repl(match: re.Match[str]) -> str:
        label = match.group("text")
        anchor = normalize_anchor(match.group("anchor"))
        target = anchor_to_target.get(anchor)
        if not target:
            return label
        target_path = Path(target["path"])
        link = _rel_link(current_proto_dir, target_path, anchor)
        return f"[{label}]({link})"

    def _scalar_repl(match: re.Match[str]) -> str:
        label = match.group("text")
        anchor = normalize_anchor(match.group("anchor"))
        target_path = GENERATED_DIR / f"{SCALAR_FILE_SLUG}.md"
        link = _rel_link(current_proto_dir, target_path, anchor)
        return f"[{label}]({link})"

    text = LOCAL_ANCHOR_LINK.sub(_repl, text)
    text = SCALAR_LINK.sub(_scalar_repl, text)
    def _google_repl(match: re.Match[str]) -> str:
        typename = match.group(1)
        anchor = typename.lower()
        return f"[google.protobuf.{typename}](https://protobuf.dev/reference/protobuf/google.protobuf/#{anchor})"
    text = GOOGLE_PROTO_LINK.sub(_google_repl, text)
    return text


def parse_type_blocks(src: str) -> list[dict[str, Any]]:
    lines = src.splitlines()
    i = 0
    current_proto = ""
    out: list[dict[str, Any]] = []

    while i < len(lines):
        label_match = LABEL_LINE.match(lines[i].strip())
        if not label_match:
            i += 1
            continue

        label = normalize_anchor(label_match.group(1))

        if i + 1 < len(lines):
            proto_match = PROTO_HEADING.match(lines[i + 1].strip())
            if proto_match:
                current_proto = proto_match.group(1)

        if i + 1 >= len(lines):
            i += 1
            continue

        heading_match = TYPE_HEADING.match(lines[i + 1].strip())
        if not heading_match:
            i += 1
            continue

        type_name = heading_match.group(1).strip()
        start = i
        j = i + 2
        while j < len(lines):
            if LABEL_LINE.match(lines[j].strip()):
                break
            j += 1

        block = "\n".join(lines[start:j]).strip() + "\n"
        out.append(
            {
                "name": type_name,
                "label": label,
                "proto": current_proto,
                "proto_dir": _proto_dir_from_path(current_proto),
                "block": block,
            }
        )
        i = j

    return out


def extract_scalar_section(src: str) -> str:
    lines = src.splitlines()
    start = None
    for idx, line in enumerate(lines):
        if line.strip().lower() == "(scalar-value-types)=":
            start = idx
            break

    if start is None:
        return ""

    block = "\n".join(lines[start:]).strip() + "\n"
    return block


def load_descriptions() -> dict[str, str]:
    if not DESCRIPTION_PATH.exists():
        return {}
    return json.loads(DESCRIPTION_PATH.read_text(encoding="utf-8"))


def describe_type(name: str, desc_map: dict[str, str]) -> str:
    if name in desc_map:
        return desc_map[name]
    for suffix in ("Request", "Response", "Feedback"):
        if name.endswith(f".{suffix}"):
            base = name.rsplit(".", 1)[0]
            if base in desc_map:
                return f"{suffix} payload for {base}."
    return ""


def _strip_self_heading(block: str, label: str, name: str) -> str:
    lines = block.splitlines()
    out: list[str] = []
    i = 0
    removed = False
    while i < len(lines):
        if not removed and lines[i].strip().lower() == f"({label})=":
            if i + 1 < len(lines) and lines[i + 1].strip().lower() == f"### {name}".lower():
                i += 2
                removed = True
                continue
        out.append(lines[i])
        i += 1
    return "\n".join(out).strip() + "\n"


def build_type_page(entry: dict[str, Any]) -> str:
    current_dir = entry["out_dir"]
    block = rewrite_local_links(entry["block"], entry["anchor_to_target"], current_dir)
    block = _strip_self_heading(block, entry["label"], entry["name"])
    description = entry.get("description", "")
    children = entry.get("children") or []
    child_section = ""
    if children:
        lines = ["", "## Subtypes", ""]
        for child in children:
            child_path = (current_dir / f"{child['slug']}.md").relative_to(current_dir)
            lines.append(
                f"- [{child['name']}]({child_path.as_posix()}#{child['label']})"
            )
        lines.append("")
        child_section = "\n".join(lines)
    parts = [
        f"# {entry['name']}\n\n",
        f"- Source proto: `{entry['proto']}`\n",
        "\n",
    ]
    if description:
        parts.append(f"{description}\n\n")
    if child_section:
        parts.append(child_section)
    parts.append(block)
    return "".join(parts)


def build_scalar_page(block: str, anchor_to_target: dict[str, dict[str, str]]) -> str:
    rewritten = rewrite_local_links(block, anchor_to_target, GENERATED_DIR)
    return (
        "# Scalar Value Types\n\n"
        f"{rewritten}"
    )


def main() -> None:
    if not PROTOS_MD.exists():
        raise FileNotFoundError(f"Cannot find {PROTOS_MD}")

    src = PROTOS_MD.read_text(encoding="utf-8")
    entries = parse_type_blocks(src)
    entries.sort(key=lambda x: x["name"].lower())
    scalar_block = extract_scalar_section(src)
    desc_map = load_descriptions()

    # Anchor -> target path for cross-page links.
    anchor_to_target: dict[str, dict[str, str]] = {}
    for e in entries:
        proto_dir = GENERATED_DIR / e["proto_dir"]
        anchor_to_target[e["label"]] = {
            "path": str(proto_dir / f"{slugify(e['name'])}.md")
        }
    if scalar_block:
        anchor_to_target["scalar-value-types"] = {
            "path": str(GENERATED_DIR / f"{SCALAR_FILE_SLUG}.md")
        }

    toctree_lines: list[str] = []
    # Build parent -> children map (e.g., ArmCommand -> ArmCommand.Feedback)
    by_name = {e["name"]: e for e in entries}
    children_map: dict[str, list[dict[str, str]]] = {}
    children_seen: dict[str, set[str]] = {}
    for e in entries:
        if "." in e["name"]:
            parent = e["name"].split(".", 1)[0]
            if parent in by_name:
                seen = children_seen.setdefault(parent, set())
                if e["name"] in seen:
                    continue
                seen.add(e["name"])
                children_map.setdefault(parent, []).append(
                    {
                        "name": e["name"],
                        "slug": slugify(e["name"]),
                        "label": e["label"],
                        "proto_dir": e["proto_dir"],
                    }
                )
    for k in children_map:
        children_map[k].sort(key=lambda x: x["name"].lower())

    per_proto: dict[str, list[dict[str, str]]] = {}
    for e in entries:
        proto_dir = GENERATED_DIR / e["proto_dir"]
        proto_dir.mkdir(parents=True, exist_ok=True)
        e["anchor_to_target"] = anchor_to_target
        e["out_dir"] = proto_dir
        e["description"] = describe_type(e["name"], desc_map)
        # Keep only children within same proto and only Request/Response/Feedback
        allowed_suffixes = {"Request", "Response", "Feedback"}
        children = [
            c
            for c in children_map.get(e["name"], [])
            if c["proto_dir"] == e["proto_dir"]
            and c["name"].split(".")[-1] in allowed_suffixes
        ]
        e["children"] = children
        md = Path(anchor_to_target[e["label"]]["path"])
        md.write_text(build_type_page(e), encoding="utf-8")
        per_proto.setdefault(e["proto_dir"], []).append(e)

    if scalar_block:
        scalar_path = GENERATED_DIR / f"{SCALAR_FILE_SLUG}.md"
        scalar_path.write_text(build_scalar_page(scalar_block, anchor_to_target), encoding="utf-8")

    # Per-proto index pages and full type index
    for proto_dir, items in per_proto.items():
        index_path = GENERATED_DIR / proto_dir / "index.rst"
        items.sort(key=lambda x: x["name"].lower())
        title = proto_dir.replace("_", " ").title().replace(" ", "")
        entries_toctree = [slugify(item["name"]) for item in items]
        content = "\n".join(
            [
                title,
                "=" * len(title),
                "",
                ".. toctree::",
                "   :maxdepth: 1",
                "",
            ]
            + [f"   {name}" for name in entries_toctree]
        )
        index_path.write_text(content, encoding="utf-8")

    # Full type index (best-effort; skip if not writable)
    try:
        TYPE_INDEX_RST.write_text(
            "\n".join(
                [
                    "Protobuf Types",
                    "==============",
                    "",
                    ".. toctree::",
                    "   :maxdepth: 1",
                    "",
                    *sorted(
                        {
                            f"{e['proto_dir']}/{slugify(e['name'])}"
                            for e in entries
                        }
                    ),
                    "",
                ]
            ),
            encoding="utf-8",
        )
    except PermissionError:
        print(f"[proto-types] skipped writing {TYPE_INDEX_RST} (permission denied)")
    print(f"[proto-types] generated {len(entries)} type pages")


if __name__ == "__main__":
    main()
