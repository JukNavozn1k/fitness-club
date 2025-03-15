from sqlalchemy import Integer, String
from sqlalchemy.orm import relationship, Mapped, mapped_column
from .database import Base

from typing import List

class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    username: Mapped[str] = mapped_column(String(32), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(128), nullable=False)
    
    # Связь с ролями через ассоциативную таблицу
    roles: Mapped[List["Role"]] = relationship("Role", secondary="user_roles", back_populates="users",lazy='selectin')
