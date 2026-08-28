
# 🏠 Cotonou Immo AI 🇧🇯

## Application de Machine Learning pour l'estimation des prix immobiliers à Cotonou, intégrant un modèle Random Forest, une API FastAPI et une interface interactive Streamlit.

## 📌 Table des matières
### 1. Présentation du projet
### 2. Objectifs
### 3. Pourquoi ce projet
### 4. Fonctionnalités
### 5. Architecture
### 6. Technologies utilisées
### 7. Structure du projet
### 8. Dataset
### 9. Variables utilisées
### 10. Préparation des données
### 11. Modèle de Machine Learning
### 12. Entraînement
### 13. Évaluation du modèle
### 14. Interprétation des résultats
### 15. API FastAPI
### 16. Interface Streamlit
### 17. Fonctionnement complet
### 18. Historique des estimations
### 19. Estimation du prix au m²
### 20. Statistiques
### 21. Graphiques
### 22. Installation
### 23. Lancement du projet
### 24. Utilisation
### 25. Exemple
### 26. API : exemple de requête
### 27. API : exemple de réponse
### 28. Gestion des erreurs
### 29. Limites du projet
### 30. Améliorations futures
### 31. Perspectives MLOps
### 32. Compétences démontrées
### 33. Résultats du projet
### 34. Avertissement
### 35. Auteur
## 1. 🏠 Présentation du projet

Cotonou Immo AI est un projet personnel de Machine Learning ayant pour objectif de développer une application capable d'estimer le prix d'un bien immobilier à Cotonou à partir de plusieurs caractéristiques.

L'utilisateur renseigne les caractéristiques d'un bien immobilier, notamment :

## 📍 le quartier ;
## 🏠 le type de bien ;
## 📐 la superficie ;
## 🛏️ le nombre de chambres ;
## 🚪 le nombre de pièces ;
## 🚿 le nombre de salles de bain ;
## 🚗 le nombre de garages.

Ces informations sont envoyées à une API développée avec FastAPI.

L'API utilise ensuite un modèle de Machine Learning entraîné avec Scikit-learn afin de produire une estimation du prix.

Le résultat est finalement renvoyé à l'interface Streamlit et affiché à l'utilisateur.

## 2. 🎯 Objectifs

Le projet poursuit plusieurs objectifs.

Objectif principal

Construire une chaîne complète de Machine Learning allant de la donnée jusqu'à l'utilisation du modèle dans une application.

Données
   ↓
Nettoyage
   ↓
Préparation
   ↓
Entraînement
   ↓
Évaluation
   ↓
Sauvegarde du modèle
   ↓
API FastAPI
   ↓
Interface Streamlit
   ↓
Estimation immobilière
Objectifs techniques

Le projet permet également de travailler sur :

la préparation des données ;
l'analyse d'un dataset immobilier ;
l'entraînement d'un modèle de régression ;
l'évaluation d'un modèle ;
la sauvegarde d'un modèle avec Joblib ;
la création d'une API REST ;
la communication entre une interface et une API ;
la création d'une interface utilisateur avec Streamlit ;
la gestion des erreurs ;
la visualisation des résultats ;
la mise en place d'un historique des prédictions.
## 3. 💡 Pourquoi ce projet ?

Le marché immobilier de Cotonou peut présenter une forte variation des prix selon plusieurs facteurs :

la localisation ;
la superficie ;
le type de bien ;
le nombre de chambres ;
le nombre de pièces ;
le nombre de salles de bain ;
le nombre de garages ;
etc.

L'objectif n'est donc pas simplement de créer une calculatrice de prix.

L'idée est de construire un système de prédiction basé sur les données.

Le projet constitue ainsi une première expérience concrète dans le domaine de la Data Science et du Machine Learning appliqué à un problème réel.

## 4. 🚀 Fonctionnalités
### 🏠 Estimation immobilière

L'utilisateur peut sélectionner un quartier et entrer les caractéristiques du bien.

L'application retourne ensuite une estimation du prix.

### 📍 Sélection du quartier

Les quartiers disponibles sont proposés directement dans une liste.

L'utilisateur n'a donc pas besoin d'écrire manuellement le nom du quartier.

Exemples :

Fidjrossè
Fidjrossè Plage
Fidjrossè Houénoussou
Akpakpa
Akpakpa CEN-SAD
Akpakpa Jack Zone Super
Akpakpa Midombo
Sainte Rita
Haie Vive
Cadjèhoun
Cotonou Centre

