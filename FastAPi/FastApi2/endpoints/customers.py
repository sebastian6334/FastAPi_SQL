import datetime
from typing import List

from fastapi import Depends, APIRouter, HTTPException
from pydantic.class_validators import Validator
from sqlalchemy.orm import Session
from crud import customer_crud
from validators import ValidatorPesel
import models
from schemas import customer_schemas as schemas


from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/",response_model=schemas.Customer)
def create_customer(
    customer: schemas.CustomerCreate ,db: Session = Depends(get_db)
    ):
    db_customer = customer_crud.get_customer_by_pesel(db, pesel=customer.pesel)
    if db_customer:
        raise HTTPException(status_code=400, detail="Pesel is already registered")
    customer.birthday = ValidatorPesel(customer.pesel).get_birth_date()
    cr = customer_crud.create_customer(db=db, customer=customer)
    return cr

@router.get("/", response_model=List[schemas.Customer])
def read_customers(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
    ):
    customers = customer_crud.get_customers(db, skip=skip, limit=limit)
    return customers    

@router.get("/{customer_id}", response_model=schemas.Customer)
def read_customer(
    customer_id: int, db: Session = Depends(get_db)
    ):
    db_customer = customer_crud.get_customer(db, customer_id=customer_id)
    if db_customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return db_customer

@router.put("/{customer_id}",response_model=schemas.Customer)
def update_customer( *, db:Session = Depends(get_db),
    customer_id: int,
    customer_in: schemas.CustomerUpg,
):
    customer = customer_crud.get_customer(db, customer_id=customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    else:
        customer = customer_crud.update_customer(db, customer=customer, customer_in=customer_in)
    return customer
        
@router.delete("/{customer_id}")
async def delete_customer(
    customer_id: int, db: Session = Depends(get_db)
    ):
    db_customer = customer_crud.get_customer(db, customer_id=customer_id)
    if db_customer is None:
        return{"message:" f"item doesn't exist"}
    else:  
        customer_crud.delete_customer_from_db(db=db, customer_id=customer_id)  
        return {"message:" f"successfully deleted item with id: {customer_id}"}

# @router.put("/customer/{customer_id}", response_model=schemas.Customer_upg)
# async def update_customer(
#     customer_id: int, customer:schemas.Customer_upg, db:Session = Depends(get_db)
#     ):
#     customer_to_update = db.query(models.Customer).filter(models.Customer.id==customer_id).first()
#     customer_to_update.id=customer.id
#     customer_to_update.first_name=customer.first_name
#     customer_to_update.second_name=customer.second_name
#     customer_to_update.age=customer.age
#     db.commit()
#     return customer_to_update
