from celery import Celery
from django.conf import settings
import os


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")

app = Celery('tasks', broker=getattr(settings, 'CELERY_BROKER_URL'))
