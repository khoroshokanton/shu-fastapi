from datetime import datetime, timezone, timedelta

from passlib.context import CryptContext
from jose import jwt

from app.core.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password, salt=settings.auth.salt)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=10)
    to_encode.update({"exp": expire})

    encode_jwt = jwt.encode(
        to_encode, settings.auth.secret_key, algorithm=settings.auth.algorithm
    )
    return encode_jwt


def decode_jwt(token: str) -> dict:
    decode = jwt.decode(
        token=token, key=settings.auth.secret_key, algorithms=[settings.auth.algorithm]
    )

    return decode
