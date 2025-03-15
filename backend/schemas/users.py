from pydantic import BaseModel
from typing import List

from .rbac import RoleOut

# Схемы для User
class UserBase(BaseModel):
    username: str

class UserOut(UserBase):
    id: int
    user_roles: List['RoleOut'] = []

    class Config:
        from_attributes = True