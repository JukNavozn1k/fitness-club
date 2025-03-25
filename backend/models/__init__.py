import os
import importlib

from .database import db,Base
from .mongo import MongoDatabase

from core.config import settings

model_dir = os.path.dirname(__file__)

for filename in os.listdir(model_dir):
    if filename.endswith('.py') and filename not in ['__init__.py','database.py', 'mongo.py']:
        module_name = f".{filename[:-3]}"  # убираем .py из имени файла
        importlib.import_module(f"models.{filename[:-3]}")

from beanie import Document
class TestDoc(Document):
    name : str

mongo = MongoDatabase(settings.mongo.get_url(), settings.mongo.mongo_db_name, [TestDoc])