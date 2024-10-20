from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    HOST:str
    PORT:int
    RELOAD: bool

    class Config:
        env_file=".env"

settings = Settings()