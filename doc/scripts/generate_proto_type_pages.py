#!/usr/bin/env python3
"""Split the protoc-gen-doc output into one MyST page per proto type.

Inputs (doc/source/sdk/protos/):
  generated/protos.md      protoc-gen-doc markdown, patched by patch_protos_md.py
  generated/protos.json    protoc-gen-doc json (oneof groups, RPC request/response types)
  command_descriptions.json  {type name: one-paragraph description}
  type_notes.json          extra text per type, see load_notes()

Outputs (doc/source/sdk/protos/generated/):
  <module>/<type>.md, <module>/index.rst, proto_types.rst, scalar-value-types.md, SDK_TAG

manual/scripts/generate_reference.py converts these MyST pages into the VitePress site.
Everything a page says comes from the inputs above, so `make protoc-doc` reproduces the
committed pages exactly; never edit the generated pages by hand.
"""
from __future__ import annotations

import json
import os
import re
import subprocess
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
PROTOS_DIR = ROOT / "source" / "sdk" / "protos"
GENERATED_DIR = PROTOS_DIR / "generated"
PROTOS_MD = GENERATED_DIR / "protos.md"
PROTOS_JSON = GENERATED_DIR / "protos.json"
TYPE_INDEX_RST = GENERATED_DIR / "proto_types.rst"
SDK_TAG_FILE = GENERATED_DIR / "SDK_TAG"
SCALAR_FILE_SLUG = "scalar-value-types"
DESCRIPTION_PATH = PROTOS_DIR / "command_descriptions.json"
NOTES_PATH = PROTOS_DIR / "type_notes.json"
SDK_CHECKOUT = ROOT.parent / "external" / "rby1-sdk"
MANUAL_DIR = ROOT.parent / "manual"
# Where the type pages end up in the site, relative to manual/ (for links to other manual pages).
SITE_GENERATED_DIR = Path("sdk/protos/generated")
SDK_REPO = "https://github.com/RainbowRobotics/rby1-sdk"

LABEL_LINE = re.compile(r"^\(([^)]+)\)=\s*$")
PROTO_HEADING = re.compile(r"^##\s+(rb/api/[^\s]+\.proto)\s*$")
TYPE_HEADING = re.compile(r"^###\s+(.+?)\s*$")
LOCAL_ANCHOR_LINK = re.compile(
    r"\[(?P<text>[^\]]+)\]\(#(?P<anchor>rb-api-[^)#\s]+|rb_api-[^)#\s]+)\)"
)
SCALAR_LINK = re.compile(r"\[(?P<text>[^\]]+)\]\(#(?P<anchor>scalar-value-types)\)")
GOOGLE_PROTO_LINK = re.compile(r"\[google\.protobuf\.([A-Za-z0-9_]+)\]\([^)]+\)")
TABLE_HEADER = re.compile(r"^\|\s*(Field|Name|Method Name)\s*\|")
TABLE_RULE = re.compile(r"^\|[-| :]+\|$")
# MyST admonition kinds a note may use; generate_reference.py turns them into ::: containers.
ADMONITION_KINDS = ("note", "tip", "important", "warning", "danger")


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


def _rel_link(from_dir: Path, to_path: Path) -> str:
    # Each type has its own page, so links point to the page without an anchor.
    return Path(os.path.relpath(to_path, from_dir)).as_posix()


def sdk_tag() -> str:
    """SDK tag the protos come from: $SDK_TAG (make protoc-doc passes it), else the tag the
    external/rby1-sdk checkout is at."""
    if os.environ.get("SDK_TAG"):
        return os.environ["SDK_TAG"]
    result = subprocess.run(
        ["git", "-C", str(SDK_CHECKOUT), "describe", "--tags", "--exact-match"],
        capture_output=True, text=True, check=False,
    )
    if result.returncode != 0:
        raise RuntimeError(f"Set SDK_TAG: {SDK_CHECKOUT} is not checked out at a tag")
    return result.stdout.strip()


