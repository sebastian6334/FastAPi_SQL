from sqlalchemy.sql.sqltypes import Date
from typing import Optional
from pydantic import BaseModel

class ItemBase(BaseModel):
    name: str
    description: Optional[str] = None

class ItemCreate(ItemBase):
    name: str
    description: str

class ItemUpdate(ItemBase):
    name: str
    description: str

class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True