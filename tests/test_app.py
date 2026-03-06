# tests/test_app.py
# Tests FastAPI structurés avec le pattern AAA (Arrange-Act-Assert)

import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_root_endpoint():
    # Arrange
    # (Préparer le contexte si besoin)

    # Act
    response = client.get("/")

    # Assert
    assert response.status_code == 200
    # Adapter l'assertion suivante selon la réponse attendue
    # assert response.json() == {"message": "Hello World"}
