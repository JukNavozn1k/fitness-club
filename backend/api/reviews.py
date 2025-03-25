from fastapi import APIRouter, Depends

from dependencies.auth import get_current_user

router = APIRouter(prefix='/reviews', tags=['Reviews'])


@router.post('/add_review')
async def add_review(user = Depends(get_current_user)):
    ...
    