from fastapi import APIRouter,HTTPException


from schemas.auth import AuthSchema
from schemas.users import UserSchema

from services.users import user_service

router = APIRouter(prefix='/auth',tags=['Authentication'])

@router.post('/login')
async def login(schema: AuthSchema):
    return {}

@router.post('/register',response_model=UserSchema)
async def register(schema: AuthSchema):
    try:
        user = await user_service.register(schema.model_dump())    
        return user
    except Exception as e:
        raise HTTPException(status_code=409,detail='User already exists')
