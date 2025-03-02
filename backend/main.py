from fastapi import FastAPI
from fastapi.responses import ORJSONResponse


from api import router as api_router

from core.config import settings
from core.admin import admin

app = FastAPI(title=settings.app.title, version=settings.app.version)
app.include_router(api_router, default_response_class=ORJSONResponse)

admin.update_app(app)

import models
admin.auto_register_all_models(models)
