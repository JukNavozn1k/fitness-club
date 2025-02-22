from fastapi import FastAPI

from core.config import settings
from api import router as api_router
app = FastAPI()
app.include_router(api_router,
                   prefix=settings.api.prefix)

@app.get('/')
async def test():
    return settings.db
    