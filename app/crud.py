
from . import models, schemas
from sqlalchemy.orm import Session


def get_lojista_por_email(db: Session, email: str):
    return db.query(models.Lojista).filter(models.Lojista.email == email).first()

def get_lojista_por_cpf_cnpj(db: Session, cpf_cnpj: str):
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

def get_usuario_por_email(db: Session, email: str):
    return db.query(models.Usuario).filter(models.Usuario.email == email).first()

def get_usuario_por_cpf_cnpj(db: Session, cpf_cnpj: str):
    return db.query(models.Usuario).filter(models.Usuario.cpf_cnpj == cpf_cnpj).first()

def criar_usuario(db: Session, user: schemas.UsuarioBase):
    db_usuario = models.Usuario(
        nome=user.nome,
        cpf_cnpj=user.cpf_cnpj,
        email=user.email, 
        senha=user.senha,
        saldo=user.saldo
    )
    
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

def criar_transacao(db: Session, transacao: schemas.TransacaoBase):
    db_transacao = models.Transacao(
        valor_transacao=transacao.valor_transacao,
        id_pagador=transacao.id_pagador,
        id_recebedor=transacao.id_recebedor
    )

    db.add(db_transacao)
    db.commit()
    db.refresh(db_transacao)
    return db_transacao


