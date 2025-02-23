from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from core.config import settings
from api import router as api_router
app = FastAPI()
app.include_router(api_router,
                   prefix=settings.api.prefix,
                   default_response_class=ORJSONResponse)

@app.get('/')
async def test():
    return settings.auth
    