from __future__ import absolute_import
from celery import Celery
import os

from config.settings import CELERY_BROKER_URL

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
print(f'CELERY_BROKER_URL: {CELERY_BROKER_URL}')
app = Celery('config',
             broker=CELERY_BROKER_URL,
             backend=None,
             include=['cars.tasks'])

