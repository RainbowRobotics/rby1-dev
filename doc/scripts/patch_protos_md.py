#!/usr/bin/env python3
"""Turn the HTML anchors of protoc-gen-doc markdown into MyST labels (input of generate_proto_type_pages.py).

Usage: patch_protos_md.py generated/protos.md   (edits the file in place; running it twice changes nothing)
"""
import re
import sys
from pathlib import Path

p = Path(sys.argv[1])
s = p.read_text(encoding="utf-8")

# <a name="rb-api-XXX"></a> (or id=) + the next ### heading -> (rb-api-xxx)= label + ### heading
def repl(m):
    anchor = m.group(1).strip()
    heading = m.group(2).strip()
    label = anchor.lower()  # labels are lower case; links are lowered the same way
    return f"({label})=\n### {heading}\n"

s2 = re.sub(
    r'<a\s+(?:name|id)="([^"]+)"></a>\s*\n\s*###\s+([^\n]+)\n',
    repl,
    s
)

# <a name="rb_api_XXX"></a> (or id=) + optional "Top" link + the next ## heading -> (rb_api_xxx)= label + ## heading
def repl_proto(m):
    anchor = m.group(1).strip()
    heading = m.group(2).strip()
    label = anchor.lower()
    return f"({label})=\n## {heading}\n"

s2 = re.sub(
    r'<a\s+(?:name|id)="(rb_api_[^"]+)"></a>\s*\n'
    r'(?:<p\s+align="right">\s*<a\s+href="#top">Top</a>\s*</p>\s*\n\s*)?'
    r'##\s+([^\n]+)\n?',
    repl_proto,
    s2
)

# Scalar types: all links go to the one "Scalar Value Types" section.
SCALAR_TYPES = [
    "double", "float",
    "int32", "int64", "uint32", "uint64",
    "sint32", "sint64",
    "fixed32", "fixed64",
    "sfixed32", "sfixed64",
    "bool", "string", "bytes"
]

# Label the "Scalar Value Types" section.
if "(scalar-value-types)=" not in s2:
    s2 = s2.replace(
        "## Scalar Value Types",
        "(scalar-value-types)=\n## Scalar Value Types",
        1
    )

# Remove the HTML anchors in the scalar table.
for t in SCALAR_TYPES:
    s2 = re.sub(
        rf'<a\s+name="{t}"\s*/>\s*{t}',
        t,
        s2
    )

# [double](#double) -> [double](#scalar-value-types)
for t in SCALAR_TYPES:
    s2 = re.sub(
        rf'\[{t}\]\(#\s*{t}\)',
        f'[{t}](#scalar-value-types)',
        s2
    )


p.write_text(s2, encoding="utf-8")
print(f"[patch-protos] patched {p}")
