from __future__ import print_function

# a demonstration to pull descriptive information out of AWS
# By Peter HJ van Eijk 

# uses env variables for AWS authentication.
# sudo easy_install awscli
# command line: aws configure
# aws ec2 describe-availability-zones

import json
import urllib
import boto3

print('Loading function')

ec2 = boto3.client('ec2')

print(ec2.describe_availability_zones())
print(ec2.describe_regions())
regions = ec2.describe_regions().get('Regions',[] )

for region in regions:
    reg=region['RegionName']
    print(reg)
    ec2con = boto3.client('ec2',region_name=reg)        
    print(ec2con.describe_instances()['Reservations'])
    

print("S3 buckets...")
s3 = boto3.client('s3')
s3 = boto3.resource('s3')

for bucket in s3.buckets.all():
    print(bucket.name)

# more ideas. Pull status info from other API endpoints. I.e. IOT devices. DNS providers. 

