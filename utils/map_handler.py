# -*- coding: utf-8 -*-
"""
Module de gestion des points de compost
"""

import streamlit as st
import pandas as pd
import os
import sys

# Ajouter le dossier parent au path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import absolu
from utils.config import PATH_COMPOST, DATA_DIR


def charger_points_compost():
    """Charge les points de compost"""
    try:
        if not os.path.exists(PATH_COMPOST):
            df = pd.DataFrame({
                'nom': ['Point Compost Central', 'Jardin Partagé Nord'],
                'adresse': ['123 Rue Verte 75001 Paris', '45 Avenue Bio 75002 Paris'],
                'latitude': [48.8566, 48.8606],
                'longitude': [2.3522, 2.3376],
                'quartier': ['Centre', 'Nord'],
                'horaires': ['Lun-Dim 8h-20h', 'Mar-Sam 9h-18h'],
                'contact': ['01 23 45 67 89', '01 98 76 54 32'],
                'ouvert': [True, True]
            })
            
            os.makedirs(DATA_DIR, exist_ok=True)
            df.to_csv(PATH_COMPOST, index=False, encoding='utf-8')
            return df
        
        df = pd.read_csv(PATH_COMPOST, encoding='utf-8')
        return df
        
    except Exception as e:
        st.error(f"Erreur : {e}")
        return pd.DataFrame(columns=[
            'nom', 'adresse', 'latitude', 'longitude', 
            'quartier', 'horaires', 'contact', 'ouvert'
        ])