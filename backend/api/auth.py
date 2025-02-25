from fastapi import APIRouter
from .base import oauth2_schema
router = APIRouter(prefix='/auth',tags=['Authentication'])

@router.post('/login')
async def login():
    return {}

@router.post('/register')
async def register():
    return {}