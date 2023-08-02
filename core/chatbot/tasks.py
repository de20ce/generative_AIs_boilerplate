from asgiref.sync import async_to_sync
from celery import shared_task
from channels.layers import get_channel_layer
import json
import logging
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

channel_layer = get_channel_layer()

def dummy_response(input):
    if input['text'] != "":
        return input['text'] + " again"
    else:
        return  "Please, you should enter a text"

@shared_task
def get_response(channel_name, input_data):
    logging.info(f'channel: {channel_name}, input: {input_data}')
    logging.info(f'input keys in get_Response : {input_data.keys()}')
    response = dummy_response(input_data)
    
    response_data = response # should be serialized if object

    async_to_sync(channel_layer.send)(
        channel_name,
        {
            "type": "chat_message",
            "text": [{"msg": response_data, "source": "bot"}],
        },
    )
    logging.info(f'after sending channel step  : {channel_name}, input: {response_data}')
