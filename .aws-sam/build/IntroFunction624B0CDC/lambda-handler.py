import json

def main(event, context):
    # save event to logs
    print(event)

    return {
        'statusCode': 200,
        'body': event,

        # when invoking the function locally with SAM,
        # the event object will be empty
        # here's an alternative JSON output
        # 'body': json.dumps({
        #     'hello': 'world'
        # }),
    }