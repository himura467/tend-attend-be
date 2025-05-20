locals {
  private_cidr = cidrsubnet(var.vpc_cidr, 1, 1)
  subnet_bits  = var.subnet_mask - (split("/", var.vpc_cidr)[1] + 1)
}

data "aws_availability_zones" "available" {
  state = "available"
}

resource "aws_vpc" "this" {
  cidr_block = var.vpc_cidr
}

resource "aws_subnet" "private" {
  count             = length(data.aws_availability_zones.available.names)
  vpc_id            = aws_vpc.this.id
  cidr_block        = cidrsubnet(local.private_cidr, local.subnet_bits, count.index)
  availability_zone = data.aws_availability_zones.available.names[count.index]
}

resource "aws_db_subnet_group" "aurora" {
  name       = "tend-attend-aurora-subnet-group"
  subnet_ids = aws_subnet.private[*].id
}
