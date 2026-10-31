
from pydantic import BaseModel, EmailStr


class LoginRequest(BaseModel):
    email: EmailStr
    senha: str


class LoginResposta(BaseModel):
    access_token: str
    token_type: str = "bearer"
