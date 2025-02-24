import jwt
from typing import Optional
from core.config import settings


class AuthService:
    def __init__(self):
        # Устанавливаем секретные ключи для кодирования и декодирования токенов
        self.secret_key = settings.auth.secret_key
        self.refresh_key = settings.auth.refresh_key

    # Функция для декодирования токена
    def decode_token(self, token: str, is_refresh: bool = False):
        key = self.refresh_key if is_refresh else self.secret_key
        
        try:
            decoded = jwt.decode(token, key, algorithms=['HS256'])
            return decoded
        except jwt.ExpiredSignatureError:
            raise jwt.ExpiredSignatureError("Token expired")
        except jwt.InvalidTokenError:
            raise jwt.InvalidTokenError("Invalid token")

    # Функция для парсинга токена из заголовка
    def get_token_from_header(self, authorization: Optional[str] = None, is_refresh: bool = False):
        if authorization is None:
            raise ValueError("Authorization header missing")
        
        # Извлекаем токен из заголовка "Bearer <token>"
        token_prefix = "Bearer "
        if not authorization.startswith(token_prefix):
            raise ValueError("Invalid token type")
        
        token = authorization[len(token_prefix):]
        return self.decode_token(token, is_refresh)
    

# # Пример использования на fast api
# @app.get("/secure-data")
# async def get_secure_data(authorization: Optional[str] = Header(None)):
#     try:
#         decoded_token = auth_service.get_token_from_header(authorization)
#         return {"message": "You are authorized", "token": decoded_token}
#     except (jwt.ExpiredSignatureError, jwt.InvalidTokenError, ValueError) as e:
#         # Обрабатываем исключения
#         raise HTTPException(status_code=401, detail=str(e))