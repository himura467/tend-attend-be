output "qrcode_ecr_repository_url" {
  description = "The URL of the ECR repository for the QR code server Lambda function"
  value       = aws_ecr_repository.qrcode_server.repository_url
}
