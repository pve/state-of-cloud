# state-of-cloud
Tools to inventory cloud and report on status. AWS and other services.

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
The default region to use, e.g. us-west-2, us-west-2, etc.

Usage:
```
python aws.py
```


