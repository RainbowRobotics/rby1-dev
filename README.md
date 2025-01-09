# RBY1-DEV


## Protoc
[Protoc](https://github.com/protocolbuffers/protobuf/releases/tag/v21.12)

### protoc-gen-doc
```bash
# Ubuntu
sudo apt update
sudo apt install golang -y

# Mac
brew install go

go version

# 환경변수 zshrc or bashrc
echo 'export PATH=$PATH:$HOME/go/bin' >> ~/.zshrc
source ~/.zshrc

go install github.com/pseudomuto/protoc-gen-doc/cmd/protoc-gen-doc@latest

protoc-gen-doc --version

# rby1-sdk/protos 위치에서 실행
../../protoc-21.12/bin/protoc -I=. --doc_out=../../docs/development/rby1-sdk/protos --doc_opt=markdown,protos.md rb/api/*.proto
```

```bash
# 일반적인 클론: 전체 레포 가져옴
git clone https://github.com/example/large-repo.git

# sparse-checkout: 특정 폴더만 가져옴
git clone --no-checkout https://github.com/example/large-repo.git
cd large-repo
git sparse-checkout init
git sparse-checkout set docs/ src/
git checkout main
```