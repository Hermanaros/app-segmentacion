import streamlit as st
import os

# --- CONFIG GENERAL ---
st.set_page_config(page_title="Segmentador Actitudinal", layout="wide")

# --- ESTILO PERSONALIZADO ---
st.markdown("""
    <style>
        body {
            background-color: #121B5A;
        }
        .main {
            background-color: #121B5A;
            color: blue;
        }
        .segmento {
            font-size: 30px;
            font-weight: bold;
            color: #FFC300;
        }
        .ranking-box {
            background-color: #1A237E;
            padding: 15px;
            border-radius: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# --- ATRIBUTOS A ORDENAR ---
atributos = [
    "Expresar mi verdadero yo; explorar nuevos estilos, marcar tendencia",
    "Jugar con mi identidad sin seguir un código de vestimenta social",
    "Vestirme para sentirme en sintonía conmigo mismo y el entorno",
    "Sentirme aceptado, ser parte del grupo",
    "Sentirme relajado y cómodo con la ropa que uso; desaparecer entre la multitud",
    "Uso ropa por comodidad en lugar de por estilo; no me preocupo demasiado por la moda",
    "Crear un estilo propio sin seguir lo que está de moda",
    "Vestirme para el éxito, busco ser respetado/admirado"
]

# --- FUNCIÓN CLASIFICACIÓN ---
def clasificar_segmento(top3):
    categorias = {
        "FASHIONISTA": 0,
        "TRENDSETTER": 0,
        "PRAGMÁTICO": 0,
        "AHORRADOR": 0
    }

    for atributo in top3:
        texto = atributo.lower()
        if any(x in texto for x in ["estilo", "tendencia", "vestirme para el éxito"]):
            categorias["FASHIONISTA"] += 1
        if any(x in texto for x in ["verdadero yo", "identidad", "crear un estilo"]):
            categorias["TRENDSETTER"] += 1
        if any(x in texto for x in ["comodidad", "desaparecer", "no me preocupo"]):
            categorias["PRAGMÁTICO"] += 1
        if any(x in texto for x in ["aceptado", "parte del grupo", "respetado"]):
            categorias["AHORRADOR"] += 1

    return max(categorias, key=categorias.get)

# --- LAYOUT PRINCIPAL ---
logo_path = os.path.join("asset", "logo.png")  # ruta relativa del logo

top = st.columns([0.8, 0.2])
with top[0]:
    st.markdown("### 🧭 Tu segmento es:")
    if "ranking" in st.session_state and len(st.session_state.ranking) == 3:
        segmento = clasificar_segmento(st.session_state.ranking)
        st.markdown(f"<div class='segmento'>{segmento}</div>", unsafe_allow_html=True)
    else:
        st.markdown("*Selecciona 3 atributos para ver tu segmento.*")
with top[1]:
    if os.path.exists(logo_path):
        st.image(logo_path, width=120)

st.markdown("---")

# --- UI INTERACTIVA ---
col1, col2 = st.columns(2)

with col1:
    st.markdown("## 🧩 Elige los 3 atributos más importantes respecto a tu vínculo con la moda:")
    seleccion = st.multiselect(
        "Selecciona 3 atributos, donde el 1ro es el MÁS importante:",
        options=atributos,
        max_selections=3,
        key="ranking"
    )

with col2:
    st.markdown("## 📋 Tu elección:")
    if seleccion:
        st.markdown("<div class='ranking-box'>", unsafe_allow_html=True)
        for i, attr in enumerate(seleccion, 1):
            st.markdown(f"**{i}.** {attr}")
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.info("Selecciona hasta 3 atributos")
