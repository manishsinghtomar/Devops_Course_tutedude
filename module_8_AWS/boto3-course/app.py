import boto3
from dotenv import load_dotenv
import os

load_dotenv()

ACCESS_KEY_ID = os.getenv('ACCESS_KEY_ID')
SECRET_ACCESS_KEY = os.getenv('SECRET_ACCESS_KEY')

# print(ACCESS_KEY_ID)

# Create an S3 resource
# s3 = boto3.resource('s3', aws_access_key_id=ACCESS_KEY_ID, aws_secret_access_key=SECRET_ACCESS_KEY)

# get all buckets
# for bucket in s3.buckets.all():
#     print(bucket.name)

# BUCKET_NAME = 'course-test-tutedude-manish'

# Create a new bucket
# s3.create_bucket(Bucket=BUCKET_NAME, CreateBucketConfiguration = {'LocationConstraint': 'ap-south-1'})

# Delete a bucket
# s3.Bucket(BUCKET_NAME).delete()

# Read a file from the bucket
# s3.Bucket(BUCKET_NAME).download_file('dotfiles/nvim/init.vim', 'test.txt')




# AWS PARAM STORE

ssm = boto3.client('ssm', aws_access_key_id=ACCESS_KEY_ID, aws_secret_access_key=SECRET_ACCESS_KEY, region_name='ap-south-1')

# Get a parameter from the parameter store

response = ssm.get_parameter(Name='bread', WithDecryption=True)

print(response['Parameter']['Value'])





# access s3 object through public url

# with open('https://course-test-tutedude-manish.s3.ap-south-1.amazonaws.com/requirements.txt','r') as f:
#     print(f.read())


import pandas as pd
df = pd.read_csv('https://course-test-tutedude-manish.s3.ap-south-1.amazonaws.com/requirements.txt')
print(df.head())