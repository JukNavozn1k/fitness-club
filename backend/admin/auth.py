from sqladmin.authentication import AuthenticationBackend
from starlette.requests import Request

from schemas.auth import AuthSchema
from services.users import user_service

class AdminAuth(AuthenticationBackend):
    async def login(self, request: Request) -> bool:
        try:
            form = await request.form()     
            validated_form = AuthSchema(**form)
            token = await user_service.login(validated_form.model_dump())
            if token:
                request.session.update({"Authorization": f'Bearer {token["token"]}'})
                return True
            return False
        except: return False

    async def logout(self, request: Request) -> bool:
        request.session.clear()
        return True

    async def authenticate(self, request: Request) -> bool:
        try: 
            token = request.session.get("Authorization")
            user_service.auth_service.parse_token(token)
            return True
        except Exception as e:
            return False 




