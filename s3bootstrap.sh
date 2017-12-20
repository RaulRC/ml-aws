#!/bin/bash
yum update -y
aws s3 cp s3://poc-ml-op/resources/requirements.txt requirements.txt --region eu-west-1
pip install -r requirements.txt
