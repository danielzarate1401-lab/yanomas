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

# --- 5. LÓGICA DE PANTALLAS ---

if not st.session_state.jugando:
    # --- PANTALLA DE INICIO ---
    # Lanzamos el efecto visual al cargar el menú
    st.snow() 
    
    st.write("") 
    st.write("")
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        # Imagen de portada
        st.image("https://github.com/danielzarate1401-lab/yanomas/blob/main/Creig%20Toker.jpeg?raw=true", use_container_width=True)
        
        # Título Estilizado
        st.markdown("""
            <h1 style='text-align: center; color: #d81b60; font-family: "Brush Script MT", cursive; font-size: 60px;'>
                Nuestra Historia ❤️
            </h1>
            <p style='text-align: center; font-size: 22px; color: #333;'>
                Un viaje por nuestros primeros 5 meses
            </p>
        """, unsafe_allow_html=True)
        
        st.write("")
        if st.button("✨ COMENZAR AVENTURA ✨", use_container_width=True):
            st.session_state.jugando = True
            st.rerun()

else:
    # --- PANTALLA DE JUEGO ---
    # Buscamos la escena actual (si no existe, va a la 0)
    escena = historia.get(st.session_state.paso, historia[0])
    
    # Control de Música: Solo cambia si el link es distinto
    if escena.get("musica") != st.session_state.musica_actual:
        st.session_state.musica_actual = escena.get("musica")
        if escena.get("musica"):
            st.audio(escena["musica"], format="audio/mp3", autoplay=True)

    # Diseño de la Escena
    c1, c2, c3 = st.columns([1, 2, 1])
    
    with c2:
        # Imagen con efecto Shake si aplica
        clase_anim = "personaje-shake" if escena.get("animacion") == "shake" else ""
        st.markdown(f'''
            <img src="{escena["imagen"]}" 
                 class="{clase_anim}" 
                 style="width:100%; border-radius:20px; border: 5px solid white; box-shadow: 0px 10px 30px rgba(0,0,0,0.2);">
        ''', unsafe_allow_html=True)
        
        # Caja de Texto
        st.markdown(f"""
            <div class="dialogo-box">
                <div class="nombre-personaje">{escena['personaje']}</div>
                {escena['texto']}
            </div>
        """, unsafe_allow_html=True)

        st.write("")

        # Lógica de Botones (Opciones vs Continuar)
        if "opciones" in escena:
            cols_btn = st.columns(len(escena["opciones"]))
            for i, opt in enumerate(escena["opciones"]):
                if cols_btn[i].button(opt["texto"], use_container_width=True):
                    st.session_state.paso = opt["destino"]
                    st.rerun()
        else:
            sig = escena.get("siguiente")
            if sig is not None:
                if st.button("Continuar ➔", use_container_width=True):
                    st.session_state.paso = sig
                    st.rerun()
            else:
                # Botón Final que regresa al menú
                if st.button("Finalizar con Amor ❤️", use_container_width=True):
                    st.balloons()
                    st.session_state.paso = 0
                    st.session_state.jugando = False # Regresa a la pantalla de inicio
                    st.rerun()
