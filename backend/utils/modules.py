# utils/module_loader.py
import pkgutil
import importlib
from typing import List, Any

def load_modules(package_module: Any) -> List[Any]:
    """
    Загружает и возвращает список модулей, найденных в пакете.
    
    :param package_module: модуль пакета (например, models)
    :return: список импортированных модулей
    """
    modules = []
    for loader, module_name, is_pkg in pkgutil.iter_modules(package_module.__path__):
        full_module_name = f"{package_module.__name__}.{module_name}"
        module = importlib.import_module(full_module_name)
        modules.append(module)
    return modules
