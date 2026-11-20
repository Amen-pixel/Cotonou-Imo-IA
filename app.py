"""Interface Streamlit : formulaire -> appel de l'API -> prix estimé."""
import json
import os
from pathlib import Path

import pandas as pd
import requests
import streamlit as st

# ============================================================
# CONFIGURATION
# ============================================================

st.set_page_config(page_title="Cotonou Immo AI", page_icon="🏠", layout="centered")

# Adresse de l'API : variable API_URL sur Render, sinon l'API locale
API_URL = (
    os.getenv("API_URL", "http://127.0.0.1:8005").rstrip("/").removesuffix("/predict")
    + "/predict"
)

# Listes des quartiers / types de biens (créées par projet.py)
OPTIONS = json.loads((Path(__file__).parent / "options.json").read_text(encoding="utf-8"))

if "historique" not in st.session_state:
    st.session_state.historique = []

# ============================================================
# STYLE
# ============================================================

st.markdown("""
<style>
.stApp, .main { background: #000000 !important; }

.main-title {
    text-align: center; font-size: 45px; font-weight: 900;
    background: linear-gradient(90deg, #ff3d00, #ff9800, #ffc107, #00e676);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    margin-top: 10px; margin-bottom: 5px;
}
.subtitle { text-align: center; color: #ffffff; font-size: 18px; margin-bottom: 30px; }

.card {
    background: #111111; border-radius: 18px; padding: 25px; margin-bottom: 25px;
    border-top: 3px solid #ff5722; border-right: 3px solid #ffc107;
    border-bottom: 3px solid #00e676; border-left: 3px solid #f44336;
    box-shadow: 0 0 20px rgba(255, 152, 0, 0.12);
}
.card h3 { color: #ffc107 !important; font-size: 24px; }
.card p { color: #ffffff !important; line-height: 1.8; }

h1, h2 { color: #ff9800 !important; }
h3 { color: #ffc107 !important; }
label { color: #ffffff !important; font-weight: 700 !important; }
p { color: #ffffff; }

div[data-baseweb="select"] > div {
    background-color: #111111 !important; border: 1px solid #ff9800 !important;
    color: #ffffff !important; border-radius: 10px;
}
div[data-baseweb="select"] span { color: #ffffff !important; }
input {
    background-color: #111111 !important; color: #ffffff !important;
    border: 1px solid #00e676 !important; border-radius: 10px !important;
}

.stButton > button {
    width: 100%;
    background: linear-gradient(90deg, #ff3d00, #ff9800, #ffc107) !important;
    color: #000000 !important; font-size: 20px !important; font-weight: 900 !important;
    border: 2px solid #ff9800 !important; border-radius: 14px !important;
    padding: 15px !important; transition: all 0.25s ease;
}
.stButton > button:hover {
    background: linear-gradient(90deg, #f44336, #ff5722, #ff9800) !important;
    color: #ffffff !important; border: 2px solid #ff5722 !important;
    transform: scale(1.02); box-shadow: 0 0 20px rgba(255, 87, 34, 0.45);
}

hr {
    border: none !important; height: 2px !important;
    background: linear-gradient(90deg, #f44336, #ff9800, #ffc107, #00e676) !important;
}

.price-title { text-align: center; color: #ffc107 !important; font-size: 25px; font-weight: 900; margin-top: 25px; }
.price-value {
    text-align: center; color: #00e676 !important; font-size: 42px; font-weight: 900;
    margin: 8px 0 10px 0; text-shadow: 0 0 12px rgba(0, 230, 118, 0.35);
}
.price-m2 { text-align: center; color: #ff9800 !important; font-size: 20px; font-weight: 800; margin-bottom: 25px; }

div[data-testid="stExpander"] {
    background-color: #111111 !important; border: 1px solid #ff9800 !important; border-radius: 12px;
}
div[data-testid="stExpander"] summary { color: #ffc107 !important; font-weight: 700; }

.footer { text-align: center; color: #888888; font-size: 14px; margin-top: 35px; padding: 20px; }
.footer strong { color: #ff9800; }
</style>
""", unsafe_allow_html=True)

