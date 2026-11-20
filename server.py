"""API FastAPI : reçoit les caractéristiques d'un bien, renvoie le prix estimé."""
import os
from pathlib import Path

import joblib
import pandas as pd
import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

# 1. Chargement du modèle (créé par projet.py)
data = joblib.load(Path(__file__).parent / "model.pkl")
model = data["model"]

# 2. Application
app = FastAPI(
    title="Cotonou Real Estate API",
    description="API de prédiction des prix immobiliers à Cotonou",
    version="2.0.0",
)


# 3. Données attendues
class House(BaseModel):
    quartier: str
    type_bien: str
    superficie_m2: float = Field(gt=0)
    chambres: int = Field(ge=0)
    pieces: int = Field(ge=0)
    salles_bain: int = Field(ge=0)
    garages: int = Field(ge=0)


# 4. Route d'accueil (sert aussi de test "le serveur est en ligne")
@app.get("/")
def home():
    return {"message": "Cotonou Real Estate API", "status": "online"}


# 5. Route de prédiction
@app.post("/predict")
def predict(house: House):
    if house.quartier not in data["quartiers"]:
        raise HTTPException(422, f"Quartier inconnu : {house.quartier}")
    if house.type_bien not in data["types_bien"]:
        raise HTTPException(422, f"Type de bien inconnu : {house.type_bien}")

    maison = pd.DataFrame([house.model_dump()])
    prix = model.predict(maison)[0]
    return {"prix_estime_fcfa": round(float(prix))}


# 6. Lancement en local (sur Render, c'est la commande uvicorn qui démarre)
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=int(os.getenv("PORT", 8005)))
