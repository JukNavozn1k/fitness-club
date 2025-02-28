from fastapi import APIRouter

from services.users import user_service
from schemas.auth import AuthSchema
from schemas.users import UserSchema

router = APIRouter(prefix='/auth',tags=['Authentication'])

@router.post('/login')
async def login(schema: AuthSchema):
    return {}

@router.post('/register',response_model=UserSchema)
async def register(schema: AuthSchema):
    user = await user_service.register(schema.model_dump())    
    return user