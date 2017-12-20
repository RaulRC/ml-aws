#!/bin/bash
yum update -y
yum install git -y
git clone https://github.com/RaulRC/ml-aws.git
mkdir data
aws s3 cp s3://poc-ml-op/data/iris.data data/iris.data --region eu-west-1
aws s3 cp s3://poc-ml-op/resources/requirements.txt requirements.txt --region eu-west-1
pip install -r requirements.txt --no-cache-dir
python ml-aws/hello-world.py

