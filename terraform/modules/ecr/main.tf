resource "aws_ecr_repository" "tend_attend_repo" {
  name         = var.server_repository
  force_delete = true
}

resource "terraform_data" "docker_push" {
  triggers_replace = [timestamp()]
  provisioner "local-exec" {
    command = <<EOF
      echo "Logging in to Amazon ECR..."
      aws ecr get-login-password --region ${var.aws_region} | docker login --username AWS --password-stdin ${aws_ecr_repository.tend_attend_repo.repository_url}

      echo "Tagging ${var.server_repository} image..."
      docker tag ${var.server_repository}:latest ${aws_ecr_repository.tend_attend_repo.repository_url}:latest

      echo "Pushing ${var.server_repository} image to Amazon ECR..."
      docker push ${aws_ecr_repository.tend_attend_repo.repository_url}:latest
    EOF
  }
  depends_on = [aws_ecr_repository.tend_attend_repo]
}

resource "time_sleep" "wait_for_push" {
  depends_on      = [terraform_data.docker_push]
  create_duration = "30s"
}
