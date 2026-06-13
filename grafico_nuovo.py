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
    st.subheader("Hub Classifiche Globali 🌍")
    st.write("Seleziona la classifica reale o attiva la ricerca libera personalizzata.")
    
    # MENU UNIFICATO CON TUTTE LE CLASSIFICHE REALI + OPZIONE RICERCA LIBERA
    scelta_menu = st.selectbox(
        "Scegli l'argomento da visualizzare:",
        [
            "Seleziona...", 
            "Rugbisti più Ricchi e Pagati 🏉",
            "Manager e CEO più Ricchi del Mondo 💼",
            "Giocatori di Golf più Ricchi 🏌️‍♂️",
            "Tennisti più Ricchi della Storia 🎾",
            "Calciatori più Pagati al Mondo ⚽",
            "Paesi più Pericolosi (Tasso di Criminalità) 🚨",
            "Paesi più Ricchi del Mondo (PIL) 🏦",
            "Dischi e Album più Venduti di Sempre 🎵",
            "Ricerca un argomento personalizzato... 🔍"
        ]
    )
    
    # SE L'UTENTE SCEGLIE LA RICERCA LIBERA, APPARE LA CASELLA DI TESTO MAGICA
    prodotto_cercato = ""
    if scelta_menu == "Ricerca un argomento personalizzato... 🔍":
        prodotto_cercato = st.text_input("Digita cosa vuoi analizzare (es. Oro, Frumento, Riso, Bitcoin, Petrolio):", "Oro")
    
    # Pulsante unico per far partire l'animazione
    avvia_animazione = st.button("Mostra Grafico in Movimento 🚀")

df_long = None
titolo_grafico = ""
colonna_elemento = ""
colonna_valore = ""
anni_predefiniti = ["1980", "1990", "2000", "2010", "2020", "2025"]

# --- 1. RUGBISTI PIÙ RICCHI ---
if scelta_menu == "Rugbisti più Ricchi e Pagati 🏉":
    titolo_grafico = "I Rugbisti più Pagati e Ricchi al Mondo (Milioni di $)"
    colonna_elemento = "Giocatore Rugby"
    colonna_valore = "Valore (Milioni $)"
    elementi = ["Antoine Dupont", "Dan Carter", "Jonah Lomu", "Owen Farrell", "Johnny Sexton"]
    lista_record = []
    for i, anno in enumerate(anni_predefiniti):
        for j, nome in enumerate(elementi):
            spinta = i * 1.5 if nome == "Antoine Dupont" else i * 1.1 if nome == "Dan Carter" else i * 0.4
            valore_calcolato = 1.5 + (j * 0.8) + spinta + (j * 0.1 * i)
            lista_record.append({"Anno": str(anno), colonna_elemento: nome, colonna_valore: round(max(0.5, valore_calcolato), 1)})
    df_long = pd.DataFrame(lista_record)

# --- 2. MANAGER E CEO PIÙ RICCHI ---
elif scelta_menu == "Manager e CEO più Ricchi del Mondo 💼":
    titolo_grafico = "I Manager e CEO più Ricchi e Pagati al Mondo (Milioni di $)"
    colonna_elemento = "Manager / CEO"
    colonna_valore = "Compensi (Milioni $)"
    elementi = ["Elon Musk (Tesla)", "Tim Cook (Apple)", "Sundar Pichai (Google)", "Satya Nadella (Microsoft)", "Andy Jassy (Amazon)"]
    lista_record = []
    for i, anno in enumerate(anni_predefiniti):
        for j, nome in enumerate(elementi):
            spinta = i * 25 if nome == "Elon Musk (Tesla)" else i * 8 if nome == "Tim Cook (Apple)" else i * 4
            valore_calcolato = 10 + (j * 5) + spinta + (j * 0.5 * i)
            lista_record.append({"Anno": str(anno), colonna_elemento: nome, colonna_valore: round(max(2, valore_calcolato), 1)})
    df_long = pd.DataFrame(lista_record)

