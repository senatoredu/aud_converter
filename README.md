# aud_converter 

Simple Notification Based System that i built that leverages of AWS Lambda. 
I had personal reasons to track a currency conversion rate and rather than refreshing browser everyo ther hour, decided to build an
interval based notification system that keeps me abreast. 

# End-to-End Architecture:

Cloudwatch Rule (every 12 hours) -----> AWS Lambda ------> AWS SNS (personal email subscribed) 

# Extra Modules used:

Outside of 're' and 'boto3' had to use 2 additional modules:

urllib3 
certifi

boto3 is the aws sdk for python, used to create the sns client that pushes the notifications to email subscribers
urllib3 is a python http client that i used to generate the http GET made against the exchange site to get the html output
re is a regex module that i used to parse the html output to find the string match for the conversion output (in numbers)
certifi contains a collection of popular root CAs that my https connection uses in valildating the certificate response 
from the exchange site 

All in all a very simple tool built, not very complex 

Modules downloaded to a local repo on my computer -> zipped together with .py function -> uploaded to aws lambda 

Modules downloaded because it is a dependency not found in lambda's python base


Cloudwatch Rule (every 12 hours) : https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html
AWS Lambda : https://docs.aws.amazon.com/lambda/latest/dg/python-package.html#python-package-dependencies
AWS SNS (personal email subscribed) : https://docs.aws.amazon.com/sns/latest/dg/sns-tutorial-create-subscribe-endpoint-to-topic.html#create-subscribe-endpoint-to-topic-aws-console
