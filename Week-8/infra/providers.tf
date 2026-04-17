terraform {
  backend "s3" {
    bucket = "state-bucket-292659698930"
    key    = "Devops/Week-8/infra/terraform.tfstate"
    region = "us-east-1"
  }
}