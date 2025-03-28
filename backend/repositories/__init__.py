from .users import get_user_repository
from .reviews import get_reviews_repository
from .permissions import get_permissions_repository,get_roles_repository
user_repository = get_user_repository()
reviews_repository = get_reviews_repository()





roles_repository = get_roles_repository()
permissions_repository = get_permissions_repository()