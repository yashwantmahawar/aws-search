import boto3
from default import Defaults


class AWSUtility:
    def assume_aws_role_arn(self, arn, aws_account_name):
        sts_client = Defaults().get_aws_default_session()
        assumed_role_object = sts_client.assume_role(
            RoleArn=arn,
            RoleSessionName=aws_account_name
        )
        credentials = assumed_role_object['Credentials']
        assume_role_session = boto3.Session(
            aws_access_key_id=credentials['AccessKeyId'],
            aws_secret_access_key=credentials['SecretAccessKey'],
            aws_session_token=credentials['SessionToken'],

        )
        return assume_role_session
