from pydantic import BaseModel
from datetime import datetime

class UserOut(BaseModel):

    username: str
    joined_date: datetime