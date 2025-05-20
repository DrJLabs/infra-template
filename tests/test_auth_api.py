from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)

def test_login_returns_token():
    response = client.post("/auth/login")
    assert response.status_code == 200
    body = response.json()
    token = body.get("token")
    assert isinstance(token, str) and token
