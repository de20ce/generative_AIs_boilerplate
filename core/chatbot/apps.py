from django.apps import AppConfig

import sys
from urllib.parse import urlparse

from django.conf import settings


class ChatbotConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'chatbot'

    def ready(self) -> None:
        #return super().ready()

        if settings.DEV_SERVER and settings.USE_NGROK:
            from pyngrok import ngrok
            addrport = urlparse("http://{}".format(sys.argv[-1]))
            port = addrport.port if addrport.netloc and addrport.port else 8000

            # Open a ngrok tunnel to the dev server
            public_url = ngrok.connect(port).public_url
            print("ngrok tunnel \"{}\" -> \"http://0.0.0.0:{}\"".format(public_url, port))

            # Update any base URLs or webhooks to use the public ngrok URL
            settings.BASE_URL = public_url 
            ChatbotConfig.init_webhooks(public_url)

