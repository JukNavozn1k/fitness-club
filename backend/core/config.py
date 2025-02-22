from pydantic_settings import BaseSettings,SettingsConfigDict
from pydantic import BaseModel

class DatabaseSettings(BaseSettings):
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

    def get_asyncpg_url(self, test: bool = False) -> str:
        if test:
            return f"postgresql+asyncpg://{self.test_db_user}:{self.test_db_pass}@{self.test_db_host}:{self.test_db_port}/{self.test_db_name}"
        return f"postgresql+asyncpg://{self.db_user}:{self.db_pass}@{self.db_host}:{self.db_port}/{self.db_name}"


class ApiPrefix(BaseSettings):
    prefix: str = '/api'

class Settings(BaseSettings):
    api: ApiPrefix = ApiPrefix()
    db: DatabaseSettings = DatabaseSettings()


settings = Settings()
print(settings.db)