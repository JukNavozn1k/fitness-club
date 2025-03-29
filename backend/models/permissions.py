from beanie import Document,Indexed,Link

from typing import List,Optional
from pydantic import Field

# --- MongoDB модели (Beanie ODM) ---
class Permission(Document):
    """
    Динамические разрешения с валидацией имен.
    Формат: <область>:<действие> (пример: "users:create")
    """
    name: Indexed(str, unique=True) = Field(..., pattern="^[a-z]+:[a-z_]+$")
    description: str = Field(default="")
    category: str = Field(default="general")
    
    class Settings:
        name = "rbac_permissions"
        indexes = ["category"]  # Добавляем индекс для категорий

class Role(Document):
    """Роли с наследованием и привязкой к разрешениям"""
    name: Indexed(str, unique=True)
    permissions: List[Link["Permission"]] = Field(default=[])
    parent_roles: List[Link["Role"]] = Field(default=[])  # Наследование ролей
    is_default: bool = Field(default=False)
    
    class Settings:
        name = "rbac_roles"