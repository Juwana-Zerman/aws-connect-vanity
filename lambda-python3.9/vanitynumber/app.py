import json
import boto3
from botocore import endpoint
#from phonenumbers.phonenumberutil import phonenumbers
import os
#import vanitynumber
from wordify import *


# Help with examples working with DynamoDB, Boto3, and Python https://highlandsolutions.com/blog/hands-on-examples-for-working-with-dynamodb-boto3-and-python

# Python phonenumbers module https://pypi.org/project/phonenumbers/
def phoneNumberParse(phoneNum):
    import phonenumbers
    try:
        number = phonenumbers.parse(phoneNum, None)
        if phonenumbers.is_valid_number(number):
            return {
                "country_code": number.country_code,
                "phoneNum": number.national_number
            }
        else:
            return None
    except:
        print("This isn't a valid contact number.")
        return None

# CRUD help from AWS Documentation https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GettingStarted.Python.03.html#GettingStarted.Python.03.03
def update_phoneNumber(phoneNum, vanityNumber, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url='http://localhost:8000').Table('customer_Vanity_Numbers')

    table = dynamodb.Table('customer_Vanity_Numbers')

    return table.update_item(
            Key={
                'ContactNumber': phoneNum,
                'VanityNumbers': vanityNumber
            },
            ReturnValues= "UPDATED_NEW"
    )
# CRUD help from AWS Documentation https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GettingStarted.Python.03.html#GettingStarted.Python.03.03
# and
# Query help from GetCustomerInfo https://blogs.perficient.com/2017/10/11/3-steps-on-creating-premium-caller-contact-flow-with-amazon-connect/
def get_phoneNumber(phoneNum, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url='http://localhost:8000').Table('customer_Vanity_Numbers')

    table = dynamodb.Table('customer_Vanity_Numbers')

    try:
        response = table.query(
            KeyConditionExpression="ContactNumber = :v1",
            ExpressionAttributeValues={
                ':v1': phoneNum,
            },
            ScanIndexForward=False,
            Limit=1
        )
        items = response['Items']

        if len(items) == 0:
            return None
        else:
            return items[0]
    except:
        return None

def lambda_handler(event, context):
    phoneNumber = event['Details']['ContactData']['CustomerEndpoint']['Address']
    print("Customer Phone Number: " + phoneNumber)
    if not phoneNumberParse(phoneNumber):
        return {"message": "failed"}

    number = str(phoneNumberParse(phoneNumber).get('phoneNum'))
    print("The contact number is: " + phoneNumber)
    vanityNumber = find_words_from_numbers(
        number, max_number_results_to_output=5)
    if not get_phoneNumber(phoneNumber):
        update_phoneNumber(phoneNumber, vanityNumber)
    print("The best vanity numbers for this number are: " + {get_phoneNumber(phoneNumber).get('VanityNumbers')})
    return {"VanityNumber1": get_phoneNumber(phoneNumber).get('VanityNumbers')[0],
            "VanityNumber2": get_phoneNumber(phoneNumber).get('VanityNumbers')[1],
            "VanityNumber3": get_phoneNumber(phoneNumber).get('VanityNumbers')[2],
            "VanityNumber4": get_phoneNumber(phoneNumber).get('VanityNumbers')[3],
            "VanityNumber5": get_phoneNumber(phoneNumber).get('VanityNumbers')[4]
            }
