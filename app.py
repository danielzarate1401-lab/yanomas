# --- BASE DE DATOS DE TU HISTORIA ---
historia = {
    0: {
        "personaje": "Daniel",
        "texto": "Mi niño bonito, hoy cumplimos un mes más de relación y ahora que es parte de otro año quiero que sea más especial...",
        "imagen": "TU_URL_AQUÍ",
        "musica": "TU_URL_MUSICA_INICIO",
        "siguiente": 1
    },
    1: {
        "personaje": "Daniel",
        "texto": "Quiero dar lo mejor de mí para ti y por ambos. Por nuestro futuro y pasado, quiero aprender muchas más cosas...",
        "imagen": "TU_URL_AQUÍ",
        "siguiente": 2
    },
    2: {
        "personaje": "Daniel",
        "texto": "A programar, a vivir, a ser un novio tan bueno como tú.",
        "imagen": "TU_URL_AQUÍ",
        "siguiente": 3
    },
    3: {
        "personaje": "Daniel",
        "texto": "Porque aunque tú digas que no, eres el mejor novio del mundo. ❤️",
        "imagen": "TU_URL_AQUÍ",
        "animacion": "shake",
        "siguiente": 4
    },
    4: {
        "personaje": "Daniel",
        "texto": "Jamás me había sentido tan querido y correspondido por alguien.",
        "imagen": "TU_URL_AQUÍ",
        "siguiente": 5
    },
    5: {
        "personaje": "Daniel",
        "texto": "Haces que quiera dejar de huir de los problemas. Haces que me sienta bien conmigo mismo.",
        "imagen": "TU_URL_AQUÍ",
        "siguiente": 6
    },
    6: {
        "personaje": "Daniel",
        "texto": "Haces que quiera dar más de mí sin sentirme presionado. Te amo tanto, gracias por ser tú.",
        "imagen": "TU_URL_AQUÍ",
        "siguiente": 7
    },
    7: {
        "personaje": "Daniel",
        "texto": "Mi niño... Bueno, ya que me gusta ser mandoneado, me gustaría que respondas una pregunta:",
        "imagen": "TU_URL_AQUÍ",
        "siguiente": 8
    },
    8: {
        "personaje": "Daniel",
        "texto": "¿Qué quieres hacer ahora?",
        "imagen": "TU_URL_AQUÍ",
        "opciones": [
            {"texto": "Recordar (Pasado)", "destino": 10},
            {"texto": "Planificar (Futuro)", "destino": 20}
        ]
    },

    # --- CAMINO: RECORDAR (Empieza en 10) ---
    10: {
        "personaje": "Daniel",
        "texto": "Elegiste recordar... Vamos a dar un viaje por estos 5 meses.",
        "imagen": "TU_URL_PASADO",
        "musica": "TU_URL_MUSICA_NOSTALGICA",
        "siguiente": None 
    },
    # ... sigue añadiendo 11, 12, etc.

    # --- CAMINO: PLANIFICAR (Empieza en 20) ---
    20: {
        "personaje": "Daniel",
        "texto": "¡Me encanta mirar hacia adelante contigo! Esto es lo que sueño...",
        "imagen": "TU_URL_FUTURO",
        "musica": "TU_URL_MUSICA_ALEGRE",
        "siguiente": None
    },
    # ... sigue añadiendo 21, 22, etc.
}

# Lógica de estado
if 'paso' not in st.session_state:
    st.session_state.paso = 0

escena = historia[st.session_state.paso]

# --- RENDERIZADO ---
col1, col2, col3 = st.columns([1, 2, 1]) # Centrar contenido

with col2:
    # Mostrar Imagen con bordes redondeados (vía HTML)
    st.markdown(f'<img src="{escena["imagen"]}" style="width:100%; border-radius:20px; border: 5px solid white;">', unsafe_allow_html=True)
    
    # Caja de diálogo estilizada
    st.markdown(f"""
        <div class="dialogo-box">
            <div class="nombre-personaje">{escena['personaje']}</div>
            {escena['texto']}
        </div>
    """, unsafe_allow_html=True)

    st.write("") # Espacio
    
    # Botón centrado
    if st.button("Continuar"):
        if escena["siguiente"] is not None:
            st.session_state.paso = escena["siguiente"]
            st.rerun()
