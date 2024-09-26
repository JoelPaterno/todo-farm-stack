#data access layer
from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorCollection
from pymongo import ReturnDocument

from pydantic import BaseModel
from uuid import uuid4

class ListSummary(BaseModel):
    id: str
    name: str
    item_count: int

    @staticmethod
    def from_doc(doc) -> "ListSummary":
        return ListSummary(
            id=str(doc["_id"]),
            name=doc["name"],
            item_count=doc["item_count"]
        ) 
class ToDoListItem(BaseModel):
    id: str
    label: str
    checked: bool

    @staticmethod
    def from_doc(item) -> "ToDoListItem":
        return ToDoListItem(
            
        )