# ============================================================
# TITRE ET INTRODUCTION
# ============================================================

st.markdown('<div class="main-title">🏠 COTONOU IMMO AI 🤖</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">🇧🇯 Intelligence artificielle pour l’estimation '
    'immobilière à Cotonou</div>',
    unsafe_allow_html=True,
)

st.markdown("""
<div class="card">
<h3>✨ Bienvenue sur Cotonou Immo AI</h3>
<p>🤖 Notre modèle de <b>Machine Learning</b> analyse les caractéristiques
de votre bien afin de produire une estimation de son prix.</p>
<p>
📍 Choisissez votre quartier<br>
🏠 Choisissez le type de bien<br>
📐 Entrez les caractéristiques<br>
🚀 Lancez l'estimation<br>
💰 Découvrez le prix estimé
</p>
</div>
""", unsafe_allow_html=True)

# ============================================================
# FORMULAIRE
# ============================================================

st.markdown("## 🏡 CARACTÉRISTIQUES DU BIEN")

col1, col2 = st.columns(2)

with col1:
    quartier = st.selectbox("📍 Quartier", OPTIONS["quartiers"])
    superficie = st.number_input(
        "📐 Superficie (m²)", min_value=1.0, max_value=5000.0, value=300.0, step=10.0
    )
    chambres = st.number_input("🛏️ Chambres", min_value=0, max_value=30, value=3, step=1)

with col2:
    type_bien = st.selectbox("🏠 Type de bien", OPTIONS["types_bien"])
    pieces = st.number_input("🚪 Nombre de pièces", min_value=1, max_value=50, value=5, step=1)
    salles_bain = st.number_input("🚿 Salles de bain", min_value=0, max_value=20, value=2, step=1)

garages = st.number_input("🚗 Nombre de garages", min_value=0, max_value=20, value=1, step=1)

if not OPTIONS["superficie_min"] <= superficie <= OPTIONS["superficie_max"]:
    st.warning(
        f"⚠️ Le modèle a appris sur des biens de {OPTIONS['superficie_min']:,.0f} "
        f"à {OPTIONS['superficie_max']:,.0f} m². Hors de cette zone, "
        "l'estimation est moins fiable."
    )

st.divider()

# ============================================================
# BOUTON ESTIMATION
# ============================================================

st.markdown("### 🚀 PRÊT À CONNAÎTRE LE PRIX ?")

