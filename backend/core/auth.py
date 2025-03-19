from abc import ABC, abstractmethod
from typing import Optional
from fastapi import Request, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

class TokenGateway(ABC):
    @abstractmethod
    def get_token(self) -> Optional[str]:
        pass

class FastAPITokenGateway(TokenGateway):
    def __init__(self, authorization: HTTPAuthorizationCredentials = None):
        self.authorization = authorization

    def get_token(self) -> Optional[str]:
        if not self.authorization:
            return None
        return self.authorization.credentials

class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super().__init__(auto_error=auto_error)

    async def __call__(self, request: Request) -> FastAPITokenGateway:
        try:
            credentials = await super().__call__(request)
            return FastAPITokenGateway(credentials)
        except:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authentication credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )

jwt_bearer = JWTBearer()
