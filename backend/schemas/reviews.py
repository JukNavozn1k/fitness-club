from pydantic import BaseModel,Field
from datetime import datetime
from .users import UserOut

class ReviewCreate(BaseModel):
    rating: int = Field(..., ge=1, le=5)  # Оценка от 1 до 5
    comment: str = Field(default="")
    

class ReviewOut(ReviewCreate):
    user: UserOut  # Здесь будет выводиться информация о пользователе через Pydantic схему
    created_at: datetime = Field(default_factory=datetime.utcnow)
