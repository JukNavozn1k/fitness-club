from pydantic import BaseModel,Field
from datetime import datetime
from .users import UserOut

from .base import EntityBase

class ReviewBase(BaseModel):
    rating: int = Field(..., ge=1, le=5)  # Оценка от 1 до 5
    comment: str = Field(default="")
    

class CreatedReview(ReviewBase):
    user: UserOut  
    created_at: datetime = Field(default_factory=datetime.utcnow)


class ReviewOut(EntityBase,CreatedReview):
    ...

    