Les modalités réellement apprises par le modèle dépendent toutefois des catégories présentes dans le dataset d'entraînement.

### 🏡 Type de bien

L'utilisateur peut sélectionner :

Villa
Maison
Appartement
Immeuble
Terrain
### 📐 Caractéristiques numériques

L'application permet de renseigner :

superficie ;
chambres ;
pièces ;
salles de bain ;
garages.
### 💰 Prix estimé

Après l'appel à l'API, l'application affiche le prix estimé.

Exemple :

### 💰 Prix estimé :


203,796,667 FCFA
### 📊 Prix estimé au m²

L'application calcule également une valeur indicative du prix par mètre carré :

Prix au m² = Prix estimé / Superficie

Par exemple, pour :

Prix = 203 796 667 FCFA
Superficie = 350 m²

on obtient environ :

582 276 FCFA/m²
## 📜 Historique

Chaque estimation réalisée pendant la session est enregistrée dans l'application.

L'utilisateur peut ainsi comparer plusieurs biens.

## 📈 Statistiques

L'application calcule notamment :

nombre d'estimations ;
prix moyen ;
prix minimum ;
prix maximum ;
prix moyen au m².
## 📊 Graphiques

Deux visualisations sont proposées :

Évolution des prix

Le graphique permet de visualiser les prix des différentes estimations réalisées.

Évolution du prix au m²

Une seconde visualisation permet de comparer les prix au m².

## 5. 🏗️ Architecture

L'application utilise une architecture en plusieurs couches.

                    👤 UTILISATEUR
                          │
                          ▼
                ┌───────────────────┐
                │     Streamlit     │
                │      app.py       │
                └─────────┬─────────┘
                          │
                    HTTP POST
                          │
                          ▼
                ┌───────────────────┐
                │      FastAPI      │
                │     server.py     │
                └─────────┬─────────┘
                          │
                          ▼
                ┌───────────────────┐
                │    model.pkl      │
                │ Random Forest     │
                └─────────┬─────────┘
                          │
                          ▼
                  💰 PRIX ESTIMÉ
                          │
                          ▼
                ┌───────────────────┐
                │     Streamlit     │
                │ affichage résultat│
                └───────────────────┘

Cette séparation permet de ne pas mélanger :

l'entraînement du modèle ;
la logique de prédiction ;
l'API ;
l'interface graphique.
6. 🛠️ Technologies utilisées
Python

Langage principal du projet.

Pandas

Utilisé pour manipuler les données et construire les DataFrames.

import pandas as pd
Scikit-learn

Utilisé pour le Machine Learning.

Il permet notamment :

de séparer les données ;
d'entraîner le modèle ;
d'effectuer les prédictions ;
de calculer les métriques d'évaluation.
Random Forest

Le modèle utilisé pour effectuer la prédiction est un Random Forest Regressor.

Joblib

Utilisé pour sauvegarder et recharger le modèle entraîné.

joblib.dump(...)

puis :

joblib.load(...)
FastAPI

FastAPI fournit l'API permettant à l'application Streamlit de communiquer avec le modèle.

Uvicorn

Uvicorn permet d'exécuter le serveur FastAPI.

Dans notre configuration, le serveur est lancé directement avec :

python3 server.py
Streamlit

Streamlit est utilisé pour créer l'interface utilisateur.

## 7. 📁 Structure du projet

La structure du projet est la suivante :

cotonou-immo-ai/
│
├── app.py
│
├── server.py
│
├── projet1.py
│
├── model.pkl
│
├── requirements.txt
│
├── .gitignore
│
└── README.md
app.py

Contient l'interface Streamlit.

server.py

Contient l'API FastAPI.

Il reçoit les caractéristiques du bien et transmet les données au modèle.

projet1.py

Contient le code d'entraînement du modèle.

model.pkl

Contient le modèle entraîné sauvegardé avec Joblib.

Ce fichier est utilisé par l'API pour effectuer les prédictions.

requirements.txt

Contient les dépendances Python du projet.

.gitignore

Permet d'empêcher certains fichiers d'être envoyés vers Git.

README.md

Contient la documentation du projet.

## 8. 📊 Dataset

Le projet utilise un dataset immobilier consacré à Cotonou et utilisé pour entraîner le modèle.

Le fichier utilisé dans le projet est :

