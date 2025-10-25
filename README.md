## Prédiction du Statut de Compte – MLOps de bout en bout
![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/API-FastAPI-009688?logo=fastapi&logoColor=white)
![Streamlit](https://img.shields.io/badge/Dashboard-Streamlit-FF4B4B?logo=streamlit&logoColor=white)
![MLflow](https://img.shields.io/badge/Tracking-MLflow-0194E2?logo=mlflow&logoColor=white)
![Docker](https://img.shields.io/badge/Container-Docker-2496ED?logo=docker&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/CI/CD-GitHub_Actions-2088FF?logo=githubactions&logoColor=white)
![SHAP](https://img.shields.io/badge/Explainability-SHAP-FE7A16?logo=plotly&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

---

### Démonstration interactive
[![Streamlit Cloud](https://img.shields.io/badge/App_Streamlit-Cliquez%20ici%20pour%20tester%20l'application%20en%20ligne-FF4B4B?logo=streamlit&logoColor=white)](https://predictionstatutcompte-kfxgmqeampjqfsoe6nbpjq.streamlit.app/)

---


### Objectif du projet

Ce projet illustre la mise en œuvre **complète d’un pipeline MLOps** permettant de :
- **entraîner un modèle de machine learning** (Random Forest),
- **déployer une API de prédiction** via FastAPI et Docker,
- **automatiser les tests, le build et le déploiement** avec GitHub Actions,
- **offrir une interface utilisateur intuitive** sur Streamlit Cloud.
  
Le tout avec un suivi expérimental via **MLflow**, une explicabilité avec **SHAP**, et un monitoring via notebook Jupyter.

Cette démarche suit une logique **modulaire et scalable**, typique d’un pipeline MLOps de production.

Elle inclut :
- **MLflow** pour le suivi des expérimentations,  
- **FastAPI** pour l’exposition du modèle en API REST,  
- **Docker** pour la conteneurisation,  
- **GitHub Actions** pour le CI/CD,  
- **Streamlit Cloud** pour le tableau de bord de prédiction,  
- **SHAP** pour l’explicabilité des décisions,  
- **Monitoring manuel** pour suivre les performances du modèle.

### Description rapide du pipeline

| Étape | Technologie | Description |
|:------|:-------------|:------------|
| **Entraînement** | MLflow | Suivi et versionnement du modèle |
| **Déploiement API** | FastAPI + Docker | Déploiement d’une API REST pour la prédiction |
| **CI/CD** | GitHub Actions | Build + tests + push automatique sur Docker Hub |
| **Interface utilisateur** | Streamlit Cloud | Interface de prédiction accessible en ligne |
| **Explicabilité & Monitoring** | SHAP + Notebook | Analyse de l’importance des variables et suivi des métriques |

### Structure du dépôt

PredictionStatutCompte/
│── app/
│   ├── FastAPI.py              # API FastAPI pour servir le modèle
│
│── Scripts/
│   ├── train_model.py           # Entraînement et sauvegarde du modèle
│   ├── web_app.py                   # Application Streamlit
│
│── tests/
│   ├── test_api.py              # Tests unitaires de l'API FastAPI
│
│── models/                      # Modèles sauvegardés
│── Donnees/                        # Données d'entraînement et de test
│── monitoring.ipynb             # Suivi des performances du modèle
│── shap.ipynb                   # Explicabilité des variables avec SHAP
│── requirements.txt             # Dépendances Python
│── Dockerfile                   # Image Docker de l’API
│── .github/workflows/mlops.yml  # Workflow CI/CD GitHub Actions
│── README.md                    # Documentation du projet

### Résultat attendu

L’application prédit si un **compte client** est **actif ou inactif**,  
à partir de caractéristiques sociodémographiques et comportementales (revenu, âge, type d’abonnement, etc).

**Exemple d'appel à l'API :**

```
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
}



```
<a href="images/AppStreamlit.pdf">
  <img src="images/imageDrift.png" alt="Aperçu du PDF" width="800"/>
</a>

```
