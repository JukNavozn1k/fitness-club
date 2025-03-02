# app/infrastructure/admin.py

from sqladmin import Admin as SQLAdmin
from sqlalchemy import inspect
from fastapi import FastAPI
from core.database import db

class Admin:
    def __init__(self, db, app: FastAPI = None):
        """
        Инициализация класса для работы с SQLAdmin.
        :param db: объект базы данных (инфраструктурный слой)
        :param app: объект FastAPI (опционально, если передан — инициализирует admin)
        """
        self.db = db
        self.app = app
        self.admin = SQLAdmin(app, db.engine) if app else None

    def update_app(self, app: FastAPI):
        """Метод для обновления app (если это нужно)."""
        self.app = app
        self.admin = SQLAdmin(app, self.db.engine)  # Инициализируем админку с новым app

    def register_model(self, model):
        """Регистрация модели в админке."""
        class DynamicModelView(SQLAdmin.ModelView, model=model):
            # Автоматически получаем все поля модели
            column_list = [column.name for column in inspect(model).columns]
            # Определение других параметров, если нужно (например, фильтрация, сортировка и т.д.)

        self.admin.add_view(DynamicModelView)
    
    def auto_register_all_models(self, models_module):
        """Автоматическая регистрация всех моделей из модуля models."""
        for model in models_module.__all__:
            if hasattr(model, '__tablename__'):
                self.register_model(model)

admin = Admin(db)