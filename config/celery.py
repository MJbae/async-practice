from __future__ import absolute_import
from celery import Celery
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

app = Celery('config',
             broker='redis://localhost:6379/1',
             backend='rpc://',
             include=['cars.tasks'])

