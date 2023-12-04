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
    db_usuario_email = crud.get_usuario_por_email(db, email=user.email)
    db_usuario_cpf_cnpj = crud.get_usuario_por_cpf_cnpj(db, cpf_cnpj=user.cpf_cnpj)
    if db_usuario_email:
        raise HTTPException(status_code=400, detail="Email de usuario já está registrado")
    elif db_usuario_cpf_cnpj:
        raise HTTPException(status_code=400, detail="CPF ou CNPJ de usuario já está registrado")
    return crud.criar_usuario(db=db, user=user)

