# from fastapi.encoders import jsonable_encoder
# from sqlalchemy.orm import Session
# from sqlalchemy.sql.expression import update

# import models
# import schemas

# def get_customer(db: Session, customer_id:int):
#     return db.query(models.Customer).filter(models.Customer.id == customer_id).first()

# def get_customer_by_pesel(db: Session, pesel:str):
#     return db.query(models.Customer).filter(models.Customer.pesel == pesel).first()

# def get_customers(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.Customer).offset(skip).limit(limit).all()
    
# def create_customer(db: Session, customer: schemas.CustomerCreate):
#     db_customer = models.Customer(**customer.dict())
#     db.add(db_customer)
#     db.commit()
#     db.refresh(db_customer)
#     return db_customer       

# def get_item(db:Session, item_id:int):
#     return db.query(models.Item).filter(models.Item.id == item_id).first()

# def get_items(db:Session, skip = 0, limit: int = 100):
#     return db.query(models.Item).offset(skip).limit(limit).all()

# def create_customer_item(db:Session, item: schemas.ItemCreate, customer_id: int):
#     db_item = models.Item(**item.dict(), owner_id=customer_id)
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item    

# def update_item(db_session: Session, *, item: models.Item, item_in: schemas.ItemUpdate) -> models.Item:
#     item_data = jsonable_encoder(item)
#     update_data = item_in.dict(skip_defaults=True)
#     for field in item_data:
#         if field in update_data:
#             setattr(item, field, update_data[field])
#     db_session.add(item)
#     db_session.commit()
#     db_session.refresh(item)
#     return item

# def update_customer(db_session: Session, *, customer: models.Customer, customer_in: schemas.Customer_upg) -> models.Customer:
#     item_data = jsonable_encoder(customer)
#     update_data = customer_in.dict(skip_defaults=True)
#     for field in item_data:
#         if field in update_data:
#             setattr(customer, field, update_data[field])
#     db_session.add(customer)
#     db_session.commit()
#     db_session.refresh(customer)
#     return customer
    

# # async def update_customer(customer_id: int, customer:schemas.Customer_upg, db:Session):
# #     customer_to_update = db.query(models.Customer).filter(models.Customer.id==customer_id).first()
# #     customer_to_update.id=customer.id
# #     customer_to_update.first_name=customer.first_name
# #     customer_to_update.second_name=customer.second_name
# #     customer_to_update.age=customer.age
# #     db.commit()
# #     return customer_to_update

# def delete_item_from_db(db:Session, item_id: int):
#     db.query(models.Item).filter(models.Item.id == item_id).delete()
#     db.commit()

# def delete_customer_from_db(db:Session, customer_id: int):
#     db.query(models.Customer).filter(models.Customer.id == customer_id).delete()
#     db.commit()    
    

    