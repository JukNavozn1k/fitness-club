from datetime import datetime
from typing import List, Optional
from pydantic import Field
from beanie import Document, Link, Indexed

from .permissions import Role

class User(Document):
    """Пользовательская модель для MongoDB с RBAC"""
    username: Indexed(str, unique=True)
    password: str  # Хэш пароля
    email: Optional[str] = Field(default=None, index=True)
    joined_date: datetime = Field(default_factory=datetime.utcnow)
    roles: List[Link['Role']] = Field(default=[])
    is_active: bool = Field(default=True)
    