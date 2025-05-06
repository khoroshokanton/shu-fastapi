from pydantic import BaseModel, EmailStr


class AuthLoginEmailPasswordSchema(BaseModel):
    email: EmailStr
    password: str
