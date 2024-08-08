from fastapi.security import OAuth2PasswordBearer
from typing import Annotated
from fastapi import Depends, HTTPException, status
from app.models import User
from app.schema import TokenPayload
import jwt
from app.core.config import settings
from app.core.security import ALGORITHM
from jwt.exceptions import InvalidTokenError
from pydantic import ValidationError
from app import crud

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login/access-token")

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]) -> User:
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=ALGORITHM)
        token_data = TokenPayload(**payload)
    except (InvalidTokenError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credential"
        )
    user = await crud.get_user_by_id(token_data.sub)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

def get_current_active_user(current_user: Annotated[User, Depends(get_current_user)]) -> User:
        active_status = current_user.is_active
        if not active_status:
             raise HTTPException(
                  status_code=status.HTTP_403_FORBIDDEN,
                  detail="Could not validate credential, inactive user")
        return current_user