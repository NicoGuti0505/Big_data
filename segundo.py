import boto3

bucket = 'yummishurima'
s3 = boto3.client('s3')
response = s3.list_objects_v2(Bucket=bucket)

if 'Contents' in response:
    print(f'Archivos en el bucket {bucket}:')
    for obj in response['Contents']:
        print(f'  {obj["Key"]}')
else:
    print(f'El bucket {bucket} no contiene objetos.')
