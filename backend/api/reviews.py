from fastapi import APIRouter, Depends

from dependencies.auth import get_current_user
from services import reviews_service
from schemas.reviews import ReviewCreate,ReviewOut
from schemas.users import UserOut
router = APIRouter(prefix='/reviews', tags=['Reviews'])


@router.post('/add_review')
async def add_review(review: ReviewCreate ,user : dict = Depends(get_current_user)):
    data = review.model_dump()
    data['user'] = user
    new_review = await reviews_service.add_review(data)

    return new_review
    