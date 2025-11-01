# -*- coding: utf-8 -*-
"""
Tracking - HabitTrack Green
Suivi quotidien des habitudes

Auteur: Batoul ZORKOT & Laure Charmille
Date: 2025
"""

import streamlit as st
import pandas as pd
from datetime import datetime
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from utils.habit_manager import charger_habitudes, charger_historique, sauvegarder_historique
from utils.stats_calculator import calculer_streak
from utils.styles import get_custom_css, COLORS, get_gradient

st.set_page_config(
    page_title="Tracking - HabitTrack Green",
    page_icon="✅",
    layout="wide"
)

st.markdown(get_custom_css(), unsafe_allow_html=True)

# === HEADER ===
st.title("✅ Tracking Quotidien")
st.write(f"📅 {datetime.now().strftime('%A %d %B %Y')}")
st.divider()

# Charger les données
habitudes = charger_habitudes()
historique = charger_historique()

if len(habitudes) == 0:
    st.warning("⚠️ Aucune habitude à tracker. Va dans 'Paramètres' pour en créer !")
    st.stop()

# Grouper par catégorie
categories = habitudes['categorie'].unique()

# Calculer les stats du jour
aujourd_hui = datetime.now().date()
historique_aujourdhui = historique[historique['date'].dt.date == aujourd_hui]
completions_aujourdhui = len(historique_aujourdhui)
pourcentage_jour = int((completions_aujourdhui / len(habitudes)) * 100) if len(habitudes) > 0 else 0

# === MESSAGE DU JOUR ===
if completions_aujourdhui == 0:
    message = "🚀 C'est parti !"
    desc = "Commence ta journée du bon pied ! 💜"
    couleur = get_gradient('lilas')
elif pourcentage_jour < 50:
    message = "🌱 Bien commencé !"
    desc = "Allez, encore un petit effort ! 💙"
    couleur = get_gradient('bleu_ciel')
elif pourcentage_jour < 100:
    message = "💚 Très Bon Travail !"
    desc = "Tu es sur la bonne voie ! 🚀"
    couleur = get_gradient('vert_sauge')
else:
    message = "🌟 Journée Parfaite !"
    desc = "Tu as tout complété ! Champion ! 🎉"
    couleur = get_gradient('corail')

st.markdown(f"""
<div style="background: {couleur};
            padding: 40px;
            border-radius: 20px;
            text-align: center;
            color: white;
            box-shadow: 0 8px 16px rgba(0,0,0,0.2);
            margin-bottom: 30px;">
    <h1 style="color: white; margin: 0; font-size: 2.5em;">{message}</h1>
    <p style="font-size: 1.3em; margin: 15px 0; opacity: 0.95;">{desc}</p>
    <p style="font-size: 1.1em; margin-top: 20px; opacity: 0.9;">
        ✅ <strong>{completions_aujourdhui}/{len(habitudes)}</strong> habitudes complétées • 
        📊 <strong>{pourcentage_jour}%</strong> de progression
    </p>
</div>
""", unsafe_allow_html=True)

st.divider()

# === TRACKING PAR CATÉGORIE ===
for categorie in sorted(categories):
    habitudes_cat = habitudes[habitudes['categorie'] == categorie]
    
    couleur_cat = {
        "Écologie": "vert_sauge",
        "Santé": "corail",
        "Personnel": "bleu_ciel",
        "Travail": "lilas",
        "Social": "rose"
    }.get(categorie, "beige")
    
    with st.expander(f"{categorie} ({len(habitudes_cat)} habitudes)", expanded=True):
        for _, habitude in habitudes_cat.iterrows():
            col1, col2, col3 = st.columns([3, 1, 1])
            
            with col1:
                # Vérifier si déjà complétée aujourd'hui
                deja_complete = len(historique[
                    (historique['habitude_id'] == habitude['id']) &
                    (historique['date'].dt.date == aujourd_hui)
                ]) > 0
                
                checked = st.checkbox(
                    f"{habitude['icone']} **{habitude['nom']}**",
                    value=deja_complete,
                    key=f"check_{habitude['id']}"
                )
                
                # Sauvegarder
                if checked and not deja_complete:
                    nouvelle_entree = pd.DataFrame({
                        'date': [datetime.now()],
                        'habitude_id': [habitude['id']],
                        'note': ['']
                    })
                    historique = pd.concat([historique, nouvelle_entree], ignore_index=True)
                    sauvegarder_historique(historique)
                    st.rerun()
                
                elif not checked and deja_complete:
                    historique = historique[
                        ~((historique['habitude_id'] == habitude['id']) &
                          (historique['date'].dt.date == aujourd_hui))
                    ]
                    sauvegarder_historique(historique)
                    st.rerun()
            
            with col2:
                streak = calculer_streak(habitude['id'], historique)
                if streak > 0:
                    st.markdown(f"""
                    <div style="background: {get_gradient('corail')};
                                color: white;
                                padding: 10px;
                                border-radius: 10px;
                                text-align: center;
                                font-weight: bold;">
                        🔥 {streak} jours
                    </div>
                    """, unsafe_allow_html=True)
            
            with col3:
                total = len(historique[historique['habitude_id'] == habitude['id']])
                st.markdown(f"""
                <div style="background: {get_gradient(couleur_cat)};
                            color: white;
                            padding: 10px;
                            border-radius: 10px;
                            text-align: center;
                            font-weight: bold;">
                    ✅ {total}
                </div>
                """, unsafe_allow_html=True)

st.divider()

# === GUIDE COMPOSTAGE ===
st.markdown("## 🌱 Guide du Compostage")

with st.expander("📖 Tout savoir sur le compostage"):
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"""
        <div style="background: white;
                    padding: 20px;
                    border-radius: 12px;
                    border-left: 5px solid {COLORS['vert_sauge']['main']};
                    box-shadow: 0 2px 6px rgba(0,0,0,0.08);">
            <h4 style="color: {COLORS['vert_sauge']['dark']};">✅ À Composter</h4>
            <ul style="color: #555; line-height: 1.8;">
                <li>🥕 Épluchures de fruits et légumes</li>
                <li>☕ Marc de café et sachets de thé</li>
                <li>🥚 Coquilles d'œufs écrasées</li>
                <li>🍞 Pain rassis (en petits morceaux)</li>
                <li>🌿 Fleurs fanées</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div style="background: white;
                    padding: 20px;
                    border-radius: 12px;
                    border-left: 5px solid {COLORS['corail']['main']};
                    box-shadow: 0 2px 6px rgba(0,0,0,0.08);">
            <h4 style="color: {COLORS['corail']['dark']};">❌ À Éviter</h4>
            <ul style="color: #555; line-height: 1.8;">
                <li>🥩 Viande et poisson</li>
                <li>🧀 Produits laitiers</li>
                <li>🍟 Aliments gras ou huileux</li>
                <li>🦴 Os</li>
                <li>🐱 Litière d'animaux</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

st.divider()

# === FOOTER ===
st.markdown(f"""
<div style="text-align: center; padding: 20px; color: #666;">
    <p style="font-size: 1em;">
        💪 Continue comme ça, tu es sur la bonne voie !
    </p>
</div>
""", unsafe_allow_html=True)