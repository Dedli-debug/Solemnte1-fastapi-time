from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "mensaje" in response.json()


def test_time():
    response = client.get("/time")
    assert response.status_code == 200
    data = response.json()
    assert "time" in data
    assert "source" in data
    assert data["source"] == "SHOA NTP"