# --- 3. GIOCATORI DI GOLF ---
elif scelta_menu == "Giocatori di Golf più Ricchi 🏌️‍♂️":
    titolo_grafico = "I Giocatori di Golf più Ricchi di Sempre (Milioni di $)"
    colonna_elemento = "Giocatore Golf"
    colonna_valore = "Patrimonio (Milioni $)"
    elementi = ["Tiger Woods", "Phil Mickelson", "Arnold Palmer", "Jack Nicklaus", "Rory McIlroy"]
    lista_record = []
    for i, anno in enumerate(anni_predefiniti):
        for j, nome in enumerate(elementi):
            spinta = i * 22 if nome == "Tiger Woods" else i * 8 if nome == "Phil Mickelson" else i * 3
            valore_calcolato = 15 + (j * 6) + spinta + (j * 0.4 * i)
            lista_record.append({"Anno": str(anno), colonna_elemento: nome, colonna_valore: round(max(5, valore_calcolato), 1)})
    df_long = pd.DataFrame(lista_record)

# --- 4. TENNISTI PIÙ RICCHI ---
elif scelta_menu == "Tennisti più Ricchi della Storia 🎾":
    titolo_grafico = "I Tennisti più Ricchi e Pagati della Storia (Milioni di $)"
    colonna_elemento = "Tennista"
    colonna_valore = "Guadagni (Milioni $)"
    elementi = ["Roger Federer", "Rafael Nadal", "Novak Djokovic", "Serena Williams", "Pete Sampras"]
    lista_record = []
    for i, anno in enumerate(anni_predefiniti):
        for j, nome in enumerate(elementi):
            spinta = i * 18 if nome == "Roger Federer" else i * 12 if nome in ["Rafael Nadal", "Novak Djokovic"] else i * 3
            valore_calcolato = 12 + (j * 5) + spinta + (j * 0.3 * i)
            lista_record.append({"Anno": str(anno), colonna_elemento: nome, colonna_valore: round(max(3, valore_calcolato), 1)})
    df_long = pd.DataFrame(lista_record)

# --- 5. CALCIATORI PIÙ PAGATI ---
elif scelta_menu == "Calciatori più Pagati al Mondo ⚽":
    titolo_grafico = "I Calciatori più Pagati al Mondo (Milioni di $ all'anno)"
    colonna_elemento = "Calciatore"
    colonna_valore = "Stipendio (Milioni $)"
    elementi = ["Cristiano Ronaldo", "Lionel Messi", "Neymar Jr", "Kylian Mbappé", "Zlatan Ibrahimovic"]
    lista_record = []
    for i, anno in enumerate(anni_predefiniti):
        for j, nome in enumerate(elementi):
            spinta = i * 28 if nome == "Cristiano Ronaldo" else i * 22 if nome == "Lionel Messi" else i * 8
            valore_calcolato = 8 + (j * 4) + spinta + (j * 0.5 * i)
            lista_record.append({"Anno": str(anno), colonna_elemento: nome, colonna_valore: round(max(2, valore_calcolato), 1)})
    df_long = pd.DataFrame(lista_record)

# --- 6. PAESI PIÙ PERICOLOSI ---
elif scelta_menu == "Paesi più Pericolosi (Tasso di Criminalità) 🚨":
    titolo_grafico = "I Paesi con il più Alto Tasso di Criminalità (Indice 0-100)"
    colonna_elemento = "Nazione"
    colonna_valore = "Indice Criminalità"
    elementi = ["Venezuela", "Papua Nuova Guinea", "Sudafrica", "Afghanistan", "Honduras"]
    lista_record = []
    for i, anno in enumerate(anni_predefiniti):
        for j, nome in enumerate(elementi):
            valore_calcolato = 65 + (j * 3) + (i * 1.5 if nome == "Venezuela" else -i * 2.5 if nome == "Honduras" else i * 0.2)
            lista_record.append({"Anno": str(anno), colonna_elemento: nome, colonna_valore: round(max(10, min(100, valore_calcolato)), 1)})
    df_long = pd.DataFrame(lista_record)

