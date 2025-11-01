# -*- coding: utf-8 -*-
"""
Dashboard - HabitTrack Green
Affiche les statistiques et la progression

Auteur: Batoul ZORKOT & Laure Charmille
Date: 2025
"""

import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import sys
import os
import plotly.graph_objects as go

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from utils.habit_manager import charger_habitudes, charger_historique
from utils.stats_calculator import calculer_streak
from utils.styles import get_custom_css, COLORS, get_gradient

st.set_page_config(
    page_title="Dashboard - HabitTrack Green",
    page_icon="📊",
    layout="wide"
)

st.markdown(get_custom_css(), unsafe_allow_html=True)

# === HEADER ===
st.title("📊 Dashboard")
st.write("Visualise ta progression et tes statistiques !")
st.divider()

# Charger les données
habitudes = charger_habitudes()
historique = charger_historique()

if len(habitudes) == 0:
    st.warning("⚠️ Aucune habitude créée. Va dans 'Paramètres' pour commencer !")
    st.stop()

if len(historique) == 0:
    st.info("📝 Commence à tracker tes habitudes pour voir tes statistiques !")
    st.stop()

# === CALCULS ===
total_habitudes = len(habitudes)
total_completions = len(historique)

streaks = []
for _, h in habitudes.iterrows():
    streak = calculer_streak(h['id'], historique)
    streaks.append(streak)

meilleur_streak = max(streaks) if streaks else 0

date_debut = (datetime.now() - timedelta(days=30)).date()
historique_30j = historique[historique['date'].dt.date >= date_debut]
completions_30j = len(historique_30j)
taux_global = int((completions_30j / (total_habitudes * 30)) * 100) if total_habitudes > 0 else 0

premiere_date = historique['date'].min().date()
derniere_date = historique['date'].max().date()
jours_utilisation = (derniere_date - premiere_date).days + 1

moyenne_jour = round(total_completions / jours_utilisation, 1) if jours_utilisation > 0 else 0

# === MESSAGE MOTIVANT ===
if taux_global >= 80:
    message_titre = "🌟 Performance Exceptionnelle !"
    message_desc = "Tu es incroyable ! Continue sur cette lancée, champion ! 💪"
    couleur = get_gradient('corail')
elif taux_global >= 50:
    message_titre = "💚 Très Bon Travail !"
    message_desc = "Tu progresses super bien ! Continue comme ça ! 🚀"
    couleur = get_gradient('vert_sauge')
else:
    message_titre = "🌱 On Y Croit !"
    message_desc = "Chaque jour est une nouvelle opportunité ! Tu peux le faire ! 💪"
    couleur = get_gradient('rose')

st.markdown(f"""
<div style="background: {couleur};
            padding: 40px;
            border-radius: 20px;
            text-align: center;
            color: white;
            box-shadow: 0 8px 16px rgba(0,0,0,0.2);
            margin-bottom: 30px;">
    <h1 style="color: white; margin: 0; font-size: 2.5em;">{message_titre}</h1>
    <p style="font-size: 1.3em; margin: 15px 0; opacity: 0.95;">{message_desc}</p>
    <p style="font-size: 1.1em; margin-top: 20px; opacity: 0.9;">
        📅 <strong>{jours_utilisation}</strong> jours d'utilisation • 
        ✅ <strong>{total_completions}</strong> habitudes complétées • 
        🔥 <strong>{meilleur_streak}</strong> jours de streak
    </p>
</div>
""", unsafe_allow_html=True)

st.divider()

