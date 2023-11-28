from pydantic import BaseModel

class LojistaBase(BaseModel):
    id_lojista: int
    nome: str
    cpf_cnpj: str
    email: str
    senha: str
    saldo: float

    class Config:
        orm_mode = True

class LojistaCreate(LojistaBase):
    pass

class UsuarioBase(BaseModel):
    id_usuario: int
    nome: str
    cpf_cnpj: str
    email: str
    senha: str
    saldo: float

    class Config:
        orm_mode = True

class UsuarioCreate(UsuarioBase):
    pass

class TransacaoBase(BaseModel):
    id_transacao: int
    valor_transacao: float
    id_pagador:  int
    id_recebedor:  int

    class Config:
        orm_mode = True

class TransacaoCreate(TransacaoBase):
    pass