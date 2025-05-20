module "route53" {
  source      = "../../modules/route53"
  domain_name = "aws.${var.domain_name}"
}
