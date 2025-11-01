# -*- coding: utf-8 -*-
"""
Module pour les styles CSS
"""

import sys
import os

# Ajouter le dossier parent au path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import absolu
from utils.config import COLORS


def get_gradient(couleur_nom):
    """Génère un dégradé CSS"""
    if couleur_nom in COLORS:
        light = COLORS[couleur_nom]['light']
        main = COLORS[couleur_nom]['main']
        return f"linear-gradient(135deg, {light} 0%, {main} 100%)"
    return "linear-gradient(135deg, #F0F0F0 0%, #D8D8D8 100%)"


def get_custom_css():
    """Retourne le CSS personnalisé"""
    
    vert_main = COLORS['vert_sauge']['main']
    vert_dark = COLORS['vert_sauge']['dark']
    vert_light = COLORS['vert_sauge']['light']
    beige_main = COLORS['beige']['main']
    beige_dark = COLORS['beige']['dark']
    beige_light = COLORS['beige']['light']
    corail_main = COLORS['corail']['main']
    corail_dark = COLORS['corail']['dark']
    
    return f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
        
        html, body, [class*="st-"] {{
            font-family: 'Poppins', sans-serif;
        }}
        
        .stApp {{
            background: linear-gradient(135deg, {beige_light} 0%, {beige_main} 100%);
        }}
        
        .main .block-container {{
            padding: 2rem;
        }}
        
        [data-testid="stSidebar"] {{
            background: linear-gradient(180deg, {beige_dark} 0%, {beige_main} 100%);
            border-right: 2px solid {vert_light};
        }}
        
        [data-testid="stSidebar"] h1,
        [data-testid="stSidebar"] h2,
        [data-testid="stSidebar"] h3 {{
            color: {vert_dark};
            font-weight: 700;
        }}
        
        h1, h2, h3 {{
            font-weight: 700;
            color: {vert_dark};
        }}
        
        .stButton > button {{
            background-color: {vert_main};
            color: white;
            border: none;
            border-radius: 10px;
            padding: 12px 24px;
            font-weight: 600;
            transition: all 0.3s ease;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        
        .stButton > button:hover {{
            background-color: {vert_dark};
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(0,0,0,0.15);
        }}
        
        .stButton > button[kind="primary"] {{
            background-color: {corail_main};
        }}
        
        .stButton > button[kind="primary"]:hover {{
            background-color: {corail_dark};
        }}
        
        .stCheckbox {{
            padding: 10px;
            background-color: white;
            border-radius: 12px;
            border: 2px solid {beige_dark};
            transition: all 0.3s ease;
        }}
        
        .stCheckbox:hover {{
            border-color: {vert_main};
            box-shadow: 0 2px 6px rgba(0,0,0,0.05);
        }}
        
        .stRadio {{
            padding: 10px;
            background-color: white;
            border-radius: 12px;
            border: 2px solid {beige_dark};
        }}
        
        .stExpander {{
            background: white;
            border: 2px solid {beige_dark};
            border-radius: 15px;
            margin-bottom: 1rem;
        }}
        
        .streamlit-expanderHeader {{
            padding: 15px;
            font-weight: 600;
            font-size: 1.1em;
            color: {vert_dark};
            background: white;
            border-radius: 15px;
        }}
        
        .streamlit-expanderHeader:hover {{
            background: {beige_light};
            border-color: {vert_main};
        }}
        
        .stTextInput > div > div > input,
        .stTextArea > div > div > textarea,
        .stSelectbox > div > div {{
            border-radius: 10px;
            border: 2px solid {beige_dark};
            background: white;
        }}
        
        .stTextInput > div > div > input:focus,
        .stTextArea > div > div > textarea:focus {{
            border-color: {vert_main};
            box-shadow: 0 0 0 3px {vert_light};
        }}
        
        .stProgress > div > div > div {{
            background-color: {vert_main};
        }}
        
        hr {{
            border-color: {beige_dark};
            opacity: 0.3;
        }}
        
        .stDownloadButton > button {{
            background-color: {vert_main};
            color: white;
        }}
        
        .stDownloadButton > button:hover {{
            background-color: {vert_dark};
        }}
    </style>
    """