# https://aws.amazon.com/fr/sdk-for-python/


import boto3

s3 = boto3.resource('s3')

# affichage du nom des buckets
# for bucket in s3.buckets.all():
#     print(bucket.name)

onUpload = False
filename = 'lupus.jpg'
buckename = 'bucket-demo-pamela13'
key = 'boto3/' + filename

if onUpload == True:
  data = open(filename, 'rb')
  s3.Bucket(bucketname).put_object(Key=key, Body=data)

