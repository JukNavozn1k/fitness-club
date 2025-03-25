from fastapi import APIRouter, Depends

from dependencies.auth import get_current_user

from schemas.reviews import ReviewBase

router = APIRouter(prefix='/reviews', tags=['Reviews'])


@router.post('/add_review')
async def add_review(review: ReviewBase ,user = Depends(get_current_user)):
    return user['id']
    