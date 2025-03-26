from sqlalchemy import Integer, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from .database import Base

from datetime import datetime

from beanie import Document,Indexed

from pydantic import Field

class UserSQL(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    username: Mapped[str] = mapped_column(String(32), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(128), nullable=False)
   
    joined_date: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)


class UserMongo(Document):
    username: Indexed(str, unique=True) = Field(...)
    password: str = Field(...)

    joined_date: datetime = Field(default_factory=datetime.utcnow)


    class Settings:
        name = "users"