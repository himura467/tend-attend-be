terraform {
  required_version = "1.10.2"
  backend "s3" {
    profile      = "himura"
    bucket       = "tend-attend-terraform-state"
    key          = "terraform.tfstate"
    region       = "ap-northeast-1"
    acl          = "private"
    encrypt      = true
    use_lockfile = true
  }
}
