from uuid import uuid4
from pydantic import BaseModel
from motor.motor_asyncio import AsyncIOMotorCollection
from bson import ObjectId
from pymongo import ReturnDocument

class ListSummary(BaseModel):
    id: str
    name: str
    item_count: int

    @staticmethod
    def from_doc(doc) -> "ListSummary":
        return ListSummary(
            id=str(doc["_id"]),
            name=str(doc["name"]),
            item_count=str(doc["item_count"])
        )

class ToDoListItem(BaseModel):
    id: str
    label: str
    checked: bool

    @staticmethod
    def from_doc(item) -> "ToDoListItem":
        return ToDoListItem(
            id=item["id"],
            label=item["label"],
            checked=bool(item["checked"])
        )

class ToDoList(BaseModel):
    id=str
    name=str
    items=list[ToDoListItem]

    @staticmethod
    def from_doc(doc) -> "ToDoList":
        return ToDoList(
            id=str(doc["_id"]),
            name=doc["name"],
            items=[ToDoListItem.from_doc(item) for item in doc["items"]]
        )

class ToDoDAL:
    def __init__(self, todo_collection: AsyncIOMotorCollection):
        self._todo_collection = todo_collection
