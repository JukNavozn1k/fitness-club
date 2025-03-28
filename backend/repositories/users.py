from repositories.base import AbstractMongoRepository
from models import User
from typing import Optional, Dict, Any

class UserMongoRepository(AbstractMongoRepository):
    async def retrieve_by_username(self, username: str) -> Optional[Dict]:
        """Получение пользователя по username"""
        return await self.retrieve_by_field('username', username)
    
    async def get_with_roles(self, user_id: Any) -> Optional[Dict]:
        """Получение пользователя с подгруженными ролями"""
        user = await self.retrieve(user_id, populate=["roles"])
        return user
    
    async def add_role(self, user_id: Any, role_id: Any) -> bool:
        """Добавление роли пользователю"""
        user = await self.model.get(user_id)
        if not user:
            return False
        
        if role_id not in [str(role.id) for role in user.roles]:
            user.roles.append(role_id)
            await user.save()
        return True
    
    async def remove_role(self, user_id: Any, role_id: Any) -> bool:
        """Удаление роли у пользователя"""
        user = await self.model.get(user_id)
        if not user:
            return False
        
        user.roles = [role for role in user.roles if str(role.id) != str(role_id)]
        await user.save()
        return True

def get_user_repository():
    return UserMongoRepository(User)