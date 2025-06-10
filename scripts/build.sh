#!/usr/bin/env bash

set -e

ROOT_DIR=$(cd $(dirname $0)/..; pwd)

# Server build
PYTHON_VERSION=$(cat ${ROOT_DIR}/ta-api/.python-version)
rm -f server-python.zip server.zip server-dependencies.zip
bash ${ROOT_DIR}/scripts/export_requirements.sh ta-api
docker build -f ${ROOT_DIR}/docker/server/Dockerfile \
  --build-arg PYTHON_VERSION=${PYTHON_VERSION} \
  --platform linux/amd64 \
  --no-cache \
  --provenance=false \
  -t tend-attend-server:latest ${ROOT_DIR} --progress=plain
SERVER_CONTAINER_ID=$(docker create --platform linux/amd64 tend-attend-server:latest)
docker cp "$SERVER_CONTAINER_ID":/python ${ROOT_DIR}
docker cp "$SERVER_CONTAINER_ID":/main.py ${ROOT_DIR}
docker cp "$SERVER_CONTAINER_ID":/dependencies ${ROOT_DIR}
docker rm -v "$SERVER_CONTAINER_ID"
zip -r -X server-python.zip python/ -x "*/__pycache__/*"
zip -r -X server.zip main.py
cd dependencies && zip -r -X ../server-dependencies.zip python/ -x "*/__pycache__/*" && cd ..
rm -rf ${ROOT_DIR}/python ${ROOT_DIR}/main.py ${ROOT_DIR}/dependencies ${ROOT_DIR}/requirements.txt

# ML Server build
docker build -f ${ROOT_DIR}/docker/ml-server/Dockerfile \
  --target development \
  --platform linux/amd64 \
  --no-cache \
  --provenance=false \
  -t tend-attend-ml:latest ${ROOT_DIR} --progress=plain

# QR Code Server build
PNPM_VERSION=$(grep -o '"pnpm@[^"]*"' ${ROOT_DIR}/ta-qrcode/package.json | grep -o '[0-9]*\.[0-9]*\.[0-9]*')
docker build -f ${ROOT_DIR}/docker/qrcode-server/Dockerfile \
  --build-arg PNPM_VERSION=${PNPM_VERSION} \
  --platform linux/amd64 \
  --no-cache \
  --provenance=false \
  -t tend-attend-qrcode:latest ${ROOT_DIR} --progress=plain
