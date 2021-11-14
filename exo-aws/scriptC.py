#correction
import boto3

ec2 = boto3.resource('ec2')

ids = open('instanceIds.txt', 'r').readlines()

for i in ids:
  ec2.Instance(i.strip()).terminate()
