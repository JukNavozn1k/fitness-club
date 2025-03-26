import os
import importlib

from .database import db,Base
from .mongo import MongoDatabase

from core.config import settings

from .users import UserSQL,UserMongo
from .reviews import ReviewMongo

# model_dir = os.path.dirname(__file__)

# for filename in os.listdir(model_dir):
#     if filename.endswith('.py') and filename not in ['__init__.py','database.py', 'mongo.py']:
#         module_name = f".{filename[:-3]}"  # убираем .py из имени файла
#         importlib.import_module(f"models.{filename[:-3]}")


mongo = MongoDatabase(settings.mongo.get_url(), settings.mongo.mongo_db_name, [ReviewMongo,UserMongo])