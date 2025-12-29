## Prédiction du Statut de Compte – MLOps de bout en bout
![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/API-FastAPI-009688?logo=fastapi&logoColor=white)
![Streamlit](https://img.shields.io/badge/Dashboard-Streamlit-FF4B4B?logo=streamlit&logoColor=white)
![MLflow](https://img.shields.io/badge/Tracking-MLflow-0194E2?logo=mlflow&logoColor=white)
![Docker](https://img.shields.io/badge/Container-Docker-2496ED?logo=docker&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/CI/CD-GitHub_Actions-2088FF?logo=githubactions&logoColor=white)
![SHAP](https://img.shields.io/badge/Explainability-SHAP-FE7A16?logo=plotly&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
### Vue d'ensemble
Ce projet démontre ma capacité à concevoir, industrialiser et déployer un modèle de Machine Learning de bout en bout, en appliquant les bonnes pratiques MLOps utilisées en entreprise.
De la préparation des données à la mise en production du modèle via FastAPI, en passant par une chaîne CI/CD complète avec Docker & GitHub Actions, le projet inclut également :
- Explicabilité du modèle (SHAP)
- Monitoring pour suivre la dérive et les performances
- Application Streamlit Cloud pour une interface utilisateur accessible
- Versioning et tracking des expériences via MLflow
**Objectif :** montrer comment un Data Scientist peut livrer un modèle fiable, reproductible, traçable et explicable, prêt à être utilisé en production.


### Démonstration interactive
👉 [Tester l'application en ligne (Streamlit cloud)](https://statut-compte-clients-payyhi4bgvt38ggybofviy.streamlit.app/)
**Image Docker, disponible ici :**
[![Docker Image](https://img.shields.io/badge/Docker%20Hub-alseny87%2Fstatusclients--api-blue?logo=docker)](https://hub.docker.com/r/alseny87/statusclients-api)

### Objectif du projet
Cette solution illustre une mise en œuvre complète d’un pipeline MLOps, permettant de :
- Entraîner un modèle de machine learning (Random Forest, MLflow tracking)
- Déployer une API de prédiction performante via FastAPI
- Conteneuriser l’API pour une reproductibilité totale (Docker)
- Automatiser les tests, le build et le déploiement avec GitHub Actions
- Offrir une interface utilisateur claire via Streamlit Cloud
- Analyser l’importance des variables avec SHAP (explicabilité)
- Suivre les performances et détecter la dérive des données via un notebook de monitoring
Cette approche suit une logique **modulaire, scalable et industrielle**, typique d’un pipeline MLOps utilisé en production.

Elle inclut :
**MLflow — suivi des expérimentations**
- Versioning modèle
- Tracking des hyperparamètres
- Comparaison des runs

**FastAPI — exposer le modèle en API REST**
- Endpoint /predict
- Validation des données via Pydantic
- Performance, scalabilité, documentation automatique Swagger

**Docker — conteneurisation**
- Image légère et reproductible
- Déploiement portable sur tout environnement

**GitHub Actions — CI/CD**
- Pipeline complet automatisé incluant :
- Tests unitaires (pytest)
- Build Docker
- Push vers Docker Hub
- Test réel de l’API via curl

**Streamlit Cloud — interface utilisateur**
- Formulaire client
- Appel API en direct
- Affichage instantané de la prédiction

**SHAP — explicabilité**
- Importance des features
- Analyse locale et globale

**Monitoring — Jupyter Notebook**
- Suivi régulier de la qualité du modèle
- Détection de la dérive statistique
- KPIs ML (F1-score, recall, précision…)
  
``` 
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

``` 

### Déploiement & Exécution

#### Exécution locale
```
git clone https://github.com/DataEngineer87/Statut-Compte-Clients.git  
cd Statut-Compte-Clients  # Entre dans le dossier du projet
python -m venv venv  
source venv/bin/activate  
pip install -r requirements.txt  

# Lancement du serveur FastAPI en mode développement
uvicorn app.fast_api:app --reload --host 127.0.0.1 --port 8000  
```


### Pour tester l’API localement
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
}'
```
### Résultat attendu

L’application prédit si un **compte client** est **actif ou inactif**,  
à partir de caractéristiques sociodémographiques et comportementales (revenu, âge, type d’abonnement, etc).

Dans cet exemple, on a : 
```
{"prediction": "Active"}
```

### Déploiement avec Docker

```
docker build -t alseny87/statusclients-api:latest .
docker run -d -p 8000:8000 --name fastapi_app alseny87/statusclients-api:latest

# Vérification si l’API répond correctement sur le port exposé (8000)
curl http://127.0.0.1:8000/predict

```

### CI/CD — GitHub Actions

Workflow automatisé dans .github/workflows/mlops.yml

```
- name: Vérification du /predict
  run: |
    docker run -d -p 8000:8000 --name fastapi_test ${{ secrets.DOCKER_USERNAME }}/statusclients-api:latest
    sleep 5
    curl -X POST http://127.0.0.1:8000/predict -H "Content-Type: application/json" -d '{"gender": "Male", ...}'
```
**Le workflow ci_cd.yml automatise :**
-Checkout du code
-Installation de Python 3.13
-Installation des dépendances + tests
-Connexion Docker Hub (via secrets)
-Build & Push de l’image Docker
-Vérification automatique du endpoint /predict
**Chaque push sur main relance automatiquement le pipeline CI/CD complet.**

### Application Streamlit (Cloud)

Interface interactive pour tester le modèle :
[![Ouvrir sur Streamlit Cloud](https://img.shields.io/badge/Open%20App-Streamlit%20Cloud-FF4B4B?logo=streamlit&logoColor=white)](https://statutcompteclients-3qzfz7vqnheonajkygypwp.streamlit.app/)

### Monitoring & Explicabilité
Les notebooks intégrés permettent de :
- suivre les performances du modèle dans le temps,
- Détecter les dérives de données avec MLflow et un tableau de bord Streamlit.
- Analyser l’évolution du modèle
- expliquer les variables clés grâce à SHAP.

Ils ne sont pas inclus dans le workflow CI/CD (par souci d’efficacité), mais servent à des ***analyses post-déploiement.***
#### Explicabilité du modèle avec SHAP
Analyse des variables les plus influentes sur la prédiction du statut client (actif/inactif).

![SHAP Feature Importance](https://raw.githubusercontent.com/DataEngineer87/Prediction_statut_compte/main/reports/shap_summary.png)

#### Monitoring du modèle

#### Tableau de bord 
<a href="images/AppStreamlit.pdf">
  <img src="images/imageDrift.png" alt="Aperçu du PDF" width="800"/>
</a>

### Technique d'empilement

```
| Catégorie                 | Outils & Technologies |
| ------------------------- | --------------------- |
| **Langage principal**     | Python 3.10+          |
| **API Backend**           | FastAPI               |
| **Conteneurisation**      | Docker                |
| **CI/CD Automation**      | GitHub Actions        |
| **Interface Utilisateur** | Streamlit Cloud       |
| **Suivi Expériences**     | MLflow                |
| **Explicabilité**         | SHAP                  |
| **Tests Unitaires**       | pytest                |

```

### Points Forts du Projet
- Pipeline MLOps complet — du notebook au déploiement
- API conteneurisée et testée automatiquement
- Intégration continue (CI) et livraison continue (CD)
- Visualisation interactive avec Streamlit
- Explicabilité et transparence avec SHAP
- Architecture cloud-ready (Docker + GitHub Actions)
- Code structuré et maintenable pour production

# Auteur

**Alseny**

**Data Scientist confirmé orienté MLOps & GenAI**



