import json

def event_handler(event, context):
    body = {
        "event": event,
    }

    print("log_group_name: {}",context.log_group_name)
    print("log_stream_name: {}", context.log_stream_name)

    ret = {
        "statusCode": 200,
        "body": json.dumps(body),
    }

    print(ret)
    return ret
