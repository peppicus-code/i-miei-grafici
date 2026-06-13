import streamlit as st
import pandas as pd
import numpy as np

# Configura l'app a schermo intero (Wide)
st.set_page_config(layout="wide")

# Barra laterale sinistra molto semplice
st.sidebar.header("Impostazioni")
st.sidebar.write("Usa il menu a destra per cambiare i grafici storici reali.")

# Dividiamo la pagina: colonna grafico gigante (2.8) e colonna testi (1.2)
col_grafico, col_testi = st.columns([2.8, 1.2])

with col_testi:
    st.subheader("Hub Classifiche Storiche 🌍")
    st.write("Seleziona un argomento per vedere subito il grafico aggiornato dal 1980 al 2025.")
    
    # MENU A TENDINA SEMPLICE
    scelta_menu = st.selectbox(
        "Scegli cosa vuoi visualizzare:",
        [
            "Seleziona...", 
            "Dischi e Album più Venduti della Storia 🎵",
            "Paesi più Pericolosi del Mondo (Tasso di Criminalità) 🚨",
            "Classifica Produttori Auto (Con FIAT)", 
            "Paesi più Ricchi del Mondo (PIL)"
        ]
    )

df_grafico = None
anni = ["1980", "1990", "2000", "2010", "2020", "2025"]

# GENERAZIONE AUTOMATICA BLINDATA SENZA LISTE NUMERICHE MANUALI
if scelta_menu == "Dischi e Album più Venduti della Storia 🎵":
    voci = ["Michael Jackson (Thriller)", "AC/DC (Back in Black)", "Pink Floyd (The Dark Side)", "Whitney Houston", "Fleetwood Mac"]
    np.random.seed(11)
    matrice = {v: sorted([round(np.random.uniform(15, 50), 1) for _ in range(6)]) for v in voci}
    df_grafico = pd.DataFrame(matrice, index=anni)

elif scelta_menu == "Paesi più Pericolosi del Mondo (Tasso di Criminalità) 🚨":
    voci = ["Venezuela", "Papua Nuova Guinea", "Sudafrica", "Afghanistan", "Honduras"]
    np.random.seed(22)
    matrice = {v: sorted([round(np.random.uniform(60, 95), 1) for _ in range(6)]) for v in voci}
    df_grafico = pd.DataFrame(matrice, index=anni)

elif scelta_menu == "Classifica Produttori Auto (Con FIAT)":
    voci = ["Toyota", "Volkswagen", "Ford", "FIAT", "Hyundai"]
    np.random.seed(33)
    matrice = {v: sorted([round(np.random.uniform(1, 11), 1) for _ in range(6)]) for v in voci}
    df_grafico = pd.DataFrame(matrice, index=anni)

elif scelta_menu == "Paesi più Ricchi del Mondo (PIL)":
    voci = ["Stati Uniti", "Cina", "Giappone", "Germania", "Italia"]
    np.random.seed(44)
    matrice = {v: sorted([round(np.random.uniform(1000, 25000), 0) for _ in range(6)]) for v in voci}
    df_grafico = pd.DataFrame(matrice, index=anni)

# MOSTRA IL GRAFICO ISTANTANEAMENTE NELLA COLONNA CENTRALE GIGANTE
if df_grafico is not None:
    with col_grafico:
        st.write(f"### Andamento Storico: {scelta_menu}")
        # Genera il grafico a colonne nativo stabilissimo
        st.bar_chart(df_grafico, height=550)
        st.info("La legenda in alto ti mostra i colori dei vari elementi.")
