from pydantic import BaseModel, EmailStr, Field

class CreateUserSchema(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(..., min_length=6)

class UserSchema(BaseModel):
    id: int
    username: str
    email: EmailStr

    class Config:
        orm_mode = True

class LoginSchema(BaseModel):
    username: str
    password: str
