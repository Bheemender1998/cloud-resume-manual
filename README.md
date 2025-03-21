
# The Cloud Resume Challenge - AWS

Welcome to the **Cloud Resume Challenge - AWS**! This challenge is designed to guide you through creating an interactive resume hosted on AWS, incorporating a variety of cloud technologies and best practices.

## Project Overview

The challenge consists of creating a static resume webpage with the following features and requirements:

1. **Certification**
   - Your resume needs to have the **AWS Cloud Practitioner** certification.
   - If you have a more advanced AWS cert, that's fine, but not required.
   - The certification exam can be taken online for $100 USD.

2. **HTML**
   - Your resume should be written in **HTML**, not a Word document or PDF.

3. **CSS**
   - Style your resume with **CSS**. You don’t need to be a designer, but make sure it’s visually appealing.

4. **Static Website**
   - Host your HTML resume as a **static website** on **Amazon S3**.
   - Avoid using services like Netlify or GitHub Pages for this project, as we need to focus on S3.

5. **HTTPS**
   - Use **Amazon CloudFront** to enable HTTPS on your S3 static website for security.

6. **DNS**
   - Point a custom **DNS domain** to the CloudFront distribution so that your resume can be accessed with a custom domain (e.g., `my-c00l-resume-website.com`).
   - You can use **Amazon Route 53** or any other DNS provider.

7. **JavaScript**
   - Include a **visitor counter** on your resume page that displays how many people have accessed the site.

8. **Database**
   - Use **Amazon DynamoDB** to store and update the visitor counter.

9. **API**
   - Create an **API** (using **AWS API Gateway** and **Lambda**) to communicate between your JavaScript front-end and DynamoDB.

10. **Python**
    - Write your Lambda function in **Python**, utilizing the **boto3** library to interact with AWS services.

11. **Tests**
    - Include tests for your Python code to ensure it functions properly.

12. **Infrastructure as Code (IaC)**
    - Define your API resources (DynamoDB, API Gateway, Lambda) using **AWS Serverless Application Model (SAM)**.
    - Deploy your infrastructure using the **AWS SAM CLI**.

13. **Source Control**
    - Use **GitHub** to host your backend and frontend code.

14. **CI/CD (Backend)**
    - Set up **GitHub Actions** to automatically deploy your API when changes are pushed to your repository.
    - Ensure that Python tests are run before deployment.

15. **CI/CD (Frontend)**
    - Create another GitHub repository for your frontend website.
    - Set up GitHub Actions to update your S3 bucket when changes are made to the frontend code.

16. **Blog Post**
    - Write a short blog post (hosted on **Dev.to** or **Hashnode**) describing the lessons you learned while working on this project.
    - Include a link to the blog post in the text of your resume.

---

For more detailed strategies, tools, and further challenges to help you get hired in the cloud, check out the **AWS edition of the Cloud Resume Challenge Guidebook**.

Good luck, and happy building!
