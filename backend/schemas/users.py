from pydantic import BaseModel
from typing import List

# Схемы для User
class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class UserOut(UserBase):
    id: int
    roles: List['RoleOut'] = []

    class Config:
        orm_mode = True