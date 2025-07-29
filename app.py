import streamlit as st

# Atributos disponibles
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

st.set_page_config(page_title="Segmentador Attitudinal", layout="wide")

# 💅 Estética general
st.markdown("""
<style>
    .main {
        background-color: #1e1e1e;
        color: white;
    }
    .segmento {
        font-size: 30px;
        font-weight: bold;
        color: #FFC300;
    }
    .ranking-box {
        background-color: #333;
        padding: 15px;
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)

# 🧠 Función de clasificación por top 3
def clasificar_segmento(top3):
    categorias = {
        "FASHIONISTAS": 0,
        "TRENDSETTERS": 0,
        "PRAGMÁTICOS": 0,
        "AHORRADORES": 0
    }

    for atributo in top3:
        texto = atributo.lower()
        if any(x in texto for x in ["estilo", "tendencia", "vestirme para el éxito"]):
            categorias["FASHIONISTAS"] += 1
        if any(x in texto for x in ["verdadero yo", "identidad", "crear un estilo"]):
            categorias["TRENDSETTERS"] += 1
        if any(x in texto for x in ["comodidad", "desaparecer", "no me preocupo"]):
            categorias["PRAGMÁTICOS"] += 1
        if any(x in texto for x in ["aceptado", "parte del grupo", "respetado"]):
            categorias["AHORRADORES"] += 1

    return max(categorias, key=categorias.get)

# 🧭 Resultado arriba si hay selección válida
ranking = st.session_state.get("ranking", [])

if "ranking" not in st.session_state:
    st.session_state.ranking = []

if len(st.session_state.ranking) == 3:
    segmento = clasificar_segmento(st.session_state.ranking)
    st.markdown(f"### 🧭 Tu segmento es: <span class='segmento'>{segmento}</span>", unsafe_allow_html=True)
    st.markdown("---")

# 🎯 Layout de columnas (izquierda: selección, derecha: ranking)
col1, col2 = st.columns(2)

with col1:
    st.markdown("## 🧩 Elige tus **3 atributos** más importantes:")
    seleccion = st.multiselect(
        "Selecciona exactamente 3 atributos:",
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
        st.info("Selecciona hasta 3 atributos a la izquierda.")

