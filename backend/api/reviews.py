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
    

@router.get('/get_my_review')
async def get_my_review():
  
    data = {
    "id": "67e4139ee00b9b451e3e25da",
    "rating": 1,
    "comment": "",
    "user": {
        "id": "67e406a51ed9ea88845c0c79",
        "username": "string",
        "joined_date": "2025-03-26T13:52:37.597000"
    },
    "created_at": "2025-03-26T14:47:58.349000"
}
    
    return ReviewOut(**data).model_dump()
    

@router.get('/get_reviews',response_model=List[ReviewOut])
async def list_review():
    reviews = await reviews_service.get_reviews()

    return reviews
    