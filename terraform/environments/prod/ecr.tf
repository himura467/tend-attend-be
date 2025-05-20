module "ecr" {
  source            = "../../modules/ecr"
  aws_region        = var.aws_region
  server_repository = "tend-attend-server"
}
