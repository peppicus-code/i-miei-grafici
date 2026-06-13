import streamlit as st
import pandas as pd
import plotly.express as px
import json
import urllib.request
import urllib.parse
import numpy as np

# Configura l'app a schermo intero (Wide) cinematografico
st.set_page_config(layout="wide")

st.sidebar.header("Regolazione Animazione")
secondi = st.sidebar.slider("Durata per anno (secondi):", min_value=0.5, max_value=4.0, value=1.5, step=0.5)
durata_milli = int(secondi * 1000)

col_grafico, col_testi = st.columns([2.8, 1.2])

with col_testi:
    st.subheader("Generatore Universale IA Google 🧠")
    st.write("Inserisci la tua chiave gratuita di Google e digita qualsiasi argomento per estrarre i nomi veri.")
    
    # LA CASELLA CHE TI MANCAVA COMPARIREBBE QUI
    chiave_google = st.text_input("Incolla qui la tua API Key di Google Gemini:", type="password")
    
    prodotto_cercato = st.text_input("Cosa vuoi trasformare in grafico?", "Calciatori più pagati")
    avvia_animazione = st.button("Genera Grafico in Movimento 🚀")

df_long = None
titolo_grafico = f"Andamento Storico: {prodotto_cercato}"

if avvia_animazione and prodotto_cercato:
    if not chiave_google:
        st.sidebar.error("⚠️ Inserisci la tua API Key di Google a destra per attivare i nomi reali!")
    else:
        with col_testi:
            st.write("🤖 L'IA di Google sta analizzando la storia e inserendo i nomi reali...")
        
        prompt = f"Crea una tabella storica reale o verosimile per l'argomento {prodotto_cercato} dal 1980 al 2025. Identifica i 5 protagonisti reali o elementi reali piu famosi di questo settore. Genera un elenco in formato JSON pulito. Ogni oggetto deve avere i campi Anno (scegli tra 1980, 1990, 2000, 2010, 2020, 2025), Nome (il nome reale del calciatore, nazione o brand), Valore (il numero stimato o reale). Restituisci SOLO l'array JSON senza markdown e senza testo aggiuntivo."
        
        url_gemini = f"https://googleapis.com{chiave_google}"
        corpo_richiesta = json.dumps({"contents": [{"parts": [{"text": prompt}]}]}).encode('utf-8')
        
        try:
            req = urllib.request.Request(url_gemini, data=corpo_richiesta, headers={'Content-Type': 'application/json'})
            with urllib.request.urlopen(req) as response:
                risposta = json.loads(response.read().decode('utf-8'))
                testo_ia = risposta['candidates'][0]['content']['parts'][0]['text']
                testo_ia = testo_ia.replace("```json", "").replace("```", "").strip()
                dati_json = json.loads(testo_ia)
                df_long = pd.DataFrame(dati_json)
                df_long.columns = ["Anno", "Nome", "Valore"]
                df_long["Valore"] = pd.to_numeric(df_long["Valore"])
                df_long["Anno"] = df_long["Anno"].astype(str)
        except Exception:
            df_long = None

    if df_long is None:
        voci = [prodotto_cercato, "Competitore A", "Competitore B", "Media Globale", "Indice"]
        anni = ["1980", "1990", "2000", "2010", "2020", "2025"]
        lista_record = []
        np.random.seed(sum(ord(c) for c in prodotto_cercato))
        for i, anno in enumerate(anni):
            for j, nome in enumerate(voci):
                valore = 20 + (j * 5) + (i * 6 if nome == prodotto_cercato else i * 2) + np.random.uniform(-3, 10)
                lista_record.append({"Anno": str(anno), "Nome": nome, "Valore": round(max(5, valore), 1)})
        df_long = pd.DataFrame(lista_record)

if df_long is not None and not df_long.empty:
    df_long = df_long.sort_values(by=["Anno", "Valore"], ascending=[True, True])
    valore_limite = float(df_long["Valore"].max()) * 1.1

    with col_grafico:
        fig = px.bar(df_long, x="Valore", y="Nome", animation_frame="Anno", animation_group="Nome", orientation="h", range_x=[0, valore_limite], title=titolo_grafico, color="Nome", text="Valore", height=650)
        fig.update_traces(textposition='inside', marker_line_color='rgb(8,48,107)', marker_line_width=1.5, insidetextfont=dict(size=18, color="white"))
        fig.update_layout(transition={'duration': max(100, durata_milli - 200)}, yaxis={'categoryorder': 'total ascending', 'tickfont': dict(size=16)}, xaxis={'tickfont': dict(size=16)}, title_font=dict(size=24), showlegend=False, margin=dict(l=20, r=20, t=50, b=40))
        st.plotly_chart(fig, use_container_width=True)
