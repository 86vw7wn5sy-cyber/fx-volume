import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_healthcheck():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_pairs():
    response = client.get("/api/v1/market/pairs")
    assert response.status_code == 200
    data = response.json()
    assert "pairs" in data
    assert len(data["pairs"]) > 0


def test_symbol_data():
    response = client.get("/api/v1/market/EURUSD")
    assert response.status_code == 200
    data = response.json()
    assert data["symbol"] == "EURUSD"
    assert "price" in data
