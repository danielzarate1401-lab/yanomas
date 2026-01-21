import streamlit as st

# --- 1. CONFIGURACIÓN ---
st.set_page_config(page_title="Felices 5 meses", layout="wide")

# Estilos CSS
st.markdown("""
    <style>
    .stApp { background: linear-gradient(to bottom, #ffdde1, #ee9ca7); }
    .dialogo-box {
        background-color: rgba(255, 255, 255, 0.8);
        border: 3px solid #f06292;
        border-radius: 15px;
        padding: 20px;
        margin-top: 20px;
        color: #333;
        font-family: 'Verdana', sans-serif;
        font-size: 20px;
    }
    .nombre-personaje { font-weight: bold; color: #d81b60; font-size: 24px; }
    @keyframes shake {
      0% { transform: translate(1px, 1px) rotate(0deg); }
      10% { transform: translate(-1px, -2px) rotate(-1deg); }
      50% { transform: translate(-1px, 2px) rotate(-1deg); }
      100% { transform: translate(1px, -2px) rotate(-1deg); }
    }
    .personaje-shake { animation: shake 0.5s infinite; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. LÓGICA DE ESTADO (Sin espacios al inicio) ---
if 'paso' not in st.session_state:
    st.session_state.paso = 0

if 'musica_actual' not in st.session_state:
    st.session_state.musica_actual = None

# --- 3. BASE DE DATOS ---
historia = {
    0: {
        "personaje": "Daniel",
        "texto": "Mi niño bonito, hoy cumplimos un mes más de relación...",
        "imagen": "https://github.com/danielzarate1401-lab/yanomas/blob/main/Creig%20Toker.jpeg?raw=true",
        "siguiente": 1
    },
    1: {
        "personaje": "Daniel",
        "texto": "Quiero dar lo mejor de mí para ti y por ambos.",
        "imagen": "https://github.com/danielzarate1401-lab/yanomas/blob/main/Creig%20Toker.jpeg?raw=true",
        "siguiente": 2
    },
    2: {
        "personaje": "Daniel",
        "texto": "A programar, a vivir, a ser un novio tan bueno como tú.",
        "imagen": "https://github.com/danielzarate1401-lab/yanomas/blob/main/Creig%20Toker.jpeg?raw=true",
        "siguiente": 3
    },
    3: {
        "personaje": "Daniel",
        "texto": "Porque aunque tú digas que no, eres el mejor novio del mundo. ❤️",
        "imagen": "https://github.com/danielzarate1401-lab/yanomas/blob/main/Creig%20Toker.jpeg?raw=true",
        "animacion": "shake",
        "siguiente": 4
    },
    4: {
        "personaje": "Daniel",
        "texto": "Jamás me había sentido tan querido y correspondido por alguien.",
        "imagen": "https://github.com/danielzarate1401-lab/yanomas/blob/main/Creig%20Toker.jpeg?raw=true",
        "siguiente": 5
    },
    5: {
        "personaje": "Daniel",
        "texto": "Haces que quiera dejar de huir de los problemas. Haces que me sienta bien conmigo mismo.",
        "imagen": "https://github.com/danielzarate1401-lab/yanomas/blob/main/Creig%20Toker.jpeg?raw=true",
        "siguiente": 6
    },
    6: {
        "personaje": "Daniel",
        "texto": "Haces que quiera dar más de mí sin sentirme presionado. Te amo tanto.",
        "imagen": "https://github.com/danielzarate1401-lab/yanomas/blob/main/Creig%20Toker.jpeg?raw=true",
        "siguiente": 7
    },
    7: {
        "personaje": "Daniel",
        "texto": "Mi niño... ya que me gusta ser mandoneado, responde una pregunta:",
        "imagen": "https://github.com/danielzarate1401-lab/yanomas/blob/main/Creig%20Toker.jpeg?raw=true",
        "siguiente": 8
    },
    8: {
        "personaje": "Daniel",
        "texto": "¿Qué quieres hacer ahora?",
        "imagen": "https://github.com/danielzarate1401-lab/yanomas/blob/main/Creig%20Toker.jpeg?raw=true",
        "opciones": [
            {"texto": "Recordar", "destino": 10},
            {"texto": "Planificar", "destino": 20}
        ]
    },
    10: {
        "personaje": "Daniel",
        "texto": "Elegiste recordar... Vamos al pasado. ❤️",
        "imagen": "https://github.com/danielzarate1401-lab/yanomas/blob/main/Creig%20Toker.jpeg?raw=true",
        "siguiente": None
    },
    20: {
        "personaje": "Daniel",
        "texto": "Elegiste planificar... ¡Nuestro futuro será increíble!",
        "imagen": "https://github.com/danielzarate1401-lab/yanomas/blob/main/Creig%20Toker.jpeg?raw=true",
        "siguiente": None
    }
}

# Obtener escena actual
escena = historia.get(st.session_state.paso, historia[0])

# --- 4. RENDERIZADO ---
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    clase_anim = "personaje-shake" if escena.get("animacion") == "shake" else ""
    st.markdown(f'<img src="{escena["imagen"]}" class="{clase_anim}" style="width:100%; border-radius:20px; border: 5px solid white;">', unsafe_allow_html=True)
    
    st.markdown(f'<div class="dialogo-box"><div class="nombre-personaje">{escena["personaje"]}</div>{escena["texto"]}</div>', unsafe_allow_html=True)
    
    st.write("")

    if "opciones" in escena:
        cols = st.columns(len(escena["opciones"]))
        for i, opt in enumerate(escena["opciones"]):
            if cols[i].button(opt["texto"]):
                st.session_state.paso = opt["destino"]
                st.rerun()
    else:
        siguiente = escena.get("siguiente")
        if siguiente is not None:
            if st.button("Continuar ➔"):
                st.session_state.paso = siguiente
                st.rerun()
        else:
            if st.button("Finalizar ❤️"):
                st.balloons()
                st.session_state.paso = 0
                st.rerun()
