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

# USER CRUD

#GET
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

#GET ALL
def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

#CREATE
def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

#UPDATE
def update_user(db: Session, user_id: int, user: schemas.UserUpdate):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user:
        for key, value in user.dict(exclude_unset=True).items():
            setattr(db_user, key, value)
        db.commit()
        db.refresh(db_user)
    return db_user

#DELETE
def delete_user(db: Session, user_id: int):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user



# POST CRUD

#GET
def get_post(db: Session, post_id: int):
    return db.query(models.Post).filter(models.Post.id == post_id).first()

#GET ALL
def get_posts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Post).offset(skip).limit(limit).all()

#CREATE
def create_post(db: Session, post: schemas.PostCreate):
    db_post = models.Post(**post.model_dump())
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

#UPDATE
def update_post(db: Session, post_id: int, post: schemas.PostUpdate):
    db_post = db.query(models.Post).filter(models.Post.id == post_id).first()
    if db_post:
        for key, value in post.dict(exclude_unset=True).items():
            setattr(db_post, key, value)
        db.commit()
        db.refresh(db_post)
    return db_post

#DELETE
def delete_post(db: Session, post_id: int):
    db_post = db.query(models.Post).filter(models.Post.id == post_id).first()
    if db_post:
        db.delete(db_post)
        db.commit()
    return db_post

# TAG CRUD

#GET
def get_tag(db: Session, tag_id: int):
    return db.query(models.Tag).filter(models.Tag.id == tag_id).first()

#GET ALL
def get_tags(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Tag).offset(skip).limit(limit).all()

#CREATE
def create_tag(db: Session, tag: schemas.TagCreate):
    db_tag = models.Tag(**tag.model_dump())
    db.add(db_tag)
    db.commit()
    db.refresh(db_tag)
    return db_tag

#DELETE
def delete_tag(db: Session, tag_id: int):
    db_tag = db.query(models.Tag).filter(models.Tag.id == tag_id).first()
    if db_tag:
        db.delete(db_tag)
        db.commit()
    return db_tag