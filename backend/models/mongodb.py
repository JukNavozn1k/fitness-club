from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from core.config import settings

class MongoDB:
    def __init__(self, uri: str, db_name: str):
        self.client = AsyncIOMotorClient(uri)
        self.db = self.client[db_name]

    async def init(self):
        await init_beanie(database=self.db, document_models=[])  # Add your document models here

    def get_database(self):
        return self.db

mongodb = MongoDB(settings.mongo.get_url(), settings.mongo.mongo_db_name)
