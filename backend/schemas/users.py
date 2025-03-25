from pydantic import BaseModel
from datetime import datetime

# Схемы для User
class UserBase(BaseModel):
    username: str

class UserOut(BaseModel):
    username: str
    joined_date: datetime