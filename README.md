**Cloud Resume Challenge - Manual Implementation**

**Overview**

This repository contains the manual implementation of the Cloud Resume Challenge. The challenge is designed to integrate multiple AWS services to build a fully functional cloud-based resume website while following best practices in cloud computing, serverless architecture, and automation.

In this implementation, all AWS resources were manually configured through the AWS Management Console, without using Infrastructure as Code (IaC) tools like AWS SAM or Terraform. This allows for a detailed understanding of each AWS component and how they interact with one another.

**Project Architecture**

The Cloud Resume Challenge consists of the following components:

**Frontend:**

A static website built using HTML, CSS, and JavaScript.
Hosted on Amazon S3 with CloudFront for global content delivery.
Integrated with AWS Route 53 for a custom domain.

**Backend:**

AWS API Gateway to expose a REST API endpoint.
AWS Lambda function (Python) to interact with the database.
Amazon DynamoDB to store and track visitor counts.

**Security & Monitoring:**

AWS IAM Roles & Policies to ensure secure access.
CORS Configuration to allow cross-origin requests.
Amazon CloudWatch for logging and monitoring Lambda executions.

**Technologies Used**

AWS S3 - Static website hosting
Amazon CloudFront - Content Delivery Network (CDN)
AWS Route 53 - Domain name management
AWS API Gateway - REST API creation
AWS Lambda - Serverless function execution
Amazon DynamoDB - NoSQL database for visitor count
IAM Roles & Policies - Secure access control
CloudWatch - Monitoring and logging

**Steps Taken**

Created an S3 Bucket and enabled static website hosting.
Configured CloudFront to serve the website securely.
Set up Route 53 to connect the website to a custom domain.
Built a Visitor Counter API using:
API Gateway (to expose an endpoint)
AWS Lambda (to process visitor data)
DynamoDB (to store visitor count)
Integrated JavaScript (AJAX Fetch) in the frontend to display live visitor count.
Configured IAM Roles & Policies to ensure proper security measures.
Enabled CORS on API Gateway to allow web requests from the frontend.
Deployed and tested the solution to confirm end-to-end functionality.
Pushed the code to GitHub for version control and documentation.

**Future Enhancements**

Implement the same project using AWS SAM (Infrastructure as Code)
Implement the same project using Terraform (Infrastructure as Code)

Compare all three approaches in a blog post
Automate deployments with GitHub Actions
Improve UI design for a better user experience

**Blog Comparison (Coming Soon)**

Once all three implementations (Manual, AWS SAM, Terraform) are completed, a detailed comparison blog will be written covering:
Pros & Cons of each approach
Ease of setup and management
Automation benefits with IaC
Best practices for cloud-based applications

Author
Bheemender Gurram
