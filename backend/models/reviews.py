
from beanie import Document,Link

from datetime import datetime
from beanie import Document

from pydantic import Field

from .users import User

class Review(Document):
    user : Link[User]
    rating: int = Field(..., ge=1, le=5)  # Оценка от 1 до 5
    comment: str = Field(default="")
    created_at: datetime = Field(default_factory=datetime.utcnow)

    class Settings:
        name = "reviews"
