#!/bin/bash
# System update
yum update -y
# Install Git
yum install git -y
# Clone repo
git clone https://github.com/RaulRC/ml-aws.git
# Fetch data
mkdir data
aws s3 cp s3://poc-ml-op/data/iris.data data/iris.data --region eu-west-1
aws s3 cp s3://poc-ml-op/resources/requirements.txt requirements.txt --region eu-west-1
# Install dependencies
pip install -r requirements.txt --no-cache-dir
# Execute program
python ml-aws/hello-world.py
# Write output
aws s3 cp output.txt s3://poc-ml-op/resources/output.txt --region eu-west-1
# Terminate instance
aws ec2 terminate-instances --instance-ids $(curl -s http://169.254.169.254/latest/meta-data/instance-id) --region eu-west-1
