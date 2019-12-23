# aws-ic

A wrapper for EC2 Instance Connect to make a ssh connection to keyless EC2 instances more streamlined and secure.

## Requirements

* Python3 w/ pip
* [Proper IAM Permissions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-connect-set-up.html#ec2-instance-connect-configure-IAM-role)

## Setup

* `pip install awc-ic`
* [Configure AWS credentials](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html#configuration)

## Usage

aws-ic takes two ordered arguments:

`aws-ic <ssh_user> <instance_id>`

Example:

`aws-ic ec2-user i-abcd1234`
