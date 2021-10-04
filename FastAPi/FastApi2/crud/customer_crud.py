from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import update
from validators import ValidatorPesel
import models
from schemas import customer_schemas as schemas

def get_customer(db: Session, customer_id:int):
    return db.query(models.Customer).filter(models.Customer.id == customer_id).first()

def get_customer_by_pesel(db: Session, pesel:str):
    return db.query(models.Customer).filter(models.Customer.pesel == pesel).first()

def get_customers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Customer).offset(skip).limit(limit).all()
    
def create_customer(db: Session, customer: schemas):
    db_customer = models.Customer(**customer.dict())
    print(db_customer)
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer       

def update_customer(db: Session, *, customer: models.Customer, customer_in: schemas.CustomerUpg) -> models.Customer:
    item_data = jsonable_encoder(customer)
    update_data = customer_in.dict(skip_defaults=True)
    for field in item_data:
        if field in update_data:
            setattr(customer, field, update_data[field])
    db.add(customer)
    db.commit()
    db.refresh(customer)
    return customer
    
def delete_customer_from_db(db:Session, customer_id: int):
    db.query(models.Customer).filter(models.Customer.id == customer_id).delete()
    db.commit()    