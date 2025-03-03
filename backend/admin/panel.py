import pkgutil
import importlib
from sqladmin import Admin as SQLAdmin, ModelView  # Импортируем ModelView напрямую
from sqlalchemy import inspect

from core.database import db, Base  # Используем Base из core/database.py

from admin.auth import admin_auth

class Admin:
    def __init__(self, db, app, auth):
        """
        Инициализация класса для работы с SQLAdmin.
        :param db: объект базы данных (инфраструктурный слой)
        :param app: объект FastAPI (опционально, если передан — инициализирует admin)
        """
        self.db = db
        self.app = app
        self.auth = auth
        self.admin = SQLAdmin(app, self.db.engine,authentication_backend=self.auth) if app and auth else None

    def update_app(self, app):
        """Метод для обновления app (если это нужно)."""
        self.app = app
        self.admin = SQLAdmin(self.app, self.db.engine,authentication_backend=self.auth)

    def register_model(self, model):
        """Регистрация модели в админке."""
        print(f"Registering model {model.__name__}")  # Отладка
        
        class DynamicModelView(ModelView, model=model):
            # Автоматически получаем все поля модели
            column_list = [column.name for column in inspect(model).columns]
        
        self.admin.add_view(DynamicModelView)
    
    def auto_register_all_models(self, models_module):
        """Автоматическая регистрация всех моделей из модуля models."""
        for loader, module_name, is_pkg in pkgutil.iter_modules(models_module.__path__):
            print(f"Loading module: {module_name}")
            module = importlib.import_module(f"models.{module_name}")
            # Регистрируем все классы, которые являются моделями (наследуют от Base)
            for attr_name in dir(module):
                attr = getattr(module, attr_name)
                if isinstance(attr, type) and issubclass(attr, Base) and attr is not Base:
                    print(f"Registering model: {attr.__name__}")
                    self.register_model(attr)


admin = Admin(db,None,admin_auth)
