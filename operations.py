from tg import TG
from ec2 import EC2


class Operation:
    def __init__(self):
        pass

    def find_operation(self, arg):
        if arg[1].lower() == "update":
            return "update"
        else:
            return "search"

    def update_ec2(self, profile, defaults):
        print("updating ec2", profile, "profile")

        if profile == "all":
            for profile in defaults.aws_accounts:
                EC2().update_ec2(profile["arn"], profile["name"])
        else:
            flag = 0
            for account in defaults.aws_accounts:
                if account["name"] == profile:
                    EC2().update_ec2(account["arn"], account["name"])
                    flag = 1
                    break
            if flag == 0:
                print("No matching profile found")

    def search_ec2(self, args):
        EC2().search_ec2(args)

    def update_tg(self, profile, defaults):
        print("updating tg", profile, "profile")

        if profile == "all":
            for profile in defaults.aws_accounts:
                TG().update_tg(profile["arn"], profile["name"])
        else:
            flag = 0
            for account in defaults.aws_accounts:
                if account["name"] == profile:
                    TG().update_tg(account["arn"], account["name"])
                    flag = 1
                    break
            if flag == 0:
                print("No matching profile found")

    def search_tg(self, args):
        TG().search_tg(args)