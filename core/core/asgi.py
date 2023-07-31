"""
ASGI config for core project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application
import chatbot.routing
import text2text.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

asgi_chatbot_app = get_asgi_application()

application = ProtocolTypeRouter(
    {
        "http": asgi_chatbot_app,
        "websocket": AllowedHostsOriginValidator(
            AuthMiddlewareStack(URLRouter(text2text.routing.websocket_urlpatterns))
        ),
    }
)


