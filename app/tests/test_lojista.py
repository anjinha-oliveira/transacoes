from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.database import Base
from app.main import app, get_db

SQLALCHEMY_DATABASE_URL = "sqlite://"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db


client = TestClient(app)


def test_garante_criacao_de_lojista():
    response = client.post(
        "/lojista/",
        json={
            "nome": "Angela Lucia",
            "cpf_cnpj": "000.123.000-99",
            "email": "angelalucia@gmail.com",
            "senha": "lucia",
            "saldo": 2000,
        },
    )
    assert response.status_code == 200
    assert response.json() == {
        "nome": "Angela Lucia",
        "cpf_cnpj": "000.123.000-99",
        "email": "angelalucia@gmail.com",
        "senha": "lucia",
        "saldo": 2000.0,
    }


def test_garante_que_nao_recebe_cpf_cnpj_vazio():
    response = client.post(
        "/lojista/",
        json={
            "nome": "Fernando teofilo",
            "cpf_cnpj": "",
            "email": "fernandoteofilo@gmail.com",
            "senha": "fernando",
            "saldo": "2000",
        },
    )
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "type": "string_too_short",
                "loc": ["body", "cpf_cnpj"],
                "msg": "String should have at least 14 characters",
                "input": "",
                "ctx": {"min_length": 14},
                "url": "https://errors.pydantic.dev/2.5/v/string_too_short",
            }
        ]
    }


def test_garante_que_nao_recebe_email_vazio():
    response = client.post(
        "/lojista/",
        json={
            "nome": "Fernando teofilo",
            "cpf_cnpj": "000.000.999-00",
            "email": "",
            "senha": "fernando",
            "saldo": "2000",
        },
    )
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "type": "string_too_short",
                "loc": ["body", "email"],
                "msg": "String should have at least 10 characters",
                "input": "",
                "ctx": {"min_length": 10},
                "url": "https://errors.pydantic.dev/2.5/v/string_too_short",
            }
        ]
    }
