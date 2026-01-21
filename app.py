import streamlit as st

# --- 1. CONFIGURACIÓN ---
st.set_page_config(page_title="Felices 5 meses", layout="wide")

# --- 2. ESTILOS CSS ---
st.markdown("""
    <style>
    .stApp { background: linear-gradient(to bottom, #ffdde1, #ee9ca7); }
    .dialogo-box {
        background-color: rgba(255, 255, 255, 0.85);
        border: 3px solid #f06292;
        border-radius: 15px;
        padding: 25px;
        margin-top: 20px;
        color: #333;
        font-family: 'Verdana', sans-serif;
        font-size: 18px;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
    }
    .nombre-personaje { font-weight: bold; color: #d81b60; font-size: 22px; margin-bottom: 8px; }
    
    /* Animación de sacudida */
    @keyframes shake {
      0% { transform: translate(1px, 1px) rotate(0deg); }
      10% { transform: translate(-1px, -2px) rotate(-1deg); }
      30% { transform: translate(3px, 2px) rotate(0deg); }
      50% { transform: translate(-1px, 2px) rotate(-1deg); }
      100% { transform: translate(1px, -2px) rotate(-1deg); }
    }
    .personaje-shake { animation: shake 0.5s infinite; }
    
    /* Botones personalizados */
    .stButton>button {
        border-radius: 20px;
        border: 2px solid #f06292;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #f06292;
        color: white;
        transform: scale(1.05);
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. INICIALIZACIÓN DE ESTADOS (MEMORIA) ---
if 'paso' not in st.session_state:
    st.session_state.paso = 0
if 'musica_actual' not in st.session_state:
    st.session_state.musica_actual = "ninguna"
if 'jugando' not in st.session_state:
    st.session_state.jugando = False

# --- 4. BASE DE DATOS (HISTORIA) ---
historia = {
    0: {
        "personaje": "Daniel",
        "texto": "Mi niño bonito, hoy cumplimos un mes más de relación y ahora que es parte de otro año quiero que sea más especial.",
        "imagen": "https://github.com/danielzarate1401-lab/yanomas/blob/main/Creig%20Toker.jpeg?raw=true",
        "musica": "https://raw.githubusercontent.com/danielzarate1401-lab/yanomas/main/el%20profe.mp3",
        "siguiente": 1
    },
    1: {
        "personaje": "Daniel",
        "texto": "Quiero dar lo mejor de mí para ti y por ambos. Por nuestro futuro y pasado, quiero aprender muchas más cosas.",
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
        "texto": "Porque aunque tú digas que no, eres el mejor novio del mundo.",
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
        "texto": "Haces que quiera dar más de mí sin sentirme presionado. Te amo tanto, gracias por ser tú.",
        "imagen": "https://github.com/danielzarate1401-lab/yanomas/blob/main/Creig%20Toker.jpeg?raw=true",
        "siguiente": 7
    },
    7: {
        "personaje": "Daniel",
        "texto": "Mi niño... Bueno, ya que me gusta ser mandoneado, me gustaría que respondas una pregunta:",
        "imagen": "https://github.com/danielzarate1401-lab/yanomas/blob/main/Creig%20Toker.jpeg?raw=true",
        "siguiente": 8
    },
    8: {
        "personaje": "Daniel",
        "texto": "¿Qué quieres hacer?",
        "imagen": "https://github.com/danielzarate1401-lab/yanomas/blob/main/Creig%20Toker.jpeg?raw=true",
        "opciones": [
            {"texto": "Recordar (Pasado)", "destino": 10},
            {"texto": "Planificar (Futuro)", "destino": 20}
        ]
    },
    # CAMINO RECORDAR
    10: {
        "personaje": "Daniel",
        "texto": "Elegiste recordar... (Escribe aquí tu primer recuerdo)",
        "imagen": "https://github.com/danielzarate1401-lab/yanomas/blob/main/Creig%20Toker.jpeg?raw=true",
        "siguiente": None
    },
    # CAMINO PLANIFICAR
    20: {
        "personaje": "Daniel",
        "texto": "Elegiste planificar... (Escribe aquí tus planes)",
        "imagen": "https://github.com/danielzarate1401-lab/yanomas/blob/main/Creig%20Toker.jpeg?raw=true",
        "siguiente": None
    }
}

# --- 5. LÓGICA DE PANTALLAS ---

if not st.session_state.jugando:
    # PANTALLA DE INICIO
    st.snow()
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.write("")
        st.write("")
        st.image("https://github.com/danielzarate1401-lab/yanomas/blob/main/Creig%20Toker.jpeg?raw=true", use_container_width=True)
        st.markdown("<h1 style='text-align: center; color: #d81b60; font-family: cursive;'>Nuestra Historia ❤️</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'>Un regalo especial para mi niño</p>", unsafe_allow_html=True)
        if st.button("✨ COMENZAR ✨", use_container_width=True):
            st.session_state.jugando = True
            st.rerun()
else:
    # PANTALLA DE JUEGO
    escena = historia.get(st.session_state.paso, historia[0])
    
    # Manejo de audio
   nueva_musica = escena.get("musica", st.session_state.musica_actual)
    
    if "musica" in escena: # Si la escena define música (aunque sea None)
        if escena["musica"] != st.session_state.musica_actual:
            st.session_state.musica_actual = escena["musica"]
            if escena["musica"]:
                st.audio(escena["musica"], format="audio/mp3", autoplay=True, loop=True)
            else:
                # Si es None, no renderizamos el audio y la música se detiene al recargar
                st.write("🎵 *Silencio*")

    c1, c2, c3 = st.columns([1, 2, 1])
    with c2:
        clase_anim = "personaje-shake" if escena.get("animacion") == "shake" else ""
        st.markdown(f'<img src="{escena["imagen"]}" class="{clase_anim}" style="width:100%; border-radius:20px; border: 5px solid white;">', unsafe_allow_html=True)
        
        st.markdown(f"""
            <div class="dialogo-box">
                <div class="nombre-personaje">{escena['personaje']}</div>
                {escena['texto']}
            </div>
        """, unsafe_allow_html=True)

        st.write("")
        
        if "opciones" in escena:
            cols = st.columns(len(escena["opciones"]))
            for i, opt in enumerate(escena["opciones"]):
                if cols[i].button(opt["texto"], key=f"btn_{i}", use_container_width=True):
                    st.session_state.paso = opt["destino"]
                    st.rerun()
        else:
            sig = escena.get("siguiente")
            if sig is not None:
                if st.button("Continuar ➔", use_container_width=True):
                    st.session_state.paso = sig
                    st.rerun()
            else:
                if st.button("Finalizar ❤️", use_container_width=True):
                    st.balloons()
                    st.session_state.paso = 0
                    st.session_state.jugando = False
                    st.rerun()
