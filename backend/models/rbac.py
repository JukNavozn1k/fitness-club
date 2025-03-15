from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import relationship, Mapped, mapped_column
from .database import Base

from typing import List 

# Модель Role
class Role(Base):
    __tablename__ = 'roles'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(32), unique=True, nullable=False)
    
    # Связь с пользователями через ассоциативную таблицу
    users: Mapped[List["User"]] = relationship("User", secondary="user_roles", back_populates="roles")
    
    # Связь с правами через ассоциативную таблицу
    permissions: Mapped[List["Permission"]] = relationship("Permission", secondary="role_permissions", back_populates="roles")

# Модель Permission
class Permission(Base):
    __tablename__ = 'permissions'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(64), unique=True, nullable=False)
    
    # Связь с ролями через ассоциативную таблицу
    roles: Mapped[List["Role"]] = relationship("Role", secondary="role_permissions", back_populates="permissions")

# Ассоциативная модель для User <-> Role
class UserRole(Base):
    __tablename__ = "user_roles"
    
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), primary_key=True)
    role_id: Mapped[int] = mapped_column(Integer, ForeignKey("roles.id"), primary_key=True)
    
    # Не нужен явный relationship, поскольку они уже прописаны в моделях User и Role

# Ассоциативная модель для Role <-> Permission
class RolePermission(Base):
    __tablename__ = "role_permissions"
    
    role_id: Mapped[int] = mapped_column(Integer, ForeignKey("roles.id"), primary_key=True)
    permission_id: Mapped[int] = mapped_column(Integer, ForeignKey("permissions.id"), primary_key=True)
    
    # Не нужен явный relationship, поскольку они уже прописаны в моделях Role и Permission
