# aws-connect-vanity

### Description
The purpose of this project is to create a Lambda that converts a caller's phone number to vanity numbers when they call into an Amazon Connect Contact Center. The best 5 resulting vanity numbers along with the caller's number will be saved in a DynamoDB table.
An Amazon Connect contact flow will be created that looks at the caller's phone number and repeats the vanity possibilities that come back from the Lambda function. The requirements state to provide 3 vanity numbers to the caller, but since the requirements were to get 5 vanity numbers I had the prompt say all 5 since I didn't have time to set up some type of ranking to choose the best of the 5.

The live number for this Amazon Connect environment is: **+1 213-737-8507**
(for a short while)



1. Include explanation for why I chose to implement the solution the way I did and any struggles and problems I had to overcome while implementing the solution.


#### With more time, other features I would have included or implemented for the "real world"!
 1. I would have set up ranking for the vanity numbers to choose numbers that had more words, or only used the last 7 digits.
 2. For ease of implementing, this project only uses US numbers and in the real world a client could need this feature to possibly use international numbers so that would need to be integrated.
 3. This feature would likely be integrated into a more robust contact flow with many choices so maybe this feature could be a choice for a caller to choose while they wait on hold to pass the time. This would require adding a customer input block into the contact flow.
 4. Speaking of customer input blocks, maybe a feature could be to ask the caller's input on if they like a certain vanity number response, and if not create another, or let them choose an option to make as many vanity numbers as they like or until the app no longer has vanity numbers to provide. It would be nice to include an option to exit the feature if the caller is allowed to listen to more vanity numbers.
 5. I would have liked to check out a more comprehensive dictionary list of words.
 6. I would have also liked to test and try different ways to get the voice prompt to pronounce the vanity number output read to the caller. It was not natural sounding and it would need to be for the "real world".

#### Shortcuts
The shortcuts taken due to time constraints that would be bad practice in production are:

- Only formatting the app to use U.S. phone numbers
- Not doing more thorough testing that went beyond the basics and what was provided by the SAM CLI creation
- Not checking to see if I could have been more specific with IAM permissions on the roles used. Cloud providers tout the principle of least privilege and the roles used for Lambda and DynamoDB had full access
- Not checking to see if a more robust dictionary of words was available

### Instructions to build this project and test locally
##### Steps
1. Make sure the following dependencies are installed locally:
- [DynamoDB](https://aws.amazon.com/dynamodb/)
- [Python](https://www.python.org/)
- [Docker](https://www.docker.com/)
- SAM CLI - [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html)
2. Fork or clone this repository
##### Create Local DynamoDB Table (for testing)
3. Locally, I used the following script to create a DynamoDB table. The script can be found in the AWS documentation [here](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Tools.CLI.html).
```
aws dynamodb create-table \
    --table-name customer_Vanity_Numbers \
    --attribute-definitions \
        AttributeName=phoneNum,AttributeType=S \
    --key-schema AttributeName=phoneNum,KeyType=HASH \
    --provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5
```
4. Follow the documentation for each resource to get it started and working locally. With your database active, Docker started, and all other resources installed run the following command to change to the directory that the ```template.yaml``` file is located in. ``` cd lambda-python3.9```
##### Use the SAM CLI to build and test locally
5. Now you can run ```sam build --use-container``` to build the app locally using docker. This command will build the source of your application.
6. Once that completes you can test the app by running ```sam local invoke "LambdaFunction" -e events/event.json``` If this works correctly you should see some output in the terminal showing vanity numbers for the number currently listed in the ```events/event.json``` file. Feel free to change the number in this file and run the ```sam local invoke...``` command listed above to test and see different output.
##### Deploy the application
7. To deploy your application for the first time, run the following ```sam deploy --guided``` This command will package and deploy your application to AWS, with a series of prompts:

* **Stack Name**: The name of the stack to deploy to CloudFormation. This should be unique to your account and region, and a good starting point would be something matching your project name.
* **AWS Region**: The AWS region you want to deploy your app to.
* **Confirm changes before deploy**: If set to yes, any change sets will be shown to you before execution for manual review. If set to no, the AWS SAM CLI will automatically deploy application changes.
* **Allow SAM CLI IAM role creation**: Many AWS SAM templates, including this example, create AWS IAM roles required for the AWS Lambda function(s) included to access AWS services. By default, these are scoped down to minimum required permissions. To deploy an AWS CloudFormation stack which creates or modifies IAM roles, the `CAPABILITY_IAM` value for `capabilities` must be provided. If permission isn't provided through this prompt, to deploy this example you must explicitly pass `--capabilities CAPABILITY_IAM` to the `sam deploy` command.
* **Save arguments to samconfig.toml**: If set to yes, your choices will be saved to a configuration file inside the project, so that in the future you can just re-run `sam deploy` without parameters to deploy changes to your application.





### Cleanup

To delete the sample application that you created, use the AWS CLI. Based on the name used in this application, you can run the following:

```bash
aws cloudformation delete-stack --stack-name aws-connect-vanity
```

## Resources

See the [AWS SAM developer guide](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html) for an introduction to SAM specification, the SAM CLI, and serverless application concepts.

### Dependencies

- [Amazon Connect](https://aws.amazon.com/connect/?nc2=h_ql_prod_ce_con)
- [AWS Lambda](https://aws.amazon.com/lambda/?nc2=h_ql_prod_fs_lbd)
- [DynamoDB](https://aws.amazon.com/dynamodb/)
- [Python](https://www.python.org/)
- [Docker](https://www.docker.com/)
- SAM CLI - [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html)
- Git and GitHub
