#!/usr/bin/env bash

set -e

ROOT_DIR=$(cd $(dirname $0)/..; pwd)

PYTHON_VERSION=$(cat ${ROOT_DIR}/ta-api/.python-version)

rm -f app.zip
bash ${ROOT_DIR}/scripts/export-requirements.sh
docker build -f ${ROOT_DIR}/docker/server/Dockerfile \
  --build-arg PYTHON_VERSION=${PYTHON_VERSION} \
  --platform linux/amd64 \
  --no-cache \
  --provenance=false \
  -t tend-attend:latest ${ROOT_DIR} --progress=plain
CONTAINER_ID=$(docker create --platform linux/amd64 tend-attend:latest)
docker cp "$CONTAINER_ID":/app ${ROOT_DIR}
docker rm -v "$CONTAINER_ID"
zip --recurse-paths -X app.zip ${ROOT_DIR}/app
rm -rf ${ROOT_DIR}/app
rm ${ROOT_DIR}/requirements.txt
