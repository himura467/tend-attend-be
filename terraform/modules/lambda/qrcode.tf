resource "aws_s3_bucket" "qrcode_dependencies_layer" {
  bucket = "tend-attend-lambda-qrcode-dependencies-layer"
}

resource "aws_s3_object" "qrcode_dependencies_layer" {
  bucket = aws_s3_bucket.qrcode_dependencies_layer.id
  key    = "qrcode-dependencies.zip"
  source = "../../../qrcode-dependencies.zip"
  etag   = filemd5("../../../qrcode-dependencies.zip")
}

resource "aws_lambda_layer_version" "qrcode_dependencies" {
  layer_name          = "QRCodeDependencies"
  compatible_runtimes = ["nodejs22.x"]
  s3_bucket           = aws_s3_bucket.qrcode_dependencies_layer.id
  s3_key              = aws_s3_object.qrcode_dependencies_layer.key
  source_code_hash    = filebase64sha256("../../../qrcode-dependencies.zip")
}

resource "aws_lambda_function" "qrcode" {
  function_name    = "tend-attend-qrcode-lambda-function"
  role             = aws_iam_role.lambda.arn
  filename         = "../../../qrcode.zip"
  source_code_hash = filebase64sha256("../../../qrcode.zip")
  handler          = "dist/index.handler"
  runtime          = "nodejs22.x"
  layers           = [aws_lambda_layer_version.qrcode_dependencies.arn]
  timeout          = var.qrcode_lambda_timeout
  memory_size      = var.qrcode_lambda_memory_size
  vpc_config {
    subnet_ids         = var.subnet_ids
    security_group_ids = var.security_group_ids
  }
}

resource "aws_lambda_function_url" "qrcode" {
  function_name      = aws_lambda_function.qrcode.function_name
  authorization_type = "AWS_IAM"
  cors {
    allow_credentials = false
    allow_headers     = ["content-type"]
    allow_methods     = ["GET"]
    allow_origins     = var.allow_origins
    expose_headers    = []
    max_age           = 86400
  }
}