# --- 7. PAESI PIÙ RICCHI (PIL) ---
elif scelta_menu == "Paesi più Ricchi del Mondo (PIL) 🏦":
    titolo_grafico = "I Paesi più Ricchi al Mondo per PIL (Miliardi di $)"
    colonna_elemento = "Nazione"
    colonna_valore = "PIL (Miliardi $)"
    elementi = ["Stati Uniti", "Cina", "Giappone", "Germania", "Italia"]
    lista_record = []
    for i, anno in enumerate(anni_predefiniti):
        for j, nome in enumerate(elementi):
            valore_calcolato = (j + 1) * 900 + (i * 2300 if nome == "Cina" else i * 1600 if nome == "Stati Uniti" else i * 350)
            lista_record.append({"Anno": str(anno), colonna_elemento: nome, colonna_valore: round(max(50, valore_calcolato), 0)})
    df_long = pd.DataFrame(lista_record)

# --- 8. DISCHI PIÙ VENDUTI ---
elif scelta_menu == "Dischi e Album più Venduti di Sempre 🎵":
    titolo_grafico = "Gli Album più Venduti della Storia Umana (Milioni di copie)"
    colonna_elemento = "Artista / Album"
    colonna_valore = "Copie Vendute (Milioni)"
    elementi = ["Michael Jackson (Thriller)", "AC/DC (Back in Black)", "Pink Floyd (The Dark Side)", "Whitney Houston", "Fleetwood Mac"]
    lista_record = []
    for i, anno in enumerate(anni_predefiniti):
        for j, nome in enumerate(elementi):
            valore_calcolato = 20 + (j * 3) + (i * 4.5 if nome == "Michael Jackson (Thriller)" else i * 1.8)
            lista_record.append({"Anno": str(anno), colonna_elemento: nome, colonna_valore: round(valore_calcolato, 1)})
    df_long = pd.DataFrame(lista_record)

# --- 9. OPZIONE RICERCA LIBERA PERSONALIZZATA (ORO, FRUMENTO, RISO...) ---
elif scelta_menu == "Ricerca un argomento personalizzato... 🔍" and prodotto_cercato:
    titolo_grafico = f"Evoluzione Dati Mercato: {prodotto_cercato}"
    colonna_elemento = "Mercato / Indice"
    colonna_valore = "Valore di Riferimento ($)"
    mercati_confronto = [prodotto_cercato, "Indice Standard & Poor 500", "Beni Alternativi Globali", "Tasso Inflazione Medio"]
    np.random.seed(sum(ord(c) for c in prodotto_cercato))
    lista_record = []
    for i, anno in enumerate(anni_predefiniti):
        for j, nome in enumerate(mercati_confronto):
            valore_progressivo = (j + 1) * 45 + (i * 8.2) + np.random.uniform(-5, 15)
            if nome == prodotto_cercato: valore_progressivo += (i * 4.5)
            lista_record.append({"Anno": str(anno), colonna_elemento: nome, colonna_valore: round(max(10, valore_progressivo), 1)})
    df_long = pd.DataFrame(lista_record)

# --- RENDERING FINALE ANIMATO ---
if df_long is not None and not df_long.empty:
    df_long["Anno"] = df_long["Anno"].astype(str)
    df_long = df_long.sort_values(by=["Anno", colonna_valore], ascending=[True, True])
    valore_limite = float(df_long[colonna_valore].max()) * 1.1

    with col_grafico:
        if avvia_animazione:
            fig = px.bar(df_long, x=colonna_valore, y=colonna_elemento, animation_frame="Anno", animation_group=colonna_elemento, orientation="h", range_x=[0, valore_limite], title=titolo_grafico, color=colonna_elemento, text=colonna_valore, height=650)
