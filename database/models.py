from sqlalchemy import Column, Table, ForeignKey, JSON, Integer, String, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID


from .database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    login = Column(String, unique=True)
    password = Column(String)
    tags = relationship("Tag", backref="user")

class Tag(Base):
    __tablename__ = "tags"
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    tag = Column(String)
    user = relationship("User", backref="tags")

class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    author = Column(String)
    tags = relationship("Tag", backref="post")