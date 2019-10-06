import os
import sys


class AwsSmsProvider(object):

    def __init__(self, **kargs):
        if 'boto3' not in sys.modules: 
            import boto3
        if 'region_name' not in kargs:
           kargs['region_name'] = os.environ.get('AWS_SNS_REGION_NAME', 
                                                 'us-east-1')
        self.client = boto3.client('sns', **kargs)

    # TODO: Add tags
    def send(self, phone_number, message):
        response = self.client.publish(
            PhoneNumber=phone_number,
            Message=message,
        )

        if response['ResponseMetadata']['HTTPStatusCode'] == 200:
            return True, response['MessageId']
        else:
            return False, RuntimeError()


def get_provider_sms(name='aws', **kargs):
    provider = {
        'aws': AwsSmsProvider(**kargs)
    }
    return provider[name]
