Cloud Resume Challenge - Manual Deployment
This repository contains the manual implementation of the Cloud Resume Challenge. The project showcases how to deploy a cloud-based resume website with a visitor counter using AWS services and Netlify for hosting.
Architecture Overview
The architecture follows a manual deployment approach where we configure AWS services without Infrastructure as Code (IaC). The key components include:
•	Netlify: Hosts the static resume website.
•	AWS API Gateway: Acts as an entry point to handle API requests.
•	AWS Lambda: A serverless function to interact with the database.
•	AWS DynamoDB: A NoSQL database to store and retrieve visitor count.
•	GitHub Actions: Automates deployment of backend updates.
Project Breakdown
1. Frontend (Static Website)
•	Developed the HTML, CSS, and JavaScript files for the resume.
•	Added JavaScript logic to fetch and update the visitor count.
•	Hosted the static files on Netlify.
2. Backend (API & Database)
•	Created an AWS Lambda function to read/write visitor count from DynamoDB.
•	Configured an API Gateway to expose the Lambda function as a REST API.
•	Set up DynamoDB with a table to store visitor data.
3. CI/CD Pipeline (GitHub Actions)
•	Configured GitHub Actions to automate deployment of backend changes.
•	Used AWS CLI to update Lambda function on code changes.
Deployment Steps
1. Setup AWS Services Manually
•	Created a DynamoDB Table (Name: visitorCounter, Primary Key: id).
•	Deployed a Lambda function to update and retrieve visitor count.
•	Configured API Gateway to connect with Lambda.
•	Enabled CORS for API Gateway.
2. Hosting on Netlify
•	Deployed the frontend files to Netlify.
•	Updated the API endpoint in JavaScript to point to API Gateway.
3. Configuring GitHub Actions for Automation
•	Created an AWS IAM user with necessary permissions.
•	Added GitHub secrets for AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY.
•	Configured a workflow file in .github/workflows/deploy.yml to automate Lambda function updates.
Testing & Validation
•	Verified visitor count increments when visiting the site.
•	Checked API Gateway logs to confirm successful API calls.
•	Monitored DynamoDB updates for real-time data changes.
Future Enhancements
•	Implement AWS CloudFront for improved content delivery.
•	Migrate hosting to AWS S3 + CloudFront for a fully AWS-hosted solution.
•	Implement authentication for API security.
Repository Structure
cloud-resume-manual/
├── frontend/            # Static website files
│   ├── index.html
│   ├── style.css
│   ├── script.js
│   ├── assets/
├── backend/             # Lambda function code
│   ├── lambda_function.py
│   ├── requirements.txt
├── .github/workflows/   # GitHub Actions CI/CD setup
│   ├── deploy.yml
├── README.md            # Project documentation

Contributing

Feel free to contribute by submitting issues or pull requests. Improvements and optimizations are always welcome!

Author
Bheemender Gurram
LinkedIn

License
This project is licensed under the MIT License.


Credits: @[Gilbert Mutai](https://github.com/Mutai-Gilbert/Mutai-Gilbert)
