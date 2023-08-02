from asgiref.sync import async_to_sync
from celery import shared_task
from channels.generic.websocket import WebsocketConsumer
from transformers import pipeline
import json
import logging
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

# Load the template and tokenizer
generator = pipeline("text-generation", model='distilgpt2')

from .tasks import get_response
class ChatConsumer(WebsocketConsumer):
    def receive(self, text_data):
        logging.info(f'Received text: {text_data}')

        text_data_json = json.loads(text_data)
        logging.info(f'just before sending to engine: {text_data_json}')

        # Client input
        user_input = text_data_json.get('text', '')

        if user_input:
            # Call the task synchronously
            response_data = get_response(user_input)
            
        else:
            response_data = "Please, you should enter a text"

        async_to_sync(self.channel_layer.send)(
            self.channel_name,
            {
                "type": "chat_message",
                "text": [{"msg": response_data, "source": "bot"}],
            }
        )

    def chat_message(self, event):
        text = event["text"]
        self.send(text_data=json.dumps({"text": text}))