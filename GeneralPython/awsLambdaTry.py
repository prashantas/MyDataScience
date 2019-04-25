import json
import os
import decimal
from urllib.parse import urlparse  # Python 3
str_encode = str.encode
from string import ascii_lowercase
from string import ascii_uppercase
import base64
import string
from math import floor

import boto3
dynamodb = boto3.resource('dynamodb')

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)
        
def toBase62(num, b=62):
    if b <= 0 or b > 62:
        return 0
    base = string.digits + ascii_lowercase + ascii_uppercase
    r = num % b
    res = base[r]
    q = floor(num / b)
    while q:
        r = q % b
        q = floor(q / b)
        res = base[int(r)] + res
    return res


def toBase10(num, b=62):
    base = string.digits + ascii_lowercase + ascii_uppercase
    print("base:{}".format(base))
    limit = len(num)
    res = 0
    for i in range(limit):
        res = b * res + base.find(num[i])
    return res
        

def lambda_handler(event, context):
    print("############## inside lambda handler &&&&&&&&&&&&&&&&&&&&&&&&&&&")
    #table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])
    table = dynamodb.Table('WEB_URL')
    tableLastid = dynamodb.Table('LAST_ID')
    
    print("####EVENT:::"+ str(event))
    token = event["token"] or event['pathParameters']['token'] or event['queryStringParameters']['token'] or 1
    print("######## after token read...{}".format(token))
    #ID = event['pathParameters']['id']
    ID = toBase10(str(token))
    #ID = int( str(token),10)
    print("ID after tobase10:{}".format(ID))
    
    print("ID:"+str(ID))

    # fetch todo from the database
    result = table.get_item(
        Key={
            "ID": int(ID)
        }
    )
    
    print("result: "+ str(result))

    original_url = result['Item']['TEXT']
    # create a response
    response = {
        "statusCode": 200,
        #"body": json.dumps(result['Item']['TEXT'],cls=DecimalEncoder)
        "original_url": json.dumps(original_url,cls=DecimalEncoder)
    }

    return response


    ######################################################################################################################
    #######################################################################################################################
    ######################################################################################################################
    short_url_post $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


    import json
import os
import decimal
from urllib.parse import urlparse  # Python 3
str_encode = str.encode
from string import ascii_lowercase
from string import ascii_uppercase
import base64
import string
from math import floor
    
import boto3
dynamodb = boto3.resource('dynamodb')

def toBase62(num, b=62):
    if b <= 0 or b > 62:
        return 0
    base = string.digits + ascii_lowercase + ascii_uppercase
    r = num % b
    res = base[r]
    q = floor(num / b)
    while q:
        r = q % b
        q = floor(q / b)
        res = base[int(r)] + res
    return res


def toBase10(num, b=62):
    base = string.digits + ascii_lowercase + ascii_uppercase
    limit = len(num)
    res = 0
    for i in range(limit):
        res = b * res + base.find(num[i])
    return res

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)
    
def get_last_id():
    table = dynamodb.Table('LAST_ID')
    response = table.scan(Limit=1)
    data = response['Items']
    print("## inside get_last_id: data:"+ str(data))
    return int(data[0]["lastid"])
    

def lambda_handler(event, context):
    # TODO implement
    #original_url = str_encode(request.form.get('url'))
    tableWeb = dynamodb.Table('WEB_URL')
    tableLastid = dynamodb.Table('LAST_ID')
    
    original_url = event['url']
    if urlparse(original_url).scheme == '':
        url = 'http://' + original_url
    else:
        url = original_url
    
    print("###ulr:"+str(url))    
    last_id = get_last_id()
    print("#### the last_id:{}".format(last_id))
    
    responseLastid = tableLastid.update_item(
        Key={
            'ID': 3
        },
        UpdateExpression="set lastid = :r",
        ExpressionAttributeValues={
        ':r': last_id+1,
        },
        ReturnValues="UPDATED_NEW"
    )
    
    print("# the last_id table updated")
    
    response = tableWeb.put_item(
        Item={
            'ID': last_id+1,
            #'TEXT': base64.urlsafe_b64encode(url)
            'TEXT': url
            
        }
    )
    
    encoded_string = toBase62(last_id+1)
    
    return {
        'statusCode': 200,
        'last_id': last_id,
        'token':encoded_string
        


    }

    
