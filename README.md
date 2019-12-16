# aws-ssh

A wrapper for EC2 Instance Connect to make connecting to keyless EC2 instances more streamlined.

## Requirements

* Python3
* boto3
* cryptography
* [Proper IAM Permissions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-connect-set-up.html#ec2-instance-connect-configure-IAM-role)

## Setup

* Clone the aws-ssh repository
* Install required packages with `pip install -r requirements.txt`
* [Configure AWS credentials](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html#configuration)

## Usage

aws-ssh takes two ordered arguments:

`./aws-ssh <ssh_user> <instance_id>`

Example:

`./aws-ssh ec2-user i-abcd1234`

## Install (Optional)

Copy aws-ssh to your favorite bin folder.

`cp aws-ssh /usr/bin/`
