from typing import Optional
from services.auth import AuthService
from repositories.users import sql_user_repository
# class UserService:
#     def __init__(self, repository, auth_service: Optional[AuthService] = None):
#         self.repository = repository
#         self.auth_service = auth_service
        
#     async def create(data: dict):
#         res = await self.repository.create(data)

# user_service = UserService(sql_user_repository, None)