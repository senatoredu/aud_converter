import boto3
import urllib3
import certifi
import re

def lambda_handler(event, context):
    sns = boto3.client('sns')
    url = 'https://zar.currencyrate.today/aud/1000'
    http = urllib3.PoolManager(ca_certs=certifi.where())
    r =  http.request('GET', url)
    r = r.data.decode('utf-8')
    aud = re.findall(r'\$[0-9,.]+', r)
    aud = ''.join(aud)
    message = 'Hello Edu, Right now 2000 Rands is', aud

    topicArn = 'arn:aws:sns:eu-west-1:123456789:EXCHANGE'

    sns.publish(
        TopicArn = topicArn,
        Message = message
   )

