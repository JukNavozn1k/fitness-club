from sqlalchemy import Integer, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from .database import Base

from datetime import datetime

from beanie import Document,Indexed,Link
from typing import List

from enum import Enum


from pydantic import Field

class UserSQL(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    username: Mapped[str] = mapped_column(String(32), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(128), nullable=False)
   
    joined_date: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

class Permission(str, Enum):
    CREATE_USER = "create_user"
    DELETE_USER = "delete_user"
    EDIT_ROLES = "edit_roles"
    VIEW_USERS = "view_users"



class RoleMongo(Document):
    name: Indexed(str, unique=True)  # type: ignore
    permissions: List[Permission]
    
    class Settings:
        name = "roles"

class UserMongo(Document):
    username: Indexed(str, unique=True) = Field(...)
    password: str = Field(...)

    joined_date: datetime = Field(default_factory=datetime.utcnow)
    roles : List[Link[RoleMongo]] = []

    class Settings:
        name = "users"