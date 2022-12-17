variable "access_key" {
    default     = ""
}

variable "secret_key" {
    default     = ""
}

variable "region" {
    type        = string
    description = "Default region for the S3 bucket"
    default     = "us-east-1"
}