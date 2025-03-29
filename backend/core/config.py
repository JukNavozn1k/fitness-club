from typing import Dict, List, Optional
from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings

class App(BaseSettings):
    title: str = 'FastAPI'
    version: str = '1.0.0'
    frontend_url: str = '*'

class Auth(BaseSettings):
    secret_key: str = 'foo'
    refresh_key: str = 'bar'
    access_token_expiration: int = 15  # days
    refresh_token_expiration: int = 15

class Database(BaseSettings):
    db_name: str
    db_user: str
    db_pass: str
    db_host: str
    db_port: int
    
    test_db_name: str
    test_db_user: str
    test_db_pass: str
    test_db_host: str
    test_db_port: int

    echo: bool = True
    
    def get_url(self, test: bool = False) -> str:
        if test:
            return f"postgresql+asyncpg://{self.test_db_user}:{self.test_db_pass}@{self.test_db_host}:{self.test_db_port}/{self.test_db_name}"
        return f"postgresql+asyncpg://{self.db_user}:{self.db_pass}@{self.db_host}:{self.db_port}/{self.db_name}"

class MongoDB(BaseSettings):
    mongo_user: str = 'mongoadmin'
    mongo_password: str = 'secret'
    mongo_host: str = 'mongo'
    mongo_port: int = 27017
    mongo_db_name: str = 'fitness'
    mongo_rbac_collection_prefix: str = 'rbac_'  # Префикс для коллекций RBAC

    def get_url(self) -> str:
        return f"mongodb://{self.mongo_user}:{self.mongo_password}@{self.mongo_host}:{self.mongo_port}/"

class RBACRoleConfig(BaseModel):
    """Конфигурация отдельной роли"""
    permissions: List[str] = Field(default=["profile:read"])
    inherits: List[str] = Field(default=[])
    is_default: bool = False
    description: Optional[str] = None

class RBACSettings(BaseSettings):
    """Настройки системы RBAC"""
    auto_create_missing: bool = Field(
        default=True,
        description="Автоматически создавать недостающие permissions"
    )
    
    roles: Dict[str, RBACRoleConfig] = Field(
        default={
            # Клиент (обычный пользователь)
            "client": RBACRoleConfig(
                is_default=True,
                permissions=[
                    "review:create",
                    "review:read", 
                    "review:update",
                    "review:delete",
                    "profile:create",
                    "profile:read",
                    "profile:update",
                    "profile:delete"
                ],
                description="Base role for regular users"
            ),
            
            # Фитнес-тренер
            "trainer": RBACRoleConfig(
                permissions=[
                    "schedule:create",
                    "schedule:read",
                    "schedule:update", 
                    "schedule:delete",
                    "program:create",
                    "program:read",
                    "program:update",
                    "program:delete",
                    "exercise:create",
                    "exercise:read",
                    "exercise:update",
                    "exercise:delete",
                    "equipment:create",
                    "equipment:read",
                    "equipment:update",
                    "equipment:delete"
                ],
                inherits=["client"],  # Наследуем права клиента
                description="Fitness trainer role"
            ),
            
            # Администратор
            "admin": RBACRoleConfig(
                permissions=["*"],
                description="Full system access"
            )
        }
    )
    
    class Config:
        env_prefix = "RBAC_"
        env_nested_delim = "__"

class Settings(BaseSettings):
    app: App = App()
    db: Database = Database()
    auth: Auth = Auth()
    mongo: MongoDB = MongoDB()
    rbac: RBACSettings = RBACSettings()

settings = Settings()