from sqladmin import Admin as SQLAdmin, ModelView
from sqlalchemy import inspect

import models

class AdminPanel:
    def __init__(self, db):
        self.db = db
        self.auth = None
        self.admin = None

    def init_app(self, app):
        self.admin = SQLAdmin(app, self.db.engine, authentication_backend=self.auth)

    def register_model(self, model):
        class DynamicModelView(ModelView, model=model):
            column_list = [column.name for column in inspect(model).columns]

        self.admin.add_view(DynamicModelView)

    def auto_register_all_models(self, models_module):
        modules = dir(models)
        for module in modules:
            for attr_name in dir(module):
                attr = getattr(module, attr_name)
                if isinstance(attr, type) and issubclass(attr, models.Base) and attr is not models.Base:
                    self.register_model(attr)



panel = AdminPanel(models.db)
