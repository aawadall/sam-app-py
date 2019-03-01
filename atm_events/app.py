import json
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def event_handler(event, context):

    body = {
        "event": event,
    }

    logger.info("log_group_name: {}".format(context.log_group_name))
    logger.info("log_stream_name: {}".format(context.log_stream_name))

    ret = {
        "statusCode": 200,
        "body": json.dumps(body),
    }

    print(ret)
    return ret
