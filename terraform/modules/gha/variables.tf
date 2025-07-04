variable "github_org" {
  description = "GitHub organization name"
  type        = string
}

variable "github_repo" {
  description = "GitHub repository name"
  type        = string
}

variable "qrcode_server_ecr_arn" {
  description = "ARN of the ECR repository for QR code server"
  type        = string
}

variable "qrcode_lambda_arn" {
  description = "ARN of the Lambda function for QR code generation"
  type        = string
}

variable "google_project_id" {
  description = "Google Cloud project ID"
  type        = string
}

variable "google_project_number" {
  description = "Google Cloud project number"
  type        = string
}
