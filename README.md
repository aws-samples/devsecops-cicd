## AWS DevSecOps Pipeline

DevSecOps pipeline using AWS cloudnative services and open source security vulnerability scanning tools.

![CodeBuild badge](https://codebuild.us-west-2.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoieDJkVmY0VXl2bVRjaFdBYkRzZExTNS9ZTUZVQXE4Sy9GMkh1dk1sOE54VkJKcEowOGdXcnJiZDlGL1RGeXJGUmR5UHlWT1psaks2N1dKbk5qUSt6L1BnPSIsIml2UGFyYW1ldGVyU3BlYyI6InhST3ZVeEZ6bkxLWC9IZG4iLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=master)

This DevSecOps pipeline uses AWS DevOps tools CodeBuild, AWS CodeCommit, AWS CodeDeploy, and AWS CodePipeline along with other AWS services.  It is highly recommended to fully test the pipeline in lower environments and adjust as needed before deploying to production.

### Build and Test: 

The buildspecs and property files for vulnerability scanning using AWS CodeBuild:
* buildspec-owasp-depedency-check.yml: buildspec file to perform SCA analysis using OWASP Dependency-Check.
* buildspec-sonarqube.yml: buildspec file to perform SAST analysis using SonarQube.
* buildspec-phpstan.yml: buildspec file to perform SAST analysis using PHPStan. This opensource tool is only applicable for scanning PHP application.
* buildspec-owasp-zap.yml: buildspec file to perform DAST analysis using OWASP Zap.
* Composer.json: PHP package manager for installing PHPStan and dependencies.
* phpstan.neon: configuration file for PHPStan.
* Sonar-project.properties: SonarQube configuration file.

### Lambda files:

AWS lambda is used to parse the scanning analysis results and post it to AWS Security Hub
* import_findings_security_hub.py: to parse the scanning results, extract the vulnerability details.
* securityhub.py: to post the vulnerability details to AWS Security Hub in ASFF format (AWS Security Finding Format) .

### CloudFormation for Pipeline:

* codepipeline-template.yml: CloudFormation template to deploy the DevSecOps Pipeline 

## Deploying pipeline:

1.	Log in to your AWS account if you have not done so already. Choose the CloudFormation service from the menu and select Launch Stack to launch the AWS CloudFormation console. Select the prepopulated AWS    CloudFormation pipeline template. Choose Next.
2.	Fill in the stack parameter as shown below (Figure 2 and Figure 3).
3.	Provide Code details, such as repository name and the branch to trigger the pipeline.
4.	Select the SAST tool (SonarQube or PHPStan) for code analysis, enter API Token, and the SAST tool URL. You can skip SonarQube details if PHPStan is selected as SAST tool.
5.	Select the DAST tool (OWASP Zap) for dynamic testing, enter API Token, DAST tool URL, and the application URL to run the scan.
6.	Provide the Lambda function S3 bucket name, filename, and the handler name.
7.	Provide the Elastic Beanstalk environment and application details for staging and production to which this pipeline will be deploying the application code. 
8.	Provide the e-mail address(es) to receive notifications for approvals and pipeline status changes. Please note, once the pipeline is deployed, you will have to confirm the subscription by clicking on the provided link in the email to receive the notifications.

Note: The provided CloudFormation template in this blog is formatted for AWS GovCloud, if you are setting this up in standard region, you will have to adjust the partition name in the CloudFormation template. For example, change arn values from “arn:aws-us-gov” to “arn:aws”. 


## License

Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0