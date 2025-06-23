resource "google_project_service" "artifact_registry" {
  project = var.google_project_id
  service = "artifactregistry.googleapis.com"
}

resource "google_artifact_registry_repository" "ml_server" {
  location               = var.google_region
  repository_id          = var.ml_server_repository
  format                 = "DOCKER"
  cleanup_policy_dry_run = false
  docker_config {
    immutable_tags = true
  }
  cleanup_policies {
    id     = "keep-minimum-versions"
    action = "KEEP"
    most_recent_versions {
      keep_count = 2
    }
  }
  cleanup_policies {
    id     = "delete-old-versions"
    action = "DELETE"
    condition {
      tag_state  = "ANY"
      older_than = "24h"
    }
  }
}
