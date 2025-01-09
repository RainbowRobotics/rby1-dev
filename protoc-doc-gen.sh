#!/bin/bash
set -e

cd rby1-sdk/protos
../../protoc-21.12/bin/protoc -I=. --doc_out=../../docs/development/rby1-sdk/protos --doc_opt=markdown,protos-v.md rb/api/*.proto

cd ../../docs/development/rby1-sdk/protos
python proto_helper.py