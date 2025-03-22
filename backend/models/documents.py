from beanie import Document
from pydantic import BaseModel
from typing import Optional

class User(Document):
    username: str
    email: str
    full_name: Optional[str] = None

    class Settings:
        collection = "users"

class Product(Document):
    name: str
    description: Optional[str] = None
    price: float

    class Settings:
        collection = "products"
