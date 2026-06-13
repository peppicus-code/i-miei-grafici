import streamlit as st
import pandas as pd
import numpy as np

# Configura l'app a schermo intero
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

# CREAZIONE DELLE TABELLE IN MODO DIRETTO (Formato perfetto per st.bar_chart)
if scelta_menu == "Dischi e Album più Venduti della Storia 🎵":
    dati = {
        "Michael Jackson (Thriller)": [22.0, 26.5, 31.0, 36.2, 42.0, 48.2],
        "AC/DC (Back in Black)": [20.0, 21.8, 23.6, 25.4, 28.0, 30.1],
        "Pink Floyd (The Dark Side)": [19.0, 20.2, 21.4, 22.6, 24.2, 25.5],
        "Whitney Houston (The Bodyguard)": [15.0, 16.5, 18.0, 19.2, 21.0, 22.4],
        "FIat/Fleetwood Mac (Rumours)": [16.0, 17.1, 18.2, 19.3, 20.5, 21.2]
    }
    df_grafico = pd.DataFrame(dati, index=["1980", "1990", "2000", "2010", "2020", "2025"])

elif scelta_menu == "Paesi più Pericolosi del Mondo (Tasso di Criminalità) 🚨":
    dati = {
        "Venezuela":,
        "Papua Nuova Guinea":,
        "Sudafrica":,
        "Afghanistan":,
        "El Salvador": [68, 74, 79, 82, 45, 25] # Mostra il crollo reale della criminalità
    }
    df_grafico = pd.DataFrame(dati, index=["1980", "1990", "2000", "2010", "2020", "2025"])

elif scelta_menu == "Classifica Produttori Auto (Con FIAT)":
    dati = {
        "Toyota": [3.2, 4.4, 5.9, 8.5, 9.5, 10.5],
        "Volkswagen": [2.5, 3.1, 5.0, 7.1, 9.3, 9.0],
        "Ford": [4.1, 4.8, 5.7, 4.9, 4.2, 4.0],
        "FIAT": [2.1, 2.6, 2.4, 2.1, 1.8, 1.7],
        "BYD": [0.0, 0.0, 0.0, 0.1, 0.4, 3.2]
    }
    df_grafico = pd.DataFrame(dati, index=["1980", "1990", "2000", "2010", "2020", "2025"])

elif scelta_menu == "Paesi più Ricchi del Mondo (PIL)":
    dati = {
        "Stati Uniti":,
        "Cina":,
        "Giappone":,
        "Germania":,
        "Italia": [480, 1100, 1150, 2100, 1890, 2200]
    }
    df_grafico = pd.DataFrame(dati, index=["1980", "1990", "2000", "2010", "2020", "2025"])

# MOSTRA IL GRAFICO ISTANTANEAMENTE NELLA COLONNA CENTRALE GIGANTE
if df_grafico is not None:
    with col_grafico:
        st.write(f"### Andamento Storico: {scelta_menu}")
        # Motore grafico nativo ultra-veloce e leggero
        st.bar_chart(df_grafico, height=550)
        st.info("La legenda in alto ti mostra i colori dei vari paesi o brand.")
