import re
import tomllib

# pyproject.toml에서 버전 정보 읽기
pyproject_path = "../../../../rby1-sdk/pyproject.toml"
with open(pyproject_path, "rb") as file:  # 'rb' 모드로 읽기
    pyproject_data = tomllib.load(file)

version = pyproject_data["tool"]["poetry"]["version"]

# 원본 파일 읽기
with open("protos-v.md", "r") as file:
    content = file.read()

# HTML 앵커를 VitePress 헤더로 변환하는 함수
def convert_anchors_to_headers(content):
    # a name 태그를 찾아서 헤더로 변환
    content = re.sub(r'<a name="rb-api-(.*?)"></a>', r'## \1 {#rb-api-\1}', content)

    # 언더스코어(_)를 하이픈(-)으로 변환
    content = re.sub(r'_', '-', content)

    return content

# 변환된 내용으로 헤더를 교체
content_modified = convert_anchors_to_headers(content)

# 새로운 파일 이름 생성
new_filename = f"protos-v.md"

# 수정된 파일 저장
with open(new_filename, "w") as file:
    file.write(content_modified)

print(f"version: {version}")
print(f"File saved as {new_filename}")