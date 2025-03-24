from sqlalchemy import Integer, String, Enum, DateTime
from sqlalchemy.orm import relationship, Mapped, mapped_column
from .database import Base
from enum import Enum as PyEnum
from typing import List
from datetime import datetime

# Перечисление разрешений
class PermissionEnum(PyEnum):
    CREATE_WORKOUT = "create_workout"
    DELETE_WORKOUT = "delete_workout"
    UPDATE_WORKOUT = "update_workout"
    VIEW_WORKOUT = "view_workout"

# Перечисление ролей с разрешениями
class RoleEnum(PyEnum):
    ADMIN = "admin"
    TRAINER = "trainer"
    MEMBER = "member"

    @property
    def permissions(self):
        if self == RoleEnum.ADMIN:
            return [PermissionEnum.CREATE_WORKOUT, PermissionEnum.DELETE_WORKOUT, PermissionEnum.UPDATE_WORKOUT, PermissionEnum.VIEW_WORKOUT]
        elif self == RoleEnum.TRAINER:
            return [PermissionEnum.CREATE_WORKOUT, PermissionEnum.UPDATE_WORKOUT, PermissionEnum.VIEW_WORKOUT]
        elif self == RoleEnum.MEMBER:
            return [PermissionEnum.VIEW_WORKOUT]
        return []

class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    username: Mapped[str] = mapped_column(String(32), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(128), nullable=False)
    role: Mapped[RoleEnum] = mapped_column(Enum(RoleEnum), nullable=False)
    joined_date: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
