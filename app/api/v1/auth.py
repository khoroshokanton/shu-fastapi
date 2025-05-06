from fastapi import APIRouter, HTTPException, status, Depends, Response

from app.schemas.user import UserCreateSchema
from app.schemas.auth import AuthLoginEmailPasswordSchema
from app.service.user import UserService
from app.core.auth import get_password_hash, create_access_token
from app.core.database import db

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register")
async def register(
    user_data: UserCreateSchema, session=Depends(db.get_session)
) -> dict:
    user = await UserService.get_one_or_none(session=session, email=user_data.email)
    if user is not None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="Пользователь уже существует"
        )
    user_data_dict = user_data.model_dump()
    user_data_dict.pop("password")
    user_data_dict["hashed_password"] = get_password_hash(user_data.password)

    await UserService.create(session=session, values=user_data_dict)
    return {"message": "success"}


@router.post("/login")
async def login(
    response: Response,
    user_data: AuthLoginEmailPasswordSchema,
    session=Depends(db.get_session),
) -> str:
    Exeption = HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST, detail="Неверный логин или пароль"
    )

    user = await UserService.get_one_or_none(session=session, email=user_data.email)
    if user is None:
        raise Exeption

    hashed_password = get_password_hash(user_data.password)
    if hashed_password != user.hashed_password:
        raise Exeption

    access_token = create_access_token({"email": user_data.email})
    response.set_cookie(key="access_token", value=access_token, httponly=True)

    return access_token


@router.post("/logout")
async def logout(response: Response):
    response.delete_cookie("access_token")
