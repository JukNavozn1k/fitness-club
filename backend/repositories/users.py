from repositories.base import AbstractMongoRepository
from models import User
from typing import Optional, Dict, Any, List

class UserMongoRepository(AbstractMongoRepository):
    async def retrieve_by_username(self, username: str) -> Optional[Dict]:
        """Получение пользователя по username с базовой информацией"""
        return await self.retrieve_by_field('username', username)

    async def retrieve_with_roles(self, user_id: Any) -> Optional[Dict]:
        """Получение пользователя с полной подгрузкой ролей"""
        return await self.retrieve(user_id, populate=["roles"])

    async def list_users_with_roles(self, filters: Dict = None) -> List[Dict]:
        """Список пользователей с подгруженными ролями"""
        return await self.list(filters=filters, populate=["roles"])

    async def add_role(self, user_id: Any, role_id: Any) -> bool:
        """Добавление роли через атомарную операцию"""
        result = await self.update_many(
            filters={"_id": user_id},
            update_data={"$addToSet": {"roles": role_id}}
        )
        return result > 0

    async def remove_role(self, user_id: Any, role_id: Any) -> bool:
        """Удаление роли через атомарную операцию"""
        result = await self.update_many(
            filters={"_id": user_id},
            update_data={"$pull": {"roles": role_id}}
        )
        return result > 0

    async def bulk_add_roles(self, user_ids: List[Any], role_id: Any) -> int:
        """Массовое добавление роли"""
        return await self.update_many(
            filters={"_id": {"$in": user_ids}},
            update_data={"$addToSet": {"roles": role_id}}
        )

def get_user_repository():
    return UserMongoRepository(User)