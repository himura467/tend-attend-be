output "github_org" {
  description = "GitHub organization name"
  value       = local.fields["GitHub Org"]
}

output "github_repo" {
  description = "GitHub repository name"
  value       = local.fields["GitHub Repo"]
}

output "domain_name" {
  description = "Domain name for the application"
  value       = local.fields["Domain Name"]
}

output "jwt_secret_key" {
  description = "JWT secret key used for signing tokens"
  value       = local.fields["JWT Secret Key"]
  sensitive   = true
}

output "db_shard_count" {
  description = "Number of shards for the database"
  value       = local.fields["DB Shard Count"]
}

output "common_dbname" {
  description = "Common database name"
  value       = local.fields["Common DB Name"]
}

output "sequence_dbname" {
  description = "Sequence database name"
  value       = local.fields["Sequence DB Name"]
}

output "shard_dbname_prefix" {
  description = "Prefix for shard database names"
  value       = local.fields["Shard DB Name Prefix"]
}

output "ml_cloud_run_service_name" {
  description = "Cloud Run service name for ML server"
  value       = local.fields["ML Cloud Run Service Name"]
}

output "ml_gar_repository" {
  description = "Google Artifact Registry repository for ML server"
  value       = local.fields["ML GAR Repository"]
}

output "qrcode_ecr_repository" {
  description = "ECR repository for QR code server"
  value       = local.fields["QR Code ECR Repository"]
}
