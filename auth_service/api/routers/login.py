from fastapi import APIRouter

router = APIRouter(
    prefix="/login"
    )


@router.get("/access-token") 
def login_access_token():
    return {"Message": "This is the access token"}