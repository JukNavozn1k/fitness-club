from sqlalchemy import Integer, String
from sqlalchemy.orm import relationship, Mapped, mapped_column
from .database import Base

class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    username: Mapped[str] = mapped_column(String(32), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(128), nullable=False)
    
    # Связь с ассоциацией ролей
    user_roles: Mapped[list['UserRole']] = relationship("UserRole", back_populates="user", cascade="all, delete-orphan")
    
    # Удобное получение ролей через ассоциацию
    @property
    def roles(self) -> list["Role"]:
        return [ur.role for ur in self.user_roles]

    def __str__(self):
        return f'{self.username}'