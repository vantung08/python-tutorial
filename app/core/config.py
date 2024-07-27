from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    mongodb_uri: str

    class Config: # fallback
        env_file = ".env"

settings = Settings()
