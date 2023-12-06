from pydantic import BaseModel, ConfigDict, constr

class LojistaBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    nome: str
    cpf_cnpj: constr(min_length=14, max_length=18)
    email: constr(min_length=10, max_length=30)
    senha: str
    saldo: float


class LojistaRead(LojistaBase):
    id_lojista: int


class UsuarioBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    nome: str
    cpf_cnpj: constr(min_length=14, max_length=18)
    email: constr(min_length=10, max_length=30)
    senha: str
    saldo: float


class UsuarioRead(UsuarioBase):
    id_usuario: int


class TransacaoBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    valor_transacao: float
    id_pagador:  int
    id_recebedor:  int


class TransacaoCreate(TransacaoBase):
    id_transacao: int
