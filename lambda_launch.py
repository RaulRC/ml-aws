import boto3
import botocore

def lambda_handler(event, context):
    print boto3.__version__
    """ Lambda handler taking [message] and creating a httpd instance with an echo. """
    
    BUCKET_NAME = event['bucket']
    KEY = event['bucketKey']
    s3 = boto3.client('s3')
    init_script = ""

    try:
        respS3 = s3.get_object(Bucket=BUCKET_NAME, Key=KEY)
        init_script = respS3['Body'].read().decode('utf-8')
        print "Running script: "
        print init_script
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            print("The object does not exist.")
        else:
            raise
        
        
        AMI = event['ami']
        INSTANCE_TYPE = event["instanceType"]
        EC2 = boto3.client('ec2', region_name=event['region'])
        
        print 'Running script:'
        print init_script
        
        if event['launch'] == "True" :
            instance = EC2.run_instances(
                ImageId=AMI,
                InstanceType=INSTANCE_TYPE,
                MinCount=1,
                MaxCount=1,
                InstanceInitiatedShutdownBehavior='terminate',
                UserData=init_script,
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
