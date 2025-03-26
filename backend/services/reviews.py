from repositories import reviews_repository
class ReviewsService:
    def __init__(self,repository):
        self.repository = repository

    async def add_review(self, data):
        return await self.repository.add_review(data)
    
    async def get_reviews(self):
        return await self.repository.list(populate=['user'])

def get_reviews_service():
    return ReviewsService(reviews_repository)