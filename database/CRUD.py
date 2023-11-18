from sqlalchemy.orm import Session
from fastapi import HTTPException
from . import models, schemas

# def create_user(db: Session, user: schemas.UserCreate):
#     db_user = models.User(nickname=user.nickname, name=user.name, surname=user.surname,
#                           grade=user.grade, contacts=user.contacts, description=user.description,
#                           avatar_uuid=user.avatar_uuid, is_admin=user.is_admin, is_teacher=user.is_teacher)
#     try:
#         db.add(db_user)
#         db.commit()
#         db.refresh(db_user)
#     except Exception as e:
#         raise HTTPException(status_code=500, detail='failed to create user')
#     db_authorization = models.Authorization(user_id=db_user.id, email=user.email, nickname=user.nickname,
#                                             phone_number=user.phone_number, hashed_password=hash.get_hashed_password(user.password))
#     db.add(db_authorization)
#     db.commit()
#     db.refresh(db_user)
#     return db_user

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "hashed"
    db_user = models.User(login=user.login, password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user: schemas.UserUpdate):
    fake_hashed_password = user.password + "hashed"
    db_user = models.User(login=user.login, password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_user_tag(db: Session, item: schemas.TagCreate, user_id: int):
    db_item = models.Tag(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

