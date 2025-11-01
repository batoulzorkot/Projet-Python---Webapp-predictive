# -*- coding: utf-8 -*-
"""
Configuration centralisée de l'application HabitTrack Green
Auteur: Batoul Zorkot & Laure Charmille
Date: 2025
"""

import os
from datetime import datetime

# === CHEMINS DE FICHIERS ===
DATA_DIR = 'data'

PATH_HABITUDES = os.path.join(DATA_DIR, 'habitudes.csv')
PATH_HISTORIQUE = os.path.join(DATA_DIR, 'historique.csv')
PATH_COMPOST = os.path.join(DATA_DIR, 'points_compost.csv')
PATH_FEEDBACK = os.path.join(DATA_DIR, 'feedback.csv')

# === CATÉGORIES ===
CATEGORIES = ["Écologie", "Santé", "Personnel", "Travail", "Social"]

CATEGORIES_COLORS = {
    "Écologie": "vert_sauge",
    "Santé": "corail",
    "Personnel": "bleu_ciel",
    "Travail": "lilas",
    "Social": "rose"
}

CATEGORIES_ICONES = {
    "Écologie": "🌱",
    "Santé": "💪",
    "Personnel": "✨",
    "Travail": "💼",
    "Social": "👥"
}

# === PALETTE DE COULEURS ===
COLORS = {
    'vert_sauge': {
        'main': '#A8BF9A',
        'light': '#D7E3D0',
        'dark': '#5E7C53'
    },
    'corail': {
        'main': '#E8754F',
        'light': '#F6C3B1',
        'dark': '#A34B2E'
    },
    'bleu_ciel': {
        'main': '#87CEEB',
        'light': '#D4F1F9',
        'dark': '#4F92B2'
    },
    'lilas': {
        'main': '#C8B6D3',
        'light': '#E9E0ED',
        'dark': '#8E739F'
    },
    'rose': {
        'main': '#F4C3C2',
        'light': '#FDECEC',
        'dark': '#D88A89'
    },
    'beige': {
        'main': '#F5F1E8',
        'light': '#FAF9F6',
        'dark': '#E8DCC8'
    }
}

# === INFORMATIONS APPLICATION ===
APP_INFO = {
    'name': 'HabitTrack Green',
    'version': '1.0.0',
    'description': 'Ton compagnon quotidien pour développer des habitudes positives et durables',
    'authors': ['Votre Nom', 'Nom du Binôme'],
    'email': 'votre.email@exemple.com',
    'year': datetime.now().year
}