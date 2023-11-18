from pydantic import BaseModel
from typing import List, Dict

# USER

class UserBase(BaseModel):
    login: str


class UserCreate(UserBase):
    password: str


class UserUpdate(UserBase):
    login: str
    tags: []


class User(UserBase):
    id: int
    tags: []

    class Config:
        orm_mode = True


# TAG

class TagCreate(BaseModel):
    user_id: int
    tag: str


class Tag(TagCreate):
    id: int

    class Config:
        orm_mode = True


# POST

class PostBase(BaseModel):
    name: str


class PostUpdate(PostBase):
    name: str
    tags: []


class PostCreate(PostBase):
    pass


class Post(PostBase):
    id: int
    author: str
    tags: []

    class Config:
        orm_mode = True
