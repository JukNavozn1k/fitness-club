from typing import Optional
from services.auth import AuthService
class UserService:
    def __init__(self, repository, auth_service: Optional[AuthService] = None):
        self.repository = repository


user_service = UserService(None)