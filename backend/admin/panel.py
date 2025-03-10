from sqladmin import Admin as SQLAdmin, ModelView
from sqlalchemy import inspect
import sys

class AdminPanel:
    def __init__(self,models_module,auth):
        self.models_module = models_module
        self.db = models_module.db
        self.auth = auth
        self.admin = None

    def init_app(self, app):
        self.admin = SQLAdmin(app, self.db.engine, authentication_backend=self.auth)

    def register_model(self, model):
        class DynamicModelView(ModelView, model=model):
            column_list = [column.name for column in inspect(model).columns]

        self.admin.add_view(DynamicModelView)

    def auto_register_all_models(self):
        for module_name, module in sys.modules.items():
            if module_name.startswith(self.models_module.__name__ + "."):
                for attr_name in dir(module):
                    attr = getattr(module, attr_name)
                    if isinstance(attr, type) and issubclass(attr, self.models_module.Base) and attr is not self.models_module.Base:
                        self.register_model(attr)

