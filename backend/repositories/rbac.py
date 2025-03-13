from models.rbac import Permission,Role,RolePermission,UserRole
from models import db

from repositories.base import AbstractSQLRepository

class RbacSQLRepository(AbstractSQLRepository):
    ...


sql_permission_repository = RbacSQLRepository(db.get_session, Permission)
sql_role_repository = RbacSQLRepository(db.get_session,Role)
sql_role_permission_repository = RbacSQLRepository(db.get_session,RolePermission)
sql_user_role_repository = RbacSQLRepository(db.get_session,UserRole)