def rewrite_local_links(
    text: str,
    anchor_to_target: dict[str, dict[str, str]],
    current_proto_dir: Path,
) -> str:
    def _repl(match: re.Match[str]) -> str:
        label = match.group("text")
        target = anchor_to_target.get(normalize_anchor(match.group("anchor")))
        if not target:
            return label
        return f"[{label}]({_rel_link(current_proto_dir, Path(target['path']))})"

    def _scalar_repl(match: re.Match[str]) -> str:
        label = match.group("text")
        target_path = GENERATED_DIR / f"{SCALAR_FILE_SLUG}.md"
        return f"[{label}]({_rel_link(current_proto_dir, target_path)})"

    def _google_repl(match: re.Match[str]) -> str:
        typename = match.group(1)
        return f"[google.protobuf.{typename}](https://protobuf.dev/reference/protobuf/google.protobuf/#{typename.lower()})"

    text = LOCAL_ANCHOR_LINK.sub(_repl, text)
    text = SCALAR_LINK.sub(_scalar_repl, text)
    return GOOGLE_PROTO_LINK.sub(_google_repl, text)


def join_broken_rows(block: str) -> str:
    """protoc-gen-doc keeps blank lines of multi-paragraph comments inside table cells,
    which ends the Markdown table; join such a row back into one line with <br>."""
    lines = block.splitlines()
    out: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("|") and not line.rstrip().endswith("|"):
            parts = [line.rstrip()]
            i += 1
            while i < len(lines) and not parts[-1].endswith("|"):
                if lines[i].strip():
                    parts.append(lines[i].strip())
                i += 1
            out.append("<br>".join(parts))
            continue
        out.append(line)
        i += 1
    return "\n".join(out) + ("\n" if block.endswith("\n") else "")


def _cells(row: str) -> list[str]:
    return [c.strip() for c in row.strip()[1:-1].split("|")]


def _row(cells: list[str]) -> str:
    return "| " + " | ".join(cells) + " |"


def annotate_tables(block: str, oneofs: dict[str, str], cell_notes: dict[str, str]) -> str:
    """Field tables: label oneof members and apply description overrides.
    Method tables (services): apply description overrides by method name."""
    lines = block.splitlines()
    out: list[str] = []
    kind = ""
    for idx, line in enumerate(lines):
        header = TABLE_HEADER.match(line)
        if header:
            kind = header.group(1)
            out.append(line)
            continue
        if kind and line.startswith("|") and not TABLE_RULE.match(line):
            cells = _cells(line)
            key = cells[0]
            if kind == "Field" and key in oneofs and not cells[2]:
                cells[2] = f"oneof {oneofs[key]}"
            if key in cell_notes and kind in ("Field", "Method Name"):
                cells[-1] = cell_notes[key]
            line = _row(cells) if (key in oneofs or key in cell_notes) else line
        elif not line.startswith("|"):
            kind = ""
        out.append(line)
    return "\n".join(out) + ("\n" if block.endswith("\n") else "")


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
    for idx, line in enumerate(lines):
        if line.strip().lower() == "(scalar-value-types)=":
            return "\n".join(lines[idx:]).strip() + "\n"
    return ""


def load_descriptions() -> dict[str, str]:
    if not DESCRIPTION_PATH.exists():
        return {}
    return json.loads(DESCRIPTION_PATH.read_text(encoding="utf-8"))


def load_notes() -> dict[str, dict[str, Any]]:
    """type_notes.json: {type name: {
         "admonitions": [{"kind": "warning", "text": "..."}],   boxes under the description
         "fields":  {field name: "description"},                replaces the Description cell
         "methods": {rpc name: "description"},                  replaces the Description cell
         "see_also": [{"text": "...", "path": "sdk/....md"}]    path relative to manual/
       }}  Keys starting with "_" are comments."""
    if not NOTES_PATH.exists():
        return {}
    data = json.loads(NOTES_PATH.read_text(encoding="utf-8"))
    notes = {k: v for k, v in data.items() if not k.startswith("_")}
    for name, note in notes.items():
        for box in note.get("admonitions", []):
            if box["kind"] not in ADMONITION_KINDS:
                raise ValueError(f"{NOTES_PATH.name}: {name}: unknown admonition kind {box['kind']!r}")
        for ref in note.get("see_also", []):
            target = MANUAL_DIR / ref["path"]
            source_rst = ROOT / "source" / Path(ref["path"]).with_suffix(".rst")
            if not target.exists() and not source_rst.exists():
                raise FileNotFoundError(f"{NOTES_PATH.name}: {name}: see_also target {ref['path']} not found")
    return notes


