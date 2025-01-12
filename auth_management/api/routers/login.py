from fastapi import APIRouter, Depends
from auth_management import crud
from auth_management.schema import Token
from auth_management.core.security import create_access_token
from datetime import timedelta
from auth_management.core.config import settings
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated
from auth_management.api.deps import SessionDep

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
    


# from fastapi import APIRouter

# router = APIRouter(
#     prefix="/login"
#     )


# @router.get("/access-token") 
# def login_access_token():
#     return {"Message": "This is the access token"}