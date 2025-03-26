from pydantic import BaseModel
from datetime import datetime

from .base import EntityBaseMixin

class UserOut(EntityBaseMixin, BaseModel):

    username: str
    joined_date: datetime