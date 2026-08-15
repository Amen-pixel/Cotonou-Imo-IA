import fix
import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)


# ============================================================
# 1. CHARGEMENT DU DATASET
# ============================================================

df = pd.read_csv(
    "cotonou_real_estate_500_no_duplicates.csv"
)

print("=" * 60)
print("DATASET")
print("=" * 60)

print(f"Nombre de lignes : {len(df)}")
print(f"Nombre de colonnes : {len(df.columns)}")


# ============================================================
# 2. VARIABLES
# ============================================================

features = [
    "quartier",
    "type_bien",
    "superficie_m2",
    "chambres",
    "pieces",
    "salles_bain",
    "garages"
]

target = "prix_fcfa"


# ============================================================
# 3. CONVERSION DES VARIABLES NUMÉRIQUES
# ============================================================

numeric_features = [
    "superficie_m2",
    "chambres",
    "pieces",
    "salles_bain",
    "garages"
]

for column in numeric_features:

    df[column] = pd.to_numeric(
        df[column],
        errors="coerce"
    )


df[target] = pd.to_numeric(
    df[target],
    errors="coerce"
)


# ============================================================
# 4. SUPPRIMER LES LIGNES SANS PRIX
# ============================================================

df = df.dropna(
    subset=[target]
)


# ============================================================
# 5. CRÉATION DE X ET y
# ============================================================

X = df[features].copy()

y = df[target].copy()


# ============================================================
# 6. TRAITEMENT DES VALEURS MANQUANTES
# ============================================================

for column in numeric_features:

    X[column] = X[column].fillna(
        X[column].median()
    )


for column in ["quartier", "type_bien"]:

    X[column] = X[column].fillna(
        X[column].mode()[0]
    )


# ============================================================
# 7. ENCODAGE DES VARIABLES CATÉGORIELLES
# ============================================================

X = pd.get_dummies(
    X,
    columns=["quartier", "type_bien"],
    dtype=float
)

X = X.fillna(0)


# ============================================================
# 8. SÉPARATION TRAIN / TEST
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)


print("\n")
print(f"Données entraînement : {len(X_train)}")
print(f"Données test          : {len(X_test)}")


# ============================================================
# 9. CRÉATION DU MODÈLE
# ============================================================

model = RandomForestRegressor(
    n_estimators=300,
    random_state=42,
    n_jobs=-1
)


# ============================================================
# 10. ENTRAÎNEMENT
# ============================================================

print("\nEntraînement du modèle...")

model.fit(
    X_train,
    y_train
)

print("✅ Entraînement terminé")


# ============================================================
# 11. PRÉDICTIONS
# ============================================================

y_pred = model.predict(
    X_test
)


# ============================================================
# 12. ÉVALUATION
# ============================================================

mae = mean_absolute_error(
    y_test,
    y_pred
)

rmse = np.sqrt(
    mean_squared_error(
        y_test,
        y_pred
    )
)

r2 = r2_score(
    y_test,
    y_pred
)


print("\n" + "=" * 60)
print("RÉSULTATS")
print("=" * 60)

print(
    f"MAE  : {mae:,.0f} FCFA"
)

print(
    f"RMSE : {rmse:,.0f} FCFA"
)

print(
    f"R²   : {r2:.4f}"
)


# ============================================================
# 13. SAUVEGARDE DU MODÈLE
# ============================================================

model_data = {

    "model": model,

    "columns": X.columns.tolist(),

    "features": features,

    "quartiers": sorted(
        df["quartier"]
        .dropna()
        .unique()
        .tolist()
    ),

    "types_bien": sorted(
        df["type_bien"]
        .dropna()
        .unique()
        .tolist()
    )
}


joblib.dump(
    model_data,
    "model.pkl"
)


print("\n" + "=" * 60)
print("SAUVEGARDE")
print("=" * 60)

print("✅ model.pkl créé avec succès")
