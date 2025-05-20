output "repository_url" {
  description = "URL of the Amazon ECR repository"
  value       = aws_ecr_repository.tend_attend_repo.repository_url
}
