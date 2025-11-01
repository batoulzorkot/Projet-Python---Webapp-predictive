# -*- coding: utf-8 -*-
"""
Carte Éco - HabitTrack Green
Carte interactive des points de compost

Auteur: Batoul Zorkot & Laure Charmille
Date: 2025
"""

import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from utils.map_handler import charger_points_compost
from utils.styles import get_custom_css, COLORS, get_gradient

st.set_page_config(
    page_title="Carte Éco - HabitTrack Green",
    page_icon="🗺️",
    layout="wide"
)

st.markdown(get_custom_css(), unsafe_allow_html=True)

# === HEADER ===
st.title("🗺️ Carte des Points de Compost")
st.write("Trouve les points de compost les plus proches de chez toi !")
st.divider()

# Charger les points
points = charger_points_compost()

if len(points) == 0:
    st.warning("⚠️ Aucun point de compost enregistré.")
    st.stop()

# Ajouter colonnes manquantes
if 'ouvert' not in points.columns:
    points['ouvert'] = True
if 'quartier' not in points.columns:
    points['quartier'] = 'Non spécifié'
if 'contact' not in points.columns:
    points['contact'] = 'Non disponible'

# Extraire ville
def extraire_ville(adresse):
    try:
        parties = adresse.split()
        for i, partie in enumerate(parties):
            if len(partie) == 5 and partie.isdigit():
                if i + 1 < len(parties):
                    return ' '.join(parties[i+1:])
        return "Paris"
    except:
        return "Non spécifié"

if 'ville' not in points.columns:
    points['ville'] = points['adresse'].apply(extraire_ville)

