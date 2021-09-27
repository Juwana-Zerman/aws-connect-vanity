# aws-connect-vanity

The purpose of this project is to create a Lambda that converts a caller's phone number to vanity numbers when they call into an Amazon Connect Contact Center. The best 5 resulting vanity numbers along with the caller's number will be saved in a DynamoDB table.
An Amazon Connect contact flow will be created that looks at the caller's phone number and says 3 vanity possibilities that come back from the Lambda function.

1. Include explanation for why I chose to implement the solution the way I did and any struggles and problems I had to overcome while implementing the solution.
2. Did I take any shortcuts that would be a bad practice in productions?
3. With more time, what other features would I have included? Anything to add for the "real world"?

### Steps

##### Create Local DynamoDB Table (for testing)
Locally, I used the following script to create a DynamoDB table. The script can be found in the AWS documentation [here](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Tools.CLI.html).
```
aws dynamodb create-table \
    --table-name customer_Vanity_Numbers \
    --attribute-definitions \
        AttributeName=phoneNum,AttributeType=S \
    --key-schema AttributeName=phoneNum,KeyType=HASH \
    --provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5
```


### Dependencies
- Amazon Connect
- AWS Lambda
- DynamoDB
- Python
- Amazon Lex
- Git and GitHub
