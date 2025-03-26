
from beanie import Document,Link

from datetime import datetime
from beanie import Document

from pydantic import Field

from .users import UserMongo

class ReviewMongo(Document):
    user : Link[UserMongo]
    rating: int = Field(..., ge=1, le=5)  # Оценка от 1 до 5
    comment: str = Field(default="")
    created_at: datetime = Field(default_factory=datetime.utcnow)

    class Settings:
        name = "reviews"
