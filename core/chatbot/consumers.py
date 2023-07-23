import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import logging
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
# Connection  refused (kombu)
# more info here: https://docs.celeryq.dev/en/latest/userguide/calling.html#connection-error-handling
from celery.utils.log import get_logger
logger = get_logger(__name__)


from .tasks import get_response

class ChatConsumer(WebsocketConsumer):
    
    def receive(self, text_data):
        logging.info(f'Received text: {text_data}')

        text_data_json = json.loads(text_data)
        logging.info(f'just before sending to engine: {text_data_json}')
        try:
            #get_response.delay(self.channel_name, text_data)
            res = get_response.apply_async((self.channel_name, text_data_json), ignore_result=False)
            print("In result", res.get())
            
        except get_response.OperationalError as exc:
            logger.exception('Sending task raised: %r', exc)

        async_to_sync(self.channel_layer.send)(
            self.channel_name,
            {
                "type": "chat_message",
                "text": {"msg": text_data_json["text"], "source": "user"},
            }
        )

    def chat_message(self, event):
        text = event["text"]
        self.send(text_data=json.dumps({"text": text}))