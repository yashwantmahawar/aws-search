import csv
from default import Defaults
from style import style
from awsUtility import AWSUtility


class EC2:
    def __init__(self):
        pass

    def update_ec2(self, arn, aws_account_name):
        with open("/tmp/ec2_" + aws_account_name + ".csv", "w") as inventory_write:
            inventory_writer = csv.writer(inventory_write, delimiter=',', quoting=csv.QUOTE_MINIMAL)
            ec2client = AWSUtility().assume_aws_role_arn(arn, aws_account_name).client("ec2",
                                                                                       region_name=Defaults.default_aws_region)
            ec2 = ec2client.describe_instances()
            instance_state = "N/A"
            instance_list = ec2["Reservations"]
            instance_id = ""

            print(aws_account_name, "update", len(instance_list))

            for instance in instance_list:

                i = instance["Instances"][0]
                instance_state = i["State"]["Name"]
                name = "name_not_found"
                techteam = "not_found"
                private_ip = "no_private_ip"
                sg_name = ""

                if "PrivateIpAddress" in i:
                    private_ip = i["PrivateIpAddress"]

                if "Tags" in i:
                    for tag in i["Tags"]:
                        if tag["Key"].lower() == "name":
                            name = tag["Value"]
                        if tag["Key"].lower() == "techteam":
                            techteam = tag["Value"]

                for sg in i["SecurityGroups"]:
                    sg_name = sg_name + sg["GroupName"] + "-" + sg["GroupId"] + " "

                instance_id = i["InstanceId"]

                sg_name = sg_name.strip()
                inventory_writer.writerow(["ec2", private_ip, name, sg_name, instance_id, techteam, instance_state])

    def search_ec2(self, ec2_arguments):
        detailed = False
        if "-d" in ec2_arguments:
            detailed = True
            ec2_arguments.remove("-d")

        if len(ec2_arguments) == 0:
            print("Please add search parameters")
        else:
            ec2_arguments = "|".join(ec2_arguments).split(",")
            for index, ec2_argument in enumerate(ec2_arguments):
                ec2_arguments[index] = ec2_argument.strip("|").replace("|", " ")

            # print(ec2_arguments)

            # print("Searching with given parameters [" + ", ".join(ec2_arguments) + "]")
            for ec2_argument in ec2_arguments:
                # print("searching for *******************",ec2_argument.split())
                ec2_argument = ec2_argument.split()
                for profile in Defaults.aws_accounts:
                    with open("/tmp/ec2_" + profile["name"] + ".csv", "r") as inventory:
                        inventory_reader = csv.reader(inventory, delimiter=',', quoting=csv.QUOTE_MINIMAL)

                        for line in inventory_reader:
                            if all(argument in ",".join(line) for argument in ec2_argument):
                                line = " ".join(line)
                                for argument in ec2_argument:
                                    line = line.replace(argument, style.RED + argument + style.RESET)
                                line = line.split()

                                if detailed:
                                    print(" ".join(line))
                                else:
                                    print(style.GREEN + line[1] + style.RESET, line[2])