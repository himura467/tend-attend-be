#!/usr/bin/env bash

set -e

if [[ $# -ne 1 ]]; then
  echo "Usage: $0 <environment>"
  exit 1
fi

ROOT_DIR=$(cd "$(dirname "$0")"/..; pwd)

cd "$ROOT_DIR/terraform/environments/$1"

OP_VAULT_NAME='Tend Attend' OP_APP_ENV='Production' op run --env-file "$ROOT_DIR/terraform/provider.env" -- terraform init
# terraform destroy -target=module.lambda.aws_lambda_function.server
OP_VAULT_NAME='Tend Attend' OP_APP_ENV='Production' op run --env-file "$ROOT_DIR/terraform/provider.env" -- terraform apply
