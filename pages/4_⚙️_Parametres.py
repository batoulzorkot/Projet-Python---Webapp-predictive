# -*- coding: utf-8 -*-
"""
Paramètres - HabitTrack Green
Gestion des habitudes

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

from utils.habit_manager import charger_habitudes, sauvegarder_habitudes, generer_id
from utils.styles import get_custom_css, COLORS, get_gradient

st.set_page_config(
    page_title="Paramètres - HabitTrack Green",
    page_icon="⚙️",
    layout="wide"
)

st.markdown(get_custom_css(), unsafe_allow_html=True)

# === HEADER ===
st.title("⚙️ Paramètres & Gestion des Habitudes")
st.divider()

habitudes = charger_habitudes()

# === ONGLETS ===
tab1, tab2, tab3 = st.tabs(["➕ Ajouter", "✏️ Modifier", "📊 Vue d'ensemble"])

# === TAB 1 : AJOUTER ===
with tab1:
    st.markdown("## ➕ Créer une Nouvelle Habitude")
    
    col1, col2 = st.columns(2)
    
    with col1:
        nom = st.text_input("📝 Nom de l'habitude", placeholder="Ex: Méditer 10 minutes")
        
        categorie = st.selectbox(
            "🏷️ Catégorie",
            ["Écologie", "Santé", "Personnel", "Travail", "Social"]
        )
        
        icone = st.text_input("✨ Icône (emoji)", value="🌱", max_chars=2)
    
    with col2:
        description = st.text_area(
            "📄 Description (optionnel)",
            placeholder="Pourquoi cette habitude est importante...",
            height=150
        )
    
    st.divider()
    
    if st.button("➕ Ajouter l'Habitude", type="primary", use_container_width=True):
        if nom:
            nouvelle_habitude = pd.DataFrame({
                'id': [generer_id()],
                'nom': [nom],
                'categorie': [categorie],
                'icone': [icone],
                'description': [description],
                'date_creation': [datetime.now()]
            })
            
            habitudes = pd.concat([habitudes, nouvelle_habitude], ignore_index=True)
            sauvegarder_habitudes(habitudes)
            
            st.success(f"✅ Habitude **{nom}** créée avec succès !")
            st.balloons()
            st.rerun()
        else:
            st.error("❌ Le nom de l'habitude est obligatoire !")

# === TAB 2 : MODIFIER ===
with tab2:
    st.markdown("## ✏️ Modifier ou Supprimer des Habitudes")
    
    if len(habitudes) == 0:
        st.info("🔍 Aucune habitude à modifier. Crée-en une dans l'onglet 'Ajouter' !")
    else:
        for idx, habitude in habitudes.iterrows():
            couleur_cat = {
                "Écologie": "vert_sauge",
                "Santé": "corail",
                "Personnel": "bleu_ciel",
                "Travail": "lilas",
                "Social": "rose"
            }.get(habitude['categorie'], "beige")
            
            with st.expander(f"{habitude['icone']} **{habitude['nom']}** - {habitude['categorie']}", expanded=False):
                col1, col2 = st.columns([3, 1])
                
                with col1:
                    nouveau_nom = st.text_input(
                        "Nom",
                        value=str(habitude['nom']),
                        key=f"nom_{habitude['id']}"
                    )
                    
                    nouvelle_categorie = st.selectbox(
                        "Catégorie",
                        ["Écologie", "Santé", "Personnel", "Travail", "Social"],
                        index=["Écologie", "Santé", "Personnel", "Travail", "Social"].index(habitude['categorie']),
                        key=f"cat_{habitude['id']}"
                    )
                    
                    nouvel_icone = st.text_input(
                        "Icône",
                        value=str(habitude['icone']),
                        key=f"icon_{habitude['id']}",
                        max_chars=2
                    )
                    
                    desc_value = habitude['description'] if pd.notna(habitude['description']) else ""
                    nouvelle_description = st.text_area(
                        "Description",
                        value=str(desc_value),
                        key=f"desc_{habitude['id']}"
                    )
                    
                    col_btn1, col_btn2 = st.columns(2)
                    
                    with col_btn1:
                        if st.button("💾 Sauvegarder", key=f"save_{habitude['id']}", use_container_width=True):
                            habitudes_reload = charger_habitudes()
                            habitudes_reload.loc[habitudes_reload['id'] == habitude['id'], 'nom'] = nouveau_nom
                            habitudes_reload.loc[habitudes_reload['id'] == habitude['id'], 'categorie'] = nouvelle_categorie
                            habitudes_reload.loc[habitudes_reload['id'] == habitude['id'], 'icone'] = nouvel_icone
                            habitudes_reload.loc[habitudes_reload['id'] == habitude['id'], 'description'] = nouvelle_description
                            sauvegarder_habitudes(habitudes_reload)
                            st.success("✅ Modifié !")
                            st.rerun()
                    
                    with col_btn2:
                        if st.button("🗑️ Supprimer", key=f"del_{habitude['id']}", use_container_width=True):
                            habitudes_reload = charger_habitudes()
                            habitudes_reload = habitudes_reload[habitudes_reload['id'] != habitude['id']]
                            sauvegarder_habitudes(habitudes_reload)
                            st.success("🗑️ Supprimé !")
                            st.rerun()
                
                with col2:
                    st.markdown(f"""
                    <div style="background: {get_gradient(couleur_cat)};
                                padding: 20px;
                                border-radius: 15px;
                                text-align: center;
                                color: white;
                                height: 100%;
                                display: flex;
                                flex-direction: column;
                                justify-content: center;">
                        <div style="font-size: 3em; margin-bottom: 10px;">{habitude['icone']}</div>
                        <strong style="font-size: 1.1em;">{habitude['nom']}</strong><br>
                        <small style="opacity: 0.9; margin-top: 5px;">{habitude['categorie']}</small>
                    </div>
                    """, unsafe_allow_html=True)

# === TAB 3 : VUE D'ENSEMBLE ===
with tab3:
    st.markdown("## 📊 Vue d'Ensemble de tes Habitudes")
    
    if len(habitudes) == 0:
        st.info("🔍 Aucune habitude enregistrée.")
    else:
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown(f"""
            <div style="background: {get_gradient('vert_sauge')};
                        padding: 25px;
                        border-radius: 15px;
                        text-align: center;
                        color: white;">
                <div style="font-size: 0.9em; opacity: 0.9; margin-bottom: 10px;">Total d'habitudes</div>
                <div style="font-size: 3em; font-weight: bold; margin: 10px 0;">{len(habitudes)}</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            categories = habitudes['categorie'].value_counts()
            cat_principale = categories.index[0] if len(categories) > 0 else "Aucune"
            nb_cat_principale = categories.iloc[0] if len(categories) > 0 else 0
            
            st.markdown(f"""
            <div style="background: {get_gradient('corail')};
                        padding: 25px;
                        border-radius: 15px;
                        text-align: center;
                        color: white;">
                <div style="font-size: 0.9em; opacity: 0.9; margin-bottom: 10px;">Catégorie principale</div>
                <div style="font-size: 2em; font-weight: bold; margin: 10px 0;">{cat_principale}</div>
                <div style="font-size: 0.9em; opacity: 0.8;">{nb_cat_principale} habitudes</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            date_premiere = pd.to_datetime(habitudes['date_creation']).min()
            anciennete = (datetime.now() - date_premiere).days
            
            st.markdown(f"""
            <div style="background: {get_gradient('bleu_ciel')};
                        padding: 25px;
                        border-radius: 15px;
                        text-align: center;
                        color: white;">
                <div style="font-size: 0.9em; opacity: 0.9; margin-bottom: 10px;">Ancienneté</div>
                <div style="font-size: 3em; font-weight: bold; margin: 10px 0;">{anciennete}</div>
                <div style="font-size: 0.9em; opacity: 0.8;">jours</div>
            </div>
            """, unsafe_allow_html=True)
        
        st.divider()
        
        st.markdown("### 📊 Répartition par Catégorie")
        
        couleurs_cat = {
            "Écologie": "vert_sauge",
            "Santé": "corail",
            "Personnel": "bleu_ciel",
            "Travail": "lilas",
            "Social": "rose"
        }
        
        for categorie, count in categories.items():
            pourcentage = int((count / len(habitudes)) * 100)
            couleur = couleurs_cat.get(categorie, "beige")
            
            st.markdown(f"""
            <div style="background: white;
                        padding: 15px;
                        border-radius: 10px;
                        margin: 10px 0;
                        border-left: 5px solid {COLORS[couleur]['main']};
                        box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                    <strong style="color: {COLORS[couleur]['dark']};">{categorie}</strong>
                    <span style="color: {COLORS[couleur]['dark']}; font-weight: 600;">{count} habitudes ({pourcentage}%)</span>
                </div>
                <div style="background: #f0f0f0; height: 10px; border-radius: 5px; overflow: hidden;">
                    <div style="background: {get_gradient(couleur)}; 
                                height: 100%; 
                                width: {pourcentage}%;"></div>
                </div>
            </div>
            """, unsafe_allow_html=True)

st.divider()

# === CONSEILS ===
with st.expander("💡 Conseils pour créer de bonnes habitudes"):
    st.markdown(f"""
    <div style="background: white;
                padding: 20px;
                border-radius: 10px;
                border-left: 5px solid {COLORS['vert_sauge']['main']};">
        <h4 style="color: {COLORS['vert_sauge']['dark']};">🎯 Les clés du succès :</h4>
        <ul style="font-size: 1.05em; line-height: 1.8; color: #555;">
            <li><strong>Sois spécifique</strong> : "Méditer 10 minutes" plutôt que "Être zen"</li>
            <li><strong>Commence petit</strong> : Mieux vaut 5 minutes tous les jours que 1h une fois</li>
            <li><strong>Ancre tes habitudes</strong> : Associe-les à un moment précis de ta journée</li>
            <li><strong>Mesure ton progrès</strong> : Utilise le tracking pour voir ton évolution</li>
            <li><strong>Reste flexible</strong> : Adapte tes habitudes selon ton ressenti</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.divider()

st.markdown(f"""
<div style="text-align: center; color: #666; padding: 20px;">
    <p style="font-size: 1em;">⚙️ Personnalise ton expérience HabitTrack Green</p>
    <p style="color: #999; font-size: 0.9em;">💚 Chaque habitude est un pas vers une meilleure version de toi</p>
</div>
""", unsafe_allow_html=True)