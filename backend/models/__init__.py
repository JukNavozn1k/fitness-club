import os
import importlib


from .mongo import MongoDatabase

from core.config import settings

from .users import User,Permission,Role
from .reviews import ReviewMongo

from .exercises import Equipment,Exercise,ExerciseCategory

# model_dir = os.path.dirname(__file__)

# for filename in os.listdir(model_dir):
#     if filename.endswith('.py') and filename not in ['__init__.py','database.py', 'mongo.py']:
#         module_name = f".{filename[:-3]}"  # убираем .py из имени файла
#         importlib.import_module(f"models.{filename[:-3]}")


mongo = MongoDatabase(settings.mongo.get_url(), settings.mongo.mongo_db_name, [ReviewMongo,User,
                                                                               Equipment,Exercise, ExerciseCategory])