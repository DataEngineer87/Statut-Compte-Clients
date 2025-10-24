# Prédiction du Statut de Compte – MLOps de bout en bout
![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/API-FastAPI-009688?logo=fastapi&logoColor=white)
![Streamlit](https://img.shields.io/badge/Dashboard-Streamlit-FF4B4B?logo=streamlit&logoColor=white)
![MLflow](https://img.shields.io/badge/Tracking-MLflow-0194E2?logo=mlflow&logoColor=white)
![Docker](https://img.shields.io/badge/Container-Docker-2496ED?logo=docker&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/CI/CD-GitHub_Actions-2088FF?logo=githubactions&logoColor=white)
![SHAP](https://img.shields.io/badge/Explainability-SHAP-FE7A16?logo=plotly&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

<p align="center">
  
  <img src="assets/demo.gif" alt="Démonstration de l'application Streamlit" width="700"/>
  
</p>



---

## Démonstration interactive
[![Streamlit Cloud](https://img.shields.io/badge/🚀_App_Streamlit-Testez%20l'application%20en%20ligne-FF4B4B?logo=streamlit&logoColor=white)](https://predictionstatutcompte-kfxgmqeampjqfsoe6nbpjq.streamlit.app/)


**Testez l'application en ligne :**  
👉 [predictionstatutcompte.streamlit.app](https://predictionstatutcompte-kfxgmqeampjqfsoe6nbpjq.streamlit.app/)

---

---

## Objectif du projet

Ce projet démontre la mise en place d’un pipeline **MLOps complet** :  
de l’entraînement d’un modèle de machine learning, jusqu’à son **déploiement automatisé en production**, via **FastAPI**, **Docker**, et **GitHub Actions**.

Il inclut :
- **MLflow** pour le suivi des expérimentations,  
- **FastAPI** pour l’exposition du modèle en API REST,  
- **Docker** pour la conteneurisation,  
- **GitHub Actions** pour le CI/CD,  
- **Streamlit Cloud** pour le tableau de bord de prédiction,  
- **SHAP** pour l’explicabilité des décisions,  
- **Monitoring manuel** pour suivre les performances du modèle.

## Description rapide du pipeline

| Étape | Technologie | Description |
|:------|:-------------|:------------|
| **Entraînement** | MLflow | Suivi et versionnement du modèle |
| **Déploiement API** | FastAPI + Docker | Déploiement d’une API REST pour la prédiction |
| **CI/CD** | GitHub Actions | Build + tests + push automatique sur Docker Hub |
| **Interface utilisateur** | Streamlit Cloud | Interface de prédiction accessible en ligne |
| **Explicabilité & Monitoring** | SHAP + Notebook | Analyse de l’importance des variables et suivi des métriques |

---

## Résultat attendu

L’application prédit si un **compte client** est **actif ou inactif**,  
à partir de caractéristiques sociodémographiques et comportementales (revenu, âge, type d’abonnement...).

*Exemple d’appel à l’API :*
```bash
curl -X POST http://127.0.0.1:8000/predict \
-H "Content-Type: application/json" \
-d '{
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
}'


---

## Démonstration interactive

<p align="center">
  <img src="assets/demo.gif" alt="Démonstration de l'application Streamlit" width="700"/>
</p>   

---

**Testez l'application en ligne :**
👉 [Predictionstatutcompte.web.application](https://predictionstatutcompte-kfxgmqeampjqfsoe6nbpjq.streamlit.app/)
