

from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from contextlib import asynccontextmanager
from api import router as api_router

from core.config import settings
from admin import AdminPanel


@asynccontextmanager
async def lifespan(app: FastAPI):
    import models
    admin_panel = AdminPanel(models)
    admin_panel.init_app(app)
    admin_panel.auto_register_all_models()
    yield
  

app = FastAPI(title=settings.app.title, version=settings.app.version, lifespan=lifespan)
app.include_router(api_router, default_response_class=ORJSONResponse)



