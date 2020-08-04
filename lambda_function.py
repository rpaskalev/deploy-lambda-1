import json


def lambda_handler(event, context):
    print(json.dumps(event))
    return {
        'status': 200,
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': json.dumps({'message': 'Hello-OK'})
    }