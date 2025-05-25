terraform {
  required_version = "1.10.2"
  required_providers {
    aws = {
      source  = "hashicorp/google"
      version = "6.31.1"
    }
  }
}

provider "google" {
  project = var.google_project_id
  region  = var.google_region
}
