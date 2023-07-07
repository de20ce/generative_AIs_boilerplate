from asgiref.sync import async_to_sync
from celery import shared_task
from channels.layers import get_channel_layer
import json

channel_layer = get_channel_layer()

def dummy_response(input):
    if input != "":
        return input
    else:
        return  "Please, you should enter a text"

@shared_task
def get_response(channel_name, input_data):
    response = dummy_response(input_data)
    response=json.dumps({"text": response})
    response_data = response

    async_to_sync(channel_layer.send)(
        channel_name,
        {
            "type": "chat.message",
            "text": {"msg": response_data, "source": "bot"},
        },
    )
