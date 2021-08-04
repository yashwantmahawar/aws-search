import csv
from default import Defaults
from style import style
from awsUtility import AWSUtility


class TG:
    def __init__(self):
        pass

    def update_tg(self, arn, aws_account_name):
        with open("/tmp/tg_" + aws_account_name + ".csv", "w") as inventory_write:
            inventory_writer = csv.writer(inventory_write, delimiter=',', quoting=csv.QUOTE_MINIMAL)
            tgclient = AWSUtility().assume_aws_role_arn(arn, aws_account_name).client("elbv2",
                                                                                      region_name=Defaults.default_aws_region)
            tgs = tgclient.describe_target_groups()["TargetGroups"]
            for tg in tgs:
                print(tg["TargetGroupArn"])
                tgarn = tg["TargetGroupArn"]
                tgname = tg["TargetGroupName"]
                targets = tgclient.describe_target_health(
                    TargetGroupArn=tgarn
                )["TargetHealthDescriptions"]
                for target in targets:
                    instance_id = target["Target"]["Id"]
                    instance_health = target["TargetHealth"]["State"]
                    print(instance_id, instance_health)
                    inventory_writer.writerow(["tg",tgname , instance_id, instance_health])

    def search_tg(self, arguments):

        if len(arguments) == 0:
            print("Please add search parameters")
        else:
            print("Searching with given parameters [" + ", ".join(arguments) + "]")
            for profile in Defaults.aws_accounts:
                with open("/tmp/tg_" + profile["name"] + ".csv", "r") as inventory:
                    inventory_reader = csv.reader(inventory, delimiter=',', quoting=csv.QUOTE_MINIMAL)

                    count = 0
                    for line in inventory_reader:
                        if all(argument in ",".join(line) for argument in arguments):
                            count += 1
                            print(line)

                    if count != 0:
                        print("total instance found ", count, "in", style.RED + profile["name"] + style.RESET)
                        print("")