def load_descriptor(path: Path) -> dict[str, Any]:
    """Facts the markdown output of protoc-gen-doc does not carry: oneof groups and RPC types."""
    if not path.exists():
        raise FileNotFoundError(f"Cannot find {path} (make protoc-doc writes it with --doc_opt=json)")
    data = json.loads(path.read_text(encoding="utf-8"))
    oneofs: dict[str, dict[str, str]] = {}
    rpcs: dict[str, list[dict[str, str]]] = {}
    services: list[dict[str, Any]] = []
    for f in data["files"]:
        for m in f["messages"]:
            groups = {fd["name"]: fd["oneofdecl"] for fd in m["fields"] if fd.get("isoneof")}
            if groups:
                oneofs[m["longName"]] = groups
        for s in f["services"]:
            services.append({"name": s["longName"], "proto": f["name"], "methods": s["methods"]})
            for meth in s["methods"]:
                for role, key in (("request", "requestLongType"), ("response", "responseLongType")):
                    rpcs.setdefault(meth[key], []).append(
                        {"role": role, "service": s["longName"], "proto": f["name"], "method": meth["name"]}
                    )
    return {"oneofs": oneofs, "rpcs": rpcs, "services": services}


def describe_type(name: str, desc_map: dict[str, str], link_of) -> str:
    if name in desc_map:
        return desc_map[name]
    for suffix in ("Request", "Feedback"):
        if name.endswith(f".{suffix}"):
            base = name.rsplit(".", 1)[0]
            if base in desc_map:
                return f"{suffix} part of [{base}]({link_of(base)})."
    return ""


def oneof_sentence(groups: dict[str, str]) -> str:
    by_group: dict[str, list[str]] = {}
    for field, group in groups.items():
        by_group.setdefault(group, []).append(field)
    sentences = []
    for group, fields in by_group.items():
        listed = ", ".join(f"`{f}`" for f in fields)
        sentences.append(f"Only one field of the `{group}` oneof can be set at a time: {listed}.")
    return " ".join(sentences)


def rpc_sentence(uses: list[dict[str, str]], link_of) -> str:
    parts = []
    for u in uses:
        parts.append(
            f"{u['role'].capitalize()} of the `{u['method']}` RPC of [{u['service']}]({link_of(u['service'])})."
        )
    return " ".join(parts)


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
    note = entry.get("note", {})
    block = rewrite_local_links(entry["block"], entry["anchor_to_target"], current_dir)
    block = _strip_self_heading(block, entry["label"], entry["name"])
    block = join_broken_rows(block)
    block = annotate_tables(block, entry.get("oneofs", {}), {**note.get("fields", {}), **note.get("methods", {})})

    proto_url = f"{SDK_REPO}/blob/{entry['sdk_tag']}/protos/{entry['proto']}"
    parts = [
        f"({entry['label']})=\n",
        f"# {entry['name']}\n\n",
        f"- Source proto: [`{entry['proto']}`]({proto_url}) (rby1-sdk {entry['sdk_tag']})\n",
        "\n",
    ]
    for paragraph in (entry.get("description", ""), entry.get("rpc_text", ""), entry.get("oneof_text", "")):
        if paragraph:
            parts.append(f"{paragraph}\n\n")
    for box in note.get("admonitions", []):
        parts.append(f"```{{{box['kind']}}}\n{box['text']}\n```\n\n")
    see_also = note.get("see_also", [])
    if see_also:
        site_dir = SITE_GENERATED_DIR / entry["proto_dir"]
        links = ", ".join(
            f"[{ref['text']}]({Path(os.path.relpath(ref['path'], site_dir)).as_posix()})" for ref in see_also
        )
        parts.append(f"See also: {links}.\n\n")
    children = entry.get("children") or []
    if children:
        lines = ["", "## Subtypes", ""]
        lines += [f"- [{child['name']}]({child['slug']}.md)" for child in children]
        lines.append("")
        parts.append("\n".join(lines))
    parts.append(block)
    return "".join(parts)


def build_scalar_page(block: str, anchor_to_target: dict[str, dict[str, str]]) -> str:
    rewritten = rewrite_local_links(block, anchor_to_target, GENERATED_DIR)
    # The section heading of protos.md becomes the page title.
    return rewritten.replace("## Scalar Value Types", "# Scalar Value Types", 1)


