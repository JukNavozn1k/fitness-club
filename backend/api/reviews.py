from fastapi import APIRouter, Depends

from dependencies.auth import get_current_user
from services import reviews_service
from schemas.reviews import ReviewCreate,ReviewOut
from schemas.users import UserOut
from schemas.users import UserOut
router = APIRouter(prefix='/reviews', tags=['Reviews'])


@router.post('/add_review')
async def add_review(review: ReviewCreate ,user : dict = Depends(get_current_user)):
    formated_user = UserOut(**user)
    new_review = ReviewOut(user=formated_user,**review.model_dump())
  
    new_review = await reviews_service.add_review(new_review.model_dump())

    return new_review
    