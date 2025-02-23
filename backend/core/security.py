import jwt
import datetime
# from fastapi.security.oauth2 import OAuth2PasswordBearer
# from passlib.context import CryptContext

from core.config import settings

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")

# # Хеширует пароли с солью
# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Функция для создания access токена
def create_access_token(sub):
    expiration = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days=settings.auth.lifetime_acsess)  
    payload = {
        'sub': sub,
        'exp': expiration
    }
    return jwt.encode(payload, settings.auth.secret_key, algorithm='HS256')

# Функция для создания refresh токена
def create_refresh_token(sub):
    expiration = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days=settings.auth.lifetime_refresh)  
    payload = {
        'sub': sub,
        'exp': expiration  # Время истечения токена
    }
    return jwt.encode(payload, settings.auth.refresh_key, algorithm='HS256')

# Функция для декодирования access токена
def decode_access_token(token):
    try:
        decoded = jwt.decode(token, settings.auth.secret_key, algorithms=['HS256'])
        return decoded
    except jwt.ExpiredSignatureError:
        return "Access token expired"
    except jwt.InvalidTokenError:
        return "Invalid access token"

# Функция для декодирования refresh токена
def decode_refresh_token(token):
    try:
        decoded = jwt.decode(token, settings.auth.refresh_key, algorithms=['HS256'])
        return decoded
    except jwt.ExpiredSignatureError:
        return "Refresh token expired"
    except jwt.InvalidTokenError:
        return "Invalid refresh token"

