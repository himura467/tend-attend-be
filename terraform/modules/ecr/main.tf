resource "aws_ecr_repository" "qrcode_server" {
  name                 = var.qrcode_server_repository
  force_delete         = true
  image_tag_mutability = "IMMUTABLE"
}
