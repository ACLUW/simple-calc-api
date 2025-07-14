# ACL - Unit test for Simple Calculator API

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_addition():
    response = client.post("/calculate", json={"num1": 10, "num2": 5, "operation": "add"})
    assert response.status_code == 200
    assert response.json() == {"result": 15}
