variable "qrcode_server_ecr_arn" {
  description = "ARN of the ECR repository for QR code server"
  type        = string
}

variable "qrcode_lambda_arn" {
  description = "ARN of the Lambda function for QR code generation"
  type        = string
}