# === KPIs ===
st.markdown("## 📈 Vue d'Ensemble")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <div style="background: {get_gradient('vert_sauge')};
                padding: 30px;
                border-radius: 15px;
                text-align: center;
                color: white;
                box-shadow: 0 4px 8px rgba(168, 191, 154, 0.3);">
        <div style="font-size: 1em; opacity: 0.9; margin-bottom: 10px;">Habitudes Actives</div>
        <div style="font-size: 3.5em; font-weight: bold; margin: 10px 0;">{total_habitudes}</div>
        <div style="font-size: 0.9em; opacity: 0.8;">en suivi</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div style="background: {get_gradient('rose')};
                padding: 30px;
                border-radius: 15px;
                text-align: center;
                color: white;
                box-shadow: 0 4px 8px rgba(244, 195, 194, 0.3);">
        <div style="font-size: 1em; opacity: 0.9; margin-bottom: 10px;">Taux de Réussite</div>
        <div style="font-size: 3.5em; font-weight: bold; margin: 10px 0;">{taux_global}%</div>
        <div style="font-size: 0.9em; opacity: 0.8;">sur 30 jours</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div style="background: {get_gradient('corail')};
                padding: 30px;
                border-radius: 15px;
                text-align: center;
                color: white;
                box-shadow: 0 4px 8px rgba(232, 117, 79, 0.3);">
        <div style="font-size: 1em; opacity: 0.9; margin-bottom: 10px;">Meilleur Streak</div>
        <div style="font-size: 3.5em; font-weight: bold; margin: 10px 0;">🔥 {meilleur_streak}</div>
        <div style="font-size: 0.9em; opacity: 0.8;">jours</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div style="background: {get_gradient('lilas')};
                padding: 30px;
                border-radius: 15px;
                text-align: center;
                color: white;
                box-shadow: 0 4px 8px rgba(200, 182, 213, 0.3);">
        <div style="font-size: 1em; opacity: 0.9; margin-bottom: 10px;">Moyenne / Jour</div>
        <div style="font-size: 3.5em; font-weight: bold; margin: 10px 0;">{moyenne_jour}</div>
        <div style="font-size: 0.9em; opacity: 0.8;">habitudes</div>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# === GRAPHIQUE ===
st.markdown("## 📊 Progression des 30 Derniers Jours")

dates_30j = [(datetime.now() - timedelta(days=i)).date() for i in range(29, -1, -1)]
completions_par_jour = []

for date in dates_30j:
    count = len(historique[historique['date'].dt.date == date])
    completions_par_jour.append(count)

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=dates_30j,
    y=completions_par_jour,
    mode='lines+markers',
    name='Complétions',
    line=dict(color=COLORS['vert_sauge']['main'], width=4),
    marker=dict(
        size=10, 
        color=COLORS['vert_sauge']['light'], 
        line=dict(color=COLORS['vert_sauge']['main'], width=2)
    ),
    fill='tozeroy',
    fillcolor='rgba(168, 191, 154, 0.3)'
))

