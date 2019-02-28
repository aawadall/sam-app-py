import json

def event_handler(event, context):
    body = {
    }
    ret = {
        "statusCode": 200,
        "body": json.dumps(body),
    }

    print(ret)
    return ret
