from sqladmin.authentication import AuthenticationBackend
from starlette.requests import Request

from core.config import settings

class AdminAuth(AuthenticationBackend):
    async def login(self, request: Request) -> bool:
        form = await request.form()
        username = form.get("username")
        password = form.get("password")

        # Здесь можно добавить проверку по БД или другому источнику
        if username == "admin" and password == "secret":
            request.session.update({"authenticated": True})
            return True
        return False

    async def logout(self, request: Request) -> bool:
        request.session.clear()
        return True

    async def authenticate(self, request: Request) -> bool:
        return request.session.get("authenticated", False)


admin_auth = AdminAuth(settings.auth.secret_key)