if st.button("💰 ESTIMER LE PRIX 💰", width="stretch"):

    donnees = {
        "quartier": quartier,
        "type_bien": type_bien,
        "superficie_m2": superficie,
        "chambres": chambres,
        "pieces": pieces,
        "salles_bain": salles_bain,
        "garages": garages,
    }

    # Le 1er appel peut durer ~1 minute : l'API gratuite de Render se réveille
    with st.spinner("🤖 Analyse des données immobilières (le premier appel peut être long)..."):
        try:
            response = requests.post(API_URL, json=donnees, timeout=90)

            if response.status_code == 200:
                prix = float(response.json()["prix_estime_fcfa"])
                prix_m2 = prix / superficie

                st.session_state.historique.append({
                    "Quartier": quartier,
                    "Type": type_bien,
                    "Superficie (m²)": superficie,
                    "Chambres": chambres,
                    "Pièces": pieces,
                    "Salles de bain": salles_bain,
                    "Garages": garages,
                    "Prix estimé (FCFA)": prix,
                    "Prix/m² (FCFA)": prix_m2,
                })

                st.balloons()

                st.markdown('<div class="price-title">💰 Prix estimé :</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="price-value">{prix:,.0f} FCFA</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="price-m2">📐 {prix_m2:,.0f} FCFA / m²</div>', unsafe_allow_html=True)

                st.success("🟢 Estimation réalisée avec succès !")

                with st.expander("🔎 Voir les caractéristiques utilisées"):
                    st.write(f"📍 **Quartier :** {quartier}")
                    st.write(f"🏠 **Type :** {type_bien}")
                    st.write(f"📐 **Superficie :** {superficie} m²")
                    st.write(f"🛏️ **Chambres :** {chambres}")
                    st.write(f"🚪 **Pièces :** {pieces}")
                    st.write(f"🚿 **Salles de bain :** {salles_bain}")
                    st.write(f"🚗 **Garages :** {garages}")
                    st.write(f"💰 **Prix estimé :** {prix:,.0f} FCFA")
                    st.write(f"📊 **Prix au m² :** {prix_m2:,.0f} FCFA/m²")

                st.info(
                    "ℹ️ Estimation indicative, produite par un modèle de Machine "
                    "Learning entraîné sur environ 500 biens de Cotonou. "
                    f"Écart moyen constaté lors des tests : "
                    f"{OPTIONS['mae_fcfa'] / 1e6:,.0f} millions FCFA. "
                    "Elle ne remplace pas une expertise immobilière."
                )

            else:
                st.error(f"🔴 Erreur API : HTTP {response.status_code}")
                st.code(response.text)

        except requests.exceptions.ConnectionError:
            st.error("🔴 Impossible de contacter l'API.")
            st.warning(
                "⚙️ Vérifie que le service API est démarré et que la variable "
                "`API_URL` pointe vers son adresse."
            )

        except requests.exceptions.Timeout:
            st.error("🟠 Le serveur met trop de temps à répondre. Réessaie dans un instant.")

        except Exception as e:
            st.error("🔴 Une erreur inattendue s'est produite.")
            st.code(str(e))

# ============================================================
# STATISTIQUES
# ============================================================

if st.session_state.historique:

    st.divider()
    st.markdown("## 📊 STATISTIQUES")

    df = pd.DataFrame(st.session_state.historique)

    c1, c2 = st.columns(2)
    with c1:
        st.metric("🏠 Estimations", len(df))
        st.metric("💰 Prix moyen", f"{df['Prix estimé (FCFA)'].mean():,.0f} FCFA")
    with c2:
        st.metric("📐 Prix moyen / m²", f"{df['Prix/m² (FCFA)'].mean():,.0f} FCFA")
        st.metric("📈 Prix maximum", f"{df['Prix estimé (FCFA)'].max():,.0f} FCFA")

    st.metric("📉 Prix minimum", f"{df['Prix estimé (FCFA)'].min():,.0f} FCFA")

    st.markdown("### 📈 Évolution des estimations")
    prix_chart = df[["Prix estimé (FCFA)"]].copy()
    prix_chart.index = range(1, len(prix_chart) + 1)
    st.line_chart(prix_chart)

    st.markdown("### 📐 Évolution du prix au m²")
    m2_chart = df[["Prix/m² (FCFA)"]].copy()
    m2_chart.index = range(1, len(m2_chart) + 1)
    st.line_chart(m2_chart)

    st.markdown("### 📜 Historique des estimations")
    affichage = df.copy()
    for colonne in ["Superficie (m²)", "Prix estimé (FCFA)", "Prix/m² (FCFA)"]:
        affichage[colonne] = affichage[colonne].map(lambda x: f"{x:,.0f}")
    st.dataframe(affichage, width="stretch", hide_index=True)

    if st.button("🗑️ Effacer l'historique"):
        st.session_state.historique = []
        st.rerun()

# ============================================================
# FOOTER
# ============================================================

st.divider()

st.markdown("""
<div class="footer">
🤖 <strong>Cotonou Immo AI</strong><br><br>
🇧🇯 Projet de Machine Learning — Estimation immobilière<br><br>
🧠 Random Forest &nbsp; • &nbsp; ⚡ FastAPI &nbsp; • &nbsp; 🎨 Streamlit
</div>
""", unsafe_allow_html=True)
