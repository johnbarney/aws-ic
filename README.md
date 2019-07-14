# aws-ssh

A wrapper for EC2 Instance Connect to make connecting to keyless EC2 instances more streamlined

## Setup

Requires two packages:

cryptography
boto3

You can use pip to install these packages.

`pip install -r requirements.txt`

-also-

[Requires AWS credentials to be configured.](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html#configuration)

## Usage

Takes two ordered arguments:

`./aws-ssh <ssh_user> <instance_id>`

ssh_user - User to establish SSH connection with.
instance_id - Instance ID to connect to.
