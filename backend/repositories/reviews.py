from .base import AbstractMongoRepository
from models import Review

class ReviewsRepository(AbstractMongoRepository):
    async def add_review(self, review: dict):
        return await self.create(review)
    

def get_reviews_repository():
    return ReviewsRepository(Review)