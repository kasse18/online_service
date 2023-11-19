from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import CRUD, schemas, models
from database.database import SessionLocal, engine
from typing import List, Union

app = APIRouter(
    prefix='/database',
    tags=['Database'],
)


models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# USER

@app.get('/users/{user_id}', response_model=schemas.User)
def get_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    try:
        db_user = CRUD.get_user_by_login(db, login=user.login)
    except Exception as e:
        raise HTTPException(status_code=500, detail='failed to get user')
    if db_user is None:
        raise HTTPException(status_code=404, detail='user not found')
    return db_user.user


@app.get("/users/{user_id}", response_model=List[schemas.User])
def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = CRUD.get_users(db, skip=skip, limit=limit)
    return users


@app.post('/users/', response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    try:
        user = CRUD.create_user(db, user)
    except:
        raise HTTPException(status_code=500, detail='failed to create user')
    return user


@app.post('/users/{user_id}')
def update_user(user_id: int, user_update: schemas.UserUpdate, db: Session = Depends(get_db)):
    db_user = CRUD.update_user(db, user_id, user_update)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.delete('/users/{user_id}')
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = CRUD.delete_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


# POST

@app.get("/posts/{post_id}", response_model=schemas.Post)
def get_post(post_id: int, db: Session = Depends(get_db)):
    db_post = CRUD.get_post(db, post_id)
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return db_post

@app.get("/posts/", response_model=List[schemas.Post])
def get_posts(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    posts = CRUD.get_posts(db, skip=skip, limit=limit)
    return posts

@app.post("/posts/", response_model=schemas.Post)
def create_post(post: schemas.PostCreate, db: Session = Depends(get_db)):
    try:
        post = CRUD.create_post(db, post)
    except:
        raise HTTPException(status_code=500, detail='failed to create post')
    return post

@app.put("/posts/{post_id}", response_model=schemas.Post)
def update_post(post_id: int, post_update: schemas.PostUpdate, db: Session = Depends(get_db)):
    db_post = CRUD.update_post(db, post_id, post_update)
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return db_post

@app.delete("/posts/{post_id}", response_model=schemas.Post)
def delete_post(post_id: int, db: Session = Depends(get_db)):
    db_post = CRUD.delete_post(db, post_id)
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return db_post


# TAG

@app.get("/tags/{tag_id}", response_model=schemas.Tag)
def get_tag(tag_id: int, db: Session = Depends(get_db)):
    db_tag = CRUD.get_tag(db, tag_id)
    if db_tag is None:
        raise HTTPException(status_code=404, detail="Tag not found")
    return db_tag

@app.get("/tags/", response_model=List[schemas.Tag])
def get_tags(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    tags = CRUD.get_tags(db, skip=skip, limit=limit)
    return tags

@app.post("/tags/", response_model=schemas.Tag)
def create_tag(tag: schemas.TagCreate, db: Session = Depends(get_db)):
    try:
        tag = CRUD.create_tag(db, tag)
    except:
        raise HTTPException(status_code=500, detail='failed to create tag')
    return tag

@app.delete("/tags/{tag_id}", response_model=schemas.Tag)
def delete_tag(tag_id: int, db: Session = Depends(get_db)):
    db_tag = CRUD.delete_tag(db, tag_id)
    if db_tag is None:
        raise HTTPException(status_code=404, detail="Tag not found")
    return db_tag