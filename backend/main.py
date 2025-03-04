from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from api import router as api_router

from core.config import settings
from admin import panel as admin_panel

app = FastAPI(title=settings.app.title, version=settings.app.version)
app.include_router(api_router, default_response_class=ORJSONResponse)

admin_panel.init_app(app)
# admin.auto_register_all_models(models)
