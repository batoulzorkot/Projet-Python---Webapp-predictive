# -*- coding: utf-8 -*-
"""
Module de gestion des données
"""

import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import os
import sys

# Ajouter le dossier parent au path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import absolu
from utils.config import (
    PATH_HABITUDES, 
    PATH_HISTORIQUE, 
    PATH_FEEDBACK,
    DATA_DIR
)

os.makedirs(DATA_DIR, exist_ok=True)


def charger_habitudes():
    """Charge les habitudes"""
    try:
        if not os.path.exists(PATH_HABITUDES):
            df = pd.DataFrame(columns=[
                'id', 'nom', 'categorie', 'icone', 'description', 'date_creation'
            ])
            df.to_csv(PATH_HABITUDES, index=False, encoding='utf-8')
            return df
        
        df = pd.read_csv(PATH_HABITUDES, encoding='utf-8')
        if 'date_creation' in df.columns and len(df) > 0:
            df['date_creation'] = pd.to_datetime(df['date_creation'])
        return df
        
    except Exception as e:
        st.error(f"Erreur : {e}")
        return pd.DataFrame(columns=[
            'id', 'nom', 'categorie', 'icone', 'description', 'date_creation'
        ])


def sauvegarder_habitudes(df):
    """Sauvegarde les habitudes"""
    try:
        df.to_csv(PATH_HABITUDES, index=False, encoding='utf-8')
        return True
    except Exception as e:
        st.error(f"Erreur : {e}")
        return False


def charger_historique():
    """Charge l'historique"""
    try:
        if not os.path.exists(PATH_HISTORIQUE):
            df = pd.DataFrame(columns=['date', 'habitude_id', 'note'])
            df.to_csv(PATH_HISTORIQUE, index=False, encoding='utf-8')
            return df
        
        df = pd.read_csv(PATH_HISTORIQUE, encoding='utf-8')
        if 'date' in df.columns and len(df) > 0:
            df['date'] = pd.to_datetime(df['date'])
        return df
        
    except Exception as e:
        st.error(f"Erreur : {e}")
        return pd.DataFrame(columns=['date', 'habitude_id', 'note'])


def sauvegarder_historique(df):
    """Sauvegarde l'historique"""
    try:
        df.to_csv(PATH_HISTORIQUE, index=False, encoding='utf-8')
        return True
    except Exception as e:
        st.error(f"Erreur : {e}")
        return False


def charger_feedback():
    """Charge les feedbacks"""
    try:
        if not os.path.exists(PATH_FEEDBACK):
            df = pd.DataFrame(columns=['date', 'nom', 'email', 'note', 'commentaire'])
            df.to_csv(PATH_FEEDBACK, index=False, encoding='utf-8')
            return df
        
        df = pd.read_csv(PATH_FEEDBACK, encoding='utf-8')
        if 'date' in df.columns and len(df) > 0:
            df['date'] = pd.to_datetime(df['date'])
        return df
        
    except Exception as e:
        st.error(f"Erreur : {e}")
        return pd.DataFrame(columns=['date', 'nom', 'email', 'note', 'commentaire'])


def sauvegarder_feedback(nom, email, note, commentaire):
    """Sauvegarde un feedback"""
    try:
        df = charger_feedback()
        
        nouveau_feedback = pd.DataFrame({
            'date': [datetime.now()],
            'nom': [nom],
            'email': [email],
            'note': [note],
            'commentaire': [commentaire]
        })
        
        df = pd.concat([df, nouveau_feedback], ignore_index=True)
        df.to_csv(PATH_FEEDBACK, index=False, encoding='utf-8')
        return True
        
    except Exception as e:
        st.error(f"Erreur : {e}")
        return False


def generer_id():
    """Génère un ID unique"""
    return f"habit_{datetime.now().strftime('%Y%m%d_%H%M%S')}"


def obtenir_statistiques_globales():
    """Calcule des statistiques globales"""
    try:
        habitudes = charger_habitudes()
        historique = charger_historique()
        
        aujourd_hui = datetime.now().date()
        il_y_a_7j = aujourd_hui - timedelta(days=7)
        
        total_habitudes = len(habitudes)
        total_completions = len(historique)
        
        if len(historique) > 0:
            historique_recent = historique[historique['date'].dt.date >= il_y_a_7j]
            habitudes_actives = historique_recent['habitude_id'].nunique()
        else:
            habitudes_actives = 0
        
        return {
            'total_habitudes': total_habitudes,
            'total_completions': total_completions,
            'habitudes_actives_7j': habitudes_actives
        }
        
    except:
        return {
            'total_habitudes': 0,
            'total_completions': 0,
            'habitudes_actives_7j': 0
        }