import boto3

def lambda_handler(event, context):
    print boto3.__version__
    """ Lambda handler taking [message] and creating a httpd instance with an echo. """
    # bash script to run:
    #  - update and install httpd (a webserver)
    #  - start the webserver
    #  - create a webpage with the provided message.
    #  - set to shutdown the instance in 5 minutes.
    init_script = """#!/bin/bash
    yum update -y
    yum install -y httpd24
    service httpd start
    chkconfig httpd on
    echo """ + "hello" + """ > /var/www/html/index.html
    shutdown -H +5"""
    
    AMI = event['ami']
    INSTANCE_TYPE = event["instanceType"]
    EC2 = boto3.client('ec2', region_name=event['region'])
    
    print 'Running script:'
    print init_script
    
    if event['launch'] == "True" :
        instance = EC2.run_instances(
            ImageId=AMI,
            InstanceType=INSTANCE_TYPE,
            MinCount=1, # required by boto, even though it's kinda obvious.
            MaxCount=1,
            InstanceInitiatedShutdownBehavior='terminate', # make shutdown in script terminate ec2
            UserData=init_script, # file to run on instance init.
            KeyName=event["key"],
            SecurityGroupIds=[event['groupId']],
            IamInstanceProfile={
                'Arn': event["iamInstanceProfileArn"]
            },
            TagSpecifications=[
                {
                    'ResourceType': 'instance',
                    'Tags': [
                        {
                            'Key': 'Name',
                            'Value': event['instanceName']
                        },
                    ]
                },
            ],
        )
        
        print "New instance created."
        instance_id = instance['Instances'][0]['InstanceId']
        print instance_id
    else:
        print "Faked instance"
        instance_id = "faked-instance-id"
    return instance_id
