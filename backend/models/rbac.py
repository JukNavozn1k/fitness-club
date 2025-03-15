from sqlalchemy import ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship, Mapped, mapped_column
from .database import Base

# Ассоциация User <-> Role
user_roles = Table(
    "user_roles",
    Base.metadata,
    mapped_column("user_id", Integer, ForeignKey("users.id"), primary_key=True),
    mapped_column("role_id", Integer, ForeignKey("roles.id"), primary_key=True)
)

# Ассоциация Role <-> Permission
role_permissions = Table(
    "role_permissions",
    Base.metadata,
    mapped_column("role_id", Integer, ForeignKey("roles.id"), primary_key=True),
    mapped_column("permission_id", Integer, ForeignKey("permissions.id"), primary_key=True)
)

class Role(Base):
    __tablename__ = 'roles'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(32), unique=True, nullable=False)
    
    # Прямая связь Role -> User через user_roles
    users: Mapped[list["User"]] = relationship("User", secondary=user_roles, back_populates="roles", lazy='selectin')
    # Прямая связь Role -> Permission через role_permissions
    permissions: Mapped[list["Permission"]] = relationship("Permission", secondary=role_permissions, back_populates="roles", lazy='selectin')

    def __str__(self):
        return self.name

class Permission(Base):
    __tablename__ = 'permissions'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(64), unique=True, nullable=False)

    # Прямая связь Permission -> Role через role_permissions
    roles: Mapped[list["Role"]] = relationship("Role", secondary=role_permissions, back_populates="permissions", lazy='selectin')

    def __str__(self):
        return self.name
