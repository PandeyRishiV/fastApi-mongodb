from pydantic import BaseModel
from motor.motor_asyncio import AsyncIOMotorCollection


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
