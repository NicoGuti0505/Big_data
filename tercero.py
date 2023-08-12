import boto3

archivo = 'archivo.txt'

bucket = 'yummishurima'

s3 = boto3.client('s3')

s3.upload_file(archivo, bucket, archivo)

print(f'El archivo {archivo} se ha subido al bucket {bucket}.')

