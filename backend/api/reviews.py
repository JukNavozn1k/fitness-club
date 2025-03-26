from fastapi import APIRouter, Depends,status,HTTPException

from dependencies.auth import get_current_user
from services import reviews_service
from schemas.reviews import ReviewBase,CreatedReview,ReviewOut


from typing import List

router = APIRouter(prefix='/reviews', tags=['Reviews'])


@router.post('/add_review',response_model=ReviewOut)
async def add_review(review: ReviewBase ,user : dict = Depends(get_current_user)):
 
    new_review = CreatedReview(user=user,**review.model_dump())
    new_review = await reviews_service.add_review(new_review.model_dump())

    return new_review
    
@router.get('/get_reviews',response_model=List[ReviewOut])
async def list_review():
    reviews = await reviews_service.get_reviews()

    return reviews
    


@router.get('/{review_id}',response_model=ReviewOut)
async def get_review(review_id: str):
    try:
        return await reviews_service.get_review(review_id)
    except: raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Review not foun')
    
    

    