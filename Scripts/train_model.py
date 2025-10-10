#!/usr/bin/env python
# coding: utf-8

# # Modélisation

# In[1]:


import os
import json
import pandas as pd
import joblib
import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from mlflow.models.signature import infer_signature
from data_processing import encode_features

# Préparation dossiers
os.makedirs("artifacts", exist_ok=True)
os.makedirs("reports", exist_ok=True)

# Chargement des données
df_train = pd.read_csv("/home/sacko/Documents/PredictionStatutCompte/Donnees/df_train_cleaned.csv")
df_test = pd.read_csv("/home/sacko/Documents/PredictionStatutCompte/Donnees/df_test_cleaned.csv")

X_train = df_train.drop("account_status", axis=1)
y_train = df_train["account_status"]
X_test = df_test.drop("account_status", axis=1)
y_test = df_test["account_status"]

# Encodage
train_encoded = encode_features(X_train.assign(account_status=y_train))
test_encoded = encode_features(X_test.assign(account_status=y_test))

X_train_encoded = train_encoded.drop("account_status", axis=1)
y_train_encoded = train_encoded["account_status"]
X_test_encoded = test_encoded.drop("account_status", axis=1)
y_test_encoded = test_encoded["account_status"]

# Alignement colonnes
X_test_encoded = X_test_encoded.reindex(columns=X_train_encoded.columns, fill_value=0)

# Entraînement et MLflow
model = RandomForestClassifier(n_estimators=100, random_state=42)

mlflow.set_tracking_uri("file://" + os.path.abspath("/home/sacko/Documents/PredictionStatutCompte/Scripts/mlruns"))
mlflow.set_experiment("account_status_prediction")

with mlflow.start_run():
    model.fit(X_train_encoded, y_train_encoded)
    preds = model.predict(X_test_encoded)
    report = classification_report(y_test_encoded, preds, output_dict=True)
    acc = report['accuracy']

    # Sauvegarde rapport
    with open("reports/evaluation_report.json", "w") as f:
        json.dump(report, f, indent=4)
    mlflow.log_artifact("reports/evaluation_report.json")

    # Signature et modèle MLflow
    input_example = X_train_encoded.iloc[:1]
    signature = infer_signature(X_train_encoded, model.predict(X_train_encoded))

    mlflow.log_param("model_type", "RandomForest")
    mlflow.log_metric("accuracy", acc)
    mlflow.sklearn.log_model(
        sk_model=model,
        artifact_path="model",
        input_example=input_example,
        signature=signature,
        registered_model_name="account_status_rf"
    )

    # Sauvegarde modèle pour FastAPI
    joblib.dump(model, "artifacts/model.joblib")


# In[ ]:





# In[ ]:




