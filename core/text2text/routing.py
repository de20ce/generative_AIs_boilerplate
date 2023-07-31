
from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r"^ws/text2text/$", consumers.ChatConsumer.as_asgi()),
]
