# -*- coding: utf-8 -*-
"""
Script d'initialisation des données d'exemple
Auteur: Batoul ZORKOT & Laure Charmille
Date: 2025
"""

import pandas as pd
from datetime import datetime, timedelta
import os
import random

# Créer le dossier data
os.makedirs('data', exist_ok=True)


def creer_habitudes_exemple():
    """Crée des habitudes d'exemple"""
    habitudes = pd.DataFrame({
        'id': [
            'habit_001', 'habit_002', 'habit_003',
            'habit_004', 'habit_005', 'habit_006', 'habit_007'
        ],
        'nom': [
            'Trier mes déchets', 'Boire 2L d\'eau', 'Méditer 10 minutes',
            'Lire 30 minutes', 'Faire du sport', 'Composter',
            'Écrire dans mon journal'
        ],
        'categorie': [
            'Écologie', 'Santé', 'Personnel',
            'Personnel', 'Santé', 'Écologie', 'Personnel'
        ],
        'icone': ['♻️', '💧', '🧘', '📚', '🏃', '🌱', '📝'],
        'description': [
            'Séparer plastique, verre, papier et compost',
            'Rester hydraté tout au long de la journée',
            'Pratiquer la méditation pour réduire le stress',
            'Lire un livre pour s\'enrichir intellectuellement',
            'Faire au moins 30 minutes d\'exercice',
            'Mettre les déchets organiques au compost',
            'Tenir un journal de gratitude'
        ],
        'date_creation': [datetime.now() - timedelta(days=30)] * 7
    })
    
    return habitudes


def creer_historique_exemple():
    """Crée un historique d'exemple sur 30 jours"""
    habitudes_ids = [
        'habit_001', 'habit_002', 'habit_003',
        'habit_004', 'habit_005', 'habit_006', 'habit_007'
    ]
    
    historique = []
    
    for jour in range(30):
        date = datetime.now() - timedelta(days=30-jour)
        
        for habit_id in habitudes_ids:
            proba = random.uniform(0.5, 0.95)
            
            if random.random() < proba:
                historique.append({
                    'date': date,
                    'habitude_id': habit_id,
                    'note': ''
                })
    
    return pd.DataFrame(historique)


def creer_points_compost():
    """Crée des points de compost exemple"""
    points = pd.DataFrame({
        'nom': ['Point Compost Central', 'Jardin Partagé Nord', 'Compost Sud'],
        'adresse': ['123 Rue Verte 75001 Paris', '45 Avenue Bio 75002 Paris', '78 Bd Écolo 75013 Paris'],
        'latitude': [48.8566, 48.8606, 48.8320],
        'longitude': [2.3522, 2.3376, 2.3570],
        'quartier': ['Centre', 'Nord', 'Sud'],
        'horaires': ['Lun-Dim 8h-20h', 'Mar-Sam 9h-18h', 'Lun-Ven 7h-19h'],
        'contact': ['01 23 45 67 89', '01 98 76 54 32', '01 55 66 77 88'],
        'ouvert': [True, True, True]
    })
    
    return points


def initialiser_donnees():
    """Initialise toutes les données d'exemple"""
    print("🌱 HabitTrack Green - Initialisation des données")
    print("=" * 60)
    
    # 1. Habitudes
    print("\n📝 Création des habitudes d'exemple...")
    habitudes = creer_habitudes_exemple()
    habitudes.to_csv('data/habitudes.csv', index=False, encoding='utf-8')
    print(f"✅ {len(habitudes)} habitudes créées")
    
    # 2. Historique
    print("\n📊 Création de l'historique (30 jours)...")
    historique = creer_historique_exemple()
    historique.to_csv('data/historique.csv', index=False, encoding='utf-8')
    print(f"✅ {len(historique)} complétions créées")
    
    # 3. Points de compost
    print("\n🗺️ Création des points de compost...")
    points = creer_points_compost()
    points.to_csv('data/points_compost.csv', index=False, encoding='utf-8')
    print(f"✅ {len(points)} points créés")
    
    # 4. Feedback vide
    print("\n💬 Création du fichier feedback...")
    feedback = pd.DataFrame(columns=['date', 'nom', 'email', 'note', 'commentaire'])
    feedback.to_csv('data/feedback.csv', index=False, encoding='utf-8')
    print("✅ Fichier feedback créé")
    
    print("\n" + "=" * 60)
    print("🎉 Initialisation terminée !")
    print("\n🚀 Pour démarrer l'application :")
    print("   streamlit run app.py")


if __name__ == "__main__":
    try:
        initialiser_donnees()
    except Exception as e:
        print(f"❌ Erreur : {e}")