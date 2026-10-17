
from pydantic import BaseModel, Field, ConfigDict, EmailStr


class UsuarioCriar(BaseModel):
    nome: str = Field(min_length=1, max_length=100)
    cpf: str = Field(pattern=r"^\d{11}$")
    email: EmailStr = Field(max_length=80)


class UsuarioResposta(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id_usuario: int
    nome: str
    cpf: str
    email: EmailStr
    ativo: bool

class UsuarioAtualizar(BaseModel):
    nome: str = Field(min_length=1, max_length=100)
    cpf: str = Field(pattern=r"^\d{11}$")
    email: EmailStr = Field(max_length=80)