from enum import Enum
from typing import List, Optional
from fastapi import FastAPI
from pydantic import BaseModel
import pymongo

app = FastAPI()

# Mongo DB connection, db and collection
mongoClient = pymongo.MongoClient("mongodb+srv://pandeyrishiv_db_user:HRishiPandey06!@cluster0.jphkthz.mongodb.net/")
mongoDb = mongoClient["admin"]
collection = mongoDb["users"]

@app.get("/")
async def read_root():
    return {"Hello" : mongoDb.list_collection_names()}
