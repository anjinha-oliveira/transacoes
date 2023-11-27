from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Numeric
from sqlalchemy.orm import relationship

from .database import Base

class Lojista(Base):
    __tablename__ = "lojistas"

    id_lojista = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False, index=True)
    cpf_cnpj = Column(String, nullable=False, unique=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    senha = Column(String, nullable=False)
    saldo = Column(Numeric, default=True)

    transacoes = relationship("Transacao", back_populates="recebedor")

class Usuario(Base):
    __tablename__ = "usuarios"

    id_usuario = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False, index=True)
    cpf_cnpj = Column(String, nullable=False, unique=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    senha = Column(String, nullable=False)
    saldo = Column(Numeric, default=True)

    transacoes = relationship("Transacao", back_populates="pagador")


class Transacao(Base):
    __tablename__ = "transacoes"

    id_transacao = Column(Integer, primary_key=True, index=True)
    valor_transacao = Column(Numeric, default=True, nullable=False)
    
    id_pagador = Column(Integer, ForeignKey("usuarios.id_usuario"))

    id_recebedor = Column(Integer, ForeignKey("lojistas.id_lojista"))

    pagador = relationship("Usuario", back_populates="transacoes")
    recebedor = relationship("Lojista", back_populates="transacoes")