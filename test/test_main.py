from fastapi.testclient import TestClient
from main import app

def test_get_companies_success():
    with TestClient(app) as client:
        response = client.get("/ticker/AAPL")
        assert response.status_code == 200
        assert response.json() == {
            "cik": 320193,
            "name": "Apple Inc.",
            "ticker": "AAPL",
            "exchange": "Nasdaq",
        }
        assert app.state.score["AAPL"] == 1


def test_get_companies_not_found():
    with TestClient(app) as client:
        response = client.get("/ticker/C11111")
        assert response.status_code == 404
        assert response.json() == {"detail": "Company not found"}


def test_get_activity():
    with TestClient(app) as client:
        client.get("/ticker/AAPL")
        client.get("/ticker/NVDA")
        response = client.get("/activity")
        assert response.status_code == 200
        assert response.json() == {"AAPL": 1, "NVDA": 1}

def test_get_activity_empty():
    with TestClient(app) as client:
        response = client.get("/activity")
        assert response.status_code == 200
        assert response.json() == {}

def test_get_activity_repeated():
    with TestClient(app) as client:
        client.get("/ticker/AAPL")
        client.get("/ticker/AAPL")
        response = client.get("/activity")
        assert response.status_code == 200
        assert response.json() == {"AAPL": 2}