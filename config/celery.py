from __future__ import absolute_import
from celery import Celery
from celery.schedules import crontab

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
app = Celery("config")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()

app.conf.beat_schedule = {
    "destroy-all-cars": {
        "task": "cars.tasks.destroy_cars",
        "schedule": crontab(),
        "args": (),
    },
}
