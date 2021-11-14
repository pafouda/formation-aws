#correction
import boto3
import requests

ec2 = boto3.resource('ec2')

ids = open('instanceIds.txt', 'r').readlines()

for i in ids:
  instance = ec2.Instance(i.strip())
  ip = instance.public_ip_address
  try:
    r = requests.get('http://' + ip)
    message = 'OK' if r.status_code == 200 else 'NOT OK'
    print(f'IP: {ip} => { message }')
  except:
    print(f'IP: {ip} => NOT REACHABLE')
