
from sqlmodel import Session, select

from entidades.models import (
    ContratoMensal,
    StatusContrato,
)
from schemas.contratos_mensais import (
    ContratoMensalCriar,
    ContratoMensalAtualizar,
)


def cadastrar_contrato(
    db: Session,
    dados: ContratoMensalCriar,
    id_usuario: int,
) -> ContratoMensal:
    valores = dados.model_dump(exclude_unset=True)

    contrato = ContratoMensal(**valores)
    contrato.id_usuario_cadastro = id_usuario
    contrato.id_usuario_alteracao = id_usuario

    db.add(contrato)
    db.commit()
    db.refresh(contrato)

    return contrato


def listar_contratos(db: Session) -> list[ContratoMensal]:
    statement = select(ContratoMensal).where(
        ContratoMensal.status != StatusContrato.ENCERRADO
    )

    return list(db.exec(statement).all())


def buscar_contrato_por_id(
    db: Session,
    id_contrato: int,
) -> ContratoMensal | None:
    statement = select(ContratoMensal).where(
        ContratoMensal.id_contrato == id_contrato,
        ContratoMensal.status != StatusContrato.ENCERRADO,
    )

    return db.exec(statement).first()


def atualizar_contrato(
    db: Session,
    contrato: ContratoMensal,
    dados: ContratoMensalAtualizar,
    id_usuario: int,
) -> ContratoMensal:
    alteracoes = dados.model_dump(exclude_unset=True)

    for campo, valor in alteracoes.items():
        setattr(contrato, campo, valor)

    contrato.id_usuario_alteracao = id_usuario

    db.add(contrato)
    db.commit()
    db.refresh(contrato)

    return contrato


def desativar_contrato(
    db: Session,
    contrato: ContratoMensal,
    id_usuario: int,
) -> ContratoMensal:
    contrato.status = StatusContrato.ENCERRADO
    contrato.id_usuario_alteracao = id_usuario

    db.add(contrato)
    db.commit()
    db.refresh(contrato)

    return contrato
