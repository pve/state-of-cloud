from __future__ import print_function

# a demonstration to pull descriptive information out of AWS
# By Peter HJ van Eijk 

# uses env variables for AWS authentication.
# preparation:
# sudo easy_install awscli
# aws configure
## command line test: 
# aws ec2 describe-availability-zones

import json
import urllib
import boto3

ec2 = boto3.client('ec2')

print("Regions", end=" ")
regions = ec2.describe_regions().get('Regions',[] )
regionnames = [x.get('RegionName', []) for x in regions]
print(regionnames)
print("Zones", end=" "),
print(ec2.describe_availability_zones()['AvailabilityZones'])
zonenames = [x.get('AvailabilityZones', []) for x in zones]
print(zonenames)

def reservations():
    for region in regions:
        reg=region['RegionName']
        print(reg, end=" ")
        ec2con = boto3.client('ec2',region_name=reg)        
        print(ec2con.describe_instances()['Reservations'])
# per instance: name, zone, size, tags
reservations()

print("S3 buckets...")
s3 = boto3.client('s3')
s3 = boto3.resource('s3')

for bucket in s3.buckets.all():
    print(bucket.name, end=" ")
    
print("")    

# more ideas. Pull status info from other API endpoints. I.e. IOT devices. DNS providers.
# time requests. error handling; dashboard.