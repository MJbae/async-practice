from __future__ import absolute_import
from celery import Celery

app = Celery('config',
             broker='redis://localhost:6379/1',
             backend='rpc://',
             include=['cars.tasks'])
