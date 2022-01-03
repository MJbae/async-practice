import json
from asyncio import exceptions

from cars.models import Car, Customer
from config.celery import app


@app.task
def update_car_name(car_id, customer_id):
    response = {"result": "success"}
    try:
        car = Car.objects.get(id=car_id)
    except Car.DoesNotExist:
        response["result"] = "car_id가 올바르지 않습니다."
        return json.dumps(response)

    try:
        customer = Customer.objects.get(id=customer_id)
    except Customer.DoesNotExist:
        response["result"] = "customer_id가 올바르지 않습니다."
        return json.dumps(response)

    modified_name = f"{car.name}'s {customer.name}"
    car.name = modified_name
    car.save()

    return json.dumps(response)
