
from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import relationship, Mapped, mapped_column
from .database import Base

class Role(Base):
    __tablename__ = 'roles'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(32), unique=True, nullable=False)
    
    user_roles: Mapped[list['UserRole']] = relationship("UserRole", back_populates="role", cascade="all, delete-orphan")
    role_permissions: Mapped[list['RolePermission']] = relationship("RolePermission", back_populates="role", cascade="all, delete-orphan")
    
    @property
    def permissions(self) -> list["Permission"]:
        return [rp.permission for rp in self.role_permissions]
    
    def __str__(self):
        return self.name

class Permission(Base):
    __tablename__ = 'permissions'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(64), unique=True, nullable=False)
    
    role_permissions: Mapped[list['RolePermission']] = relationship("RolePermission", back_populates="permission", cascade="all, delete-orphan")
    
    @property
    def roles(self) -> list["Role"]:
        return [rp.role for rp in self.role_permissions]
    
    def __str__(self):
        return self.name

# Ассоциация User <-> Role
class UserRole(Base):
    __tablename__ = "user_roles"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=False)
    role_id: Mapped[int] = mapped_column(Integer, ForeignKey("roles.id"), nullable=False)
    
    user: Mapped["User"] = relationship("User", back_populates="user_roles")
    role: Mapped["Role"] = relationship("Role", back_populates="user_roles")

# Ассоциация Role <-> Permission
class RolePermission(Base):
    __tablename__ = "role_permissions"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    role_id: Mapped[int] = mapped_column(Integer, ForeignKey("roles.id"), nullable=False)
    permission_id: Mapped[int] = mapped_column(Integer, ForeignKey("permissions.id"), nullable=False)
    
    role: Mapped["Role"] = relationship("Role", back_populates="role_permissions")
    permission: Mapped["Permission"] = relationship("Permission", back_populates="role_permissions")
