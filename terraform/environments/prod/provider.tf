terraform {
  required_version = "1.10.2"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "5.81.0"
    }
    google = {
      source  = "hashicorp/google"
      version = "6.42.0"
    }
    google-beta = {
      source  = "hashicorp/google-beta"
      version = "6.42.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

provider "aws" {
  alias  = "us_east_1"
  region = "us-east-1"
}

provider "google" {
  project = var.google_project_id
  region  = var.google_region
}

provider "google-beta" {
  project = var.google_project_id
  region  = var.google_region
}

data "google_project" "this" {
  project_id = var.google_project_id
}
