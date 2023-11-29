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


@app.post("/lojista/", response_model=schemas.LojistaBase)
def criar_lojista(user: schemas.LojistaBase, db: SessionLocal = Depends(get_db)):
    db_lojista_email = crud.get_usuario_por_email(db, email=user.email)
    db_lojista_cpf_cnpj = crud.get_usuario_por_cpf_cnpj(db, cpf_cnpj=user.cpf_cnpj)
    if db_lojista_email:
        raise HTTPException(status_code=400, detail="Email já está registrado")
    elif db_lojista_cpf_cnpj:
        raise HTTPException(status_code=400, detail="CPF ou CNPJ já está registrado")
    return crud.criar_lojista(db=db, user=user)
