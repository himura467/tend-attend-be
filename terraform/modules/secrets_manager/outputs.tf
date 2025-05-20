output "aurora_credentials" {
  description = "Credentials for the Aurora database"
  value       = jsondecode(data.aws_secretsmanager_secret_version.data_aurora_credentials.secret_string)
  sensitive   = true
}
