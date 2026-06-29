from pydantic import BaseModel, Field

class TokenSchema(BaseModel):
    access_token: str
    token_type: str = "bearer"

class LoginResponseSchema(BaseModel):
    token: TokenSchema
    user: "UserSchema"

    class Config:
        orm_mode = True
