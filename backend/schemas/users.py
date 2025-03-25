from pydantic import BaseModel
from beanie import PydanticObjectId
from datetime import datetime



class UserOut(BaseModel):
    id: PydanticObjectId
    username: str
    joined_date: datetime