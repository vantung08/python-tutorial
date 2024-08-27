from fastapi import APIRouter, Depends
from app import crud
from app.schema import Token
from app.core.security import create_access_token
from datetime import timedelta
from app.core.config import settings
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated
from app.api.deps import SessionDep

router = APIRouter(
    prefix="/login"
    )


@router.post("/access-token") 
def login_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], session: SessionDep) -> Token:
    try:
        email = form_data.username
        password = form_data.password
        login_user = crud.authenticate_user(session=session, email=email, password=password)
        access_token_expire = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        return Token(access_token=create_access_token(login_user.email, access_token_expire))
    except Exception as e:
        raise Exception(f"Unable to login the user due to the following error: {e}")
    