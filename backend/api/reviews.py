from fastapi import APIRouter, Depends

from dependencies.auth import get_current_user
from services import reviews_service
from schemas.reviews import ReviewCreate,ReviewOut
from schemas.users import UserOut
router = APIRouter(prefix='/reviews', tags=['Reviews'])


@router.post('/add_review')
async def add_review(review: ReviewCreate ,user = Depends(get_current_user)):
    review = ReviewOut(user=user['id'],**review.model_dump())
    await reviews_service.add_review(review.model_dump())
    return review
    