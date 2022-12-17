# Required provider
terraform {
    required_providers {
        aws = {
            source  = "hashicorp/aws"
            version = "~> 4.0"
        }
    }
}

# Config for the AWS Provider
provider "aws" {
    access_key  = "${var.access_key}"
    secret_key  = "${var.secret_key}" 
    region      = "${var.region}"
}

# Create an S3 bucket
resource "aws_s3_bucket" "bucket" {
    bucket = "exodia-super-bucket"
    acl    = "private"
}