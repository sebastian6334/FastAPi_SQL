# from fastapi import Body
# from pydantic.errors import DateError
# from pydantic.fields import Field
# from pydantic.main import validate_custom_root_type
# from sqlalchemy.sql.sqltypes import Date
# from validators import  ValidatorPesel
# import datetime
# from typing import List, Optional
# from pydantic import BaseModel, ValidationError, validator, root_validator

# # class ItemBase(BaseModel):
# #     name: str
# #     description: Optional[str] = None

# # class ItemCreate(ItemBase):
# #     name: str
# #     description: str

# # class ItemUpdate(ItemBase):
# #     name: str
# #     description: str

# # class Item(ItemBase):
# #     id: int
# #     owner_id: int

# #     class Config:
# #         orm_mode = True

# class CustomerBase(BaseModel):
#     pesel: str
#     birthday: Optional[datetime.date]
#     age: Optional[int]

#     @validator('pesel')
#     def validate_pesel(cls, _pesel):
#         if len(_pesel) == 11: 
#             return ValidatorPesel(_pesel).finish()
#         else:
#             raise ValidationError('wrong length of pesel')

#     # @root_validator(pre=True)
#     # # pylint: disable=no-self-argument
#     # def validate_date_for_bounds(cls, values):
#     #     values["birthday"] = ValidatorPesel(values["pesel"]).get_birth_date()
#     #     return values  

# # class CustomerDate(CustomerBase):
# #     birthday: Optional[datetime.date]

# #     @validator('birthday')
# #     def validate_birthday(cls, _birthday):
# #         return print(ValidatorPesel(_birthday).get_birth_date())

# class CustomerCreate(CustomerBase):
#     first_name: str
#     second_name: str
#     created_at: Optional[datetime.datetime] = datetime.datetime.now()

# class Customer(CustomerBase):
#     id: int 
#     first_name: str
#     second_name: str
#     age: Optional[int] 
#     items: List[Item] = []
#     created_at: Optional[datetime.datetime] 
#     last_modified:Optional[datetime.datetime]
    
#     class Config:
#         orm_mode = True

# class CustomerUpg(CustomerBase):
#     first_name: str
#     second_name: str
#     age: int
#     last_modified:Optional[datetime.datetime]

#     class Config:
#         orm_mode = True


