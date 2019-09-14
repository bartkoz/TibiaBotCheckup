from celery import Celery
from django.conf import settings

app = Celery('tasks', broker=getattr(settings, 'CELERY_BROKER_URL'))
