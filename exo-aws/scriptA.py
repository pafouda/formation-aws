#correction
import boto3

client = boto3.client('ec2')

numInstances = int(input('Nombre de VMs à instancier: '))

imageId = 'ami-0a49b025fffbbdac6' # ubuntu server 20.04 eu-central-1
sgId = 'sg-0f1731f6fd0e257ce' # sgFirst => ssh + http
keyName = 'kp-first'

userData = """#!/bin/bash
apt update
apt install -y apt-transport-https ca-certificates curl gnupg lsb-release
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" |sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
apt update
apt install -y docker-ce docker-ce-cli containerd.io
docker run -d --name apache -p 80:80 httpd:2.4-alpine"""


response = client.run_instances(
  ImageId=imageId,
  InstanceType='t2.micro',
  KeyName=keyName,
  MaxCount=numInstances,
  MinCount=numInstances,
  SecurityGroupIds=[sgId],
  UserData=userData,
  DryRun=False
)

# production en sortie d'un fichier texte contenant 
# les identifiants des instances générées

instanceIds = ''

for instance in response['Instances']:
  if instanceIds == '':
    instanceIds = instance['InstanceId']
  else:
    instanceIds += '\n' + instance['InstanceId']

with open("instanceIds.txt", "w") as f:
  f.write(instanceIds)


'''
# https://rdrr.io/github/cloudyr/aws.ec2/man/run_instances.html
# https://boto3.amazonaws.com/v1/documentation/api/latest/guide/migrationec2.html
# https://stackoverflow.com/questions/32863768/how-to-create-an-ec2-instance-using-boto3
# https://stackoverflow.com/questions/67016403/how-to-get-arn-of-my-ec2-instance-using-boto3
# https://stackoverflow.com/questions/48072398/get-list-of-ec2-instances-with-specific-tag-and-value-in-boto3

import boto3
ec2= boto3.client('ec2', region_name='eu-central-1')

nbreVm = int(input("Saisissez le nombre de vms à créer : "))

response = ec2.run_instances(
    BlockDeviceMappings=[
        {
            'DeviceName': '/dev/xvda',             #non spécifié quand on veut attacher un volume ebs
            'Ebs': {

                'DeleteOnTermination': True,

            },
        },
    ],
    ImageId='ami-0a49b025fffbbdac6',
    InstanceType='t2.micro',
    MaxCount=2,
    MinCount=2,
    Monitoring={
        'Enabled': False
    },
    
)

instances = ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
for instance in instances:
    print(instance.id, instance.instance_type)
    '''