# ml-aws
PoC for ML arch on AWS

* Lambda ec2 handler API
```json
{
  "key": "yourPEM",
  "region": "yourRegion",
  "launch": "True", 
  "iamInstanceProfileArn" : "yourInstanceProfileARN",
  "groupId" : "yourGroupName",
  "ami" : "ami-1a962263",
  "instanceType" : "t2.micro",
  "instanceName" : "yourInstanceName",
  "bucket" : "yourBucketName",
  "bucketKey" : "yourFolder/yourFile"
}
```

* launch: True|False in order to test. Launch=False will not launch the instance, just simulate the lambda call. Testing purposes.
* groupId: the name of the permissions group e.g: General
