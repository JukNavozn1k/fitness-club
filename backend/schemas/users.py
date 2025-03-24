from pydantic import BaseModel
from datetime import datetime

# Схемы для User
class UserBase(BaseModel):
    username: str

class UserOut(UserBase):
    id: int
    role: str
    joined_date: datetime

    class Config:
        from_attributes = True