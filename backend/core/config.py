from pydantic_settings import BaseSettings

class App(BaseSettings):
    title: str = 'FastAPI'
    version : str = '1.0.0'

class Auth(BaseSettings):
    secret_key : str = 'foo'
    refresh_key : str = 'bar'

    lifetime_secret: int = 15 # time in days
    lifetime_refresh: int = 15

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

    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 10

    def get_url(self, test: bool = False) -> str:
        if test:
            return f"postgresql+asyncpg://{self.test_db_user}:{self.test_db_pass}@{self.test_db_host}:{self.test_db_port}/{self.test_db_name}"
        return f"postgresql+asyncpg://{self.db_user}:{self.db_pass}@{self.db_host}:{self.db_port}/{self.db_name}"
    

class Settings(BaseSettings):
    app: App = App()
    db: Database = Database()
    auth: Auth = Auth()


settings = Settings()
