
from . import models, schemas
from sqlalchemy.orm import Session


def get_usuario_por_email(db: Session, email: str):
    return db.query(models.Lojista).filter(models.Lojista.email == email).first()

def get_usuario_por_cpf_cnpj(db: Session, cpf_cnpj: str):
    return db.query(models.Lojista).filter(models.Lojista.cpf_cnpj == cpf_cnpj).first()

def criar_lojista(db: Session, user: schemas.LojistaBase):
    db_lojista = models.Lojista(
        nome=user.nome,
        cpf_cnpj=user.cpf_cnpj,
        email=user.email, 
        senha=user.senha,
        saldo=user.saldo
    )
    
    db.add(db_lojista)
    db.commit()
    db.refresh(db_lojista)
    return db_lojista