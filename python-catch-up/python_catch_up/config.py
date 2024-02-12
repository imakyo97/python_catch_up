from functools import lru_cache
import os
from pydantic_settings import BaseSettings, SettingsConfigDict

def get_env_file():
    env = os.getenv("APP_ENV", "dev")
    if env == "dev":
        return "env/.dev_env"
    else:
        return "env/.dev_env"

class Settings(BaseSettings):
    db_path: str
    db_url: str 

    model_config = SettingsConfigDict(env_file=get_env_file())

@lru_cache
def get_settings():
    return Settings()
