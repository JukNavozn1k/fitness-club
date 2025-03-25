class ReviewsService:
    def __init__(self,repository):
        self.repository = repository


def get_reviews_service():
    return ReviewsService()