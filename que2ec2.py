# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 17:31:34 2021

@author: Sanket
"""


import boto3
ec2=boto3.resource('ec2')
for instance in ec2.instances.all():
    print(
        "Id: {0}\nPlatform: {1}\n Type: {2}\n Public Ipv4: {3}\nAMI: {4}\nState: {5}\n".format(
        instance.id,instance.platform,instance.instance_type,instance.public_ip_address,instance.image.id,instance.state
        )
    )