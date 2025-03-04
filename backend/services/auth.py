import jwt
from typing import Optional
from datetime import datetime, timedelta
from core.config import settings


class AuthService:
    def __init__(self):
        self.secret_key = settings.auth.secret_key
        self.refresh_key = settings.auth.refresh_key
        self.access_token_expiration = settings.auth.access_token_expiration
        self.refresh_token_expiration = settings.auth.refresh_token_expiration

    def create_access_token(self, data: dict):
        expiration = datetime.utcnow() + timedelta(days=self.access_token_expiration)
        to_encode = data.copy()
        if "sub" in to_encode:
            to_encode["sub"] = str(to_encode["sub"])
        to_encode.update({"exp": expiration})
        encoded_jwt = jwt.encode(to_encode, self.secret_key, algorithm='HS256')
        return {'token': encoded_jwt, 'type': 'Bearer'}

    def create_refresh_token(self, data: dict):
        expiration = datetime.utcnow() + timedelta(days=self.refresh_token_expiration)
        to_encode = data.copy()
        to_encode.update({"exp": expiration})
        encoded_jwt = jwt.encode(to_encode, self.refresh_key, algorithm='HS256')
        return {'token': encoded_jwt, 'type': 'Bearer'}

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

