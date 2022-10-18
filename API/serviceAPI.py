from fastapi import FastAPI

from config import db

service = FastAPI()

@service.get('/get-order-data')
def get_data(restaurant: str):
    data = db.get_data_from_database(restaurant)
    return data