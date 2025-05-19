#!/usr/bin/env bash

set -e

ROOT_DIR=$(cd $(dirname $0)/..; pwd)

bash ${ROOT_DIR}/scripts/export-requirements.sh
docker build -f ${ROOT_DIR}/docker/server/Dockerfile -t tend-attend --no-cache --provenance=false . --progress=plain
rm ${ROOT_DIR}/requirements.txt
