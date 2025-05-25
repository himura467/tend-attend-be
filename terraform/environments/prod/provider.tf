terraform {
  required_version = "1.10.2"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "5.81.0"
    }
    google = {
      source  = "hashicorp/google"
      version = "6.31.1"
    }
  }
}

provider "aws" {
  profile = var.aws_profile
  region  = var.aws_region
}

provider "google" {
  project = var.google_project_id
  region  = var.google_region
}
