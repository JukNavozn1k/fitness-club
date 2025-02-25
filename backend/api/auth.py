from fastapi import APIRouter
from repositories.users import sql_user_repository

from uuid import uuid4

router = APIRouter(prefix='/auth',tags=['Authentication'])

@router.post('/login')
async def login():
    data = {'username' : '22', 'password' : '22'}
    await sql_user_repository.create(data)
    return data

@router.post('/register')
async def register():
    return {}