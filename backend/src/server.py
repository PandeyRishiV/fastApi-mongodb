from motor.motor_asyncio import AsyncIOMotorClient
from contextlib import asynccontextmanager
from fastapi import FastAPI, status
import os

from pydantic import BaseModel

from backend.src.dal import ListSummary, ToDoDAL, ToDoList

collection = "todo_lists"
DEBUG = os.environ.get("DEBUG","").strip().lower() in {"1","true","on","yes"}
mongoClient = os.environ["MONGODB_URL"]

@asynccontextmanager
async def lifespan(app: FastAPI):

    client = AsyncIOMotorClient(mongoClient)
    db = client.get_default_database()

    pong = await db.command("ping")
    if(int(pong["ok"]) != 1): raise Exception("Cluster connection is not ok")

    todo_lists = db.get_collection(collection)
    app.todo_dal = ToDoDAL(todo_lists)

    yield

    client.close()

app = FastAPI(lifespan=lifespan, debug=DEBUG)
