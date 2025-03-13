from pydantic import BaseModel
from typing import List
# Схемы для Permission
class PermissionBase(BaseModel):
    name: str

class PermissionCreate(PermissionBase):
    pass

class PermissionOut(PermissionBase):
    id: int

    class Config:
        from_attributes = True

# Схемы для Role
class RoleBase(BaseModel):
    name: str

class RoleCreate(RoleBase):
    permission_ids: List[int] = []

class RoleOut(RoleBase):
    id: int
    permissions: List[PermissionOut] = []

    class Config:
        from_attributes = True
