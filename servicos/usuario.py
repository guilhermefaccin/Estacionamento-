
from sqlmodel import Session, select
from entidades.models import Usuario
from schemas.usuario import UsuarioCriar, UsuarioAtualizar


def cadastrar_usuario(dados: UsuarioCriar, db: Session):
    usuario = Usuario.model_validate(dados.model_dump())

    db.add(usuario)
    db.commit()
    db.refresh(usuario)

    return usuario

from sqlmodel import select



def listar_usuarios(db: Session) -> list[Usuario]:
    comando = select(Usuario).where(Usuario.ativo == True)
    usuarios = db.exec(comando).all()
    return list(usuarios)


def buscar_usuario_por_id(
    id_usuario: int,
    db: Session
) -> Usuario | None:
    comando = select(Usuario).where(
        Usuario.id_usuario == id_usuario
    )

    usuario = db.exec(comando).first()

    return usuario

def atualizar_usuario(
    id_usuario: int,
    dados: UsuarioAtualizar,
    db: Session
) -> Usuario | None:
    usuario = buscar_usuario_por_id(id_usuario, db)

    if usuario is None:
        return None

    usuario.nome = dados.nome
    usuario.cpf = dados.cpf
    usuario.email = str(dados.email)

    db.add(usuario)
    db.commit()

    return usuario



def desativar_usuario(
    id_usuario: int,
    db: Session
) -> Usuario | None:
    usuario = buscar_usuario_por_id(id_usuario, db)

    if usuario is None:
        return None

    usuario.ativo = False

    db.add(usuario)
    db.commit()
    db.refresh(usuario)

    return usuario
