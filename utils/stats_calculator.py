"""
Module de calculs statistiques (ex: streaks)
"""

import pandas as pd
from datetime import datetime, timedelta

def calculer_streak(habitude_id, historique_df):
    """
    Calcule le streak (série) actuel pour une habitude donnée.
    """
    if historique_df.empty:
        return 0

    # Filtrer l'historique pour cette habitude et trier
    hist_habitude = historique_df[historique_df['habitude_id'] == habitude_id].copy()
    if hist_habitude.empty:
        return 0

    # S'assurer que 'date' est bien au format date (sans l'heure)
    hist_habitude['date_jour'] = hist_habitude['date'].dt.date
    
    # Garder une seule entrée par jour (au cas où)
    dates_completes = sorted(hist_habitude['date_jour'].unique(), reverse=True)

    streak = 0
    aujourd_hui = datetime.now().date()
    
    # Si la dernière date n'est ni aujourd'hui ni hier, le streak est 0
    if aujourd_hui not in dates_completes and (aujourd_hui - timedelta(days=1)) not in dates_completes:
        return 0
        
    # Si c'est complété aujourd'hui
    if aujourd_hui in dates_completes:
        streak = 1
        jour_precedent = aujourd_hui - timedelta(days=1)
        
        # Continuer à compter en arrière
        while jour_precedent in dates_completes:
            streak += 1
            jour_precedent -= timedelta(days=1)
            
    # Si ce n'est pas complété aujourd'hui, mais hier oui
    elif (aujourd_hui - timedelta(days=1)) in dates_completes:
        streak = 1
        jour_precedent = aujourd_hui - timedelta(days=2)
        
        # Continuer à compter en arrière
        while jour_precedent in dates_completes:
            streak += 1
            jour_precedent -= timedelta(days=1)
            
    return streak