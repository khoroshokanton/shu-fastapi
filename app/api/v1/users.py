from fastapi import APIRouter, Depends, Request, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import db
from app.service.user import UserService
from app.core.auth import decode_jwt
from app.schemas.user import UserReadSchema

router = APIRouter(prefix="/users", tags=["Пользователи"])


async def get_token_from_cookies(request: Request) -> str | None:
    return request.cookies.get("access_token")


async def get_current_user(
    token=Depends(get_token_from_cookies),
    session: AsyncSession = Depends(db.get_session),
):
    expt = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail="Необходимо войти в аккаунт"
    )

    if token is None:
        raise expt

    payload = decode_jwt(token)
    user = await UserService.get_one_or_none(session, email=payload["email"])

    if user is None:
        raise expt

    return user


@router.get("/me")
async def me(user: UserReadSchema = Depends(get_current_user)):
    return user
