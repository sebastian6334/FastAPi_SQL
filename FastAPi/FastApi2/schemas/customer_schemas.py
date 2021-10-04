from sqlalchemy.sql.sqltypes import Date
from validators import  ValidatorPesel
import datetime
from typing import List, Optional
from pydantic import BaseModel, ValidationError, validator
from schemas.item_schemas import Item
from schemas.address_schemas import Address

class CustomerBase(BaseModel):
    pesel: str
    birthday: Optional[datetime.date]

    @validator('pesel')
    def validate_pesel(cls, _pesel):
        if len(_pesel) == 11: 
            return ValidatorPesel(_pesel).finish()
        else:
            raise ValidationError('wrong length of pesel')

class CustomerCreate(CustomerBase):
    first_name: str
    second_name: str
    created_at: Optional[datetime.datetime] = datetime.datetime.now()

class Customer(CustomerBase):
    id: int 
    items: List[Item] = []
    addresses: List[Address] = []
    created_at: Optional[datetime.datetime] 
    last_modified:Optional[datetime.datetime]
    
    class Config:
        orm_mode = True

class CustomerUpg(CustomerBase):
    first_name: str
    second_name: str
    last_modified:Optional[datetime.datetime]

    class Config:
        orm_mode = True
