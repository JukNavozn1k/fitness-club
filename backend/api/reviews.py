from fastapi import APIRouter, Depends

from dependencies.auth import get_current_user
from services import reviews_service
from schemas.reviews import ReviewCreate,ReviewOut
from schemas.users import UserOut

from typing import List

router = APIRouter(prefix='/reviews', tags=['Reviews'])


@router.post('/add_review',response_model=ReviewOut)
async def add_review(review: ReviewCreate ,user : dict = Depends(get_current_user)):
 
    new_review = ReviewOut(user=user,**review.model_dump())
    new_review = await reviews_service.add_review(new_review.model_dump())

    return new_review
    

@router.get('/get_my_reviews',response_model=List[ReviewOut])
async def get_my_reviews(user : dict = Depends(get_current_user)):
    reviews = await reviews_service.get_user_reviews(user)

    return reviews
    

@router.get('/get_reviews',response_model=List[ReviewOut])
async def list_review():
    reviews = await reviews_service.get_reviews()

    return reviews
    