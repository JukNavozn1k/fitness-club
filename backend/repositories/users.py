from repositories.base import AbstractSQLRepository
from models.users import User

from models.database import db


class UserSQLRepository(AbstractSQLRepository):
    async def retrieve(self, pk, options = None):
        return await super().retrieve(pk, options)
    async def retrieve_by_username(self, username: str):
        res = await self.retrieve_by_field('username', username)
        return res


def get_user_repository():
    return UserSQLRepository(db.get_session, User)