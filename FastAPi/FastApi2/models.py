from typing import Text
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.sql.sqltypes import DATETIME, TIMESTAMP, Date, DateTime

from database import Base

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(100))
    second_name = Column(String(100))
    pesel = Column(String, unique=True)
    birthday = Column(DateTime)
    created_at = Column(DateTime)
    last_modified = Column(DateTime)
    
    items = relationship("Item", back_populates="owner")
    addresses = relationship("Addresses", back_populates="owner")

class Addresses(Base):
    __tablename__ = "addresses" 

    id = Column(Integer, primary_key=True, index=True)
    city = Column(String(100))
    street = Column(String(100))
    house_number = Column(Integer)
    phone_number = Column(String(100))
    e_mail = Column(String(100))
    owner_id = Column(Integer, ForeignKey("customers.id"))

    owner = relationship("Customer", back_populates="addresses")

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key = True, index=True)
    name = Column(String(100))
    description = Column(String)
    owner_id = Column(Integer, ForeignKey("customers.id"))

    owner = relationship("Customer", back_populates="items")