# === STATISTIQUES ===
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
    <div style="background: {get_gradient('vert_sauge')};
                padding: 25px;
                border-radius: 15px;
                text-align: center;
                color: white;">
        <div style="font-size: 3em;">🌍</div>
        <div style="font-size: 2em; font-weight: bold; margin: 10px 0;">{len(points)}</div>
        <div>Points disponibles</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    points_ouverts = len(points[points['ouvert'] == True])
    st.markdown(f"""
    <div style="background: {get_gradient('corail')};
                padding: 25px;
                border-radius: 15px;
                text-align: center;
                color: white;">
        <div style="font-size: 3em;">✅</div>
        <div style="font-size: 2em; font-weight: bold; margin: 10px 0;">{points_ouverts}</div>
        <div>Ouverts maintenant</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    villes = points['ville'].nunique()
    st.markdown(f"""
    <div style="background: {get_gradient('bleu_ciel')};
                padding: 25px;
                border-radius: 15px;
                text-align: center;
                color: white;">
        <div style="font-size: 3em;">📍</div>
        <div style="font-size: 2em; font-weight: bold; margin: 10px 0;">{villes}</div>
        <div>Villes couvertes</div>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# === CARTE ===
st.markdown("## 🗺️ Carte Interactive")

centre_lat = points['latitude'].mean()
centre_lon = points['longitude'].mean()

m = folium.Map(
    location=[centre_lat, centre_lon],
    zoom_start=12,
    tiles='OpenStreetMap'
)

for _, point in points.iterrows():
    couleur = 'green' if point['ouvert'] else 'red'
    
    nom = point.get('nom', 'Point de compost')
    adresse = point.get('adresse', 'Adresse non disponible')
    quartier = point.get('quartier', 'Non spécifié')
    horaires = point.get('horaires', 'Horaires non disponibles')
    contact = point.get('contact', 'Non disponible')
    ouvert = point.get('ouvert', True)
    
    google_maps_url = f"https://www.google.com/maps/search/?api=1&query={point['latitude']},{point['longitude']}"
    
    popup_html = f"""
    <div style="font-family: 'Poppins', sans-serif; min-width: 250px;">
        <h4 style="color: {COLORS['vert_sauge']['dark']}; margin: 0 0 10px 0;">{nom}</h4>
        <p style="margin: 5px 0;"><strong>📍</strong> {adresse}</p>
        <p style="margin: 5px 0;"><strong>🏘️</strong> {quartier}</p>
        <p style="margin: 5px 0;"><strong>🕐</strong> {horaires}</p>
        <p style="margin: 5px 0;"><strong>📞</strong> {contact}</p>
        <p style="margin: 10px 0;">
            <span style="background: {'#4CAF50' if ouvert else '#f44336'}; 
                         color: white; 
                         padding: 5px 10px; 
                         border-radius: 5px;">
                {'✅ Ouvert' if ouvert else '❌ Fermé'}
            </span>
        </p>
        <div style="margin-top: 15px;">
            <a href="{google_maps_url}" target="_blank" 
               style="background: {COLORS['vert_sauge']['main']};
                      color: white;
                      padding: 10px 20px;
                      border-radius: 8px;
                      text-decoration: none;
                      display: inline-block;
                      font-weight: bold;">
                🗺️ Obtenir l'itinéraire
            </a>
        </div>
    </div>
    """
    
    folium.Marker(
        location=[point['latitude'], point['longitude']],
        popup=folium.Popup(popup_html, max_width=350),
        tooltip=nom,
        icon=folium.Icon(color=couleur, icon='leaf', prefix='fa')
    ).add_to(m)

st_folium(m, width=1200, height=600)

st.divider()

# === LISTE AVEC FILTRES ===
st.markdown("## 📋 Liste des Points de Compost")

col1, col2 = st.columns(2)

with col1:
    villes_uniques = sorted(list(points['ville'].unique()))
    filtre_ville = st.selectbox(
        "🏙️ Filtrer par ville",
        ["Toutes les villes"] + villes_uniques
    )

with col2:
    filtre_ouvert = st.selectbox(
        "🕐 Filtrer par statut",
        ["Tous", "Ouverts uniquement", "Fermés uniquement"]
    )

points_filtres = points.copy()

if filtre_ville != "Toutes les villes":
    points_filtres = points_filtres[points_filtres['ville'] == filtre_ville]

if filtre_ouvert == "Ouverts uniquement":
    points_filtres = points_filtres[points_filtres['ouvert'] == True]
elif filtre_ouvert == "Fermés uniquement":
    points_filtres = points_filtres[points_filtres['ouvert'] == False]

st.markdown(f"""
<div style="background: {get_gradient('beige')};
            padding: 15px;
            border-radius: 10px;
            text-align: center;
            margin-bottom: 20px;">
    <strong>{len(points_filtres)} point(s) trouvé(s)</strong>
</div>
""", unsafe_allow_html=True)

if len(points_filtres) == 0:
    st.info("🔍 Aucun point ne correspond aux filtres sélectionnés.")
else:
    for _, point in points_filtres.iterrows():
        couleur_statut = 'vert_sauge' if point['ouvert'] else 'rose'
        
        nom = point.get('nom', 'Point de compost')
        adresse = point.get('adresse', 'Adresse non disponible')
        quartier = point.get('quartier', 'Non spécifié')
        ville = point.get('ville', 'Non spécifié')
        horaires = point.get('horaires', 'Horaires non disponibles')
        contact = point.get('contact', 'Non disponible')
        ouvert = point.get('ouvert', True)
        
        google_maps_url = f"https://www.google.com/maps/search/?api=1&query={point['latitude']},{point['longitude']}"
        
        col1, col2 = st.columns([3, 1])
        
        with col1:
            st.markdown(f"""
            <div style="background: white;
                        padding: 20px;
                        border-radius: 15px;
                        border-left: 5px solid {COLORS[couleur_statut]['main']};
                        box-shadow: 0 2px 6px rgba(0,0,0,0.1);
                        margin: 15px 0;">
                <h3 style="color: {COLORS['vert_sauge']['dark']}; margin: 0 0 10px 0;">{nom}</h3>
                <p style="margin: 5px 0;">📍 <strong>{adresse}</strong></p>
                <p style="margin: 5px 0;">🏙️ {ville} • 🏘️ {quartier}</p>
                <p style="margin: 5px 0;">🕐 {horaires}</p>
                <p style="margin: 5px 0;">📞 {contact}</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
            <div style="background: {get_gradient(couleur_statut)};
                        color: white;
                        padding: 20px;
                        border-radius: 15px;
                        text-align: center;
                        font-weight: bold;
                        font-size: 1.1em;
                        margin: 15px 0;
                        height: 100px;
                        display: flex;
                        align-items: center;
                        justify-content: center;">
                {'✅ Ouvert' if ouvert else '❌ Fermé'}
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown(f"""
            <div style="text-align: center; margin-top: 10px;">
                <a href="{google_maps_url}" target="_blank" 
                   style="display: inline-block;
                          background: {COLORS['vert_sauge']['main']};
                          color: white;
                          padding: 12px 24px;
                          border-radius: 10px;
                          text-decoration: none;
                          font-weight: bold;
                          box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
                    🗺️ Itinéraire
                </a>
            </div>
            """, unsafe_allow_html=True)

st.divider()

# === AIDE ===
with st.expander("ℹ️ Comment utiliser la carte ?"):
    st.markdown("""
    ### 🗺️ **Navigation sur la carte**
    - **Zoom** : Utilisez la molette ou les boutons +/-
    - **Déplacer** : Cliquez et faites glisser
    - **Info point** : Cliquez sur un marqueur pour voir les détails
    
    ### 📍 **Filtres**
    - **Par ville** : Affiche uniquement les points d'une ville
    - **Par statut** : Vois seulement les points ouverts ou fermés
    
    ### 🗺️ **Obtenir un itinéraire**
    - Clique sur **"Itinéraire"** pour ouvrir Google Maps
    - Google Maps calculera le trajet depuis ta position
    """)

st.divider()

st.markdown(f"""
<div style="text-align: center; color: #666; padding: 20px;">
    <p style="font-size: 1.1em;">💚 Ensemble pour un monde plus vert !</p>
    <p style="color: #999; font-size: 0.9em;">Données mises à jour régulièrement • {len(points)} points répertoriés</p>
</div>
""", unsafe_allow_html=True)