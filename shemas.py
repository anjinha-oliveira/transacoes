from pydantic import BaseModel

class LojistaBase(BaseModel):
    id_lojista: int
    nome: str
    cpf_cnpj: str
    email: str
    senha: str
    saldo: bool

class LojistaCreate(LojistaBase):
    pass

class UsuarioBase(BaseModel):
    id_usuario: int
    nome: str
    cpf_cnpj: str
    email: str
    senha: str
    saldo: bool

class UsuarioCreate(UsuarioBase):
    pass

class TransacaoBase(BaseModel):
    id_transacao: int
    valor_transacao: bool
    id_pagador:  int
    id_recebedor:  int

class TransacaoCreate(TransacaoBase):
    pass