from fastapi.testclient import TestClient
from unittest.mock import patch
from app.api import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

@patch("app.api.ArxivScraper.fetch")
@patch("app.api.BronzeRepository.save")
def test_ingest_endpoint_success(mock_save, mock_fetch):
    mock_fetch.return_value = [{"title": "Test Paper"}]
    mock_save.return_value = None

    response = client.post("/ingest")

    assert response.status_code == 201
    assert response.json()["status"] == "success"
    assert response.json()["records_count"] == 1

@patch("app.api.ArxivScraper.fetch")
def test_ingest_endpoint_error_handling(mock_fetch):
    mock_fetch.side_effect = Exception("Connection Timeout")
    response = client.post("/ingest")
    assert response.status_code == 500