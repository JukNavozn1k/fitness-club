from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from api import router as api_router
from core.config import settings
from admin import AdminPanel, AdminAuth
from models.mongodb import mongodb

@asynccontextmanager
async def lifespan(app: FastAPI):
    import models

    admin_panel = AdminPanel(models, auth=AdminAuth(settings.auth.secret_key))
    admin_panel.init_app(app)
    admin_panel.auto_register_all_models()

    await mongodb.init()  # Initialize MongoDB with Beanie

    yield

    await mongodb.dispose()  # Close MongoDB connection

app = FastAPI(title=settings.app.title, version=settings.app.version, lifespan=lifespan)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.app.frontend_url],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, default_response_class=ORJSONResponse)
