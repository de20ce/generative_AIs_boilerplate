import os

from celery import Celery

from django.conf import settings


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
app = Celery("core")
# app = Celery('file_upload', broker_pool_limit=1, broker=settings.CELERY_RESULT_BACKEND,
#           result_backend=settings.CELERY_BROKER_URL)  
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
