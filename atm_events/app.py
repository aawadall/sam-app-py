import json

def event_handler(event, context):
    body = {
        "event": event,
    }
    ret = {
        "statusCode": 200,
        "body": json.dumps(body),
    }

    print(ret)
    return ret
