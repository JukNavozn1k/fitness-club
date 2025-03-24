from pydantic import BaseModel
from typing import List
from enum import Enum
from datetime import datetime

# Перечисление ролей
class RoleEnum(str, Enum):
    admin = "admin"
    trainer = "trainer"
    member = "member"

# Перечисление разрешений
class PermissionEnum(str, Enum):
    create_workout = "create_workout"
    delete_workout = "delete_workout"
    update_workout = "update_workout"
    view_workout = "view_workout"

# Схемы для User
class UserBase(BaseModel):
    username: str

class UserOut(UserBase):
    id: int
    role: RoleEnum = RoleEnum.member
    joined_date: datetime

    class Config:
        from_attributes = True