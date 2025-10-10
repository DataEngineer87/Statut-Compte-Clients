# Étape 1 : image de base
FROM python:3.10-slim

# Étape 2 : répertoire de travail
WORKDIR /app

# Étape 3 : copier les fichiers nécessaires
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Étape 4 : copier le code du projet
COPY . .

# Étape 5 : exposer le port de l'API
EXPOSE 8000

# Étape 6 : commande de démarrage (FastAPI avec Uvicorn)
CMD ["uvicorn", "app.api:app", "--host", "0.0.0.0", "--port", "8000"]