def main() -> None:
    if not PROTOS_MD.exists():
        raise FileNotFoundError(f"Cannot find {PROTOS_MD}")

    src = PROTOS_MD.read_text(encoding="utf-8")
    entries = parse_type_blocks(src)
    entries.sort(key=lambda x: x["name"].lower())
    scalar_block = extract_scalar_section(src)
    desc_map = load_descriptions()
    notes = load_notes()
    descriptor = load_descriptor(PROTOS_JSON)
    tag = sdk_tag()

    unknown = sorted(set(notes) - {e["name"] for e in entries})
    if unknown:
        raise KeyError(f"{NOTES_PATH.name}: no such proto type: {', '.join(unknown)}")

    # Type name -> page path, for cross-page links.
    anchor_to_target: dict[str, dict[str, str]] = {}
    page_of: dict[str, Path] = {}
    for e in entries:
        page = GENERATED_DIR / e["proto_dir"] / f"{slugify(e['name'])}.md"
        anchor_to_target[e["label"]] = {"path": str(page)}
        page_of[e["name"]] = page
    if scalar_block:
        anchor_to_target["scalar-value-types"] = {"path": str(GENERATED_DIR / f"{SCALAR_FILE_SLUG}.md")}

    # Parent -> Request/Response/Feedback children in the same proto (e.g. ArmCommand -> ArmCommand.Request).
    by_name = {e["name"]: e for e in entries}
    children_map: dict[str, list[dict[str, str]]] = {}
    for e in entries:
        parent, _, suffix = e["name"].partition(".")
        if suffix in {"Request", "Response", "Feedback"} and parent in by_name \
                and by_name[parent]["proto_dir"] == e["proto_dir"]:
            children_map.setdefault(parent, []).append({"name": e["name"], "slug": slugify(e["name"])})
    for k in children_map:
        children_map[k].sort(key=lambda x: x["name"].lower())

    per_proto: dict[str, list[dict[str, Any]]] = {}
    for e in entries:
        proto_dir = GENERATED_DIR / e["proto_dir"]
        proto_dir.mkdir(parents=True, exist_ok=True)

        def link_of(name: str, _from: Path = proto_dir) -> str:
            return _rel_link(_from, page_of[name])

        e.update(
            anchor_to_target=anchor_to_target,
            out_dir=proto_dir,
            sdk_tag=tag,
            description=describe_type(e["name"], desc_map, link_of),
            rpc_text=rpc_sentence(descriptor["rpcs"].get(e["name"], []), link_of),
            oneofs=descriptor["oneofs"].get(e["name"], {}),
            note=notes.get(e["name"], {}),
            children=children_map.get(e["name"], []),
        )
        e["oneof_text"] = oneof_sentence(e["oneofs"]) if e["oneofs"] else ""
        page_of[e["name"]].write_text(build_type_page(e), encoding="utf-8")
        per_proto.setdefault(e["proto_dir"], []).append(e)

    if scalar_block:
        scalar_path = GENERATED_DIR / f"{SCALAR_FILE_SLUG}.md"
        scalar_path.write_text(build_scalar_page(scalar_block, anchor_to_target), encoding="utf-8")

    # Per-proto index pages: titled with the proto file name, so that they differ from the message names.
    service_names = {s["name"] for s in descriptor["services"]}
    for proto_dir, items in per_proto.items():
        index_path = GENERATED_DIR / proto_dir / "index.rst"
        if all(item["name"] in service_names for item in items):
            # Service-only file: manual/sdk/protos/index.md links the service page directly.
            index_path.unlink(missing_ok=True)
            continue
        items.sort(key=lambda x: x["name"].lower())
        title = f"{proto_dir}.proto"
        content = "\n".join(
            [title, "=" * len(title), "", ".. toctree::", "   :maxdepth: 1", ""]
            + [f"   {slugify(item['name'])}" for item in items]
        )
        index_path.write_text(content, encoding="utf-8")

    # Full type index; generate_reference.py turns it into proto_types.md.
    TYPE_INDEX_RST.write_text(
        "\n".join(
            ["Protobuf Types", "==============", "", ".. toctree::", "   :maxdepth: 1", ""]
            + sorted({f"{e['proto_dir']}/{slugify(e['name'])}" for e in entries})
            + [""]
        ),
        encoding="utf-8",
    )
    # Lets the site build check that the committed pages match the SDK tag it documents.
    SDK_TAG_FILE.write_text(f"{tag}\n", encoding="utf-8")
    print(f"[proto-types] generated {len(entries)} type pages from rby1-sdk {tag}")


if __name__ == "__main__":
    main()
