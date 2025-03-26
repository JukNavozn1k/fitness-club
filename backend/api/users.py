from fastapi import APIRouter,HTTPException,status

from schemas.users import UserOut
from typing import List
from services import user_service

router = APIRouter(prefix='/users', tags=['Users'])

@router.get('/',response_model=List[UserOut])
async def list():
    return await user_service.get_users()

@router.get('/{user_id}',response_model=UserOut)
async def retrieve(user_id: str):
    try:
        return await user_service.get_user(user_id)
    except: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='User not found')