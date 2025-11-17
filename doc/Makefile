# Minimal makefile for Sphinx documentation

# ------------------------------------------------------------------------------
# Sphinx 기본 설정
# ------------------------------------------------------------------------------
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR      = source
BUILDDIR       = build

# ------------------------------------------------------------------------------
# SDK 버전별 빌드 설정 (버전 폴더 출력 + external SDK 태그 고정)
# ------------------------------------------------------------------------------
SDK_TAG ?= dev

REPO_ROOT        := $(abspath $(CURDIR)/..)
EXTERNAL_SDK_DIR := $(REPO_ROOT)/external/rby1-sdk

OUTDIR       = $(BUILDDIR)/html/$(SDK_TAG)
DOCTREES_DIR = $(BUILDDIR)/doctrees-$(SDK_TAG)

# ------------------------------------------------------------------------------
# Python / pip
# ------------------------------------------------------------------------------
PYTHON ?= python3
PIP    ?= $(PYTHON) -m pip

# 커밋 캐시 파일(여기에 마지막 설치한 커밋을 저장)
STAMPS_DIR        := $(BUILDDIR)/.stamps
SDK_COMMIT_FILE   := $(STAMPS_DIR)/rby1-sdk.commit

# ------------------------------------------------------------------------------
# protoc-gen-doc (Docker)
# ------------------------------------------------------------------------------
DOCKER        ?= docker
PROTOC_IMAGE  ?= pseudomuto/protoc-gen-doc:latest
PROTO_SRC     ?= $(abspath $(CURDIR)/../external/rby1-sdk/protos)
PROTO_OUT_DIR ?= $(CURDIR)/$(SOURCEDIR)/sdk/protos/generated
PROTO_DOC_NAME ?= protos.md
PROTO_GLOB    ?= rb/api/*.proto

# ------------------------------------------------------------------------------
# Doxygen (C++)
# ------------------------------------------------------------------------------
DOXYFILE        ?= $(CURDIR)/Doxyfile
DOXYGEN_XML_DIR ?= $(CURDIR)/build/doxygen/xml

# ------------------------------------------------------------------------------
# PHONY
# ------------------------------------------------------------------------------
.PHONY: help protoc-doc clean-proto doxygen-doc clean-doxygen \
        html html-version sdk-pin sdk-install clean clean-version

# ------------------------------------------------------------------------------
# Help
# ------------------------------------------------------------------------------
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
	@echo
	@echo "Extra targets:"
	@echo "  html              Build docs for SDK_TAG into build/html/SDK_TAG (versioned)"
	@echo "  clean             Clean Sphinx build + generated artifacts"
	@echo "  clean-version     Clean only current SDK_TAG outputs"
	@echo "  protoc-doc        Generate Markdown docs from .proto using Docker"
	@echo "  clean-proto       Remove generated proto docs"
	@echo "  doxygen-doc       Generate Doxygen XML"
	@echo "  clean-doxygen     Remove Doxygen outputs"
	@echo
	@echo "Variables:"
	@echo "  SDK_TAG=v0.9.0 (default)"
	@echo "  PROTO_SRC=...             # Path to rby1-sdk/protos"
	@echo "  PROTO_GLOB=rb/api/*.proto # Which protos to include"

# ------------------------------------------------------------------------------
# Generate proto docs (Docker)
# ------------------------------------------------------------------------------
protoc-doc:
	@mkdir -p "$(PROTO_OUT_DIR)"
	@echo "[protoc-doc] Using PROTO_SRC=$(PROTO_SRC)"
	@echo "[protoc-doc] Writing to $(PROTO_OUT_DIR)/$(PROTO_DOC_NAME)"
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
# Doxygen (C++) via container
# ------------------------------------------------------------------------------
doxygen-doc:
	@echo "[doxygen] Using DOXYFILE=$(DOXYFILE)"
	@echo "[doxygen] Writing to DOXYGEN_XML_DIR=$(DOXYGEN_XML_DIR)"
	@$(DOCKER) run --rm \
	  -v "$(CURDIR):/data" \
	  -v "$(CURDIR)/../external:/external" \
	  nakatt/doxygen

clean-doxygen:
	@echo "[doxygen] Removing $(DOXYGEN_XML_DIR)"
	@rm -rf "$(DOXYGEN_XML_DIR)"

# ------------------------------------------------------------------------------
# SDK 태그 고정 (submodule fetch & checkout)
# ------------------------------------------------------------------------------
sdk-pin:
	@echo "[sdk-pin] Using EXTERNAL_SDK_DIR=$(EXTERNAL_SDK_DIR)"
	@git -C "$(REPO_ROOT)" submodule update --init --recursive external/rby1-sdk
	@git -C "$(EXTERNAL_SDK_DIR)" fetch --tags --prune
	@git -C "$(EXTERNAL_SDK_DIR)" checkout --recurse-submodules "$(SDK_TAG)"
	@echo "[sdk-pin] Checked out $(SDK_TAG)"

# ------------------------------------------------------------------------------
# SDK 설치 (Poetry 백엔드 호환: 일반 설치) — 커밋 비교로 스킵
# ------------------------------------------------------------------------------
sdk-install: sdk-pin
	@mkdir -p "$(STAMPS_DIR)"
	@CUR_COMMIT=$$(git -C "$(EXTERNAL_SDK_DIR)" rev-parse --short=12 HEAD 2>/dev/null || echo unknown); \
	if [ -f "$(SDK_COMMIT_FILE)" ] && [ "$$(cat $(SDK_COMMIT_FILE))" = "$$CUR_COMMIT" ]; then \
		echo "[sdk-install] skip (rby1-sdk @ $$CUR_COMMIT already installed)"; \
	else \
		echo "[sdk-install] installing rby1-sdk @ $(SDK_TAG) (commit $$CUR_COMMIT)"; \
		$(PIP) install --no-deps "$(EXTERNAL_SDK_DIR)"; \
		echo "$$CUR_COMMIT" > "$(SDK_COMMIT_FILE)"; \
	fi

# ------------------------------------------------------------------------------
# Versioned HTML build
# ------------------------------------------------------------------------------
html: html-version

html-version: sdk-pin sdk-install protoc-doc doxygen-doc
	@echo "[sphinx] Build SDK_TAG=$(SDK_TAG) -> $(OUTDIR)"
	@mkdir -p "$(OUTDIR)"
	@SDK_VERSION=$(SDK_TAG) \
	  $(SPHINXBUILD) -b html -d "$(DOCTREES_DIR)" "$(SOURCEDIR)" "$(OUTDIR)" $(SPHINXOPTS)

# ------------------------------------------------------------------------------
# Clean
# ------------------------------------------------------------------------------
clean: clean-proto clean-doxygen
	@$(SPHINXBUILD) -M clean "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

clean-version:
	@echo "[clean-version] Removing $(OUTDIR) and $(DOCTREES_DIR)"
	@rm -rf "$(OUTDIR)" "$(DOCTREES_DIR)"

# ------------------------------------------------------------------------------
# Catch-all
# ------------------------------------------------------------------------------
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
