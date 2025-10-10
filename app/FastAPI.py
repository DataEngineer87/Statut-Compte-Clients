#!/usr/bin/env python
# coding: utf-8

# In[4]:


from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Literal
import pandas as pd
import joblib
import os
from data_processing import encode_features

app = FastAPI(title="Account Status Prediction API")

# Chargement du modèle
MODEL_PATH = os.path.join("artifacts", "model.joblib")
model = joblib.load(MODEL_PATH)

# Schéma d'entrée
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

@app.get("/")
def root():
    return {"message": "API de prédiction du statut de compte"}

@app.post("/predict")
def predict(data: InputData):
    try:
        df_input = pd.DataFrame([data.dict()])
        df_input['account_status'] = 'Unknown'  # Dummy target pour encodage
        encoded = encode_features(df_input, target_col='account_status')
        encoded = encoded.drop(columns='account_status')
        # Alignement colonnes modèle
        encoded = encoded.reindex(columns=model.feature_names_in_, fill_value=0)
        pred = model.predict(encoded)[0]
        return {"prediction": pred}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# In[ ]:




