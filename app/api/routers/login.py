from fastapi import APIRouter, HTTPException
from app import crud
from app.schema import UserLogin
from app.models import Token
from app.core.security import create_access_token
from datetime import timedelta

router = APIRouter(
    prefix="/login"
    )

@router.post("/")
async def login(user: UserLogin):
    try:
        login_user = await crud.authenticate_user(user.email, user.password)
        access_token_expire = timedelta(minutes=11520)
        return Token(access_token=create_access_token(login_user.id, access_token_expire))
    except Exception as e:
        raise Exception(f"Unable to login the user due to the following error: {e}")
    