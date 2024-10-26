from fastapi import APIRouter
from fastapi.responses import JSONResponse
from shared.schemas.auth import Login
from utils.auth_service import AuthService


router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    responses={404: {"description": "Not found"}}
)


@router.post("/login", response_class=JSONResponse)
async def login_user(data: Login):
    user = await AuthService.login(login=data.login, password=data.password)
    if user:
        token = await AuthService.get_token(role=user.get('role', 'undefined'))
        return JSONResponse(status_code=200, content={'token': token})
    return JSONResponse(status_code=404,
                        content={'error': 'Такого пользователя не существует'})


@router.post("/role", response_class=JSONResponse)
async def get_role(token: str):
    role = await AuthService.get_role(token=token)
    return JSONResponse(status_code=200, content={'role': role})
