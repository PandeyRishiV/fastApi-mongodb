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

@app.get("/api/lists")
async def get_all_lists() -> list[ListSummary]:
    return [i async for i in app.todo_dal.list_todo_lists()]

class NewList(BaseModel):
    name: str

class NewListResponse(BaseModel):
    id: str
    name: str

@app.post("/api/lists",status_code=status.HTTP_201_CREATED)
async def create_todo_list(new_list: NewList) -> NewListResponse:
    return NewListResponse(
        id=app.todo_dal.create_todo_list(new_list.name),
        name=new_list.name
    )

@app.get("/api/lists/{id}")
async def get_list(id: str) -> ToDoList:
    return app.todo_dal.get_todo_list(id)

# @app.delete("/api/lists/{id}")
# async def delete_list()