from pydantic.main import BaseModel
from pydantic.networks import EmailStr

class AddressBase(BaseModel):
    city: str
    street: str
    house_number: int
    phone_number: str
    e_mail: EmailStr

class AddressCreate(AddressBase):
    city : str
    street: str
    house_number: int
    phone_number: str
    e_mail: EmailStr

class Address(AddressBase):
    id: int
    owner_id: int
    
    class Config:
        orm_mode = True
