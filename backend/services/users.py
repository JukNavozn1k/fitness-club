import bcrypt
from .rbac import user_role_service
from repositories.rbac import sql_role_repository

class UserService:
    def __init__(self, repository, auth_service=None):
        self.repository = repository
        self.auth_service = auth_service

    async def login(self, data: dict):
        res = await self.repository.retrieve_by_username(data['username'])
        if res is None:
            return None
        if self.check_password(data['password'], res['password']):
            return self.auth_service.create_access_token({'sub': res['id']})
        return None

    async def register(self, data: dict):
        data['password'] = self.hash_password(data['password'])
        res = await self.repository.create(data)
        role = await sql_role_repository.retrieve_by_field({"name": "member"})
        if not role:
            raise Exception("Role 'member' not found")
        await user_role_service.assign_role_to_user({
            "user_id": res['id'],
            "role_id": role["id"]
        })
        return res

    def hash_password(self, password: str) -> str:
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_password.decode('utf-8')

    def check_password(self, password: str, hashed_password: str) -> bool:
        return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))

    async def retrieve_by_token(self, token: str) -> dict:
        token = self.auth_service.parse_token(token)
        user_id = int(token['sub'])
        return await self.repository.retrieve(user_id)


def get_user_service(user_repository, auth_service):
    return UserService(user_repository, auth_service)