from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import update

import models
import schemas.item_schemas as schemas

def get_item(db:Session, item_id:int):
    return db.query(models.Item).filter(models.Item.id == item_id).first()

def get_items(db:Session, skip = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()

def create_customer_item(db:Session, item: schemas.ItemCreate, customer_id: int):
    db_item = models.Item(**item.dict(), owner_id=customer_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item    

def update_item(db_session: Session, *, item: models.Item, item_in: schemas.ItemUpdate) -> models.Item:
    item_data = jsonable_encoder(item)
    update_data = item_in.dict(skip_defaults=True)
    for field in item_data:
        if field in update_data:
            setattr(item, field, update_data[field])
    db_session.add(item)
    db_session.commit()
    db_session.refresh(item)
    return item

def delete_item_from_db(db:Session, item_id: int):
    db.query(models.Item).filter(models.Item.id == item_id).delete()
    db.commit()