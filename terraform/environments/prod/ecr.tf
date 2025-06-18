module "ecr" {
  source                   = "../../modules/ecr"
  qrcode_server_repository = "tend-attend-qrcode"
}
