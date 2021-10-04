from typing import List

from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from crud import customer_crud
from crud import address_crud

import models
from schemas import address_schemas as schemas

from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/{customer_id}/address/", response_model=schemas.Address)
def create_address_for_customer(
    customer_id: int, address: schemas.AddressCreate, db: Session = Depends(get_db)
    ):
    search_customer = customer_crud.get_customer(db, customer_id=customer_id)
    if search_customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    if customer_id:
        return address_crud.create_customer_address(db=db, address=address, customer_id=customer_id)     
    else:
        return{"message:" f"customer doesn't exist"}        

@router.get("/",response_model=List[schemas.Address])
def read_addresses(
    skip:int = 0, limit: int = 100, db: Session = Depends(get_db)
    ):
    addresses = address_crud.get_addresses(db, skip=skip, limit=limit)
    return addresses

@router.get("/{address_id}", response_model=schemas.Address)
async def read_address(
    address_id: int, db: Session = Depends(get_db)
    ):
    db_address = address_crud.get_address(db, address_id=address_id)
    if db_address is None:
        raise HTTPException(status_code=404, detail="Address not found")
    return db_address

@router.put("/{address_id}",response_model=schemas.Address)
def update_address( *, db:Session = Depends(get_db),
    address_id: int,
    address_in: schemas.AddressCreate,
    ):
    search_address = address_crud.get_address(db, address_id=address_id)
    if search_address is None:
        raise HTTPException(status_code=404, detail="Address not found")
    address = address_crud.get_address(db, address_id=address_id)
    if address:
        return address_crud.update_address(db, address=address, address_in=address_in)

@router.delete("/{address_id}")
async def delete_address(
    address_id: int, db: Session = Depends(get_db)
    ):
    search_address = address_crud.get_address(db, address_id=address_id)
    if search_address is None:
        raise HTTPException(status_code=404, detail="Address not found")
    else:  
        address_crud.delete_address_from_db(db=db, address_id=address_id)  
        return {"message:" f"successfully deleted address with id: {address_id}"}