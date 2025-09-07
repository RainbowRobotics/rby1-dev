# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = build

# ------------------------------------------------------------------------------
# protoc-gen-doc (Docker) settings
# ------------------------------------------------------------------------------
DOCKER              ?= docker
PROTOC_IMAGE        ?= pseudomuto/protoc-gen-doc:latest

# rby1-sdk proto 소스 경로 (문서 레포 기준 상대경로: ../external/rby1-sdk/protos)
# 필요 시: make html PROTO_SRC=/abs/path/to/rby1-sdk/protos
PROTO_SRC           ?= $(abspath $(CURDIR)/../external/rby1-sdk/protos)

# 생성물(md) 출력 디렉토리와 파일명
PROTO_OUT_DIR       ?= $(CURDIR)/$(SOURCEDIR)/sdk/protos/generated
PROTO_DOC_NAME      ?= protos.md

# 어떤 proto들을 문서화할지 (기본: rb/api/*.proto)
# 전체를 원하면: make html PROTO_GLOB='**/*.proto'
PROTO_GLOB          ?= rb/api/*.proto

# ------------------------------------------------------------------------------
# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
	@echo
	@echo "Extra targets:"
	@echo "  protoc-doc     Generate Markdown docs from .proto using Docker (protoc-gen-doc)"
	@echo "  clean-proto    Remove generated proto docs"

.PHONY: help Makefile protoc-doc clean-proto doxygen-doc clean-doxygen

# ------------------------------------------------------------------------------
# Generate proto docs (Docker)
# - mounts:
#   $(PROTO_OUT_DIR) -> /out
#   $(PROTO_SRC)     -> /protos
# - shell:
#   bash -lc 'shopt -s globstar nullglob; protoc ... /protos/$(PROTO_GLOB)'
#   (globstar로 **/*.proto 같은 패턴도 확장 가능)
# ------------------------------------------------------------------------------
protoc-doc:
	@mkdir -p "$(PROTO_OUT_DIR)"
	@echo "[protoc-doc] Using PROTO_SRC=$(PROTO_SRC)"
	@echo "[protoc-doc] Writing to   PROTO_OUT_DIR=$(PROTO_OUT_DIR)/$(PROTO_DOC_NAME)"
	@$(DOCKER) run --rm \
	  -v "$(PROTO_OUT_DIR):/out" \
	  -v "$(PROTO_SRC):/protos" \
	  --entrypoint '' \
	  $(PROTOC_IMAGE) \
	  bash -lc 'shopt -s globstar nullglob; \
	    protoc -I /protos \
	      --doc_out=/out \
	      --doc_opt=markdown,$(PROTO_DOC_NAME) \
	      /protos/$(PROTO_GLOB)'

clean-proto:
	@echo "[clean-proto] Removing $(PROTO_OUT_DIR)/$(PROTO_DOC_NAME)"
	@rm -f "$(PROTO_OUT_DIR)/$(PROTO_DOC_NAME)"

# ------------------------------------------------------------------------------
# Doxygen (C++) settings
# ------------------------------------------------------------------------------
DOXYGEN           ?= doxygen
DOXYFILE          ?= $(CURDIR)/Doxyfile
DOXYGEN_XML_DIR   ?= $(CURDIR)/build/doxygen/xml

doxygen-doc:
	@echo "[doxygen] Using DOXYFILE=$(DOXYFILE)"
	@$(DOXYGEN) "$(DOXYFILE)"
	@echo "[doxygen] XML generated at $(DOXYGEN_XML_DIR)"

clean-doxygen:
	@echo "[doxygen] Removing $(DOXYGEN_XML_DIR)"
	@rm -rf "$(DOXYGEN_XML_DIR)"

# ------------------------------------------------------------------------------
# Sphinx "make mode" (default catch-all)
# ------------------------------------------------------------------------------

# html 빌드 전에 proto 문서를 자동 생성하고 싶다면, html 규칙을 래핑합니다.
# (이 규칙이 있으면 아래의 catch-all 대신 이 규칙이 실행됩니다)
html: protoc-doc doxygen-doc
	@$(SPHINXBUILD) -M html "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

clean: clean-proto clean-doxygen
	@$(SPHINXBUILD) -M clean "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

# 다른 타깃(dirhtml 등)은 필요하면 같은 방식으로 감싸세요.
# 예) dirhtml: protoc-doc
#       @$(SPHINXBUILD) -M dirhtml "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
