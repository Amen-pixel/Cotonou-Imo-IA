"""Entraîne le modèle de prix immobilier et crée model.pkl + options.json."""
import json

import joblib
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.impute import SimpleImputer
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

CSV = "cotonou_real_estate_500_no_duplicates.csv"
TEXTE = ["quartier", "type_bien"]
NOMBRES = ["superficie_m2", "chambres", "pieces", "salles_bain", "garages"]
CIBLE = "prix_fcfa"

# 1. Données
df = pd.read_csv(CSV).dropna(subset=[CIBLE])
df["garages"] = df["garages"].fillna(0)  # case vide = pas de garage
X, y = df[TEXTE + NOMBRES], df[CIBLE]

# 2. Modèle = un "pipeline" : préparation des données + Random Forest
def creer_modele():
    preparation = ColumnTransformer([
        ("texte", OneHotEncoder(handle_unknown="ignore"), TEXTE),
        ("nombres", SimpleImputer(strategy="median"), NOMBRES),
    ])
    foret = RandomForestRegressor(n_estimators=300, random_state=42, n_jobs=-1)
    return Pipeline([("preparation", preparation), ("foret", foret)])

# 3. Test honnête : on cache 20 % des biens, puis on mesure l'erreur dessus
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42)
test = creer_modele().fit(X_tr, y_tr)
pred = test.predict(X_te)
mae = mean_absolute_error(y_te, pred)
r2 = r2_score(y_te, pred)
print(f"Erreur moyenne : {mae:,.0f} FCFA | R2 : {r2:.3f}")

# 4. Modèle final : réentraîné sur tous les biens
modele = creer_modele().fit(X, y)

# 5. Sauvegarde
quartiers = sorted(df["quartier"].unique().tolist())
types_bien = sorted(df["type_bien"].unique().tolist())

joblib.dump(
    {"model": modele, "quartiers": quartiers, "types_bien": types_bien},
    "model.pkl",
    compress=3,
)

# Listes pour les menus de l'interface (app.py)
with open("options.json", "w", encoding="utf-8") as f:
    json.dump({
        "quartiers": quartiers,
        "types_bien": types_bien,
        "superficie_min": float(df["superficie_m2"].min()),
        "superficie_max": float(df["superficie_m2"].max()),
        "mae_fcfa": round(mae),
        "r2": round(r2, 3),
    }, f, ensure_ascii=False, indent=2)

print("model.pkl et options.json créés")
