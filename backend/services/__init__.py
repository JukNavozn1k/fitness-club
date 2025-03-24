from repositories import user_repository

from .users import get_user_service
from .auth import get_auth_service


auth_service = get_auth_service()
user_service = get_user_service(user_repository, auth_service)