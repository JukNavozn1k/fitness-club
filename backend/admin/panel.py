from sqladmin import Admin as SQLAdmin, ModelView
from sqlalchemy import inspect

from core.database import db, Base
from admin.auth import admin_auth
from utils.modules import load_modules

class Admin:
    def __init__(self, db, auth):
        self.db = db
        self.auth = auth
        self.admin = None

    def init_app(self, app):
        self.admin = SQLAdmin(app, self.db.engine, authentication_backend=self.auth)

    def register_model(self, model):
        class DynamicModelView(ModelView, model=model):
            column_list = [column.name for column in inspect(model).columns]
        self.admin.add_view(DynamicModelView)

    def auto_register_all_models(self, models_module):
        modules = load_modules(models_module)
        for module in modules:
            for attr_name in dir(module):
                attr = getattr(module, attr_name)
                if isinstance(attr, type) and issubclass(attr, Base) and attr is not Base:
                    self.register_model(attr)

admin = Admin(db, admin_auth)