Cotonou real estate 500 csv no duplicates

Le dataset contient les caractéristiques nécessaires à la construction du modèle de prédiction.

L'objectif du dataset est de fournir au modèle des exemples de biens immobiliers associés à leurs prix.

## 9. 🔢 Variables utilisées

Les variables exploitées dans le modèle correspondent aux caractéristiques renseignées dans l'application.

Variable	Description
quartier	Localisation du bien
type_bien	Type de propriété
superficie_m2	Surface du bien
chambres	Nombre de chambres
pieces	Nombre de pièces
salles_bain	Nombre de salles de bain
garages	Nombre de garages
prix	Prix du bien

La variable prix constitue la variable cible du problème de Machine Learning.

## 10. 🧹 Préparation des données

Avant l'entraînement, les données doivent être transformées afin d'être utilisables par le modèle.

Les variables numériques peuvent être utilisées directement sous forme numérique.

Les variables catégorielles comme :

quartier
type_bien

doivent être transformées en représentation numérique.

Cette étape est importante car les algorithmes de Machine Learning ne peuvent pas directement traiter des chaînes de caractères comme :

"Fidjrossè"
"Villa"

sans transformation.

## 11. 🧠 Modèle de Machine Learning

Le modèle choisi est :

RandomForestRegressor

Il s'agit d'un algorithme de Machine Learning adapté aux problèmes de régression.

Dans notre cas, la variable à prédire est un nombre :

Prix immobilier

Le problème est donc un problème de régression supervisée.

## 12. 🌳 Pourquoi Random Forest ?

Un Random Forest est constitué de plusieurs arbres de décision.

Chaque arbre produit une prédiction.

Les prédictions des différents arbres sont ensuite combinées.

Schématiquement :

                    Données
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
       Arbre 1      Arbre 2      Arbre 3
          │            │            │
          ▼            ▼            ▼
       Prix 1       Prix 2       Prix 3
          │            │            │
          └────────────┼────────────┘
                       ▼
                Prix final estimé

Cette approche permet au modèle de capturer des relations potentiellement complexes entre les caractéristiques du bien et son prix.

## 13. 🏋️ Entraînement

Le dataset est séparé en deux parties :

Données d'entraînement
        +
Données de test

Les données d'entraînement servent à apprendre les relations entre les variables.

Les données de test permettent ensuite d'évaluer le modèle sur des données qu'il n'a pas utilisées directement pendant l'apprentissage.

## 14. 📏 Évaluation du modèle

Le modèle a obtenu les résultats suivants :

============================================================
RÉSULTATS
============================================================


MAE  : 58,503,300 FCFA
RMSE : 77,533,359 FCFA
R²   : 0.6236
## 15. 📐 Comprendre le MAE

MAE signifie :

Mean Absolute Error

ou :

Erreur absolue moyenne.

La valeur obtenue est :

58 503 300 FCFA

Cela signifie que, sur l'ensemble de test utilisé, l'erreur absolue moyenne des prédictions est d'environ 58,5 millions FCFA.

Ce résultat doit être interprété avec prudence compte tenu de la taille et de la qualité du dataset.

## 16. 📐 Comprendre le RMSE

RMSE signifie :

Root Mean Squared Error

Le résultat obtenu est :

77 533 359 FCFA

Le RMSE pénalise davantage les erreurs importantes.

Un écart important entre le MAE et le RMSE peut notamment indiquer la présence de prédictions particulièrement éloignées de certaines valeurs réelles.

## 17. 📊 Comprendre le R²

Le coefficient de détermination obtenu est :

R² = 0.6236

Cela indique que le modèle explique environ 62,36 % de la variabilité de la variable cible sur l'ensemble d'évaluation utilisé.

Ce résultat montre que le modèle a appris des relations utiles dans les données, mais qu'il reste une part importante de variabilité non expliquée.

Le modèle doit donc être considéré comme une première version expérimentale, et non comme un système d'expertise immobilière définitif.

## 18. 🔬 Interprétation des performances

Les performances obtenues sont intéressantes pour une première version du projet, mais elles montrent également les limites du dataset.

Un modèle immobilier peut être fortement influencé par des facteurs qui ne sont pas nécessairement présents dans les données.

Par exemple :

état réel du bâtiment ;
qualité des finitions ;
distance exacte par rapport à certains points d'intérêt ;
proximité de la mer ;
qualité de la rue ;
accessibilité ;
sécurité ;
âge du bâtiment ;
qualité du terrain ;
caractéristiques précises du quartier ;
offre et demande au moment de la vente.

