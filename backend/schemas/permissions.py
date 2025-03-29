from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field
from .base import EntityBase
from beanie import PydanticObjectId

# Схемы для Permission
class PermissionCreate(BaseModel):
    """Схема для создания разрешения"""
    name: str = Field(..., pattern="^[a-z]+:[a-z_]+$")
    description: str = ""
    category: str = "general"

class PermissionOut(EntityBase):
    """Схема для вывода разрешения"""
    name: str
    description: str
    category: str

# Схемы для Role
class RoleCreate(BaseModel):
    """Схема для создания роли"""
    name: str
    permission_ids: List[PydanticObjectId] = Field(default_factory=list)
    parent_role_ids: List[PydanticObjectId] = Field(default_factory=list)
    is_default: bool = False

class RoleUpdate(BaseModel):
    """Схема для обновления роли"""
    permission_ids: Optional[List[PydanticObjectId]] = None
    parent_role_ids: Optional[List[PydanticObjectId]] = None
    is_default: Optional[bool] = None

class RoleOut(EntityBase):
    """Схема для вывода роли"""
    name: str
    permissions: List[PermissionOut] = Field(default_factory=list)
    parent_roles: List['RoleOut'] = Field(default_factory=list)
    is_default: bool

    class Config:
        arbitrary_types_allowed = True  # Для рекурсивных ссылок


class UserUpdate(BaseModel):
    """Схема для обновления пользователя"""
    password: Optional[str] = Field(None, min_length=8)
    role_ids: Optional[List[PydanticObjectId]] = None

class UserWithRolesOut(EntityBase):
    """Схема для вывода пользователя с ролями"""
    username: str
    joined_date: datetime
    roles: List[RoleOut] = Field(default_factory=list)

