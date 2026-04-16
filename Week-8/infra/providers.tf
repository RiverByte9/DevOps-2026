terraform {
  backend "s3" {
    bucket = "state-bucket-877"
    key    = "jan26-devops-bootcamp/week8/infra/terraform.tfstate"
    region = "us-east-1"
  }
}