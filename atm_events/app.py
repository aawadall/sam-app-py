import json

def event_handler(event, context):
    body = {
        "context": json.dumps(context),
    }
    ret = {
        "statusCode": 200,
        "body": json.dumps(body),
    }

    print(ret)
    return ret
