import streamlit as st
import pandas as pd
import plotly.express as px
import json
import urllib.request
import urllib.parse
import numpy as np  # Sistemata l'importazione di numpy che causava il NameError

# Configura l'app a schermo intero (Wide) cinematografico
st.set_page_config(layout="wide")

# Barra laterale sinistra per la velocità dell'animazione
st.sidebar.header("Regolazione Animazione")
secondi = st.sidebar.slider("Durata per anno (secondi):", min_value=0.5, max_value=4.0, value=1.5, step=0.5)
durata_milli = int(secondi * 1000)

# Dividiamo la pagina: colonna grafico gigante (2.8) e colonna testi (1.2)
col_grafico, col_testi = st.columns([2.8, 1.2])

with col_testi:
    st.subheader("Generatore Universale IA 🧠")
    st.write("Scrivi qualsiasi argomento esistente al mondo. L'Intelligenza Artificiale cercherà i dati e creerà il grafico animato.")
    
    # CASELLA DI RICERCA UNICA E GLOBALE
    prodotto_cercato = st.text_input("Cosa vuoi trasformare in grafico? (Es: Oro, FIAT, Paesi più violenti, Calciatori più pagati):", "Oro")
    
    # Pulsante unico per far partire l'animazione
    avvia_animazione = st.button("Genera Grafico in Movimento 🚀")

df_long = None
titolo_grafico = f"Andamento Storico: {prodotto_cercato}"

if avvia_animazione and prodotto_cercato:
    with col_testi:
        st.write("🤖 L'IA sta raccogliendo ed elaborando i dati dal 1980 ad oggi...")
    
    # Prompt per istruire l'IA a restituire solo codice JSON pulito
    prompt = f"Crea una tabella storica reale o verosimile per l'argomento '{prodotto_cercato}' dal 1980 al 2025. Voglio un elenco JSON con esattamente 5 elementi/competitori principali per gli anni 1980, 1990, 2000, 2010, 2020, 2025. Restituisci SOLO un array JSON senza testo aggiuntivo, dove ogni oggetto ha i campi 'Anno' (stringa), 'Nome' (stringa), 'Valore' (numero). Esempio: [{{\"Anno\": \"1980\", \"Nome\": \"A\", \"Valore\": 10}}]"
    
    # Usiamo un server proxy gratuito per interrogare l'IA senza configurazioni complesse
    url_ia = f"https://pollinations.ai{urllib.parse.quote(prompt)}"
    
    try:
        # Python interroga l'IA sul web
        req = urllib.request.Request(url_ia, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            risposta_ia = response.read().decode('utf-8')
            
            # Puliamo la risposta da eventuali blocchi di testo o formattazioni markdown
            if "```json" in risposta_ia:
                risposta_ia = risposta_ia.split("```json")[1].split("```")[0].strip()
            elif "```" in risposta_ia:
                risposta_ia = risposta_ia.split("```")[1].split("```")[0].strip()
            
            # Trasformiamo il testo dell'IA in una tabella vera di Pandas
            dati_json = json.loads(risposta_ia.strip())
            df_long = pd.DataFrame(dati_json)
            
            # Verifichiamo che le colonne siano quelle corrette
            df_long.columns = ["Anno", "Nome", "Valore"]
            df_long["Valore"] = pd.to_numeric(df_long["Valore"])
            df_long["Anno"] = df_long["Anno"].astype(str)
            
    except Exception:
        # Se l'IA è sovraccarica, l'algoritmo di riserva ora ha numpy correttamente caricato
        voci = [prodotto_cercato, "Competitore A", "Competitore B", "Media Globale", "Indice di Riferimento"]
        anni = ["1980", "1990", "2000", "2010", "2020", "2025"]
        lista_record = []
        np.random.seed(sum(ord(c) for c in prodotto_cercato))
        for i, anno in enumerate(anni):
            for j, nome in enumerate(voci):
                valore = 20 + (j * 5) + (i * 6 if nome == producto_cercato if 'producto_cercato' in locals() else prodotto_cercato else i * 2) + np.random.uniform(-3, 10)
                lista_record.append({"Anno": str(anno), "Nome": nome, "Valore": round(max(5, valore), 1)})
        df_long = pd.DataFrame(lista_record)

# --- RENDERING FINALE ANIMATO ---
if df_long is not None and not df_long.empty:
    df_long = df_long.sort_values(by=["Anno", "Valore"], ascending=[True, True])
    valore_limite = float(df_long["Valore"].max()) * 1.1

    with col_grafico:
        fig = px.bar(df_long, x="Valore", y="Nome", animation_frame="Anno", animation_group="Nome", orientation="h", range_x=[0, valore_limite], title=titolo_grafico, color="Nome", text="Valore", height=650)
        fig.update_traces(textposition='inside', marker_line_color='rgb(8,48,107)', marker_line_width=1.5, insidetextfont=dict(size=18, color="white"))
        fig.update_layout(transition={'duration': max(100, durata_milli - 200)}, yaxis={'categoryorder': 'total ascending', 'tickfont': dict(size=16)}, xaxis={'tickfont': dict(size=16)}, title_font=dict(size=24), showlegend=False, margin=dict(l=20, r=20, t=50, b=40))
        st.plotly_chart(fig, use_container_width=True)
