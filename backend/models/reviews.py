
from beanie import Document,Link
from .users import UserMongo
from datetime import datetime
from beanie import Document,Indexed

from pydantic import Field


class ReviewMongo(Document):
    user: Link[UserMongo]  # Связь с пользователем
    rating: int = Field(..., ge=1, le=5)  # Оценка от 1 до 5
    comment: str = Field(default="")
    created_at: datetime = Field(default_factory=datetime.utcnow)

    class Settings:
        name = "reviews"
