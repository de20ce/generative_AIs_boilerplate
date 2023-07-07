#from django.test import TestCase

# Create your tests here.

import pytest
import json
from django.test import override_settings

from channels.generic.websocket import (
    AsyncJsonWebsocketConsumer,
    AsyncWebsocketConsumer,
    JsonWebsocketConsumer,
    WebsocketConsumer,
)
from channels.layers import get_channel_layer
from channels.testing import WebsocketCommunicator

from chatbot.consumers import ChatConsumer

import asyncio
loop = asyncio.get_event_loop()
chat_app = ChatConsumer()
#print(chat_app.channel_name)
communicator = WebsocketCommunicator(chat_app, "/chatbot/")
connected, _ = loop.run_until_complete(communicator.connect())
channel_layer = get_channel_layer()
# Test that the specific channel layer is retrieved
assert channel_layer is not None
print(channel_layer)
print(channel_layer.__dict__)   
channel_name = list(channel_layer.channels.keys())[0]
# Test that the websocket channel was added to the group on connect
message = {"type": "websocket.receive", "text": "hello world"}
#message_data=json.dumps(message)
# loop.run_until_complete(communicator.send_to( message["text"]))
loop.run_until_complete(channel_layer.send(channel_name, message))
response = loop.run_until_complete(communicator.receive_from())
