import boto3
import pandas as pd

s3 = boto3.resource(
    service_name='s3',
    region_name='us-east-1',
    aws_access_key_id='AKIA22ZZIIXPZTXQF5WG',
    aws_secret_access_key="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"
)

obj = s3.Bucket('santi-gallastegui').Object('Output/ETL2_part00000.csv').get()

foo = pd.read_csv(obj['Body'])
df = pd.DataFrame(foo)
df.to_csv('prueba.csv',index=False ,sep=',', mode='w')