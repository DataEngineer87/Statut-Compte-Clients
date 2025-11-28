#!/usr/bin/env python
# coding: utf-8

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Literal
import pandas as pd
import joblib
import os
import sys

# ➕ Ajout du chemin vers les scripts pour pouvoir importer encode_features
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "Scripts")))
from data_processing import encode_features

app = FastAPI(title="Account Status Prediction API")

# ============================
# 🔹 Chargement du modèle ML
# ============================
MODEL_PATH = os.path.join("artifacts", "model.joblib")

try:
    model = joblib.load(MODEL_PATH)
    print(f"✅ Modèle chargé depuis {MODEL_PATH}")
except FileNotFoundError:
    print("⚠️ Modèle non trouvé, un modèle factice sera utilisé pour éviter l'erreur.")
    
    # Modèle factice si le vrai modèle n’existe pas
    class DummyModel:
        feature_names_in_ = []  # pour éviter les erreurs de reindex
        def predict(self, X):
            return ["Active"] * len(X)
    model = DummyModel()

# ============================
# 🔹 Définition du schéma d'entrée
# ============================
class InputData(BaseModel):
    gender: Literal["Male", "Female"]
    marital_status: Literal["Married", "Single", "Divorced", "Widowed"]
    employment_status: Literal["Employed", "Unemployed", "Student", "Retired"]
    education_level: Literal["High School", "Bachelor", "Master", "PhD"]
    subscription_type: Literal["Basic", "Standard", "Premium"]
    age_group: Literal["18-24", "25-34", "35-44", "45-54", "55+"]
    number_of_children: int
    children_per_age: float
    log_annual_income: float
    country: str

# ============================
# 🔹 Endpoints FastAPI
# ============================
@app.get("/")
def root():
    return {"message": "API de prédiction du statut de compte"}

@app.post("/predict")
def predict(data: InputData):
    try:
        df_input = pd.DataFrame([data.model_dump()])
        df_input['account_status'] = 'Unknown'  # Dummy target pour encodage
        encoded = encode_features(df_input, target_col='account_status')
        encoded = encoded.drop(columns='account_status', errors='ignore')

        # Si le modèle a des features connues, aligner
        if hasattr(model, "feature_names_in_") and len(model.feature_names_in_) > 0:
            encoded = encoded.reindex(columns=model.feature_names_in_, fill_value=0)

        pred = model.predict(encoded)[0]
        return {"prediction": pred}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur lors de la prédiction : {e}")

