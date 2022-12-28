variable "region" {
    type        = string
    description = "Default region for the S3 bucket"
    default     = "us-east-1"
}

variable "access_key" {
    default     = "<input>"
}

variable "secret_key" {
    default     = "<input>"
}