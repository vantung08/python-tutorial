from fastapi import APIRouter
from app import crud
from app.core.security import verify_password
from app.schema import UserLogin

router = APIRouter(
    prefix="/login"
    )

@router.post("/")
async def login(user: UserLogin):
    try:
        login_user = await crud.get_user_by_email(user.email)
        if verify_password(user.password, login_user.hashed_password):
            print("You have been login successfully!")
        else:
            print("Wrong email or password!")
    except Exception as e:
        raise Exception(f"Unable to login the user due to the following error: {e}")
    