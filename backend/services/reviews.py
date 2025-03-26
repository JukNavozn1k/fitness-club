from repositories import reviews_repository
class ReviewsService:
    def __init__(self,repository):
        self.repository = repository

    async def add_review(self, data):
        return await self.repository.add_review(data)
    
    async def get_reviews(self):
        return await self.repository.list(populate=['user'])
    
    async def get_user_review(self, user: dict):
        return await self.repository.retrieve_by_field(field_name='user.$id',value=user['id'],populate=['user'])

def get_reviews_service():
    return ReviewsService(reviews_repository)