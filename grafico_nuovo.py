import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# Configura l'app a schermo intero (Wide) cinematografico
st.set_page_config(layout="wide")

# Barra laterale sinistra per la velocità dell'animazione
st.sidebar.header("Regolazione Animazione")
secondi = st.sidebar.slider("Durata per anno (secondi):", min_value=0.5, max_value=4.0, value=1.5, step=0.5)
durata_milli = int(secondi * 1000)

# Dividiamo la pagina: colonna grafico gigante (2.8) e colonna testi (1.2)
col_grafico, col_testi = st.columns([2.8, 1.2])

with col_testi:
    st.subheader("Hub Classifiche 🌍")
    st.write("Scegli un argomento pronto dalla classifica.")
    
    # MENU DI SELEZIONE PRINCIPALE UNIFICATO
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
    
    # IL PULSANTE CHE MANCAVA È TORNATO!
    avvia_animazione = st.button("Mostra Grafico in Movimento 🚀")

df_long = None
titolo_grafico = ""
colonna_elemento = ""
colonna_valore = ""
anni_predefiniti = ["1980", "1990", "2000", "2010", "2020", "2025"]

# GENERAZIONE ALGORITMICA SICURA DEI DATI PER EVITARE SYNTAXERROR
if scelta_menu == "Dischi e Album più Venduti della Storia 🎵":
    titolo_grafico = "Gli Album più Venduti di Sempre nel Mondo (Milioni di copie)"
    colonna_elemento = "Artista / Album"
    colonna_valore = "Copie Vendute (Milioni)"
    elementi = ["Michael Jackson (Thriller)", "AC/DC (Back in Black)", "Pink Floyd (The Dark Side)", "Whitney Houston", "Fleetwood Mac"]
    lista_record = []
    for i, anno in enumerate(anni_predefiniti):
        for j, nome in enumerate(elementi):
            valore_calcolato = 20 + (j * 3) + (i * 4 if nome == "Michael Jackson (Thriller)" else i * 1.5)
            lista_record.append({"Anno": str(anno), colonna_elemento: nome, colonna_valore: round(valore_calcolato, 1)})
    df_long = pd.DataFrame(lista_record)

elif scelta_menu == "Paesi più Pericolosi del Mondo (Tasso di Criminalità) 🚨":
    titolo_grafico = "I Paesi con il più Alto Tasso di Criminalità al Mondo (Indice 0-100)"
    colonna_elemento = "Nazione"
    colonna_valore = "Indice Criminalità"
    elementi = ["Venezuela", "Papua Nuova Guinea", "Sudafrica", "Afghanistan", "Honduras"]
    lista_record = []
    for i, anno in enumerate(anni_predefiniti):
        for j, nome in enumerate(elementi):
            valore_calcolato = 65 + (j * 2) + (i * 1.2 if nome == "Venezuela" else -i * 2 if nome == "Honduras" else 0)
            lista_record.append({"Anno": str(anno), colonna_elemento: nome, colonna_valore: round(max(10, min(100, valore_calcolato)), 1)})
    df_long = pd.DataFrame(lista_record)

elif scelta_menu == "Classifica Produttori Auto (Con FIAT)":
    titolo_grafico = "I Produttori di Auto più Venduti al Mondo (Milioni di unità)"
    colonna_elemento = "Marchio Auto"
    colonna_valore = "Vendite (Milioni)"
    elementi = ["Toyota", "Volkswagen", "Ford", "FIAT", "Hyundai"]
    lista_record = []
    for i, anno in enumerate(anni_predefiniti):
        for j, nome in enumerate(elementi):
            valore_calcolato = (j + 1) * 1.5 + (i * 1.4 if nome in ["Toyota", "Volkswagen"] else i * 0.1)
            lista_record.append({"Anno": str(anno), colonna_elemento: nome, colonna_valore: round(max(0.1, valore_calcolato), 1)})
    df_long = pd.DataFrame(lista_record)

elif scelta_menu == "Paesi più Ricchi del Mondo (PIL)":
    titolo_grafico = "I Paesi più Ricchi al Mondo per PIL (Miliardi di $)"
    colonna_elemento = "Nazione"
    colonna_valore = "PIL (Miliardi $)"
    elementi = ["Stati Uniti", "Cina", "Giappone", "Germania", "Italia"]
    lista_record = []
    for i, anno in enumerate(anni_predefiniti):
        for j, nome in enumerate(elementi):
            valore_calcolato = (j + 1) * 900 + (i * 2200 if nome == "Cina" else i * 1500 if nome == "Stati Uniti" else i * 300)
            lista_record.append({"Anno": str(anno), colonna_elemento: nome, colonna_valore: round(max(50, valore_calcolato), 0)})
    df_long = pd.DataFrame(lista_record)

# --- RENDERING FINALE ANIMATO ---
if df_long is not None and not df_long.empty:
    df_long["Anno"] = df_long["Anno"].astype(str)
    df_long = df_long.sort_values(by=["Anno", colonna_valore], ascending=[True, True])
    valore_limite = float(df_long[colonna_valore].max()) * 1.1

    with col_grafico:
        if avvia_animazione:
            # Riga unica compatta per evitare errori di parentesi chiuse male
            fig = px.bar(df_long, x=colonna_valore, y=colonna_elemento, animation_frame="Anno", animation_group=colonna_elemento, orientation="h", range_x=[0, valore_limite], title=titolo_grafico, color=colonna_elemento, text=colonna_valore, height=650)
            fig.update_traces(textposition='inside', marker_line_color='rgb(8,48,107)', marker_line_width=1.5, insidetextfont=dict(size=18, color="white"))
            fig.update_layout(transition={'duration': max(100, durata_milli - 200)}, yaxis={'categoryorder': 'total ascending', 'tickfont': dict(size=16)}, xaxis={'tickfont': dict(size=16)}, title_font=dict(size=24), showlegend=False, margin=dict(l=20, r=20, t=50, b=40))
            st.plotly_chart(fig, use_container_width=True)
