import boto3

s3 = boto3.client('s3')

response = s3.download_file("yummishurima","hola.txt","hola.txt")
