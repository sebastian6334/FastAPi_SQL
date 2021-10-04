from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
import models
from schemas import address_schemas as schemas

def get_address(db:Session, address_id:int):
    return db.query(models.Addresses).filter(models.Addresses.id == address_id).first()

def get_addresses(db:Session, skip = 0, limit: int = 100):
    return db.query(models.Addresses).offset(skip).limit(limit).all()

def create_customer_address(db:Session, address: schemas.AddressCreate, customer_id: int):
    db_address = models.Addresses(**address.dict(), owner_id=customer_id)
    db.add(db_address)
    db.commit()
    db.refresh(db_address)
    return db_address    

def update_address(db_session: Session, *, address: models.Addresses, address_in: schemas.AddressCreate) -> models.Addresses:
    address_data = jsonable_encoder(address)
    update_data = address_in.dict(skip_defaults=True)
    for field in address_data:
        if field in update_data:
            setattr(address, field, update_data[field])
    db_session.add(address)
    db_session.commit()
    db_session.refresh(address)
    return address

def delete_address_from_db(db:Session, address_id: int):
    db.query(models.Addresses).filter(models.Addresses.id == address_id).delete()
    db.commit()