Plus les données disponibles seront riches et fiables, plus le modèle pourra apprendre des relations pertinentes.

## 19. ⚡ API FastAPI

FastAPI joue le rôle d'intermédiaire entre l'interface et le modèle.

L'utilisateur n'appelle donc pas directement le modèle.

Le fonctionnement est :

Streamlit
    │
    │ HTTP POST
    ▼
FastAPI
    │
    ▼
Random Forest
    │
    ▼
Prix

Cette architecture est particulièrement intéressante dans une perspective de déploiement.

## 20. 🔌 Endpoint de prédiction

L'application utilise un endpoint de prédiction :

POST /predict

Les données du bien sont envoyées sous forme JSON.

Exemple :

{
    "quartier": "Fidjrossè",
    "type_bien": "Villa",
    "superficie_m2": 350,
    "chambres": 4,
    "pieces": 6,
    "salles_bain": 2,
    "garages": 2
}
## 21. 🎨 Interface Streamlit

Streamlit fournit l'interface utilisateur.

L'objectif est de permettre à une personne qui ne connaît pas Python ou le Machine Learning d'utiliser le modèle simplement.

L'utilisateur sélectionne les caractéristiques du bien puis clique sur :

### 💰 ESTIMER LE PRIX 💰
## 22. 🔄 Fonctionnement complet

Lorsqu'un utilisateur effectue une estimation :

Étape 1

L'utilisateur sélectionne le quartier.

📍 Fidjrossè
Étape 2

Il sélectionne le type de bien.

🏠 Villa
Étape 3

Il renseigne :

📐 350 m²
🛏️ 4 chambres
🚪 6 pièces
🚿 2 salles de bain
🚗 2 garages
Étape 4

Streamlit construit une requête JSON.

Étape 5

La requête est envoyée à FastAPI.

Étape 6

FastAPI charge le modèle.

Étape 7

Le modèle effectue la prédiction.

Étape 8

FastAPI renvoie le résultat.

Étape 9

Streamlit affiche le prix.

## 23. 💰 Prix au m²

Une fonctionnalité supplémentaire permet de calculer le prix estimé par mètre carré.

La formule utilisée est :

Prix au m² = Prix estimé / Superficie

Exemple :

Prix estimé = 203 796 667 FCFA


Superficie = 350 m²

Donc :

203 796 667 / 350


≈ 582 276 FCFA/m²

Cette valeur est une indication dérivée de la prédiction du modèle.

Elle ne correspond pas nécessairement au prix réel du marché au m².

## 24. 📜 Historique des estimations

L'application conserve les estimations effectuées pendant la session Streamlit.

Chaque entrée contient notamment :

Quartier
Type
Superficie
Chambres
Pièces
Salles de bain
Garages
Prix estimé
Prix/m²

Cela permet de comparer plusieurs biens.

## 25. 📊 Statistiques

À partir de l'historique, l'application calcule automatiquement :

Nombre d'estimations
Nombre d'estimations = nombre de biens analysés
Prix moyen
Prix moyen =
somme des prix / nombre d'estimations
Prix minimum

Le prix le plus faible parmi les estimations.

Prix maximum

Le prix le plus élevé parmi les estimations.

Prix moyen au m²

La moyenne des prix au m² calculés pour les biens estimés.

## 26. 📈 Graphiques

L'application propose également des graphiques permettant de visualiser :

Évolution des prix

Chaque nouvelle estimation est ajoutée au graphique.

Évolution du prix au m²

Cette visualisation permet de comparer la valeur estimée par mètre carré entre les différents biens.

## 27. 🧪 Exemple de prédiction

Un exemple testé avec le modèle :

============================================================
ESTIMATION DU PRIX D'UNE MAISON
============================================================


Quartier : Fidjrossè
Type de bien : Villa
Superficie : 350 m²
Chambres : 4
Pièces : 6
Salles de bain : 2
Garages : 2

Le modèle a produit :

Prix estimé :
207,700,000 FCFA

Cet exemple montre le fonctionnement du pipeline complet.

## 28. 🛡️ Gestion des erreurs

L'application gère plusieurs situations.

FastAPI inaccessible

Si le serveur n'est pas lancé :

### 🔴 Impossible de contacter FastAPI.
Erreur HTTP

