from fastapi import APIRouter, HTTPException, status, Header

from schemas.auth import AuthSchema, TokenSchema, TokenVerifySchema
from schemas.users import UserOut

from services.users import user_service
from services.auth import auth_service

router = APIRouter(prefix='/auth', tags=['Authentication'])


@router.post('/login', response_model=TokenSchema)
async def login(schema: AuthSchema):
    token = await user_service.login(schema.model_dump())
    if token is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials or failed to generate token"
        )
    return token


@router.post('/register', response_model=UserOut)
async def register(schema: AuthSchema):
    try:
        user = await user_service.register(schema.model_dump())
        return user
    except Exception:
        raise HTTPException(status_code=409, detail='User already exists')


@router.get('/verify-token', response_model=TokenVerifySchema)
async def verify_token(token: str = Header()):
    try:
        token = auth_service.parse_token(token)
        return {'valid': True}
    except Exception as e:
        print(e)
        return {'valid': False}


@router.get('/me', response_model=UserOut)
async def me(token: str = Header()):
    try:
        return await user_service.retrieve_by_token(token)
    except Exception:
        raise HTTPException(status_code=401, detail='Invalid token')