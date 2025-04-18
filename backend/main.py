from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from api import router as api_router
from core.config import settings

from models import mongo

from services import rbac_init_service


@asynccontextmanager
async def lifespan(app: FastAPI):
    await mongo.init()  
    # await rbac_init_service.seed()
    yield
    await mongo.dispose() 

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