Si l'API renvoie une erreur, Streamlit affiche notamment le code HTTP et la réponse du serveur.

Exemple :

### 🔴 Erreur API : HTTP 405
Timeout

Si le serveur ne répond pas suffisamment rapidement :

### 🟠 Le serveur met trop de temps à répondre.

Cette gestion facilite le débogage de l'application.

## 29. 💻 Installation
1. Cloner le projet
git clone https://github.com/USERNAME/cotonou-immo-ai.git

Puis :

cd cotonou-immo-ai
2. Créer un environnement virtuel

Linux/macOS :

python3 -m venv venv

Activation :

source venv/bin/activate
3. Installer les dépendances
pip install -r requirements.txt
## 30. ▶️ Lancement du projet

Le projet utilise deux composants principaux :

FastAPI
Streamlit
Terminal 1 — FastAPI
python3 server.py

Le serveur démarre normalement sur :

http://127.0.0.1:8000
Terminal 2 — Streamlit
streamlit run app.py

L'interface Streamlit est alors accessible depuis l'adresse affichée dans le terminal.

## 31. 🧑‍💻 Utilisation

Une fois l'application lancée :

1. Choisir un quartier
📍 Fidjrossè
2. Choisir le type de bien
🏠 Villa
3. Entrer les caractéristiques

Exemple :

Superficie : 350
Chambres : 4
Pièces : 6
Salles de bain : 2
Garages : 2
4. Cliquer
💰 ESTIMER LE PRIX 💰
5. Consulter
Prix estimé
Prix au m²
Historique
Statistiques
Graphiques
32. 🔬 Exemple de requête API
{
    "quartier": "Fidjrossè",
    "type_bien": "Villa",
    "superficie_m2": 350,
    "chambres": 4,
    "pieces": 6,
    "salles_bain": 2,
    "garages": 2
}
## 33. 📦 Exemple de réponse

La réponse dépend de l'exécution du modèle.

Exemple :

{
    "prix_estime_fcfa": 207700000
}

Streamlit récupère ensuite cette valeur pour l'afficher.

## 34. 🔐 Gestion du modèle

Le modèle est sauvegardé localement avec Joblib.

Exemple conceptuel :

joblib.dump(
    {
        "model": model,
        "columns": columns
    },
    "model.pkl"
)

Puis il peut être rechargé :

data = joblib.load("model.pkl")

Cette approche évite de réentraîner le modèle à chaque démarrage de l'application.

## 35. ⚠️ Limites du projet

Cette version présente plusieurs limites.

Taille du dataset

Le dataset utilisé pour cette version reste relativement limité pour représenter l'ensemble du marché immobilier de Cotonou.

Qualité des données

La qualité d'un modèle dépend directement de la qualité des données utilisées pour l'entraînement.

Des données incorrectes, incomplètes ou trop peu représentatives peuvent conduire à des prédictions moins fiables.

Variables limitées

Le modèle utilise un nombre limité de caractéristiques.

De nombreux facteurs immobiliers ne sont pas encore intégrés.

Localisation

Le quartier constitue une information importante, mais il ne permet pas à lui seul de représenter précisément la localisation d'un bien.

Deux biens situés dans le même quartier peuvent avoir des valeurs très différentes.

Estimation et expertise

L'application ne constitue pas une expertise immobilière professionnelle.

Le résultat doit être considéré comme une estimation algorithmique.

## 36. 🚀 Améliorations futures

Le projet peut être fortement amélioré.

📊 Dataset plus important

Une prochaine version pourrait utiliser plusieurs milliers d'annonces immobilières vérifiées.

📍 Géolocalisation

Ajouter :

latitude
longitude

permettrait au modèle d'utiliser une localisation beaucoup plus précise.

🏖️ Distance à la mer

Pour Cotonou, la distance par rapport à la côte pourrait constituer une variable intéressante.

🛣️ Accessibilité

Ajouter des variables relatives :

aux routes ;
aux transports ;
aux axes principaux ;
aux services.
🏗️ État du bâtiment

Ajouter :

neuf
bon état
à rénover
ancien

pourrait améliorer les prédictions.

🏊 Équipements

Ajouter :

piscine ;
jardin ;
terrasse ;
clôture ;
parking ;
dépendance ;
groupe électrogène ;
forage ;
etc.
## 37. 🧠 Amélioration du Machine Learning

Plusieurs modèles pourraient être comparés :

