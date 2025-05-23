#!/usr/bin/env bash

set -e

if [[ $# -ne 2 ]]; then
  echo "Usage: $0 <aws-profile> <environment>"
  exit 1
fi

export AWS_PROFILE=$1

ROOT_DIR=$(cd $(dirname $0)/..; pwd)

cd $ROOT_DIR/terraform/environments/$2

terraform init
# Force update of Lambda function by targeting the source_code_hash
terraform apply -replace="module.lambda.aws_lambda_function.this"
