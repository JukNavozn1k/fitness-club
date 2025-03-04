import os
import importlib

model_dir = os.path.dirname(__file__)

for filename in os.listdir(model_dir):
 
    if filename.endswith('.py') and filename not in  ['__init__.py']:
        module_name = f".{filename[:-3]}"  # убираем .py из имени файла
        importlib.import_module(module_name, package='.models')

