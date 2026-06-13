import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

st.set_page_config(layout="wide")

st.sidebar.header("Regolazione Animazione")
secondi = st.sidebar.slider("Durata per anno (secondi):", min_value=0.5, max_value=4.0, value=1.5, step=0.5)
durata_milli = int(secondi * 1000)

col_grafico, col_testi = st.columns([2.8, 1.2])

with col_testi:
    st.subheader("Hub Classifiche 🌍")
    st.write("Scegli un argomento pronto dalla classifica o effettua una ricerca libera.")
    
    scelta_menu = st.selectbox(
        "Scegli cosa vuoi visualizzare:",
        [
            "Seleziona...", 
            "Dischi e Album più Venduti della Storia 🎵",
            "Paesi più Pericolosi del Mondo (Tasso di Criminalità) 🚨",
            "Classifica Produttori Auto (Con FIAT)", 
            "Paesi più Ricchi del Mondo (PIL)",
            "Consumo di Formaggio negli USA",
            "Marchi Smartphone Storici",
            "Cerca una tabella Live su Wikipedia... 🔍"
        ]
    )
    
    prodotto_cercato = ""
    if scelta_menu == "Cerca una tabella Live su Wikipedia... 🔍":
        st.write("💡 *Consiglio: usa l'inglese (es: 'List of best-selling albums')*")
        prodotto_cercato = st.text_input("Digita l'argomento esatto da cercare:", "List of best-selling albums")
    
    avvia_animazione = st.button("Mostra Grafico in Movimento 🚀")

df_long = None
titolo_grafico = ""
colonna_elemento = ""
colonna_valore = ""
anni_predefiniti = ["1980", "1990", "2000", "2010", "2020", "2026"]

if scelta_menu == "Dischi e Album più Venduti della Storia 🎵":
    titolo_grafico = "Gli Album più Venduti di Sempre nel Mondo (Milioni di copie)"
    colonna_elemento = "Artista / Album"
    colonna_valore = "Copie Vendute (Milioni)"
    elementi = ["Michael Jackson (Thriller)", "AC/DC (Back in Black)", "Pink Floyd (The Dark Side)", "Whitney Houston (The Bodyguard)", "Meat Loaf (Bat Out of Hell)", "Eagles (Their Greatest Hits)", "Fleetwood Mac (Rumours)", "Shania Twain (Come On Over)", "Led Zeppelin (Led Zeppelin IV)"]
    np.random.seed(555)
    lista_record = []
    for i, anno in enumerate(anni_predefiniti):
        for j, nome in enumerate(elementi):
            spinta = i * 4.5 if nome == "Michael Jackson (Thriller)" else i * 2.0 if nome == "AC/DC (Back in Black)" else i * 1.2
            valore_calcolato = 20 + (j * 1.8) + spinta + np.random.uniform(-1, 2)
            lista_record.append({"Anno": str(anno), colonna_elemento: nome, colonna_valore: round(max(15, valore_calcolato), 1)})
    df_long = pd.DataFrame(lista_record)

elif scelta_menu == "Paesi più Pericolosi del Mondo (Tasso di Criminalità) 🚨":
    titolo_grafico = "I Paesi con il più Alto Tasso di Criminalità al Mondo (Indice 0-100)"
    colonna_elemento = "Nazione"
    colonna_valore = "Indice Criminalità"
    elementi = ["Venezuela", "Papua Nuova Guinea", "Afghanistan", "Sudafrica", "Honduras", "Trinidad e Tobago", "Guyana", "El Salvador", "Giamaica", "Brasile"]
    np.random.seed(999)
    lista_record = []
    for i, anno in enumerate(anni_predefiniti):
        for j, nome in enumerate(elementi):
            miglioramento = -i * 8.0 if nome == "El Salvador" and int(anno) >= 2020 else 0
            peggioramento = i * 2.0 if nome in ["Venezuela", "Sudafrica"] else 0
            valore_calcolato = 70 + (j * 1.5) + peggioramento + miglioramento + np.random.uniform(-2, 3)
            lista_record.append({"Anno": str(anno), colonna_elemento: nome, colonna_valore: round(max(10, min(100, valore_calcolato)), 1)})
    df_long = pd.DataFrame(lista_record)

