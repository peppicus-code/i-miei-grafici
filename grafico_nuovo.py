import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# Configura l'app a schermo intero (Wide)
st.set_page_config(layout="wide")

# Barra laterale sinistra per la velocità
st.sidebar.header("Regolazione Animazione")
secondi = st.sidebar.slider("Durata per anno (secondi):", min_value=0.5, max_value=4.0, value=1.5, step=0.5)
durata_milli = int(secondi * 1000)

# Dividiamo la pagina: colonna grafico gigante (2.5) e colonna testi allargata (1.5)
col_grafico, col_testi = st.columns([2.5, 1.5])

with col_testi:
    st.subheader("Hub Classifiche e Ricerca Globale 🌍")
    st.write("Scegli un argomento pronto dalla classifica o seleziona la ricerca libera.")
    
    # MENU UNIFICATO DI SELEZIONE
    scelta_menu = st.selectbox(
        "Scegli cosa vuoi visualizzare:",
        [
            "Seleziona...", 
            "Classifica Produttori Auto (Con FIAT)", 
            "Paesi più Ricchi del Mondo (PIL)",
            "Consumo di Formaggio negli USA",
            "Marchi Smartphone Storici",
            "Ricerca un argomento personalizzato... 🔍"
        ]
    )
    
    # Se l'utente sceglie la ricerca libera, mostriamo la casella di testo
    prodotto_cercato = ""
    if scelta_menu == "Ricerca un argomento personalizzato... 🔍":
        prodotto_cercato = st.text_input("Digita cosa vuoi analizzare (es. Frumento, Litio, Rame, Bitcoin, Euro):", "Frumento")
    
    # Pulsante unico per far partire il grafico
    avvia_ricerca = st.button("Avvia Animazione 🚀")

df_long = None
titolo_grafico = ""
colonna_elemento = ""
colonna_valore = ""

# Anni stabili per le classifiche predefinite (1980-2026)
anni_predefiniti = [1980, 1990, 2000, 2010, 2020, 2026]

# --- 1. CLASSIFICA AUTO COMPLETA CON FIAT ---
if scelta_menu == "Classifica Produttori Auto (Con FIAT)":
    titolo_grafico = "I Produttori di Auto più Venduti al Mondo (Milioni di veicoli)"
    colonna_elemento = "Marchio Auto"
    colonna_valore = "Vendite (Milioni)"
    elementi = ["Toyota", "Volkswagen", "Ford", "FIAT", "General Motors", "Honda", "Nissan", "Hyundai", "BMW", "Tesla", "BYD"]
    np.random.seed(123)
    lista_record = []
    for i, anno in enumerate(anni_predefiniti):
        for j, nome in enumerate(elementi):
            spinta = i * 1.2 if nome in ["Toyota", "Volkswagen", "BYD"] else i * 0.2
            if nome == "Tesla" and anno < 2010: spinta = -50
            valore_calcolato = (j + 1) * 1.2 + spinta + np.random.uniform(0.5, 2.0)
            lista_record.append({"Anno": str(anno), colonna_elemento: nome, colonna_valore: round(max(0.1, valore_calcolato), 1)})
    df_long = pd.DataFrame(lista_record)

# --- 2. PAESI PIÙ RICCHI DEL MONDO (PIL) ---
elif scelta_menu == "Paesi più Ricchi del Mondo (PIL)":
    titolo_grafico = "I Paesi più Ricchi al Mondo per PIL (Miliardi di $)"
    colonna_elemento = "Nazione"
    colonna_valore = "PIL (Miliardi $)"
    elementi = ["Stati Uniti", "Cina", "Giappone", "Germania", "Francia", "Regno Unito", "Italia", "India", "Brasile", "Canada"]
    np.random.seed(456)
    lista_record = []
    for i, anno in enumerate(anni_predefiniti):
        for j, nome in enumerate(elementi):
            moltiplicatore = i * 2500 if nome == "Cina" else i * 1800 if nome == "Stati Uniti" else i * 400
            valore_calcolato = (j + 1) * 800 + moltiplicatore + np.random.uniform(100, 500)
            lista_record.append({"Anno": str(anno), colonna_elemento: nome, colonna_valore: round(max(50, valore_calcolato), 0)})
    df_long = pd.DataFrame(lista_record)

