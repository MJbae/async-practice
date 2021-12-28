from celery import shared_task
import time


@shared_task
def update_car_name(car_name, customer_name):
    time.sleep(3)
    return customer_name + "'s " + car_name
