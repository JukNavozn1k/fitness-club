

from typing import Dict, List, Optional

class UserRoleService:
    def __init__(self, user_repo, role_repo, user_role_repo):
        self.user_repo = user_repo
        self.role_repo = role_repo
        self.user_role_repo = user_role_repo

    async def get_user(self, user_id: int) -> Optional[Dict]:
        return await self.user_repo.retrieve(user_id)

    async def assign_role_to_user(self, user_id: int, role_id: int) -> Dict:
        # Проверяем наличие пользователя и роли
        user = await self.user_repo.retrieve(user_id)
        role = await self.role_repo.retrieve(role_id)
        if user and role:
            association_data = {
                'user_id': user_id,
                'role_id': role_id
            }
            return await self.user_role_repo.create(association_data)
        return {}

    async def remove_role_from_user(self, user_id: int, role_id: int) -> bool:
        associations = await self.user_role_repo.list()
        target = next(
            (assoc for assoc in associations
             if assoc.get('user_id') == user_id and assoc.get('role_id') == role_id),
            None
        )
        if target:
            return await self.user_role_repo.delete(target.get('id'))
        return False

    async def get_user_roles(self, user_id: int) -> List[Dict]:
        associations = await self.user_role_repo.list()
        # Фильтруем роли, назначенные конкретному пользователю
        return [assoc for assoc in associations if assoc.get('user_id') == user_id]

    async def list_user_roles(self) -> List[Dict]:
        return await self.user_role_repo.list()

class UserRoleService:
    def __init__(self, user_repo, role_repo, user_role_repo):
        self.user_repo = user_repo
        self.role_repo = role_repo
        self.user_role_repo = user_role_repo

    async def get_user(self, user_id: int) -> Optional[Dict]:
        return await self.user_repo.retrieve(user_id)

    async def assign_role_to_user(self, user_id: int, role_id: int) -> Dict:
        # Проверяем наличие пользователя и роли
        user = await self.user_repo.retrieve(user_id)
        role = await self.role_repo.retrieve(role_id)
        if user and role:
            association_data = {
                'user_id': user_id,
                'role_id': role_id
            }
            return await self.user_role_repo.create(association_data)
        return {}

    async def remove_role_from_user(self, user_id: int, role_id: int) -> bool:
        associations = await self.user_role_repo.list()
        target = next(
            (assoc for assoc in associations
             if assoc.get('user_id') == user_id and assoc.get('role_id') == role_id),
            None
        )
        if target:
            return await self.user_role_repo.delete(target.get('id'))
        return False

    async def get_user_roles(self, user_id: int) -> List[Dict]:
        associations = await self.user_role_repo.list()
        # Фильтруем роли, назначенные конкретному пользователю
        return [assoc for assoc in associations if assoc.get('user_id') == user_id]

    async def list_user_roles(self) -> List[Dict]:
        return await self.user_role_repo.list()
