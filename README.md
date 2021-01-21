## AWS DevSecOps Pipeline

DevSecOps pipeline using AWS cloud native services and open source security vulnerability scanning tools.

![CodeBuild badge](https://codebuild.us-west-2.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoieDJkVmY0VXl2bVRjaFdBYkRzZExTNS9ZTUZVQXE4Sy9GMkh1dk1sOE54VkJKcEowOGdXcnJiZDlGL1RGeXJGUmR5UHlWT1psaks2N1dKbk5qUSt6L1BnPSIsIml2UGFyYW1ldGVyU3BlYyI6InhST3ZVeEZ6bkxLWC9IZG4iLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=master)

This DevSecOps pipeline uses AWS DevOps tools CodeBuild, AWS CodeCommit, AWS CodeDeploy, and AWS CodePipeline along with other AWS services.  It is highly recommended to fully test the pipeline in lower environments and adjust as needed before deploying to production.

### Build and Test: 

AWS Buildspec and property files for security vulnerability scanning:
* buildspec-owasp-depedency-check.yml: buildspec file to perform SCA analysis using OWASP Dependency-Check.
* buildspec-sonarqube.yml: buildspec file to perform SAST analysis using SonarQube.
* buildspec-phpstan.yml: buildspec file to perform SAST analysis using PHPStan. This opensource tool is only applicable for scanning PHP application.
* buildspec-owasp-zap.yml: buildspec file to perform DAST analysis using OWASP Zap.
* Composer.json: PHP package manager for installing PHPStan and dependencies.
* phpstan.neon: configuration file for PHPStan.
* Sonar-project.properties: SonarQube configuration file.

### Lambda files:
AWS lambda is used to parse the security scanning results and post them to AWS Security Hub
* import_findings_security_hub.py: to parse the scanning results and extract the vulnerability details.
* securityhub.py: to post the vulnerability details to AWS Security Hub in ASFF format (AWS Security Finding Format).

### CloudFormation for Pipeline:

* codepipeline-template.yml: CloudFormation template to deploy DevSecOps CICD Pipeline 

## Deploying pipeline:
Download the CloudFormation template and pipeline code from GitHub repo.

1.	Log in to your AWS account if you have not done so already. 
2.	On the CloudFormation console, choose Create Stack. 
3.	Choose the provided CloudFormation pipeline template. 
4.	Choose Next.
5.	Provide the stack parameters:
    *  Under Code, provide code details, such as repository name and the branch to trigger the pipeline.
    *	Under SAST, choose the SAST tool (SonarQube or PHPStan) for code analysis, enter the API token and the SAST tool URL. You can skip SonarQube details if using PHPStan as the SAST tool.
    *	Under DAST, choose the DAST tool (OWASP Zap) for dynamic testing and enter the API token, DAST tool URL, and the application URL to run the scan.
    *	Under Lambda functions, enter the Lambda function S3 bucket name, filename, and the handler name.
    *	Under STG Elastic Beanstalk Environment and PRD Elastic Beanstalk Environment, enter the Elastic Beanstalk environment and application details for staging and production to which this pipeline deploys the application code. 
    *	Under General, enter the email addresses to receive notifications for approvals and pipeline status changes. 


Note: The provided CloudFormation template in this blog is formatted for AWS GovCloud, if you are setting this up in standard region, you will have to adjust the partition name in the CloudFormation template. For example, change arn values from “arn:aws-us-gov” to “arn:aws”. 


## License

Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0