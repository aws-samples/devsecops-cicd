"""
 AWS Security Hub Integration
 Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 SPDX-License-Identifier: MIT-0
"""
import sys
import logging
sys.path.insert(0, "external")
import boto3

logger = logging.getLogger(__name__)

securityhub = boto3.client('securityhub')

# This function import agregated report findings to securityhub 
def import_finding_to_sh(count: int, account_id: str, region: str, created_at: str, source_repository: str, 
    source_branch: str, source_commitid: str, build_id: str, report_url: str, finding_id: str, generator_id: str,
                         normalized_severity: str, severity: str, finding_type: str, finding_title: str, finding_description: str, best_practices_cfn: str): 
    print("called securityhub.py..................")
    new_findings = []
    new_findings.append({
        "SchemaVersion": "2018-10-08",
        "Id": finding_id,
        "ProductArn": "arn:aws-us-gov:securityhub:{0}:{1}:product/{1}/default".format(region, account_id),
        "GeneratorId": generator_id,
        "AwsAccountId": account_id,
        "Types": [
            "Software and Configuration Checks/AWS Security Best Practices/{0}".format(
                finding_type)
        ],
        "CreatedAt": created_at,
        "UpdatedAt": created_at,
        "Severity": {
            "Normalized": normalized_severity,
        },
        "Title":  f"{count}-{finding_title}",
        "Description": f"{finding_description}",
        'Remediation': {
            'Recommendation': {
                'Text': 'For directions on PHP AWS Best practices, please click this link',
                'Url': best_practices_cfn
            }
        },
        'SourceUrl': report_url,
        'Resources': [
            {
                'Id': build_id,
                'Type': "CodeBuild",
                'Partition': "aws",
                'Region': region
            }
        ],
    })
    ### post the security vulnerability findings to AWS SecurityHub
    response = securityhub.batch_import_findings(Findings=new_findings)
    if response['FailedCount'] > 0:
        logger.error("Error importing finding: " + response)
        raise Exception("Failed to import finding: {}".format(response['FailedCount']))