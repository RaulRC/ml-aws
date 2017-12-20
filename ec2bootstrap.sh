#!/bin/bash
yum update -y
yum install git
aws s3 cp s3://poc-ml-op/resources/requirements.txt requirements.txt --region eu-west-1
pip install -r requirements.txt
mkdir data
aws s3 cp s3://poc-ml-op/data/iris.data data/iris.data --region eu-west-1
git clone https://github.com/RaulRC/ml-aws.git
python hello-world.py

