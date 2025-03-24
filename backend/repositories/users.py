from repositories.base import AbstractSQLRepository
from models.users import User, PermissionEnum
from models.database import db

class UserSQLRepository(AbstractSQLRepository):
    async def retrieve(self, pk, options = None):
        return await super().retrieve(pk, options)
    
    async def retrieve_by_username(self, username: str):
        res = await self.retrieve_by_field('username', username)
        return res

    async def has_permission(self, user_id: int, permission: PermissionEnum) -> bool:
        user = await self.retrieve(user_id)
        return permission in user.role.permissions

    async def get_permissions(self, user_id: int) -> list[PermissionEnum]:
        user = await self.retrieve(user_id)
        return user.role.permissions

   
def get_user_repository():
    return UserSQLRepository(db.get_session, User)