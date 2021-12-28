from __future__ import absolute_import
from celery import Celery

app = Celery('config',
             broker='amqp://maxwell:passwordOfmaxwell123@localhost/maxwell_vhost',
             backend='rpc://')
