# -*- coding: utf-8 -*-
"""
Retour Utilisateur - HabitTrack Green
Feedback et contact

Auteur: Batoul ZORKOT & Laure Charmille
Date: 2025
"""

import streamlit as st
from datetime import datetime
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from utils.styles import get_custom_css, COLORS, get_gradient
from utils.habit_manager import sauvegarder_feedback

st.set_page_config(
    page_title="Retour Utilisateur - HabitTrack Green",
    page_icon="💬",
    layout="wide"
)

st.markdown(get_custom_css(), unsafe_allow_html=True)

# === HEADER ===
st.title("💬 Retour Utilisateur")
st.write("Votre avis compte pour nous !")
st.divider()

# === FEEDBACK ===
st.markdown("## 💬 Votre Avis Nous Intéresse !")
st.write("Aidez-nous à améliorer HabitTrack Green.")

with st.form("feedback_form", clear_on_submit=True):
    
    col1, col2 = st.columns(2)
    
    with col1:
        nom = st.text_input("📝 Nom (optionnel)", placeholder="Votre nom")
    
    with col2:
        email = st.text_input("📧 Email (optionnel)", placeholder="votre@email.com")
    
    note_options = ["⭐", "⭐⭐", "⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"]
    note_str = st.radio(
        "Notez l'application :",
        options=note_options,
        index=4,
        horizontal=True,
        help="5 étoiles = Excellent !"
    )
    
    commentaire = st.text_area(
        "Laissez un commentaire :",
        placeholder="Vos suggestions, les bugs rencontrés, ce que vous aimez...",
        height=150
    )
    
    submitted = st.form_submit_button(
        "Envoyer mon avis", 
        use_container_width=True,
        type="primary"
    )
    
    if submitted:
        if commentaire:
            note_value = len(note_str)
            
            if sauvegarder_feedback(nom if nom else "Anonyme", email if email else "Non renseigné", note_value, commentaire):
                st.success("Merci ! Votre avis a bien été envoyé. 🎉")
                st.balloons()
        else:
            st.warning("Veuillez laisser un commentaire avant d'envoyer.")

st.divider()

# === CONTACT ===
st.markdown("## 📞 Contact & Support")
st.write("Une question ? Une suggestion ? Contactez-nous !")

col1, col2 = st.columns(2)

with col1:
    st.markdown(f"""
    <div style="background: {get_gradient('bleu_ciel')};
                padding: 30px;
                border-radius: 15px;
                text-align: center;
                color: white;">
        <div style="font-size: 3em; margin-bottom: 15px;">👨‍💻</div>
        <h3 style="color: white;">Développeurs</h3>
        <p style="font-size: 1.1em; opacity: 0.95;">[VOS NOMS ICI]</p>
        <p style="font-size: 1em; opacity: 0.9;">[votre.email@exemple.com]</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div style="background: {get_gradient('lilas')};
                padding: 30px;
                border-radius: 15px;
                text-align: center;
                color: white;">
        <div style="font-size: 3em; margin-bottom: 15px;">💻</div>
        <h3 style="color: white;">Code Source</h3>
        <p style="font-size: 1.1em; opacity: 0.95;">Retrouvez ce projet sur GitHub</p>
        <p style="font-size: 1em; opacity: 0.9;">[github.com/votre-username]</p>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# === OBJECTIF ===
st.markdown("## 🎯 Pourquoi HabitTrack Green ?")

st.markdown(f"""
<div style="background: white;
            padding: 30px;
            border-radius: 15px;
            border-left: 5px solid {COLORS['vert_sauge']['main']};
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
    <h3 style="color: {COLORS['vert_sauge']['dark']};">Notre Mission</h3>
    <p style="font-size: 1.1em; line-height: 1.8; color: #555;">
        Dans un monde où il est difficile de maintenir de bonnes habitudes, 
        <strong>HabitTrack Green</strong> a été créé pour vous aider à :
    </p>
    <ul style="font-size: 1.05em; line-height: 2; color: #555;">
        <li>📊 <strong>Suivre vos habitudes</strong> quotidiennement</li>
        <li>📈 <strong>Visualiser votre progression</strong> avec des statistiques claires</li>
        <li>🔥 <strong>Maintenir votre motivation</strong> grâce aux streaks</li>
        <li>🌍 <strong>Agir pour la planète</strong> avec le guide du compostage</li>
    </ul>
</div>
""", unsafe_allow_html=True)

st.divider()

# === AMÉLIORATIONS FUTURES ===
st.markdown("## 🚀 Pistes d'Amélioration Futures")

st.markdown(f"""
<div style="background: white;
            padding: 30px;
            border-radius: 15px;
            border-left: 5px solid {COLORS['bleu_ciel']['main']};
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
    <h3 style="color: {COLORS['bleu_ciel']['dark']};">Ce qui pourrait arriver...</h3>
    <ul style="font-size: 1.05em; line-height: 2; color: #555;">
        <li>👤 <strong>Comptes utilisateurs :</strong> Pour sauvegarder vos données en ligne</li>
        <li>🔔 <strong>Notifications :</strong> Des rappels pour ne jamais oublier une habitude</li>
        <li>🏆 <strong>Plus d'Achievements :</strong> Pour gamifier encore plus l'expérience</li>
        <li>🌦️ <strong>API Météo :</strong> Suggérer des habitudes éco en fonction du temps</li>
        <li>📱 <strong>Application mobile :</strong> Pour tracker en déplacement</li>
    </ul>
</div>
""", unsafe_allow_html=True)

st.divider()

st.markdown(f"""
<div style="text-align: center; padding: 20px; color: #666;">
    <p>💚 Merci pour votre contribution !</p>
    <p style="font-size: 0.9em; opacity: 0.8;">Version 1.0.0 • {datetime.now().year}</p>
</div>
""", unsafe_allow_html=True)