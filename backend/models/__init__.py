import os
import importlib

from .database import db,Base

model_dir = os.path.dirname(__file__)

for filename in os.listdir(model_dir):
    if filename.endswith('.py') and filename not in ['__init__.py','database.py','mongodb.py']:
        module_name = f".{filename[:-3]}"  # убираем .py из имени файла
        importlib.import_module(f"models.{filename[:-3]}")

