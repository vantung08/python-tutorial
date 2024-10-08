from passlib.context import CryptContext
from typing import Any
from datetime import timedelta, datetime, timezone
import jwt
from app.core.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
ALGORITHM = "HS256"

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(subject: str | Any, expires_delta: timedelta) -> str:
    expire_time = datetime.now(timezone.utc) + expires_delta
    to_encode = {"sub": str(subject), "exp": expire_time,}
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt