# -*- coding: utf-8 -*-
"""
HabitTrack Green - Page d'Accueil
Application de suivi d'habitudes avec focus écologique

Auteur: Batoul ZORKOT & Laure Charmille
Date: 2025
Version: 1.0.0
"""

import streamlit as st
from datetime import datetime
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from utils.styles import get_custom_css, COLORS, get_gradient

# Configuration
st.set_page_config(
    page_title="HabitTrack Green",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown(get_custom_css(), unsafe_allow_html=True)

# === HEADER ===
st.markdown(f"""
<div style="text-align: center; padding: 40px 20px;">
    <h1 style="font-size: 4em; margin: 0; color: {COLORS['vert_sauge']['dark']};">
        🌱 HabitTrack Green
    </h1>
    <p style="font-size: 1.5em; color: {COLORS['vert_sauge']['main']}; margin-top: 10px;">
        Transforme tes habitudes, transforme ta vie
    </p>
</div>
""", unsafe_allow_html=True)

st.divider()

# === BIENVENUE ===
st.markdown(f"""
<div style="background: {get_gradient('vert_sauge')};
            padding: 50px;
            border-radius: 20px;
            text-align: center;
            color: white;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            margin: 30px 0;">
    <h2 style="color: white; font-size: 2.5em; margin-bottom: 20px;">
        Bienvenue sur HabitTrack Green ! 🌿
    </h2>
    <p style="font-size: 1.3em; line-height: 1.8; max-width: 800px; margin: 0 auto;">
        Ton compagnon quotidien pour développer des habitudes positives et durables.
        Que ce soit pour ta santé, ton bien-être ou l'environnement, 
        <strong>chaque petit pas compte</strong> ! 💚
    </p>
</div>
""", unsafe_allow_html=True)

st.divider()

# === FONCTIONNALITÉS ===
st.markdown("## ✨ Fonctionnalités Principales")

col1, col2 = st.columns(2)

with col1:
    st.markdown(f"""
    <div style="background: white;
                padding: 30px;
                border-radius: 15px;
                border-left: 5px solid {COLORS['vert_sauge']['main']};
                box-shadow: 0 4px 8px rgba(0,0,0,0.1);
                margin: 20px 0;
                min-height: 200px;">
        <h3 style="color: {COLORS['vert_sauge']['dark']};">📊 Dashboard Intelligent</h3>
        <p style="font-size: 1.1em; color: #555; line-height: 1.6;">
            Visualise ta progression avec des statistiques détaillées et des graphiques clairs.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div style="background: white;
                padding: 30px;
                border-radius: 15px;
                border-left: 5px solid {COLORS['corail']['main']};
                box-shadow: 0 4px 8px rgba(0,0,0,0.1);
                margin: 20px 0;
                min-height: 200px;">
        <h3 style="color: {COLORS['corail']['dark']};">✅ Tracking Quotidien</h3>
        <p style="font-size: 1.1em; color: #555; line-height: 1.6;">
            Suivi simple et rapide avec streaks pour maintenir ta motivation !
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div style="background: white;
                padding: 30px;
                border-radius: 15px;
                border-left: 5px solid {COLORS['bleu_ciel']['main']};
                box-shadow: 0 4px 8px rgba(0,0,0,0.1);
                margin: 20px 0;
                min-height: 200px;">
        <h3 style="color: {COLORS['bleu_ciel']['dark']};">🗺️ Carte Éco</h3>
        <p style="font-size: 1.1em; color: #555; line-height: 1.6;">
            Découvre les points de compost près de chez toi avec notre carte interactive.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div style="background: white;
                padding: 30px;
                border-radius: 15px;
                border-left: 5px solid {COLORS['lilas']['main']};
                box-shadow: 0 4px 8px rgba(0,0,0,0.1);
                margin: 20px 0;
                min-height: 200px;">
        <h3 style="color: {COLORS['lilas']['dark']};">⚙️ Personnalisation</h3>
        <p style="font-size: 1.1em; color: #555; line-height: 1.6;">
            Crée et gère tes habitudes selon tes besoins.
        </p>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# === COMMENT COMMENCER ===
st.markdown("## 🚀 Comment Commencer ?")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
    <div style="background: {get_gradient('rose')};
                padding: 30px;
                border-radius: 15px;
                text-align: center;
                color: white;
                box-shadow: 0 4px 8px rgba(0,0,0,0.1);
                min-height: 280px;">
        <div style="font-size: 3em; margin-bottom: 15px;">1️⃣</div>
        <h3 style="color: white; margin-bottom: 10px;">Crée tes habitudes</h3>
        <p style="opacity: 0.9;">
            Va dans <strong>Paramètres</strong> et ajoute les habitudes que tu veux développer.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div style="background: {get_gradient('corail')};
                padding: 30px;
                border-radius: 15px;
                text-align: center;
                color: white;
                box-shadow: 0 4px 8px rgba(0,0,0,0.1);
                min-height: 280px;">
        <div style="font-size: 3em; margin-bottom: 15px;">2️⃣</div>
        <h3 style="color: white; margin-bottom: 10px;">Track quotidiennement</h3>
        <p style="opacity: 0.9;">
            Chaque jour, coche tes habitudes dans <strong>Tracking</strong>.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div style="background: {get_gradient('vert_sauge')};
                padding: 30px;
                border-radius: 15px;
                text-align: center;
                color: white;
                box-shadow: 0 4px 8px rgba(0,0,0,0.1);
                min-height: 280px;">
        <div style="font-size: 3em; margin-bottom: 15px;">3️⃣</div>
        <h3 style="color: white; margin-bottom: 10px;">Suis ta progression</h3>
        <p style="opacity: 0.9;">
            Consulte ton <strong>Dashboard</strong> pour voir ton évolution !
        </p>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# === CITATION ===
st.markdown(f"""
<div style="background: {get_gradient('bleu_ciel')};
            padding: 40px;
            border-radius: 20px;
            text-align: center;
            color: white;
            margin: 30px 0;
            box-shadow: 0 6px 12px rgba(0,0,0,0.1);">
    <p style="font-size: 1.8em; font-style: italic; margin: 0; line-height: 1.6;">
        "Nous sommes ce que nous répétons chaque jour.<br>
        L'excellence n'est donc pas un acte, mais une habitude."
    </p>
    <p style="font-size: 1.2em; margin-top: 20px; opacity: 0.9;">— Aristote</p>
</div>
""", unsafe_allow_html=True)

st.divider()

# === APPEL À L'ACTION ===
st.markdown(f"""
<div style="text-align: center; padding: 40px 20px;">
    <h2 style="color: {COLORS['vert_sauge']['dark']}; font-size: 2.5em; margin-bottom: 20px;">
        Prêt à commencer ton voyage ? 🌟
    </h2>
    <p style="font-size: 1.3em; color: #666; margin-bottom: 30px;">
        Utilise le menu à gauche pour naviguer dans l'application
    </p>
</div>
""", unsafe_allow_html=True)

st.divider()

# === POURQUOI HABITTRACK GREEN ===
st.markdown("## 💡 Pourquoi Choisir HabitTrack Green ?")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
    <div style="background: white;
                padding: 25px;
                border-radius: 12px;
                border-top: 4px solid {COLORS['vert_sauge']['main']};
                box-shadow: 0 2px 6px rgba(0,0,0,0.08);
                text-align: center;
                min-height: 220px;">
        <div style="font-size: 3em; margin-bottom: 15px;">🎯</div>
        <h4 style="color: {COLORS['vert_sauge']['dark']};">Simple & Efficace</h4>
        <p style="color: #666; font-size: 0.95em; line-height: 1.6;">
            Interface intuitive pour te concentrer sur l'essentiel
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div style="background: white;
                padding: 25px;
                border-radius: 12px;
                border-top: 4px solid {COLORS['corail']['main']};
                box-shadow: 0 2px 6px rgba(0,0,0,0.08);
                text-align: center;
                min-height: 220px;">
        <div style="font-size: 3em; margin-bottom: 15px;">📈</div>
        <h4 style="color: {COLORS['corail']['dark']};">Suivi Motivant</h4>
        <p style="color: #666; font-size: 0.95em; line-height: 1.6;">
            Streaks et stats pour maintenir ta motivation
        </p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div style="background: white;
                padding: 25px;
                border-radius: 12px;
                border-top: 4px solid {COLORS['bleu_ciel']['main']};
                box-shadow: 0 2px 6px rgba(0,0,0,0.08);
                text-align: center;
                min-height: 220px;">
        <div style="font-size: 3em; margin-bottom: 15px;">🌍</div>
        <h4 style="color: {COLORS['bleu_ciel']['dark']};">Focus Écologie</h4>
        <p style="color: #666; font-size: 0.95em; line-height: 1.6;">
            Guide du compostage pour agir concrètement
        </p>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# === CONSEIL ===
st.markdown(f"""
<div style="background: {get_gradient('beige')};
            padding: 30px;
            border-radius: 15px;
            border-left: 5px solid {COLORS['vert_sauge']['main']};">
    <h3 style="color: {COLORS['vert_sauge']['dark']};">💡 Conseil du jour</h3>
    <p style="font-size: 1.1em; color: #555; line-height: 1.7;">
        <strong>Commence petit !</strong> Il vaut mieux tracker 3 habitudes régulièrement 
        que d'en avoir 10 et de tout abandonner. 🌱
    </p>
</div>
""", unsafe_allow_html=True)

st.divider()

# === FOOTER ===
st.markdown(f"""
<div style="text-align: center; padding: 30px 20px; color: #888;">
    <p style="font-size: 1.1em;">💚 Fait avec amour pour la planète</p>
    <p style="font-size: 0.9em; opacity: 0.8;">
        HabitTrack Green © {datetime.now().year} • Version 1.0.0
    </p>
</div>
""", unsafe_allow_html=True)