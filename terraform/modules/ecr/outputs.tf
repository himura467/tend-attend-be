output "repository_url" {
  description = "URL of the Amazon ECR repository"
  value       = aws_ecr_repository.qrcode_server.repository_url
}
