from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
from main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "mensaje" in response.json()


@patch("main.ntplib.NTPClient")
def test_time(mock_ntp_client):
    mock_response = MagicMock()
    mock_response.tx_time = 1712170800

    mock_instance = mock_ntp_client.return_value
    mock_instance.request.return_value = mock_response

    response = client.get("/time")

    assert response.status_code == 200
    data = response.json()
    assert "time" in data
    assert "source" in data
    assert data["source"] == "SHOA NTP"