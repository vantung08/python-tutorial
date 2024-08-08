from fastapi.security import OAuth2PasswordBearer
from typing import Annotated
from fastapi import Depends, HTTPException, status
from app.models import User
from app.schema import TokenPayload
import jwt
from app.core.config import settings
from app.core.security import ALGORITHM
from jwt.exceptions import InvalidTokenError
from app import crud

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login/access-token")

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]) -> User:
    credentials_exception = HTTPException(
         status_code=status.HTTP_401_UNAUTHORIZED,
         detail="Could not validate credentials",
         headers={"WWW-Authenticate": "Bearer"}
    )
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=ALGORITHM)
        token_data = TokenPayload(**payload)
        user_email = token_data.sub
        if not user_email:
             raise credentials_exception
    except InvalidTokenError:
         raise credentials_exception
    user = await crud.get_user_by_email(token_data.sub)
    if not user:
        raise credentials_exception
    return user

def get_current_active_user(current_user: Annotated[User, Depends(get_current_user)]) -> User:
        active_status = current_user.is_active
        if not active_status:
             raise HTTPException(
                  status_code=status.HTTP_403_FORBIDDEN,
                  detail="Could not validate credential, inactive user")
        return current_user