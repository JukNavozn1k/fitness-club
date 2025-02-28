import bcrypt
from services.auth import auth_service
from repositories.users import sql_user_repository


class UserService:
    def __init__(self, repository, auth_service = None):
        self.repository = repository
        self.auth_service = auth_service
        
    async def register(self,data: dict):
        data['password'] = self.hash_password(data['password'])
        res = await self.repository.create(data)
        return res

    def hash_password(self,password: str) -> str:
        # Генерируем соль и хешируем пароль
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_password.decode('utf-8')

user_service = UserService(sql_user_repository, auth_service)