from fastapi import Depends, FastAPI, HTTPException

from . import crud, models, schemas
from .database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()

db_fake = {
    "nome": "Angela Lucia",
    "cpf_cnpj": "000.123.000-99",
    "email": "angelalucia@gmail.com",
    "senha": "lucia",
    "saldo": "2000"
}

@app.post("/lojista/", response_model=schemas.LojistaBase)
def criar_lojista(user: schemas.LojistaBase, db: SessionLocal = Depends(get_db)):    
    return crud.criar_lojista(db=db, user=user)

@app.post("/usuario/", response_model=schemas.UsuarioBase)
def criar_usuario(user: schemas.UsuarioBase, db: SessionLocal = Depends(get_db)):
    return crud.criar_usuario(db=db, user=user)

@app.post("/transacao/{cpf_cnpj}/", response_model=schemas.TransacaoBase)
def criar_trasacao(transacao: schemas.TransacaoBase, db: SessionLocal = Depends(get_db)):
    return crud.criar_transacao(db=db, transacao=transacao)
