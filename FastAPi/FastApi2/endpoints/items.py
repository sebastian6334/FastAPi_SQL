from sqlalchemy.sql.operators import exists
from typing import List

from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from crud import customer_crud
from crud import item_crud

import models
import schemas.item_schemas as schemas


from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/{customer_id}/items/", response_model=schemas.Item)
def create_item_for_customer(
    customer_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
    ):
    search_customer = customer_crud.get_customer(db, customer_id=customer_id)
    if search_customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return item_crud.create_customer_item(db=db, item=item, customer_id=customer_id)     

@router.get("/", response_model=List[schemas.Item])
def read_items(
    skip:int = 0, limit: int = 100, db: Session = Depends(get_db)
    ):
    items = item_crud.get_items(db, skip=skip, limit=limit)
    return items

@router.get("/{item_id}", response_model=schemas.Item)
async def read_item(
    item_id: int, db: Session = Depends(get_db)
    ):
    db_item = item_crud.get_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@router.put("/{item_id}",response_model=schemas.Item)
def update_item( *, db:Session = Depends(get_db),
    item_id: int,
    item_in: schemas.ItemUpdate,
):
    search_item = item_crud.get_item(db, item_id=item_id)
    if search_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    item = item_crud.get_item(db, item_id=item_id)
    if item:
        item = item_crud.update_item(db_session=db, item=item, item_in=item_in)
    return item

@router.delete("/{item_id}")
async def delete_item(
    item_id: int, db: Session = Depends(get_db)
    ):
    search_item = item_crud.get_item(db, item_id=item_id)
    if search_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    db_items = item_crud.get_item(db, item_id=item_id)
    if db_items is None:
        return{"message:" f"item doesn't exist"}
    else:  
        item_crud.delete_item_from_db(db=db, item_id=item_id)  
        return {"message:" f"successfully deleted item with id: {item_id}"}
        

# @router.put("/items/{item_id}", response_model=schemas.Item)
# async def update_item(
#     item_id: int, item:schemas.Item, db:Session = Depends(get_db)
#     ):
#     item_to_update = db.query(models.Item).filter(models.Item.id==item_id).first()
#     item_to_update.id=item.id
#     item_to_update.name=item.name
#     item_to_update.description=item.description
#     item_to_update.owner_id=item.owner_id
#     db.commit()
#     return item_to_update
