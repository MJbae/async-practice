from __future__ import absolute_import
from celery import Celery
import os

from config.settings import CELERY_BROKER_URL

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
app = Celery('config',
             broker=CELERY_BROKER_URL,
             backend='django-db',
             include=['cars.tasks'])

app.autodiscover_tasks()