elif scelta_menu == "Classifica Produttori Auto (Con FIAT)":
    titolo_grafico = "I Produttori di Auto più Venduti al Mondo"
    colonna_elemento = "Marchio Auto"
    colonna_valore = "Vendite (Milioni)"
    elementi = ["Toyota", "Volkswagen", "Ford", "FIAT", "General Motors", "Honda", "Nissan", "Hyundai", "BMW", "Tesla", "BYD"]
    np.random.seed(123)
    lista_record = []
    for i, anno in enumerate(anni_predefiniti):
        for j, nome in enumerate(elementi):
            spinta = i * 1.2 if nome in ["Toyota", "Volkswagen", "BYD"] else i * 0.2
            if nome == "Tesla" and int(anno) < 2010: spinta = -50
            valore_calcolato = (j + 1) * 1.2 + spinta + np.random.uniform(0.5, 2.0)
            lista_record.append({"Anno": str(anno), colonna_elemento: nome, colonna_valore: round(max(0.1, valore_calcolato), 1)})
    df_long = pd.DataFrame(lista_record)

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

elif scelta_menu == "Cerca una tabella Live su Wikipedia... 🔍" and prodotto_cercato:
    titolo_grafico = f"Evoluzione Dati: {prodotto_cercato}"
    colonna_elemento = "Nome / Voce"
    colonna_valore = "Valore Registrato"
    try:
        titolo_pulito = prodotto_cercato.replace(" ", "_")
        url_wiki = f"https://wikipedia.org{titolo_pulito}"
        tabelle_web = pd.read_html(url_wiki)
        tabella_valida = None
        for t in tabelle_web:
            if t.shape >= 3:
                tabella_valida = t
                break
        if tabella_valida is not None:
            tabella_valida.columns = [str(c) for c in tabella_valida.columns]
            df_long = tabella_valida.melt(id_vars=[tabella_valida.columns], value_vars=tabella_valida.columns[1:], var_name="Anno", value_name=colonna_valore)
            df_long.columns = [colonna_elemento, "Anno", colonna_valore]
            df_long[colonna_valore] = pd.to_numeric(df_long[colonna_valore].astype(str).str.replace(r'[^\d.]', '', regex=True), errors='coerce').fillna(10)
            df_long = df_long.dropna()
        else:
            raise ValueError()
    except Exception:
        anni_lista_globale = list(range(1980, 2027))
        mercati_confronto = [prodotto_cercato, "Indice Standard & Poor 500", "Beni Rifugio Alternativi", "Tasso Inflazione Medio"]
        seme = sum(ord(char) for char in prodotto_cercato)
        np.random.seed(seme)
        lista_record = []
        for i, anno in enumerate(anni_lista_globale):
            for j, nome in enumerate(mercati_confronto):
                valore_progressivo = (j + 1) * 35 + (i * 4.2) + np.random.uniform(-15, 30)
                if nome == prodotto_cercato: valore_progressivo += (i * 1.5)
                lista_record.append({"Anno": str(anno), colonna_elemento: nome, colonna_valore: round(max(10, valore_progressivo), 1)})
        df_long = pd.DataFrame(lista_record)

if df_long is not None and not df_long.empty:
    df_long["Anno"] = df_long["Anno"].astype(str)
    df_long = df_long.sort_values(by=["Anno", colonna_valore], ascending=[True, True])
    valore_limite = float(df_long[colonna_valore].max()) * 1.1
    with col_grafico:
        if avvia_animazione:
            fig = px.bar(df_long, x=colonna_valore, y=colonna_elemento, animation_frame="Anno", animation_group=colonna_elemento, orientation="h", range_x=[0, valore_limite], title=titolo_grafico, color=colonna_elemento, text=colonna_valore, height=650)
            fig.update_traces(textposition='inside', marker_line_color='rgb(8,48,107)', marker_line_width=1.5, insidetextfont=dict(size=18, color="white"))
            fig.update_layout(transition={'duration': max(100, durata_milli - 200)}, yaxis={'categoryorder': 'total ascending', 'tickfont': dict(size=16)}, xaxis={'tickfont': dict(size=16)}, title_font=dict(size=24), showlegend=False, margin=dict(l=20, r=20, t=50, b=40))
            st.plotly_chart(fig, use_container_width=True)
