import sys
import os
import pytest
from fastapi.testclient import TestClient

# ✅ Ajouter le chemin parent pour pouvoir importer app/
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.FastAPI import app  # Import de ton application FastAPI

client = TestClient(app)

def test_root_endpoint():
    """Vérifie que la racine de l'API répond bien"""
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()
    assert "API de prédiction" in response.json()["message"]

def test_predict_endpoint():
    """Teste l'endpoint /predict avec des données valides"""
    payload = {
        "gender": "Male",
        "marital_status": "Single",
        "employment_status": "Employed",
        "education_level": "Bachelor",
        "subscription_type": "Premium",
        "age_group": "35-44",
        "number_of_children": 2,
        "children_per_age": 0.5,
        "log_annual_income": 10.5,
        "country": "France"
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "prediction" in data
    assert data["prediction"] in ["Active", "Inactive", "Closed", "Unknown"]

