terraform {
  backend "s3" {
    bucket = "state-bucket-29265969893030"
    key    = "Devops/Week-8/infra/terraform.tfstate"
    region = "us-east-1"
  }
}