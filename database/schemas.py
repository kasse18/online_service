from pydantic import BaseModel
from typing import List, Dict

# USER

class UserBase(BaseModel):
    login: str


class UserCreate(UserBase):
    password: str


class UserUpdate(UserBase):
    tags: List[str]


class User(UserBase):
    id: int
    tags: List[str]

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
    tags: List[str]


class PostCreate(PostBase):
    pass


class Post(PostBase):
    id: int
    author_id: int
    tags: List[str]

    class Config:
        orm_mode = True