Linear Regression
        ↓
Decision Tree
        ↓
Random Forest
        ↓
Gradient Boosting
        ↓
XGBoost
        ↓
LightGBM

L'objectif serait de comparer leurs performances avec les mêmes données.

Les métriques pourraient être comparées dans un tableau :

Modèle	MAE	RMSE	R²
Linear Regression	...	...	...
Decision Tree	...	...	...
Random Forest	...	...	...
Gradient Boosting	...	...	...
## 38. 🔍 Validation croisée

Une prochaine version pourrait utiliser une Cross-Validation afin d'obtenir une évaluation plus robuste du modèle.

Au lieu de dépendre d'une seule séparation entraînement/test, les données pourraient être divisées en plusieurs folds.

Cela permettrait d'avoir une meilleure estimation de la capacité de généralisation du modèle.

## 39. ⚙️ Hyperparameter Tuning

Les paramètres du Random Forest pourraient être optimisés.

Par exemple :

n_estimators
max_depth
min_samples_split
min_samples_leaf
max_features

Une recherche avec :

GridSearchCV

ou :

RandomizedSearchCV

pourrait être utilisée.

## 40. 🧠 Explainable AI

Une future version pourrait expliquer pourquoi le modèle produit une certaine estimation.

Par exemple :

Superficie        ███████████████
Quartier          ███████████
Chambres          ███████
Garages           ████
Salles de bain    ███

Des outils comme SHAP pourraient permettre d'analyser l'importance des variables.

## 41. 🗄️ Base de données

Actuellement, l'historique est conservé pendant la session Streamlit.

Une évolution naturelle serait d'utiliser une base de données :

SQLite
PostgreSQL
MySQL

Architecture future :

Streamlit
    ↓
FastAPI
    ↓
PostgreSQL
    ↓
Historique

Cela permettrait de conserver les estimations même après le redémarrage de l'application.

## 42. ☁️ Déploiement

Une future version pourrait être déployée en ligne.

Architecture possible :

                    INTERNET
                       │
                       ▼
              ┌─────────────────┐
              │    Streamlit    │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │     FastAPI     │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │  ML Model       │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │   PostgreSQL    │
              └─────────────────┘
## 43. 🤖 Perspectives MLOps

Ce projet peut également évoluer vers une architecture MLOps complète.

Une future architecture pourrait inclure :

GitHub
   ↓
CI/CD
   ↓
Tests
   ↓
Build Docker
   ↓
Déploiement
   ↓
FastAPI
   ↓
Model
   ↓
Monitoring

On pourrait également intégrer :

Docker ;
GitHub Actions ;
MLflow ;
monitoring ;
versionnement des modèles ;
versionnement des datasets ;
tests automatiques ;
déploiement cloud.
## 44. 🐳 Docker

Une prochaine version pourrait être containerisée avec Docker.

Exemple d'architecture :

Docker
│
├── Streamlit
│
├── FastAPI
│
└── Model

Cela faciliterait le déploiement sur différentes machines.

## 45. 🔄 CI/CD

GitHub Actions pourrait automatiquement :

récupérer le projet ;
installer les dépendances ;
exécuter les tests ;
vérifier le code ;
construire l'application ;
préparer le déploiement.
## 46. 📈 Monitoring

Une version plus avancée pourrait suivre :

nombre de prédictions ;
temps de réponse ;
erreurs API ;
distribution des prédictions ;
dérive des données ;
performances du modèle.

Cela permettrait de détecter lorsqu'un modèle devient moins performant.

## 47. 🧪 Tests

Le projet peut également intégrer des tests automatisés.

Exemples :

tests/
│
├── test_model.py
├── test_api.py
└── test_data.py

On pourrait notamment vérifier :

que l'API répond correctement ;
que les données sont valides ;
que le modèle retourne une valeur numérique ;
que les valeurs impossibles sont rejetées.
## 48. 🔒 Sécurité

Pour un déploiement réel, plusieurs éléments supplémentaires seraient nécessaires :

validation stricte des entrées ;
authentification éventuelle ;
limitation des requêtes ;
protection de l'API ;
gestion des secrets ;
HTTPS ;
journalisation.
## 49. 📌 Compétences démontrées

Ce projet permet de démontrer plusieurs compétences.

