#!/usr/bin/env python3
import json

import boto3

def main():
    all_ec2 = {}
    all_rds = {}
    all_cache = {}
    all_elb = {}
    all_redshift = {}
    groups = {}
    defaults = {}
    membership = {}

    region_names = [x['RegionName'] for x in boto3.client('ec2').describe_regions()['Regions']]
    for region_name in region_names:
        print(region_name)

        for sg in boto3.client('ec2', region_name=region_name).describe_security_groups()['SecurityGroups']:
            if sg['GroupName'] == 'default':
                defaults[sg['GroupId']] = region_name
            membership[sg['GroupId']] = []
            groups[sg['GroupId']] = sg
            
    for x in [membership, groups, defaults, all_ec2, all_elb, all_rds, all_redshift, all_cache]:
        print(json.dumps(x, indent=4, default=lambda x: x.isoformat()))
        print('-' * 80)

    tbd = [x for x in membership if x not in defaults and not membership[x]]
    print('Empty security groups:', ' '.join(tbd))

    tbd = [x for x in defaults if membership[x]]
    print('None empty default groups:', ' '.join(tbd))


if __name__ == '__main__':
    main()
    