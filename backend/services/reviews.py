from repositories import reviews_repository
class ReviewsService:
    def __init__(self,repository):
        self.repository = repository
    

    async def get_user_review(self, user: dict):
        return await self.repository.retrieve_by_field(field_name='user.$id',value=user['id'],populate=['user'])

    async def add_review(self, data):
        user_rewiew = await self.get_user_review(data['user'])
        if not user_rewiew:
            return await self.repository.add_review(data)
        else: 
            return await self.repository.update(pk=user_rewiew['id'],data=data)
    
    async def get_review(self, review_id: any):
        return await self.repository.retrieve(pk=review_id, populate=['user'])

    async def get_reviews(self):
        return await self.repository.list(populate=['user'])
    
    

def get_reviews_service():
    return ReviewsService(reviews_repository)