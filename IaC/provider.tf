# Use AWS with version greater than or equal to 4.9.0
terraform {
    required_providers {
        aws = {
            version=">= 4.9.0"
        }
    }
}

provider "aws" {
    region = "us-east-1"
    access_key = var.aws_access_key
    secret_key = var.aws_secret_key
}