resource "aws_lambda_function" "qrcode" {
  function_name = "tend-attend-qrcode-lambda-function"
  role          = aws_iam_role.lambda.arn
  package_type  = "Image"
  image_uri     = "${var.qrcode_ecr_repository_url}:latest"
  architectures = ["x86_64"]
  timeout       = var.qrcode_lambda_timeout
  memory_size   = var.qrcode_lambda_memory_size
  environment {
    variables = {
      DOMAIN_NAME = var.domain_name
    }
  }
  lifecycle {
    ignore_changes = [image_uri]
  }
}

resource "aws_lambda_function_url" "qrcode" {
  function_name      = aws_lambda_function.qrcode.function_name
  authorization_type = "AWS_IAM"
  cors {
    allow_credentials = false
    allow_headers     = []
    allow_methods     = ["GET"]
    allow_origins     = var.allow_origins
    expose_headers    = ["content-type"]
    max_age           = 86400
  }
}
