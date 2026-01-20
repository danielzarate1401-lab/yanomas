import streamlit as st

# --- CONFIGURACIÓN ESTÉTICA ---
st.set_page_config(page_title="felices 5 meses, mi niño lindo, te amo", layout="wide")

# Inyectamos CSS para cambiar el look total de la página
st.markdown("""
    <style>
    /* Cambiar el fondo de toda la página */
    .stApp {
        background: linear-gradient(to bottom, #ffdde1, #ee9ca7);
    }
    
    /* Estilo para la caja de diálogo */
    .dialogo-box {
        background-color: rgba(255, 255, 255, 0.8);
        border: 3px solid #f06292;
        border-radius: 15px;
        padding: 20px;
        margin-top: 20px;
        color: #333;
        font-family: 'Verdana', sans-serif;
        font-size: 20px;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
    }

    /* Estilo para el nombre del personaje */
    .nombre-personaje {
        font-weight: bold;
        color: #d81b60;
        margin-bottom: 5px;
        font-size: 24px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- BASE DE DATOS MEJORADA ---
historia = {
    0: {
        "personaje": "Daniel",
        "texto": "Hola, amorcito, es curioso, nos conocimos juso cuando tu estabas programando... ❤️",
        "imagen": "https://github.com/danielzarate1401-lab/yanomas/blob/main/Creig%20Toker.jpeg?raw=true", # Reemplaza con tu URL
        "siguiente": 1
    },
    1: {
        "personaje": "Daniel",
        "texto": "Tenias razon, es muy divertido cuando aprendes a hacerlo, cof cof ia.",
        "imagen": "https://github.com/danielzarate1401-lab/yanomas/blob/main/Creig%20Toker.jpeg?raw=true",
        "siguiente": 2
    },
    2: {
        "personaje": "Daniel",
        "texto": "Resulta que, si quiero ser lo mejor para ti, debo aprender a programar como tu.",
        "imagen": "https://github.com/danielzarate1401-lab/yanomas/blob/main/Creig%20Toker.jpeg?raw=true",
        "siguiente": 3
    },
    3: {
        "personaje": "Daniel",
        "texto": "este año sera uno muy bueno donde lograremos mucho por ambos, mi niño.",
        "imagen": "https://github.com/danielzarate1401-lab/yanomas/blob/main/Creig%20Toker.jpeg?raw=true",
        "siguiente": 4
    }
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
