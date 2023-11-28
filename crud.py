from sqlalchemy.orm import Session

from . import models, schemas

def criar_lojista(db: Session, user: schemas.LojistaBase):
    db_lojista = models.Lojista(
        nome=user.nome,
        cpf_cnpj=user.cpf_cnpj,
        email=user.email, 
        senha=user.senha
    )
    db.add(db_lojista)
    db.commit()
    db.refresh(db_lojista)
    return db_lojista