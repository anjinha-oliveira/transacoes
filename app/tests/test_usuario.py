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


def test_garante_que_criacao_de_usuario():
    response = client.post(
        "/usuario/",
        json={
            "nome": "Fernando teofilo",
            "cpf_cnpj": "000.099.000-99",
            "email": "fernandoteofilo@gmail.com",
            "senha": "fernando",
            "saldo": 2000.0

        }
    )
    assert response.status_code == 200
    assert response.json() == {
        "nome": "Fernando teofilo",
        "cpf_cnpj": "000.099.000-99",
        "email": "fernandoteofilo@gmail.com",
        "senha": "fernando",
        "saldo": 2000.0
    }