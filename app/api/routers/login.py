from fastapi import APIRouter, Depends
from app import crud
from app.schema import Token
from app.core.security import create_access_token
from datetime import timedelta
from app.core.config import settings
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated

router = APIRouter(
    prefix="/login"
    )

@router.post("/access-token")
async def login_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]) -> Token:
    try:
        login_user = await crud.authenticate_user(form_data.username, form_data.password)
        access_token_expire = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        return Token(access_token=create_access_token(login_user.id, access_token_expire))
    except Exception as e:
        raise Exception(f"Unable to login the user due to the following error: {e}")
    