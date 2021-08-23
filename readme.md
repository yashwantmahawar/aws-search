# AWS Search Tool

## Description 

This tool is to made search easier for aws resources. like for every search you have to goto aws and change the service and check for resources. What is someone will dose for you and also if you can manage inventory of your resources on your local. that will make your search fast. 

## How to use this

#### Step1: create new file `config.json` at cloned location
```json
{
  "default_aws_profile_name" : "default_aws_profile_name",
  "default_aws_region" : "ap-south-1",
  "supported_resources" : ["ec2","tg"],
  "inventory": "/opt/aws_search",
  "aws_accounts" : [
    {
      "name": "account1",
      "arn": "arn:aws:iam::XXXXXXXXXXXX:role/automation_readonly"
    },
    {
      "name": "account2",
      "arn": "arn:aws:iam::XXXXXXXXXXXX:role/automation_readonly"
    },
    {
      "name": "account3",
      "arn": "arn:aws:iam::XXXXXXXXXXXX:role/automation_readonly"
    }
  ]
}
```

#### Setup alias in your bash profile
```shell
alias search="sudo python3 localpath/main.py"
```

#### Update your local inventory
```shell
search update profile all ec2   # for all profiles
search update profile account1 ec2   # for account1 profile only

search update profile all tg   # for all profiles
search update profile account1 tg   # for account1 profile only 
```

`setup completed, now you are ready to use this tool`

#### search your resources
```shell
❯ search ec2 nonprod sanctuary
Searching with given parameters [nonprod, sanctuary]
10.10.21.3 nonprod-sanctuary-scheduler
10.10.21.2 nonprod-sanctuary-frontend
10.10.21.3 nonprod-sanctuary-scheduler
total instance found 3

❯ search ec2 prod sanctuary
Searching with given parameters [prod, sanctuary]
10.10.11.1 prod-sanctuary-backend
10.10.11.1 prod-sanctuary-backend
10.10.11.2 prod-sanctuary-frontend
10.10.21.3 nonprod-sanctuary-scheduler
10.10.21.2 nonprod-sanctuary-frontend
10.10.21.3 nonprod-sanctuary-scheduler
total instance found 6

❯ search ec2 sanctuary scheduler
Searching with given parameters [sanctuary, scheduler]
10.10.21.3 nonprod-sanctuary-scheduler
10.10.21.3 nonprod-sanctuary-scheduler
total instance found 2

❯ search ec2 nonprod sanctuary
Searching with given parameters [nonprod, sanctuary]
10.10.21.3 nonprod-sanctuary-scheduler
10.10.21.2 nonprod-sanctuary-frontend
10.10.21.3 nonprod-sanctuary-scheduler
total instance found 3
```
