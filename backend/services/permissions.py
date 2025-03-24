from models.users import RoleEnum, PermissionEnum
from repositories.users import UserSQLRepository

class PermissionService:
    def __init__(self, user_repository: UserSQLRepository):
        self.user_repository = user_repository

    async def has_permission(self, user_id: int, permission: PermissionEnum) -> bool:
        user = await self.user_repository.retrieve(user_id)
        return permission in user.role.permissions
