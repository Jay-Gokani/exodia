# Required provider
terraform {
    required providers {
        aws = {
            source  = "hashicorp/aws"
            version = "~> 4.0"
        }
    }
}

# Config for the AWS Provider
provider "aws" {
    region      = "${var.region}"
}

# Create an S3 bucket
resource "aws_s3_bucket" "bucket" {
    bucket = "exodia-super-bucket"
    acl    = "private"
}

# Create an EC2 instance
# Constraints:
# t2.micro, Max Volume Size = 50GB, Max Volume IOPS = 150