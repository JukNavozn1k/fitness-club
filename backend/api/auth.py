from fastapi import APIRouter
from repositories.users import sql_user_repository

router = APIRouter(prefix='/auth',tags=['Authentication'])

@router.post('/login')
async def login():
    await sql_user_repository.create({'username': 'bob', 'password' : '1234'})
    return {}

@router.post('/register')
async def register():
    return {}