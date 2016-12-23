# state-of-cloud
Tools to inventory cloud and report on status. AWS and other services.
Usable as a working proof of concept.

Delivers a current list of AWS regions, all zones in the current region, a list of instances across all regions, and a list of all buckets of the current account.

Requires:
- python
- boto3
- aws account credentials with policies ec2-readonly-access and s3-readonly-access

For account setup you can use
```
sudo easy_install awscli
aws configure
```

Alternatively, you can introduce the credentials through environment variables.

AWS_ACCESS_KEY_ID
The access key for your AWS account.

AWS_SECRET_ACCESS_KEY
The secret key for your AWS account.

AWS_DEFAULT_REGION
The default region to use, e.g. us-east-1, us-west-2, etc.

Usage:
```
python aws.py
```

Sample output:
```
Regions:  ['eu-west-1', 'ap-southeast-1', 'ap-southeast-2', 'eu-central-1', 'ap-northeast-2', 'ap-northeast-1', 'us-east-1', 'sa-east-1', 'us-west-1', 'us-west-2']
Zones:  [['eu-west-1a', 'available'], ['eu-west-1b', 'available'], ['eu-west-1c', 'available']]
(output of describe_instances)
(S3 bucket list)

```
[![](https://images.microbadger.com/badges/image/petersgriddle/state-of-cloud.svg)](https://microbadger.com/images/petersgriddle/state-of-cloud "Get your own image badge on microbadger.com")

