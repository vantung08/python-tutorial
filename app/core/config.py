from pydantic_settings import BaseSettings
import secrets

class Settings(BaseSettings):
    mongodb_uri: str
    # SECRET_KEY: str = secrets.token_urlsafe(32)
    SECRET_KEY: str = "XN4rx935RJ8EBsf5HGMprmAlDcLnbRp0Gd021dlA0fc"
    # 60 minutes * 24 hours * 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60*24*8

    class Config: # fallback
        env_file = ".env"

settings = Settings()