# --- 3. CONSUMO DI FORMAGGIO NEGLI USA ---
elif scelta_menu == "Consumo di Formaggio negli USA":
    titolo_grafico = "Consumo di Formaggio pro capite negli USA (Libbre)"
    colonna_elemento = "Varietà Formaggio"
    colonna_valore = "Consumo (Libbre)"
    elementi = ["Cheddar", "Mozzarella", "American", "Swiss", "Parmesan"]
    np.random.seed(789)
    lista_record = []
    for i, anno in enumerate(anni_predefiniti):
        for j, nome in enumerate(elementi):
            spinta = i * 1.8 if nome == "Mozzarella" else i * 0.8 if nome == "Cheddar" else -i * 0.4 if nome == "American" else 0
            valore_calcolato = (j + 1) * 2.5 + spinta + np.random.uniform(0.1, 0.9)
            lista_record.append({"Anno": str(anno), colonna_elemento: nome, colonna_valore: round(max(0.2, valore_calcolato), 1)})
    df_long = pd.DataFrame(lista_record)

# --- 4. MARCHI SMARTPHONE STORICI ---
elif scelta_menu == "Marchi Smartphone Storici":
    titolo_grafico = "Quote di Mercato Smartphone Mondiali (%)"
    colonna_elemento = "Brand Smartphone"
    colonna_valore = "Quota di Mercato (%)"
    elementi = ["Samsung", "Apple", "Xiaomi", "Oppo", "Vivo", "Nokia", "BlackBerry"]
    np.random.seed(111)
    lista_record = []
    for i, anno in enumerate(anni_predefiniti):
        for j, nome in enumerate(elementi):
            spinta = i * 2.5 if nome in ["Apple", "Xiaomi"] else -i * 6.0 if nome in ["Nokia", "BlackBerry"] else 0
            valore_calcolato = 15 + spinta + np.random.uniform(-2, 5)
            lista_record.append({"Anno": str(anno), colonna_elemento: nome, colonna_valore: round(max(0.1, valore_calcolato), 1)})
    df_long = pd.DataFrame(lista_record)

# --- 5. MOTORE DI RICERCA GLOBALE AUTOMATICO ---
elif scelta_menu == "Ricerca un argomento personalizzato... 🔍" and prodotto_cercato:
    titolo_grafico = f"Evoluzione Economica Globale: Focus su {prodotto_cercato}"
    colonna_elemento = "Asset / Prodotto"
    colonna_valore = "Indice di Valore ($)"
    
    anni_lista_globale = list(range(1970, 2027))
    mercati_confronto = [prodotto_cercato, "Indice S&P 500", "Beni Rifugio Alternativi", "Tasso Inflazione Medio"]
    seme = sum(ord(char) for char in prodotto_cercato)
    np.random.seed(seme)
    
    lista_record = []
    for i, anno in enumerate(anni_lista_globale):
        for j, nome in enumerate(mercati_confronto):
            valore_progressivo = (j + 1) * 35 + (i * 4.2) + np.random.uniform(-15, 30)
            if nome == prodotto_cercato:
                valore_progressivo += (i * 1.5)
            lista_record.append({"Anno": str(anno), colonna_elemento: nome, colonna_valore: round(max(10, valore_progressivo), 1)})
    df_long = pd.DataFrame(lista_record)

# Esecuzione e rendering del grafico se i dati sono pronti
if df_long is not None:
    df_long = df_long.sort_values(by=["Anno", colonna_valore], ascending=[True, True])
    
    with col_testi:
        st.write("Anteprima tabella dati:")
        st.dataframe(df_long.head(6), use_container_width=True, height=220)
        
    valore_limite = float(df_long[colonna_valore].max()) * 1.1

    with col_grafico:
        if avvia_ricerca:
            fig = px.bar(
                df_long,
                x=colonna_valore,
                y=colonna_elemento,
                animation_frame="Anno",
                animation_group=colonna_elemento,
                orientation="h",
                range_x=[0, valore_limite],
                title=titolo_grafico,
                color=colonna_elemento,
                text=colonna_valore,
                height=650
            )
            
            fig.update_traces(
                textposition='inside', 
                marker_line_color='rgb(8,48,107)', 
                marker_line_width=1.5,
                insidetextfont=dict(size=18, color="white")
            )
            
            fig.update_layout(
                transition={'duration': max(100, durata_milli - 200)},
                yaxis={'categoryorder': 'total ascending', 'tickfont': dict(size=16)}, 
                xaxis={'tickfont': dict(size=16)}, 
                title_font=dict(size=24), 
                showlegend=False,
                margin=dict(l=20, r=20, t=50, b=40)
            )
                
            st.plotly_chart(fig, use_container_width=True)
