from typing import Union
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel
import pymongo
import os

app = FastAPI()
load_dotenv()
# Mongo DB connection, db and collection
mongoClient = pymongo.MongoClient(os.getenv("MONGODB_URL"))
mongoDb = mongoClient["admin"]
collection = mongoDb["users"]

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

@app.get("/")
async def read_root():
    return {"DB names" : mongoClient.list_database_names()}

@app.get("/items/{id}")
def items(id: int, q: Union[str, None] = None):
    return {"item id": id, "query":q}

@app.put("/items/{id}")
def update_item(id: int, item: Item):
    return {id: id,"name": item.name}