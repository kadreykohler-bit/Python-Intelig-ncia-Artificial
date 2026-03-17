from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# Função auxiliar para pegar o token nos testes
def get_auth_token():
    # Primeiro cadastramos o usuário de teste
    client.post("/usuarios/", json={"username": "testuser", "password": "123"})
    # Fazemos o login para obter o token
    response = client.post("/token", data={"username": "testuser", "password": "123"})
    return response.json()["access_token"]

def test_read_financeiro():
    """Testa se a página inicial está abrindo (Front-end)"""
    response = client.get("/financeiro")
    assert response.status_code == 200
    assert "Financeiro Pro" in response.text

def test_criar_receita():
    """Testa o cadastro de uma nova receita via API com Token"""
    token = get_auth_token()
    headers = {"Authorization": f"Bearer {token}"}
    
    payload = {
        "valor": 5000.0,
        "descricao": "Salário Mensal",
        "tipo": "receita"
    }
    response = client.post("/transacoes/", json=payload, headers=headers)
    assert response.status_code == 200
    assert response.json()["descricao"] == "Salário Mensal"

def test_criar_despesa_com_saldo():
    """Testa o cadastro de uma despesa quando há saldo"""
    token = get_auth_token()
    headers = {"Authorization": f"Bearer {token}"}
    
    # Adiciona saldo primeiro para não dar erro 400
    client.post("/transacoes/", json={"valor": 100.0, "descricao": "Saldo", "tipo": "receita"}, headers=headers)
    
    payload = {
        "valor": 50.0,
        "descricao": "Aluguel",
        "tipo": "despesa"
    }
    response = client.post("/transacoes/", json=payload, headers=headers)
    assert response.status_code == 200
    assert response.json()["tipo"] == "despesa"

def test_extrato_protegido():
    """Verifica se o extrato exige autenticação"""
    response = client.get("/extrato/")
    assert response.status_code == 401  # Deve falhar sem token