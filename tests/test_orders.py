from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_create_and_list_orders():
    # Ensure starting state is empty
    resp = client.get("/orders")
    assert resp.status_code == 200
    assert resp.json() == []

    new_order = {"item": "Widget", "quantity": 3}
    create_resp = client.post("/orders", json=new_order)
    assert create_resp.status_code == 201
    created = create_resp.json()
    assert created["item"] == new_order["item"]
    assert created["quantity"] == new_order["quantity"]
    assert "id" in created

    list_resp = client.get("/orders")
    assert list_resp.status_code == 200
    data = list_resp.json()
    assert len(data) == 1
    assert data[0] == created
