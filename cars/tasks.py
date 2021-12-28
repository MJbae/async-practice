from config.celery import app


@app.task
def update_car_name(car_name, customer_name):
    return customer_name + "'s " + car_name
