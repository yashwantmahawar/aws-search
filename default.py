import boto3
import json
import os


class Defaults:
    # Get config object from ./configs.json file
    configs_json_file = open(os.path.dirname(__file__) + "/configs.json", "r")
    configs = json.load(configs_json_file)

    # Load all variables from config.json files
    aws_accounts = configs["aws_accounts"]
    default_aws_profile_name = configs["default_aws_profile_name"]
    default_aws_region = configs["default_aws_region"]
    supported_resources = configs["supported_resources"]
    inventory = configs["inventory"]

    def get_aws_default_session(self):
        session = boto3.Session(profile_name=Defaults.default_aws_profile_name, region_name=Defaults.default_aws_region)
        return session.client('sts')

    def get_aws_profiles_list(self):
        aws_profiles_list = []
        for profile in Defaults.aws_accounts:
            aws_profiles_list.append(profile["name"])
        return aws_profiles_list
