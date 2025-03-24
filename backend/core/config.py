from pydantic_settings import BaseSettings

class App(BaseSettings):
    title: str = 'FastAPI'
    version: str = '1.0.0'
    frontend_url: str = '*'  # Add this line

class Auth(BaseSettings):
    secret_key : str = 'foo'
    refresh_key : str = 'bar'

    access_token_expiration: int = 15 # time in days
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


class Settings(BaseSettings):
    app: App = App()
    db: Database = Database()
    auth: Auth = Auth()
   

settings = Settings()
