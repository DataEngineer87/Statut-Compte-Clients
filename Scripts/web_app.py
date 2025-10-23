## Web application avec streamlit
import streamlit as st
import requests
import threading
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

# --- Définition de l'API FastAPI intégrée ---
app = FastAPI(title="API Prédiction Abonnement Client")

class ClientData(BaseModel):
    gender: str
    marital_status: str
    employment_status: str
    education_level: str
    subscription_type: str
    age_group: str
    number_of_children: int
    children_per_age: float
    log_annual_income: float
    country: str

@app.post("/predict")
def predict(data: ClientData):
    # Exemple simplifié de logique de prédiction
    if data.subscription_type == "Premium" or data.log_annual_income > 10:
        return {"prediction": "Active"}
    else:
        return {"prediction": "Inactive"}

# --- Lancer FastAPI en arrière-plan ---
def run_api():
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="warning")

threading.Thread(target=run_api, daemon=True).start()

# --- Configuration de la page Streamlit ---
st.set_page_config(
    page_title="Prédiction Abonnement Client",
    page_icon="📊",
    layout="centered"
)

st.title("Prédiction d'abonnement client 📈")
st.markdown(
    "Remplis les informations ci-dessous pour obtenir la prédiction de l'abonnement client."
)

# --- Formulaire ---
with st.form("client_form"):
    st.subheader("Informations personnelles")
    gender = st.selectbox("Genre", ["Male", "Female"])
    age_group = st.selectbox("Tranche d'âge", ["18-24", "25-34", "35-44", "45-54", "55-64", "65+"])
    marital_status = st.selectbox("État civil", ["Single", "Married", "Divorced", "Widowed"])
    
    st.subheader("Profession & Éducation")
    employment_status = st.selectbox("Statut professionnel", ["Employed", "Unemployed", "Self-employed", "Retired"])
    education_level = st.selectbox("Niveau d'éducation", ["High School", "Bachelor", "Master", "PhD"])
    log_annual_income = st.number_input("Log du revenu annuel", value=10.0, step=0.1, format="%.2f")
    
    st.subheader("Famille & Abonnement")
    number_of_children = st.number_input("Nombre d'enfants", min_value=0, max_value=10, step=1)
    children_per_age = st.number_input("Moyenne d'enfants par âge", min_value=0.0, step=0.1, format="%.1f")
    subscription_type = st.selectbox("Type d'abonnement", ["Basic", "Standard", "Premium"])
    country = st.text_input("Pays", value="France")
    
    submitted = st.form_submit_button("📤 Obtenir la prédiction")

# --- Validation et appel API local ---
if submitted:
    if log_annual_income <= 0:
        st.error("Le revenu annuel doit être positif.")
    else:
        payload = {
            "gender": gender,
            "marital_status": marital_status,
            "employment_status": employment_status,
            "education_level": education_level,
            "subscription_type": subscription_type,
            "age_group": age_group,
            "number_of_children": number_of_children,
            "children_per_age": children_per_age,
            "log_annual_income": log_annual_income,
            "country": country
        }

        try:
            # Appel vers l'API locale FastAPI
            response = requests.post("http://127.0.0.1:8000/predict", json=payload)
            response.raise_for_status()
            prediction = response.json().get("prediction", "Erreur : pas de réponse")
            
            st.markdown("### Résultat de la prédiction")
            st.success(f"🎯 Prédiction : **{prediction}**")
        except requests.exceptions.RequestException as e:
            st.error(f"❌ Erreur lors de la requête API : {e}")
