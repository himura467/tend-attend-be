module "route53" {
  source      = "../../modules/route53"
  domain_name = "aws.${module.op.domain_name}"
  providers = {
    aws           = aws
    aws.us_east_1 = aws.us_east_1
  }
}
