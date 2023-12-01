from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_garante_lojista_nao_recebe_email_vazio():
    response = client.post("/lojista/")
    if "email" == None:
        assert response.status_code == 400
        assert response.json() == {"message": "Campo email obrigatório"}

def test_garante_que_nao_recebe_cpf_cnj_vazio():
    response = client.post("/lojista/")
    if "cpf_cnpj" == None:
        assert response.status_code == 400
        assert response.json() == {"message": "Campo CPF ou CNPJ obrigatório"}

def test_garante_usuario_nao_recebe_email_vazio():
    response = client.post("/usuario/")
    if "email" == None:
        assert response.status_code == 400
        assert response.json() == {"message": "Campo email obrigatório"}

def test_garante_que_usuario_nao_recebe_cpf_cnpj_vazio():
    response = client.post("/usuario/")
    if "cpf_cnpj" == None:
        assert response.status_code == 400
        assert response.json() == {"message": "Campo CPF ou CNPJ obrigatório"}