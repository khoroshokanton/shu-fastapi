from pydantic import BaseModel, EmailStr, ConfigDict


class UserBaseSchema(BaseModel):
    email: EmailStr


class UserCreateSchema(UserBaseSchema):
    password: str


class UserReadSchema(UserBaseSchema):
    id: int
    hashed_password: str

    model_config = ConfigDict(from_attributes=True)
