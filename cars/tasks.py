from celery import shared_task


@shared_task
def update_car_name(car_name, customer_name):
    return customer_name + "'s " + car_name
