import requests
import os

# GitHub API URL
repo = "RainbowRobotics/rby1-release"  # 저장소 이름
api_url = f"https://api.github.com/repos/{repo}/releases"

# API 요청 보내기
response = requests.get(api_url)

if response.status_code == 200:
    releases = response.json()  # 릴리즈 정보 가져오기

    # 저장할 디렉토리 생성
    output_dir = "release_notes"
    os.makedirs(output_dir, exist_ok=True)

    # 릴리즈 노트 저장
    for release in releases:
        tag_name = release["tag_name"]
        name = release["name"]
        body = release["body"]

        # 마크다운 파일 생성
        file_path = os.path.join(output_dir, f"{tag_name}.md")
        with open(file_path, "w", encoding="utf-8") as md_file:
            md_file.write(f"# {name}\n\n")
            md_file.write(f"## Release Notes\n\n")
            md_file.write(body)

    print(f"Markdown files have been saved in the '{output_dir}' directory.")
else:
    print(f"Failed to fetch releases. Status code: {response.status_code}")