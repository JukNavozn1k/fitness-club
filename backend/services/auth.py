import jwt
from typing import Optional
from core.config import settings

class AuthService:
    def __init__(self):
        # Устанавливаем секретные ключи для кодирования и декодирования токенов
        self.secret_key = settings.auth.secret_key
        self.refresh_key = settings.auth.refresh_key

    def decode_token(self, token: str, is_refresh: bool = False):
        key = self.refresh_key if is_refresh else self.secret_key
        
        try:
            decoded = jwt.decode(token, key, algorithms=['HS256'])
            return decoded
        except jwt.ExpiredSignatureError:
            raise jwt.ExpiredSignatureError("Token expired")
        except jwt.InvalidTokenError:
            raise jwt.InvalidTokenError("Invalid token")

    def parse_token(self, authorization: Optional[str] = None, is_refresh: bool = False):
        if authorization is None:
            raise ValueError("Authorization header missing")
        
        token_prefix = "Bearer "
        if not authorization.startswith(token_prefix):
            raise ValueError("Invalid token type")
        
        token = authorization[len(token_prefix):]
        return self.decode_token(token, is_refresh)
    
auth_service = AuthService()

