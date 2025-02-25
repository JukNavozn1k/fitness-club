from repositories.base import AbstractSQLRepository

from models.users import User
from core.database import db

class UserSQLRepository(AbstractSQLRepository):
    ...

sql_user_repository = UserSQLRepository(db.get_session,User)