fig.update_layout(
    xaxis_title="Date",
    yaxis_title="Nombre d'habitudes complétées",
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    font=dict(color=COLORS['vert_sauge']['dark'], size=14),
    hovermode='x unified',
    showlegend=False,
    height=400
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

# === TOP 3 ===
st.markdown("## 🏆 Ton Top 3")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🥇 Plus Suivies")
    
    top_habitudes = historique.groupby('habitude_id').size().reset_index(name='count')
    top_habitudes = top_habitudes.sort_values('count', ascending=False).head(3)
    
    medailles = ["🥇", "🥈", "🥉"]
    
    for idx, (i, row) in enumerate(top_habitudes.iterrows()):
        habitude = habitudes[habitudes['id'] == row['habitude_id']].iloc[0]
        
        st.markdown(f"""
        <div style="background: white;
                    padding: 20px;
                    border-radius: 12px;
                    margin: 12px 0;
                    border-left: 5px solid {COLORS['vert_sauge']['main']};
                    box-shadow: 0 2px 6px rgba(0,0,0,0.08);
                    display: flex;
                    justify-content: space-between;
                    align-items: center;">
            <div>
                <span style="font-size: 1.5em;">{medailles[idx]}</span>
                <strong style="font-size: 1.1em;"> {habitude['icone']} {habitude['nom']}</strong>
            </div>
            <div style="background: {get_gradient('vert_sauge')};
                        color: white;
                        padding: 8px 16px;
                        border-radius: 20px;
                        font-weight: bold;">
                {row['count']} fois
            </div>
        </div>
        """, unsafe_allow_html=True)

with col2:
    st.markdown("### 🔥 Meilleurs Streaks")
    
    habitudes_streaks = []
    for _, hab in habitudes.iterrows():
        streak = calculer_streak(hab['id'], historique)
        if streak > 0:
            habitudes_streaks.append({'habitude': hab, 'streak': streak})
    
    habitudes_streaks = sorted(habitudes_streaks, key=lambda x: x['streak'], reverse=True)[:3]
    
    for idx, item in enumerate(habitudes_streaks):
        hab = item['habitude']
        streak = item['streak']
        
        st.markdown(f"""
        <div style="background: white;
                    padding: 20px;
                    border-radius: 12px;
                    margin: 12px 0;
                    border-left: 5px solid {COLORS['corail']['main']};
                    box-shadow: 0 2px 6px rgba(0,0,0,0.08);
                    display: flex;
                    justify-content: space-between;
                    align-items: center;">
            <div>
                <span style="font-size: 1.5em;">{medailles[idx]}</span>
                <strong style="font-size: 1.1em;"> {hab['icone']} {hab['nom']}</strong>
            </div>
            <div style="background: {get_gradient('corail')};
                        color: white;
                        padding: 8px 16px;
                        border-radius: 20px;
                        font-weight: bold;">
                🔥 {streak} jours
            </div>
        </div>
        """, unsafe_allow_html=True)

st.divider()

# === ACHIEVEMENTS ===
st.markdown("## 🏅 Achievements Débloqués")

achievements = []

if jours_utilisation >= 7:
    achievements.append({"icon": "📅", "titre": "Première Semaine", "desc": "7 jours d'utilisation"})

if meilleur_streak >= 7:
    achievements.append({"icon": "🔥", "titre": "Warrior Streak", "desc": f"{meilleur_streak} jours consécutifs"})

if taux_global >= 70:
    achievements.append({"icon": "💯", "titre": "Excellence", "desc": f"{taux_global}% de réussite"})

if total_completions >= 100:
    achievements.append({"icon": "💯", "titre": "Centenaire", "desc": "100 complétions !"})

if achievements:
    achievements_display = achievements[:3]
    cols = st.columns(len(achievements_display))
    
    for i, achievement in enumerate(achievements_display):
        with cols[i]:
            st.markdown(f"""
            <div style="background: {get_gradient('corail')};
                        color: white;
                        padding: 25px;
                        border-radius: 15px;
                        text-align: center;
                        box-shadow: 0 4px 8px rgba(232, 117, 79, 0.3);">
                <div style="font-size: 3em; margin-bottom: 10px;">{achievement['icon']}</div>
                <strong style="font-size: 1.2em;">{achievement['titre']}</strong><br>
                <small style="opacity: 0.9;">{achievement['desc']}</small>
            </div>
            """, unsafe_allow_html=True)
else:
    st.info("🏅 Continue à tracker pour débloquer des achievements !")

st.divider()

# === EXPORT ===
st.markdown("## 📥 Exporter tes Données")

st.markdown(f"""
<div style="background: {get_gradient('bleu_ciel')};
            padding: 20px;
            border-radius: 15px;
            text-align: center;
            color: white;
            margin-bottom: 20px;">
    <p style="font-size: 1.1em; margin: 0;">
        💾 Télécharge tes données en CSV pour les sauvegarder ou les analyser dans Excel
    </p>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    try:
        csv_habitudes = habitudes.to_csv(index=False, encoding='utf-8')
        st.download_button(
            label="📋 Télécharger mes Habitudes (CSV)",
            data=csv_habitudes,
            file_name=f"mes_habitudes_{datetime.now().strftime('%Y%m%d')}.csv",
            mime="text/csv",
            use_container_width=True,
            type="primary"
        )
        st.success(f"✅ {len(habitudes)} habitudes prêtes")
    except Exception as e:
        st.error(f"Erreur : {e}")

with col2:
    try:
        csv_historique = historique.to_csv(index=False, encoding='utf-8')
        st.download_button(
            label="📊 Télécharger mon Historique (CSV)",
            data=csv_historique,
            file_name=f"mon_historique_{datetime.now().strftime('%Y%m%d')}.csv",
            mime="text/csv",
            use_container_width=True,
            type="primary"
        )
        st.success(f"✅ {len(historique)} entrées prêtes")
    except Exception as e:
        st.error(f"Erreur : {e}")

st.divider()

# === FOOTER ===
st.markdown(f"""
<div style="text-align: center; padding: 20px; color: #666;">
    <p style="font-size: 1em;">
        📅 Membre depuis le {premiere_date.strftime('%d/%m/%Y')} • 
        💚 {total_completions} habitudes complétées
    </p>
</div>
""", unsafe_allow_html=True)