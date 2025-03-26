from fastapi import APIRouter

from schemas.users import UserOut
from typing import List
from services import user_service

from schemas.base import EntityBase

router = APIRouter(prefix='/users', tags=['Users'])

@router.get('/',response_model=List[UserOut])
async def list():
    return await user_service.get_users()

@router.get('/{user_id}',response_model=UserOut)
async def retrieve(user_id: str):
    user = EntityBase(id=user_id)
    return await user_service.get_user(user.model_dump())