Python
✔ Programmation Python
✔ Manipulation de données
✔ Modules
✔ Gestion des erreurs
Data Science
✔ Pandas
✔ Préparation des données
✔ Analyse des données
✔ Évaluation
Machine Learning
✔ Régression
✔ Random Forest
✔ Train/Test Split
✔ MAE
✔ RMSE
✔ R²
Backend
✔ FastAPI
✔ API REST
✔ JSON
✔ HTTP
Frontend/Data App
✔ Streamlit
✔ Formulaires
✔ Visualisation
✔ Statistiques
Déploiement / MLOps
✔ Git
✔ GitHub
✔ Architecture API + modèle
✔ Préparation au déploiement
## 50. 📊 Résultats actuels

Le modèle actuel a obtenu :

Métrique	Résultat
MAE	58 503 300 FCFA
RMSE	77 533 359 FCFA
R²	0.6236

Ces résultats constituent la performance de la version actuelle du modèle sur son ensemble d'évaluation.

Ils serviront de baseline pour les futures améliorations.

## 51. 🎯 Roadmap

Le projet peut évoluer progressivement.

✅ Version actuelle
[x] Dataset immobilier
[x] Préparation des données
[x] Random Forest
[x] Évaluation
[x] Sauvegarde du modèle
[x] FastAPI
[x] Streamlit
[x] Estimation du prix
[x] Prix au m²
[x] Historique
[x] Statistiques
[x] Graphiques
🔜 Version suivante
[ ] Dataset plus important
[ ] Feature engineering
[ ] Comparaison de plusieurs modèles
[ ] Hyperparameter tuning
[ ] Cross-validation
[ ] Analyse des erreurs
[ ] Explainable AI
🚀 Version avancée
[ ] Base PostgreSQL
[ ] Docker
[ ] Tests automatisés
[ ] GitHub Actions
[ ] MLflow
[ ] Monitoring
[ ] Déploiement cloud
[ ] CI/CD
## 52. 🏆 Vision du projet

L'objectif à long terme est de transformer Cotonou Immo AI en une véritable plateforme intelligente d'analyse immobilière.

La vision pourrait être :

                    🏠 COTONOU IMMO AI
                           │
             ┌─────────────┼─────────────┐
             │             │             │
             ▼             ▼             ▼
        💰 PRIX        📊 ANALYSE     📍 LOCALISATION
             │             │             │
             └─────────────┼─────────────┘
                           │
                           ▼
                    🤖 MACHINE LEARNING
                           │
                           ▼
                    📈 PRÉDICTIONS
                           │
                           ▼
                    ☁️ PLATEFORME

Le projet pourrait ainsi évoluer d'une simple application de prédiction vers un système complet d'analyse du marché immobilier béninois.

## 53. ⚠️ Avertissement

Cotonou Immo AI est un projet expérimental et éducatif de Machine Learning.

Les prix retournés par l'application sont des estimations produites par un modèle statistique à partir des données utilisées pour son entraînement.

Ils ne constituent pas :

une expertise immobilière ;
une évaluation officielle ;
une garantie de prix de vente ;
une estimation notariale.

La précision du système dépend notamment de la qualité, de la quantité et de la représentativité des données utilisées.

## 54. 👨‍💻 Auteur

Amen QUENUM

Projet personnel réalisé dans le cadre de l'apprentissage et de la pratique du :

# 🐍 Python
# 📊 Data Science
# 🤖 Machine Learning
# ⚡ FastAPI
# 🎨 Streamlit
# 🚀 MLOps
# ⭐ Conclusion

Cotonou Immo AI constitue une première implémentation complète d'un projet de Machine Learning appliqué à un problème concret.

Le projet ne se limite pas à l'entraînement d'un modèle.

Il couvre l'ensemble d'un petit pipeline :

                    DATA
                     │
                     ▼
             🧹 PREPROCESSING
                     │
                     ▼
              🧠 MACHINE LEARNING
                     │
                     ▼
               📊 EVALUATION
                     │
                     ▼
                💾 MODEL
                     │
                     ▼
                 ⚡ API
                     │
                     ▼
              🎨 STREAMLIT
                     │
                     ▼
             💰 PREDICTION
                     │
                     ▼
          📊 ANALYTICS & HISTORY

Le modèle actuel constitue une baseline qui pourra être améliorée avec davantage de données, de nouvelles variables, de meilleurs modèles et une infrastructure MLOps complète.

# 🚀 Cotonou Immo AI

## From data → to model → to API → to application. 🇧🇯🤖
