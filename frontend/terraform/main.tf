provider "aws" {
  region = var.region
}

resource "aws_s3_bucket" "frontend_bucket" {
  bucket        = "my-react-frontend-bucket"
  acl           = "public-read"
  force_destroy = true

  website {
    index_document = "index.html"
    error_document = "index.html"
  }
}

resource "aws_cloudfront_distribution" "cdn" {
  origin {
    domain_name = aws_s3_bucket.frontend_bucket.bucket_regional_domain_name
    origin_id   = "S3-my-react-frontend-bucket"
  }

  default_cache_behavior {
    allowed_methods  = ["GET", "HEAD"]
    cached_methods   = ["GET", "HEAD"]
    target_origin_id = "S3-my-react-frontend-bucket"

    viewer_protocol_policy = "redirect-to-https"
  }

  enabled             = true
  is_ipv6_enabled     = true
  default_root_object = "index.html"
}
