import streamlit as st

# Configuración visual de la página
st.set_page_config(page_title="Nuestra Historia", page_icon="❤️")

# Estilo personalizado para que se vea más como una novela visual
st.markdown("""
    <style>
    .main {
        background-color: #fce4ec;
    }
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        height: 3em;
        background-color: #f06292;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# --- BASE DE DATOS DE LA HISTORIA ---
# Aquí puedes añadir más escenas fácilmente
historia = {
    0: {
        "personaje": "Protagonista",
        "texto": "Hola, felices 5 mesesitos mi niño... ❤️",
        "imagen": "https://via.placeholder.com/600x400?text=Imagen+Tierna+1", 
        "audio": None, # Puedes poner un link a un mp3 aquí
        "siguiente": 1
    },
    1: {
        "personaje": "Protagonista",
        "texto": "Ha sido un tiempo maravilloso a tu lado. ¿Quieres ver una sorpresa?",
        "imagen": "https://via.placeholder.com/600x400?text=Imagen+Tierna+2",
        "siguiente": 2
    },
    2: {
        "personaje": "Fin",
        "texto": "¡Te amo mucho! Gracias por estos 5 meses.",
        "imagen": "https://via.placeholder.com/600x400?text=Final+Feliz",
        "siguiente": None
    }
}

# --- LÓGICA DEL JUEGO ---
if 'paso' not in st.session_state:
    st.session_state.paso = 0

escena = historia[st.session_state.paso]

# Mostrar Imagen
st.image(escena["imagen"], use_container_width=True)

# Caja de Diálogo
st.subheader(f"**{escena['personaje']}:**")
st.write(escena["texto"])

# Botón para avanzar
if escena["siguiente"] is not None:
    if st.button("Siguiente ➔"):
        st.session_state.paso = escena["siguiente"]
        st.rerun()
else:
    if st.button("Volver a empezar"):
        st.session_state.paso = 0
        st.rerun()