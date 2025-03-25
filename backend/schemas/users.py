from pydantic import BaseModel
from datetime import datetime

from beanie import PydanticObjectId

class UserOut(BaseModel):
    id: PydanticObjectId
    username: str
    joined_date: datetime