# 🌱 HabitTrack Green

> Ton compagnon quotidien pour développer des habitudes positives et durables

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.31-red)
![License](https://img.shields.io/badge/License-Educational-green)

---

## 📋 Table des Matières

- [Aperçu](#-aperçu)
- [Fonctionnalités](#-fonctionnalités)
- [Installation](#-installation)
- [Utilisation](#-utilisation)
- [Architecture](#️-architecture)
- [Technologies](#️-technologies)
- [Auteurs](#-auteurs)

---

## 🎯 Aperçu

**HabitTrack Green** est une application web interactive développée avec Streamlit qui permet de :
- ✅ Suivre vos habitudes quotidiennes
- 📊 Visualiser votre progression avec des statistiques détaillées
- 🔥 Maintenir votre motivation grâce aux streaks
- 🗺️ Trouver des points de compost près de chez vous
- ♻️ Apprendre à composter correctement

### Pourquoi ce projet ?

Dans un monde où il est difficile de maintenir de bonnes habitudes, HabitTrack Green offre une solution simple et visuellement attractive pour vous accompagner dans votre développement personnel, avec un focus particulier sur l'écologie.

---

## ✨ Fonctionnalités

### 📊 Dashboard Intelligent
- Statistiques complètes (taux de réussite, streaks, moyennes)
- Graphiques interactifs de progression sur 30 jours
- Top 3 des habitudes les plus suivies
- Système d'achievements
- Export des données en CSV

### ✅ Tracking Quotidien
- Interface intuitive par catégories
- Calcul automatique des streaks 🔥
- Compteur total de complétions
- Messages motivants selon la progression
- Guide du compostage intégré

### 🗺️ Carte Écologique
- Carte interactive des points de compost (Folium)
- Filtres par ville et statut (ouvert/fermé)
- Itinéraires Google Maps intégrés
- Guide complet du compostage

### ⚙️ Gestion des Habitudes
- Création, modification, suppression d'habitudes
- Catégorisation personnalisable (Écologie, Santé, Personnel, Travail, Social)
- Icônes emoji pour une meilleure visualisation
- Statistiques détaillées par habitude

### 💬 Retour Utilisateur
- Système de notation (1-5 étoiles)
- Formulaire de feedback
- Contact des développeurs
- Pistes d'amélioration futures

---

## 🚀 Installation

### Prérequis
- Python 3.8 ou supérieur
- pip (gestionnaire de paquets Python)

### Étapes d'installation

1. **Cloner le repository**
```bash
git clone https://github.com/votre-username/habittrack-green.git
cd habittrack-green
```

2. **Créer un environnement virtuel (recommandé)**
```bash
python -m venv venv

# Sur Windows
venv\Scripts\activate

# Sur Mac/Linux
source venv/bin/activate
```

3. **Installer les dépendances**
```bash
pip install -r requirements.txt
```

4. **Initialiser les données (optionnel)**
```bash
python init_data.py
```

5. **Lancer l'application**
```bash
streamlit run app.py
```

L'application s'ouvrira automatiquement dans votre navigateur à l'adresse `http://localhost:8501`

---

## 📖 Utilisation

### Premier lancement

1. **Créer vos premières habitudes**
   - Allez dans "Paramètres" (⚙️)
   - Cliquez sur "Ajouter"
   - Remplissez le formulaire (nom, catégorie, icône)

2. **Commencer le tracking**
   - Rendez-vous dans "Tracking" (✅)
   - Cochez les habitudes que vous avez accomplies aujourd'hui

3. **Suivre votre progression**
   - Consultez le "Dashboard" (📊) pour voir vos statistiques
   - Observez vos streaks augmenter !

### Fonctionnalités avancées

- **Export de données** : Téléchargez vos statistiques en CSV depuis le Dashboard
- **Carte des points de compost** : Trouvez le point le plus proche et obtenez l'itinéraire
- **Guide du compostage** : Apprenez ce que vous pouvez composter
- **Feedback** : Donnez votre avis sur l'application

---

## 🏗️ Architecture
```
habittrack-green/
│
├── app.py                      # 🏠 Page d'accueil
│
├── pages/                      # 📄 Pages Streamlit
│   ├── 1_📊_Dashboard.py
│   ├── 2_✅_Tracking.py
│   ├── 3_🗺️_Carte_Eco.py
│   ├── 4_⚙️_Parametres.py
│   └── 5_💬_Retour_Utilisateur.py
│
├── utils/                      # 🔧 Modules utilitaires
│   ├── __init__.py
│   ├── config.py               # Configuration centralisée
│   ├── styles.py               # Styles CSS personnalisés
│   ├── habit_manager.py        # Gestion des habitudes (CRUD)
│   ├── stats_calculator.py     # Calculs statistiques
│   └── map_handler.py          # Gestion de la carte
│
├── data/                       # 💾 Données (CSV)
│   ├── habitudes.csv
│   ├── historique.csv
│   ├── points_compost.csv
│   └── feedback.csv
│
├── init_data.py                # 🔧 Script d'initialisation
├── requirements.txt            # 📦 Dépendances
└── README.md                   # 📖 Ce fichier
```

### Fichiers principaux

- **`app.py`** : Point d'entrée, page d'accueil
- **`pages/`** : Pages multi-pages de Streamlit
- **`utils/habit_manager.py`** : Fonctions CRUD pour les habitudes
- **`utils/stats_calculator.py`** : Calcul des streaks et statistiques
- **`utils/styles.py`** : Palette de couleurs et CSS personnalisé
- **`data/`** : Stockage des données en CSV

---

## 🛠️ Technologies

### Langages & Frameworks
- **Python 3.x** - Langage principal
- **Streamlit** - Framework web interactif
- **HTML/CSS** - Personnalisation du design

### Bibliothèques Python
- **Pandas** - Manipulation et analyse de données
- **Plotly** - Graphiques interactifs
- **Folium** - Cartes interactives (OpenStreetMap)
- **streamlit-folium** - Intégration Folium dans Streamlit

### Gestion des données
- **CSV** - Stockage local des données
- Pas de base de données externe (simplicité et portabilité)

---

## 👥 Auteurs

**[Vos Noms]**
- 👨‍💻 Développeurs : Batoul ZORKOT & Laure Charmille
- 🎓 Étudiants en DU - Sorbonne Data Analytics
- 📧 Email : bbatoulz@outlook.com & lcharmille@gmail.com
- 💻 GitHub : [votre-username]

---

## 🎓 Contexte Académique

Ce projet a été réalisé dans le cadre d'un projet Python avec Streamlit.

**Objectifs pédagogiques :**
- Maîtriser Streamlit pour créer des applications web interactives
- Manipuler des données avec Pandas
- Créer des visualisations avec Plotly
- Intégrer des cartes avec Folium
- Gérer un projet de manière professionnelle (Git, documentation)


<div align="center">

**💚 Fait avec ❤️ pour la planète 🌍**

[⬆ Retour en haut](#-habittrack-green)

</div>