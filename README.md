# ci_cd_basic_project
ci cd practice in ocb 2026

## AWS Elastic Beanstalk deployment fix

The GitHub Actions deployment failed because the AWS user behind `${{ secrets.AWS_ACCESS_KEY_ID }}` does not have permission to call `elasticbeanstalk:CreateStorageLocation`.

This happens when the deploy action is asked to create a default Elastic Beanstalk storage bucket automatically. The fix is to use an existing S3 bucket in the same AWS region and pass it as `bucket_name` in the workflow.

### Required GitHub secret

Create a repository secret named `AWS_EB_BUCKET_NAME` and set it to the name of a bucket such as:

- `python-calculator-app-deploys-eu-central-1`

Example:

```bash
aws s3 mb s3://python-calculator-app-deploys-eu-central-1 --region eu-central-1
```

### AWS IAM policy

Attach a policy like this to the IAM user or role used by GitHub Actions:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "ElasticBeanstalkDeployPermissions",
      "Effect": "Allow",
      "Action": [
        "elasticbeanstalk:*",
        "s3:ListBucket",
        "s3:GetObject",
        "s3:PutObject",
        "s3:DeleteObject",
        "s3:CreateBucket",
        "cloudformation:DescribeStacks",
        "cloudformation:CreateStack",
        "cloudformation:UpdateStack",
        "cloudformation:DeleteStack",
        "autoscaling:Describe*",
        "ec2:Describe*",
        "elasticloadbalancing:Describe*",
        "logs:CreateLogGroup",
        "logs:CreateLogStream",
        "logs:PutLogEvents"
      ],
      "Resource": "*"
    }
  ]
}
```

If you prefer to keep using the default storage bucket flow, then grant the AWS user this additional permission:

```json
{
  "Effect": "Allow",
  "Action": "elasticbeanstalk:CreateStorageLocation",
  "Resource": "*"
}
```

The workflow in `.github/workflows/ci.yml` has been updated to use `bucket_name` instead of triggering the automatic storage-location creation path.
