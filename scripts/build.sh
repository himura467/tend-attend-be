#!/usr/bin/env bash

set -e

ROOT_DIR=$(cd $(dirname $0)/..; pwd)

PYTHON_VERSION=$(cat ${ROOT_DIR}/ta-api/.python-version)

rm -f python.zip app.zip
bash ${ROOT_DIR}/scripts/export-requirements.sh ta-api
docker build -f ${ROOT_DIR}/docker/server/Dockerfile \
  --build-arg PYTHON_VERSION=${PYTHON_VERSION} \
  --platform linux/amd64 \
  --no-cache \
  --provenance=false \
  -t tend-attend:latest ${ROOT_DIR} --progress=plain
CONTAINER_ID=$(docker create --platform linux/amd64 tend-attend:latest)
docker cp "$CONTAINER_ID":/python ${ROOT_DIR}
docker cp "$CONTAINER_ID":/app ${ROOT_DIR}
docker rm -v "$CONTAINER_ID"
zip --recurse-paths -X python.zip python -x "*/__pycache__/*" -x "*.dist-info/*"
zip --recurse-paths -X app.zip app
rm -rf ${ROOT_DIR}/python ${ROOT_DIR}/app
rm ${ROOT_DIR}/requirements.txt
