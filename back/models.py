
# from typing import Optional, List
# from pydantic import BaseModel, Field
# from datetime import datetime
# from bson import ObjectId
# class User(BaseModel):
#     username: str
#     password: str
#     email: Optional[str] = None
#     full_name: Optional[str] = None
#     disabled: Optional[bool] = None
#     authorized_pulsar_topics: Optional[List[str]]
#     viewable_by: Optional[List[str]]
#     data: Optional[dict]


# class UserInDB(User):
#     _id: ObjectId
#     date_created: datetime = Field(default_factory=datetime.utcnow)


# class UserSen(BaseModel):
#     root_id: str
#     content: dict


# class UserSenInDB(UserSen):
#     _id: ObjectId
#     timestamp: datetime = Field(default_factory=datetime.utcnow)


# class Token(BaseModel):
#     access_token: str
#     token_type: str


# class TokenData(BaseModel):
#     username: Optional[str] = None

# class Blog(BaseModel):
#     title: str
#     content: str
#     published: Optional[bool] = None
import sqlalchemy as sq
from .database import Base
import datetime
from sqlalchemy.orm import relationship


class Blog(Base):
    __tablename__ = "blogs"
    id = sq.Column(sq.Integer, primary_key=True, index=True)
    title = sq.Column(sq.String)
    body = sq.Column(sq.String)
    user_id = sq.Column(sq.Integer, sq.ForeignKey("users.id"))


class User(Base):
    __tablename__ = "users"
    id = sq.Column(sq.Integer, primary_key=True, index=True)
    name = sq.Column(sq.String)
    email = sq.Column(sq.String)
    password = sq.Column(sq.String)
