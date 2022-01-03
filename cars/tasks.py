import json
from asyncio import exceptions

from cars.models import Car, Customer
from config.celery import app


@app.task
def update_car_name(car_id, customer_id):
    try:
        car = Car.objects.get(id=car_id)
    except Car.DoesNotExist:
        return {"result": "fail", "message": "car_id가 올바르지 않습니다."}

    try:
        customer = Customer.objects.get(id=customer_id)
    except Customer.DoesNotExist:
        return {"result": "fail", "message": "customer_id가 올바르지 않습니다."}

    modified_name = f"{car.name}'s {customer.name}"
    car.name = modified_name
    car.save()

    return {"result": "success"}
