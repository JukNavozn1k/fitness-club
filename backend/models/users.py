from datetime import datetime
from typing import List
from pydantic import Field
from beanie import Document, Link, Indexed

from .rbac import Role

class User(Document):
    """Пользовательская модель для MongoDB с RBAC"""
    username: Indexed(str, unique=True)
    password: str  # Хэш пароля
  
    joined_date: datetime = Field(default_factory=datetime.utcnow)
    roles: List[Link['Role']] = []
  
    