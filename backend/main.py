from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from core.config import settings
from api import router as api_router

app = FastAPI(title=settings.app.title, version=settings.app.version)
app.include_router(api_router, default_response_class=ORJSONResponse)

