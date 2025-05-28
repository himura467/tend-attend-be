output "ml_server_url" {
  description = "The URL of the Cloud Run service for the ML server"
  value       = google_cloud_run_v2_service.ml_server.uri
}
