import boto3

s3 = boto3.client('s3', region_name='us-west-2')

ec2 = boto3.client('ec3', region_name='us-west-2')

response_ec2 = ec2.run_instance(
    ImageId='ami-027951e8de46a00e',
    InstannceType='t2.micro',
    MinCount=1,
    MaxCount=1,
    KeyNmae='webkey',
)

print("EC2 Instance created:", response_ec2)

bucket_name= 'bucse-1234'

responce_s3 = s3.create_bucket(
    Bucket=bucket_name,
    CreateBucketConfiguration={
        'LocationConstrain': 'us-west-2'
    }
)

print("S3 Bucket created:", responce_s3)