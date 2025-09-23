from motor.motor_asyncio import AsyncIOMotorClient
from contextlib import asynccontextmanager
from fastapi import FastAPI, status
import os

from pydantic import BaseModel

from backend.src.dal import ListSummary, ToDoDAL, ToDoList

collection = "todo_lists"
DEBUG = os.environ.get("DEBUG","").strip().lower() in {"1","true","on","yes"}
mongoClient = os.environ["MONGODB_URL"]
