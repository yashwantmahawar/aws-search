import sys
from default import Defaults
from operations import Operation


def main():

    defaults = Defaults()
    op = Operation()
    aws_profiles_list = defaults.get_aws_profiles_list()

    if op.find_operation(sys.argv) == "update":
        # this if block belongs to all update oprations
        if all(word in sys.argv[1:] for word in ["update", "profile"]):

            if sys.argv[3] not in aws_profiles_list and sys.argv[3].lower() != "all":
                print("Invalid Profile")
                return None
            else:
                profile = sys.argv[3].lower()

            # Update ec2 profile
            if "ec2" == sys.argv[4].lower():
                op.update_ec2(profile, defaults)

            # Update TG with given profile
            if "tg" == sys.argv[4].lower():
                op.update_tg(profile, defaults)

            # todo add more resources
    else:
        # this else block belongs to all search operations
        if sys.argv[1] == "ec2":
            op.search_ec2(sys.argv[2:])
        if sys.argv[1] == "tg":
            op.search_tg(sys.argv[2:])

if __name__ == '__main__':
    main()
