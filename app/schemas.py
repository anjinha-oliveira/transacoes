from pydantic import BaseModel

class LojistaBase(BaseModel):
    nome: str
    cpf_cnpj: str
    email: str
    senha: str
    saldo: float

    class Config:
        from_attributes = True

class LojistaRead(LojistaBase):
    id_lojista: int


class UsuarioBase(BaseModel):
    id_usuario: int
    nome: str
    cpf_cnpj: str
    email: str
    senha: str
    saldo: float

    class Config:
        from_attributes = True

class UsuarioCreate(UsuarioBase):
    pass

class TransacaoBase(BaseModel):
    id_transacao: int
    valor_transacao: float
    id_pagador:  int
    id_recebedor:  int

    class Config:
        from_attributes = True

class TransacaoCreate(TransacaoBase):
    pass