
from sqlmodel import SQLModel, Field


class Usuario(SQLModel, table=True):
    __tablename__ = "usuarios"

    id_usuario: int | None = Field(
        default=None,
        primary_key=True
    )

    nome: str = Field(
        max_length=100,
        nullable=False
    )

    cpf: str = Field(
        max_length=11,
        unique=True,
        nullable=False
    )

    email: str = Field(
        max_length=80,
        nullable=False
    )


    ativo: bool = Field(default=True, nullable=False)