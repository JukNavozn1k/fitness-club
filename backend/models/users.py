from sqlalchemy import Integer, String
from sqlalchemy.orm import relationship, Mapped, mapped_column
from .database import Base

class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    username: Mapped[str] = mapped_column(String(32), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(128), nullable=False)
    
    # Прямая связь User -> Role через user_roles
    roles: Mapped[list["Role"]] = relationship("Role", secondary=user_roles, back_populates="users", lazy='selectin')

    def __str__(self):
        return f'{self.username}'
