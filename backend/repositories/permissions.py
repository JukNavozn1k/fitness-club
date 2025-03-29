from .base import AbstractMongoRepository
from models import Role, Permission

from typing import Optional,List

class RolesRepository(AbstractMongoRepository):
    async def get_role_by_name(self, name: str) -> Optional[dict]:
        return await self.retrieve_by_field("name", name)
    
    async def create_role(self, role_data: dict) -> dict:
        return await self.create(role_data)
    
    async def get_all_roles(self, include_permissions: bool = False) -> List[dict]:
        populate = ["permissions"] if include_permissions else None
        return await self.list(populate=populate)

class PermissionsRepository(AbstractMongoRepository):
    async def get_permission_by_name(self, name: str) -> Optional[dict]:
        return await self.retrieve_by_field("name", name)
    
    async def bulk_create_permissions(self, permissions: List[dict]) -> List[dict]:
        return await self.create_many(permissions)
    
    async def get_permissions_by_names(self, names: List[str]) -> List[dict]:
        return await self.list(filters={"name": {"$in": names}})

def get_roles_repository():
    return RolesRepository(Role)

def get_permissions_repository():
    return PermissionsRepository(Permission)