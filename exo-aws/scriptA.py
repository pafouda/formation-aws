# https://rdrr.io/github/cloudyr/aws.ec2/man/run_instances.html
# https://boto3.amazonaws.com/v1/documentation/api/latest/guide/migrationec2.html
# https://stackoverflow.com/questions/32863768/how-to-create-an-ec2-instance-using-boto3
# https://stackoverflow.com/questions/67016403/how-to-get-arn-of-my-ec2-instance-using-boto3
# https://stackoverflow.com/questions/48072398/get-list-of-ec2-instances-with-specific-tag-and-value-in-boto3

import boto3
ec2 = boto3.resource('ec2', region_name='eu-central-1')

nbreVm = int(input("Saisissez le nombre de vms à créer : "))

response = ec2.run_instances(
    BlockDeviceMappings=[
        {
            'DeviceName': '/dev/xvda',
            'Ebs': {

                'DeleteOnTermination': True,
                'VolumeSize': defaut,
                'VolumeType': 'gp2'
            },
        },
    ],
    ImageId='ami-0a49b025fffbbdac6',
    InstanceType='t2.micro',
    MaxCount=5,
    MinCount=1,
    Monitoring={
        'Enabled': False
    },
    
)

instances = ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
for instance in instances:
    print(instance.id, instance.instance_type)