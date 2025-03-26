from repositories.base import AbstractSQLRepository,AbstractMongoRepository

from models import db

from models import UserMongo

class UserSQLRepository(AbstractSQLRepository):
    async def retrieve(self, pk, options = None):
        return await super().retrieve(pk, options)
    
    async def retrieve_by_username(self, username: str):
        res = await self.retrieve_by_field('username', username)
        return res



class UserMongoRepository(AbstractMongoRepository):
  
    
    async def retrieve_by_username(self, username: str):
        res = await self.retrieve_by_field('username', username)
        return res

def get_user_repository():
    return UserMongoRepository(UserMongo)