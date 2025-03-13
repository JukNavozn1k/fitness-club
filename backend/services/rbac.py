from repositories.rbac import (
    sql_role_repository,
    sql_permission_repository,
    sql_role_permission_repository,
    sql_user_role_repository
)
from typing import List, Optional


class RolePermissionService:
    def __init__(self, role_repo, permission_repo, role_permission_repo):
        self.role_repo = role_repo
        self.permission_repo = permission_repo
        self.role_permission_repo = role_permission_repo

    async def create_role(self, name: str) -> dict:
        return await self.role_repo.create({"name": name})

    async def delete_role(self, role_id: int) -> bool:
        return await self.role_repo.delete(role_id)

    async def create_permission(self, name: str) -> dict:
        return await self.permission_repo.create({"name": name})

    async def delete_permission(self, permission_id: int) -> bool:
        return await self.permission_repo.delete(permission_id)

    async def assign_permission_to_role(self, role_id: int, permission_id: int) -> dict:
        return await self.role_permission_repo.create({"role_id": role_id, "permission_id": permission_id})

    async def remove_permission_from_role(self, role_id: int, permission_id: int) -> bool:
        role_permission = await self.role_permission_repo.retrieve_by_filter({
            "role_id": role_id,
            "permission_id": permission_id
        })
        if role_permission:
            return await self.role_permission_repo.delete(role_permission[0]["id"])
        return False

    async def list_roles(self) -> List[dict]:
        return await self.role_repo.list()

    async def list_permissions(self) -> List[dict]:
        return await self.permission_repo.list()


class UserRoleService:
    def __init__(self, user_role_repo):
        self.user_role_repo = user_role_repo

    async def assign_role_to_user(self, user_id: int, role_id: int) -> dict:
        return await self.user_role_repo.create({"user_id": user_id, "role_id": role_id})

    async def remove_role_from_user(self, user_id: int, role_id: int) -> bool:
        user_role = await self.user_role_repo.retrieve_by_filter({
            "user_id": user_id,
            "role_id": role_id
        })
        if user_role:
            return await self.user_role_repo.delete(user_role[0]["id"])
        return False

    async def list_user_roles(self, user_id: int) -> List[dict]:
        return await self.user_role_repo.retrieve_by_filter({"user_id": user_id})


# Инициализация сервисов
role_permission_service = RolePermissionService(
    sql_role_repository, sql_permission_repository, sql_role_permission_repository
)

user_role_service = UserRoleService(sql_user_role_repository)
