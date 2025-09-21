from fastapi import FastAPI
from pydantic import BaseModel
import pymongo

app = FastAPI()
mongoClient = pymongo.MongoClient("mongodb+srv://pandeyrishiv_db_user:HRishiPandey06!@cluster0.jphkthz.mongodb.net/")
mongoDb = mongoClient["admin"]

@app.get("/")
def read_root():
    return {"Hello" : "World"}