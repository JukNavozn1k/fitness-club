from repositories import user_repository,roles_repository, permissions_repository

from .users import get_user_service
from .auth import get_auth_service
from .reviews import get_reviews_service

from .rbac import get_rbac_init_service,get_role_checker_service

# from .permissions import get_rbac_init_service

auth_service = get_auth_service()
user_service = get_user_service(user_repository, auth_service)
reviews_service = get_reviews_service()

rbac_init_service = get_rbac_init_service(roles_repository,permissions_repository)
role_checker_service = get_role_checker_service(roles_repository)