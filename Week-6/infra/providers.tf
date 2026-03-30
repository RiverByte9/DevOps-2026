# terraform version
# aws plugins
# random plugins
# template plugins

terraform {
  required_version = "1.14.7"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "5.50"
    }
    random = {
      source  = "hashicorp/random"
      version = "3.4.3"
    }
    template = {
      source  = "hashicorp/template"
      version = "2.2.0" # Update this to a compatible version
    }
  }
}

provider "aws" {
  region = "us-east-1"
}

# Using S3 backend
terraform {
  backend "s3" {
    bucket  = "292659698930-devops-bootcamp-states"
    key     = "2-tier-flask/dev-tfstate"
    region  = "us-east-1"
    encrypt = true
  }
}


