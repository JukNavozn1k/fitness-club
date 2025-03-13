
from typing import List, Dict, Optional
from models.rbac import Role, Permission, RolePermission
from repositories import sql_role_repository, sql_permission_repository, sql_role_permission_repository

class RolePermissionService:
    async def create_role(self, role_data: Dict) -> Dict:
        return await sql_role_repository.create(role_data)

    async def get_role(self, role_id: int) -> Optional[Dict]:
        return await sql_role_repository.retrieve(role_id)

    async def list_roles(self) -> List[Dict]:
        return await sql_role_repository.list()

    async def update_role(self, role_id: int, role_data: Dict) -> Optional[Dict]:
        return await sql_role_repository.update(role_id, role_data)

    async def delete_role(self, role_id: int) -> bool:
        return await sql_role_repository.delete(role_id)

    async def create_permission(self, permission_data: Dict) -> Dict:
        return await sql_permission_repository.create(permission_data)

    async def get_permission(self, permission_id: int) -> Optional[Dict]:
        return await sql_permission_repository.retrieve(permission_id)

    async def list_permissions(self) -> List[Dict]:
        return await sql_permission_repository.list()

    async def assign_permission_to_role(self, role_id: int, permission_id: int) -> Dict:
        # Проверка существования роли и разрешения
        role = await sql_role_repository.retrieve(role_id)
        permission = await sql_permission_repository.retrieve(permission_id)
        
        if role and permission:
            role_permission_data = {
                'role_id': role_id,
                'permission_id': permission_id
            }
            return await sql_role_permission_repository.create(role_permission_data)
        return {}

    async def remove_permission_from_role(self, role_id: int, permission_id: int) -> bool:
        # Удаление связи роли и разрешения
        async with sql_role_permission_repository.get_session() as session:
            result = await session.execute(
                select(RolePermission).filter_by(role_id=role_id, permission_id=permission_id)
            )
            role_permission = result.scalar_one_or_none()
            if role_permission:
                await session.delete(role_permission)
                await session.commit()
                return True
        return False
