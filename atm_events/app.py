import json

def event_handler(event, context):
    body = {
        "event": event,
    }
    ret = {
        "statusCode": 200,
        "log": {
            "log_group_name": context.log_group_name,
            "log_stream_name": context.log_stream_name,
        },
        "body": json.dumps(body),
    }

    print(ret)
    return ret
