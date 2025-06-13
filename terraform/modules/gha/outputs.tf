output "gha_role_arn" {
  value       = aws_iam_role.gha.arn
  description = "ARN of the IAM Role for GitHub Actions"
}
