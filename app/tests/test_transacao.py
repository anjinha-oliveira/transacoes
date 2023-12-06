import pytest

from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.crud import criar_usuario, criar_lojista, criar_transacao

from app.database import Base
from app.main import app, get_db
from app.schemas import UsuarioBase, LojistaBase, TransacaoBase

SQLALCHEMY_DATABASE_URL = "sqlite://"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


@pytest.fixture(scope="session", autouse=True)
def test_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = test_db

client = TestClient(app)


def test_garante_criacao_de_transacao(test_db):
    user = UsuarioBase(
        nome="Vera Lúcia Oliveira",
        cpf_cnpj="000.009.112-59",
        email="angelalucia@gmail.com",
        senha="234",
        saldo=200,
    )
    usuario = criar_usuario(db=test_db, user=user)
    assert usuario.id_usuario

    user = LojistaBase(
        nome="Luan Fonseca de farias",
        cpf_cnpj="111.000.000-89",
        email="luanfosceca@gmail.com",
        senha="76589",
        saldo=4.0
    )
    lojista = criar_lojista(db=test_db, user=user)
    assert lojista.id_lojista

    transacao = TransacaoBase(
        valor_transacao=20,
        id_pagador=1,
        id_recebedor=1,
    )
    response = client.post(
        "/transacao/{cpf_cnpj}/",
        json={
            "valor_transacao": 20,
            "id_pagador": 1,
            "id_recebedor": 1
        }
    )
    assert response.status_code == 200
    assert response.json() == {
        "valor_transacao": 20,
        "id_pagador": 1,
        "id_recebedor": 1
    }