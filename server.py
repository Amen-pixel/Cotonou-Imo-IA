import fix
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib
import uvicorn


# ============================================================
# 1. CHARGEMENT DU MODÈLE
# ============================================================

data = joblib.load("model.pkl")

model = data["model"]
model_columns = data["columns"]


# ============================================================
# 2. CRÉATION DE L'APPLICATION FASTAPI
# ============================================================

app = FastAPI(
    title="Cotonou Real Estate API",
    description="API de prédiction des prix immobiliers à Cotonou",
    version="1.0.0"
)


# ============================================================
# 3. STRUCTURE DES DONNÉES REÇUES
# ============================================================

class House(BaseModel):

    quartier: str
    type_bien: str
    superficie_m2: float
    chambres: int
    pieces: int
    salles_bain: int
    garages: int


# ============================================================
# 4. ROUTE PRINCIPALE
# ============================================================

@app.get("/")
def home():

    return {
        "message": "Cotonou Real Estate API",
        "status": "online"
    }


# ============================================================
# 5. ROUTE DE PRÉDICTION
# ============================================================

@app.post("/predict")
def predict(house: House):

    # --------------------------------------------------------
    # Création du DataFrame
    # --------------------------------------------------------

    nouvelle_maison = pd.DataFrame([{

        "quartier": house.quartier,

        "type_bien": house.type_bien,

        "superficie_m2": house.superficie_m2,

        "chambres": house.chambres,

        "pieces": house.pieces,

        "salles_bain": house.salles_bain,

        "garages": house.garages

    }])


    # --------------------------------------------------------
    # Encodage des variables catégorielles
    # --------------------------------------------------------

    nouvelle_maison = pd.get_dummies(

        nouvelle_maison,

        columns=[
            "quartier",
            "type_bien"
        ],

        dtype=float

    )


    # --------------------------------------------------------
    # Reproduire exactement les colonnes
    # utilisées pendant l'entraînement
    # --------------------------------------------------------

    nouvelle_maison = nouvelle_maison.reindex(

        columns=model_columns,

        fill_value=0

    )


    # --------------------------------------------------------
    # Prédiction
    # --------------------------------------------------------

    prix = model.predict(

        nouvelle_maison

    )[0]


    # --------------------------------------------------------
    # Retourner le résultat
    # --------------------------------------------------------

    return {

        "prix_estime_fcfa": round(
            float(prix)
        )

    }


# ============================================================
# 6. LANCEMENT DU SERVEUR
# ============================================================

if __name__ == "__main__":

    uvicorn.run(

        app,

        host="127.0.0.1",

        port=8005

    )
