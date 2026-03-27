#!/usr/bin/env python3
import re
import sys
from pathlib import Path

p = Path(sys.argv[1])
s = p.read_text(encoding="utf-8")

# <a name="rb-api-XXX"></a> (또는 id) + 다음 ### 헤딩을
# (rb-api-xxx)= 라벨 + ### 헤딩으로 변환
def repl(m):
    anchor = m.group(1).strip()
    heading = m.group(2).strip()
    label = anchor.lower()   # 정규화 이슈 방지
    return f"({label})=\n### {heading}\n"

s2 = re.sub(
    r'<a\s+(?:name|id)="([^"]+)"></a>\s*\n\s*###\s+([^\n]+)\n',
    repl,
    s
)

# <a name="rb_api_XXX"></a> (또는 id) + 중간 Top 링크 + 다음 ## 헤딩을
# (rb_api_xxx)= 라벨 + ## 헤딩으로 변환
def repl_proto(m):
    anchor = m.group(1).strip()
    heading = m.group(2).strip()
    label = anchor.lower()   # 정규화
    return f"({label})=\n## {heading}\n"

s2 = re.sub(
    r'<a\s+(?:name|id)="(rb_api_[^"]+)"></a>\s*\n'
    r'(?:<p\s+align="right">\s*<a\s+href="#top">Top</a>\s*</p>\s*\n\s*)?'
    r'##\s+([^\n]+)\n?',
    repl_proto,
    s2
)

### google protobuf type


#### Scalar type 
SCALAR_TYPES = [
    "double", "float",
    "int32", "int64", "uint32", "uint64",
    "sint32", "sint64",
    "fixed32", "fixed64",
    "sfixed32", "sfixed64",
    "bool", "string", "bytes"
]

# 1️⃣ Add label before "Scalar Value Types"
if "(scalar-value-types)=" not in s2:
    s2 = s2.replace(
        "## Scalar Value Types",
        "(scalar-value-types)=\n## Scalar Value Types",
        1
    )

# 2️⃣ Remove HTML anchors in scalar table
for t in SCALAR_TYPES:
    s2 = re.sub(
        rf'<a\s+name="{t}"\s*/>\s*{t}',
        t,
        s2
    )

# 3️⃣ Replace links like [double](#double) → [double](#scalar-value-types)
for t in SCALAR_TYPES:
    s2 = re.sub(
        rf'\[{t}\]\(#\s*{t}\)',
        f'[{t}](#scalar-value-types)',
        s2
    )


p.write_text(s2, encoding="utf-8")
print(f"[patch-protos] patched {p}")
