import streamlit as st
import requests
import pandas as pd


# ============================================================
# CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Cotonou Immo AI",
    page_icon="🏠",
    layout="centered"
)


# ============================================================
# HISTORIQUE
# ============================================================

if "historique" not in st.session_state:
    st.session_state.historique = []


# ============================================================
# STYLE
# ============================================================

st.markdown("""
<style>

/* ============================================================
   FOND NOIR
   ============================================================ */

.stApp {
    background: #000000 !important;
}

.main {
    background: #000000 !important;
}


/* ============================================================
   TITRE
   ============================================================ */

.main-title {
    text-align: center;
    font-size: 45px;
    font-weight: 900;

    background: linear-gradient(
        90deg,
        #ff3d00,
        #ff9800,
        #ffc107,
        #00e676
    );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;

    margin-top: 10px;
    margin-bottom: 5px;
}


.subtitle {
    text-align: center;
    color: #ffffff;
    font-size: 18px;
    margin-bottom: 30px;
}


/* ============================================================
   CARTE INTRODUCTION
   ============================================================ */

.card {

    background: #111111;

    border-radius: 18px;

    padding: 25px;

    margin-bottom: 25px;

    border-top: 3px solid #ff5722;
    border-right: 3px solid #ffc107;
    border-bottom: 3px solid #00e676;
    border-left: 3px solid #f44336;

    box-shadow:
        0 0 20px rgba(255, 152, 0, 0.12);
}


.card h3 {
    color: #ffc107 !important;
    font-size: 24px;
}


.card p {
    color: #ffffff !important;
    line-height: 1.8;
}


/* ============================================================
   TITRES
   ============================================================ */

h1 {
    color: #ff9800 !important;
}

h2 {
    color: #ff9800 !important;
}

h3 {
    color: #ffc107 !important;
}


/* ============================================================
   LABELS
   ============================================================ */

label {
    color: #ffffff !important;
    font-weight: 700 !important;
}


/* ============================================================
   INPUTS
   ============================================================ */

div[data-baseweb="select"] > div {

    background-color: #111111 !important;

    border: 1px solid #ff9800 !important;

    color: #ffffff !important;

    border-radius: 10px;
}


input {

    background-color: #111111 !important;

    color: #ffffff !important;

    border: 1px solid #00e676 !important;

    border-radius: 10px !important;
}


div[data-baseweb="select"] span {
    color: #ffffff !important;
}


/* ============================================================
   BOUTON
   ============================================================ */

.stButton > button {

    width: 100%;

    background: linear-gradient(
        90deg,
        #ff3d00,
        #ff9800,
        #ffc107
    ) !important;

    color: #000000 !important;

    font-size: 20px !important;

    font-weight: 900 !important;

    border: 2px solid #ff9800 !important;

    border-radius: 14px !important;

    padding: 15px !important;

    transition: all 0.25s ease;
}


.stButton > button:hover {

    background: linear-gradient(
        90deg,
        #f44336,
        #ff5722,
        #ff9800
    ) !important;

    color: #ffffff !important;

    border: 2px solid #ff5722 !important;

    transform: scale(1.02);

    box-shadow:
        0 0 20px rgba(255, 87, 34, 0.45);
}


/* ============================================================
   SÉPARATEUR
   ============================================================ */

hr {

    border: none !important;

    height: 2px !important;

    background: linear-gradient(
        90deg,
        #f44336,
        #ff9800,
        #ffc107,
        #00e676
    ) !important;
}


/* ============================================================
   PRIX
   ============================================================ */

.price-title {

    text-align: center;

    color: #ffc107 !important;

    font-size: 25px;

    font-weight: 900;

    margin-top: 25px;
}


.price-value {

    text-align: center;

    color: #00e676 !important;

    font-size: 42px;

    font-weight: 900;

    margin-top: 8px;

    margin-bottom: 10px;

    text-shadow:
        0 0 12px rgba(0, 230, 118, 0.35);
}


/* ============================================================
   PRIX AU M²
   ============================================================ */

.price-m2 {

    text-align: center;

    color: #ff9800 !important;

    font-size: 20px;

    font-weight: 800;

    margin-bottom: 25px;
}


/* ============================================================
   EXPANDER
   ============================================================ */

div[data-testid="stExpander"] {

    background-color: #111111 !important;

    border: 1px solid #ff9800 !important;

    border-radius: 12px;
}


div[data-testid="stExpander"] summary {

    color: #ffc107 !important;

    font-weight: 700;
}


/* ============================================================
   FOOTER
   ============================================================ */

.footer {

    text-align: center;

    color: #888888;

    font-size: 14px;

    margin-top: 35px;

    padding: 20px;
}


.footer strong {
    color: #ff9800;
}


p {
    color: #ffffff;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# URL FASTAPI
# ============================================================

API_URL = "http://127.0.0.1:8005/predict"


# ============================================================
# TITRE
# ============================================================

st.markdown(
    '<div class="main-title">🏠 COTONOU IMMO AI 🤖</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    '🇧🇯 Intelligence artificielle pour l’estimation '
    'immobilière à Cotonou'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# INTRODUCTION
# ============================================================

st.markdown("""
<div class="card">

<h3>✨ Bienvenue sur Cotonou Immo AI</h3>

<p>
🤖 Notre modèle de <b>Machine Learning</b> analyse les
caractéristiques de votre bien afin de produire une
estimation de son prix.
</p>

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
# DONNÉES DISPONIBLES
# ============================================================

quartiers = [
    "Fidjrossè",
    "Fidjrossè Plage",
    "Fidjrossè Houénoussou",
    "Akpakpa",
    "Akpakpa CEN-SAD",
    "Akpakpa Jack Zone Super",
    "Akpakpa Midombo",
    "Sainte Rita",
    "Haie Vive",
    "Cadjèhoun",
    "Cotonou Centre"
]


types_bien = [
    "Villa",
    "Maison",
    "Appartement",
    "Immeuble",
    "Terrain"
]


# ============================================================
# FORMULAIRE
# ============================================================

st.markdown(
    "## 🏡 CARACTÉRISTIQUES DU BIEN"
)


col1, col2 = st.columns(2)


with col1:

    quartier = st.selectbox(
        "📍 Quartier",
        quartiers
    )

    superficie = st.number_input(
        "📐 Superficie (m²)",
        min_value=1.0,
        max_value=5000.0,
        value=300.0,
        step=10.0
    )

    chambres = st.number_input(
        "🛏️ Chambres",
        min_value=0,
        max_value=30,
        value=3,
        step=1
    )


with col2:

    type_bien = st.selectbox(
        "🏠 Type de bien",
        types_bien
    )

    pieces = st.number_input(
        "🚪 Nombre de pièces",
        min_value=1,
        max_value=50,
        value=5,
        step=1
    )

    salles_bain = st.number_input(
        "🚿 Salles de bain",
        min_value=0,
        max_value=20,
        value=2,
        step=1
    )


garages = st.number_input(
    "🚗 Nombre de garages",
    min_value=0,
    max_value=20,
    value=1,
    step=1
)


# ============================================================
# SÉPARATEUR
# ============================================================

st.divider()


# ============================================================
# BOUTON ESTIMATION
# ============================================================

st.markdown(
    "### 🚀 PRÊT À CONNAÎTRE LE PRIX ?"
)


if st.button(
    "💰 ESTIMER LE PRIX 💰",
    use_container_width=True
):

    donnees = {

        "quartier": quartier,

        "type_bien": type_bien,

        "superficie_m2": superficie,

        "chambres": chambres,

        "pieces": pieces,

        "salles_bain": salles_bain,

        "garages": garages
    }


    with st.spinner(
        "🤖 Analyse des données immobilières..."
    ):

        try:

            response = requests.post(
                API_URL,
                json=donnees,
                timeout=10
            )


            # =================================================
            # SUCCÈS
            # =================================================

            if response.status_code == 200:

                resultat = response.json()

                prix = float(
                    resultat["prix_estime_fcfa"]
                )


                # =============================================
                # CALCUL DU PRIX AU M²
                # =============================================

                prix_m2 = prix / superficie


                # =============================================
                # AJOUT À L'HISTORIQUE
                # =============================================

                estimation = {

                    "Quartier": quartier,

                    "Type": type_bien,

                    "Superficie (m²)": superficie,

                    "Chambres": chambres,

                    "Pièces": pieces,

                    "Salles de bain": salles_bain,

                    "Garages": garages,

                    "Prix estimé (FCFA)": prix,

                    "Prix/m² (FCFA)": prix_m2
                }


                st.session_state.historique.append(
                    estimation
                )


                # =============================================
                # BALLONS
                # =============================================

                st.balloons()


                # =============================================
                # AFFICHAGE PRIX
                # =============================================

                st.markdown(
                    '<div class="price-title">'
                    '💰 Prix estimé :'
                    '</div>',
                    unsafe_allow_html=True
                )


                st.markdown(
                    f'<div class="price-value">'
                    f'{prix:,.0f} FCFA'
                    f'</div>',
                    unsafe_allow_html=True
                )


                # =============================================
                # PRIX AU M²
                # =============================================

                st.markdown(
                    f'<div class="price-m2">'
                    f'📐 {prix_m2:,.0f} FCFA / m²'
                    f'</div>',
                    unsafe_allow_html=True
                )


                st.success(
                    "🟢 Estimation réalisée avec succès !"
                )


                # =============================================
                # DÉTAILS
                # =============================================

                with st.expander(
                    "🔎 Voir les caractéristiques utilisées"
                ):

                    st.write(
                        f"📍 **Quartier :** {quartier}"
                    )

                    st.write(
                        f"🏠 **Type :** {type_bien}"
                    )

                    st.write(
                        f"📐 **Superficie :** {superficie} m²"
                    )

                    st.write(
                        f"🛏️ **Chambres :** {chambres}"
                    )

                    st.write(
                        f"🚪 **Pièces :** {pieces}"
                    )

                    st.write(
                        f"🚿 **Salles de bain :** {salles_bain}"
                    )

                    st.write(
                        f"🚗 **Garages :** {garages}"
                    )

                    st.write(
                        f"💰 **Prix estimé :** "
                        f"{prix:,.0f} FCFA"
                    )

                    st.write(
                        f"📊 **Prix au m² :** "
                        f"{prix_m2:,.0f} FCFA/m²"
                    )


                st.info(
                    "ℹ️ Cette valeur est une estimation "
                    "produite par notre modèle de Machine Learning."
                )


            # =================================================
            # ERREUR API
            # =================================================

            else:

                st.error(
                    f"🔴 Erreur API : HTTP "
                    f"{response.status_code}"
                )

                st.code(
                    response.text
                )


        except requests.exceptions.ConnectionError:

            st.error(
                "🔴 Impossible de contacter FastAPI."
            )

            st.warning(
                "⚙️ Lance d'abord le serveur avec : "
                "`python3 server.py`"
            )


        except requests.exceptions.Timeout:

            st.error(
                "🟠 Le serveur met trop de temps à répondre."
            )


        except Exception as e:

            st.error(
                "🔴 Une erreur inattendue s'est produite."
            )

            st.code(
                str(e)
            )


# ============================================================
# STATISTIQUES
# ============================================================

if len(st.session_state.historique) > 0:

    st.divider()

    st.markdown(
        "## 📊 STATISTIQUES"
    )


    df = pd.DataFrame(
        st.session_state.historique
    )


    # ========================================================
    # CALCULS
    # ========================================================

    nombre_estimations = len(df)

    prix_moyen = df[
        "Prix estimé (FCFA)"
    ].mean()

    prix_min = df[
        "Prix estimé (FCFA)"
    ].min()

    prix_max = df[
        "Prix estimé (FCFA)"
    ].max()

    prix_m2_moyen = df[
        "Prix/m² (FCFA)"
    ].mean()


    # ========================================================
    # CARTES STATISTIQUES
    # ========================================================

    c1, c2 = st.columns(2)

    with c1:

        st.metric(
            "🏠 Estimations",
            nombre_estimations
        )

        st.metric(
            "💰 Prix moyen",
            f"{prix_moyen:,.0f} FCFA"
        )


    with c2:

        st.metric(
            "📐 Prix moyen / m²",
            f"{prix_m2_moyen:,.0f} FCFA"
        )

        st.metric(
            "📈 Prix maximum",
            f"{prix_max:,.0f} FCFA"
        )


    st.metric(
        "📉 Prix minimum",
        f"{prix_min:,.0f} FCFA"
    )


    # ========================================================
    # GRAPHIQUE DES PRIX
    # ========================================================

    st.markdown(
        "### 📈 Évolution des estimations"
    )


    graphique_prix = df[
        ["Prix estimé (FCFA)"]
    ].copy()


    graphique_prix.index = range(
        1,
        len(graphique_prix) + 1
    )


    st.line_chart(
        graphique_prix
    )


    # ========================================================
    # GRAPHIQUE PRIX AU M²
    # ========================================================

    st.markdown(
        "### 📐 Évolution du prix au m²"
    )


    graphique_m2 = df[
        ["Prix/m² (FCFA)"]
    ].copy()


    graphique_m2.index = range(
        1,
        len(graphique_m2) + 1
    )


    st.line_chart(
        graphique_m2
    )


    # ========================================================
    # HISTORIQUE
    # ========================================================

    st.markdown(
        "### 📜 Historique des estimations"
    )


    historique_affichage = df.copy()


    historique_affichage[
        "Superficie (m²)"
    ] = historique_affichage[
        "Superficie (m²)"
    ].map(
        lambda x: f"{x:,.0f}"
    )


    historique_affichage[
        "Prix estimé (FCFA)"
    ] = historique_affichage[
        "Prix estimé (FCFA)"
    ].map(
        lambda x: f"{x:,.0f}"
    )


    historique_affichage[
        "Prix/m² (FCFA)"
    ] = historique_affichage[
        "Prix/m² (FCFA)"
    ].map(
        lambda x: f"{x:,.0f}"
    )


    st.dataframe(
        historique_affichage,
        use_container_width=True,
        hide_index=True
    )


    # ========================================================
    # BOUTON EFFACER
    # ========================================================

    if st.button(
        "🗑️ Effacer l'historique"
    ):

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

🧠 Random Forest
&nbsp; • &nbsp;
⚡ FastAPI
&nbsp; • &nbsp;
🎨 Streamlit

</div>
""", unsafe_allow_html=True)
