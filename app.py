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
        "texto": "Te amo tanto, gracias por ser tu",
        "imagen": "https://github.com/danielzarate1401-lab/yanomas/blob/main/Creig%20Toker.jpeg?raw=true",
        "siguiente": 8
    },
    8: {
        "personaje": "Daniel",
        "texto": "Mi niño",
        "imagen": "https://github.com/danielzarate1401-lab/yanomas/blob/main/Creig%20Toker.jpeg?raw=true",
        "siguiente": 9
    },
    9: {
        "personaje": "Daniel",
        "texto": "Te gusta esta novela visual?",
        "imagen": "https://github.com/danielzarate1401-lab/yanomas/blob/main/Creig%20Toker.jpeg?raw=true",
        "siguiente": 10
    },
    10: {
        "personaje": "Daniel",
        "texto": "Tiene muchos personajes y eso, soy yo y, yo y también esta yo, y sans deltarune ",
        "imagen": "https://github.com/danielzarate1401-lab/yanomas/blob/main/Creig%20Toker.jpeg?raw=true",
        "siguiente": 11
    },
    11: {
        "personaje": "Daniel",
        "texto": "Ah y estas tu creo ",
        "imagen": "https://github.com/danielzarate1401-lab/yanomas/blob/main/Creig%20Toker.jpeg?raw=true",
        "siguiente": 12
    },
    12: {
        "personaje": "Daniel",
        "texto": "Bueno, como otras novelas visuales esta tiene opciones de dialogos, viste asi se bueno soy",
        "imagen": "https://github.com/danielzarate1401-lab/yanomas/blob/main/Creig%20Toker.jpeg?raw=true",
        "siguiente": 13
    },
    13: {
        "personaje": "Daniel",
        "texto": "Que te parece?",
        "imagen": "https://github.com/danielzarate1401-lab/yanomas/blob/main/Creig%20Toker.jpeg?raw=true", 
         "opciones": [
            {"texto": "Menea la chapa remix", "destino": 14},
            {"texto": "Amarillo amarillo platano", "destino": 14}
    },
    14: {
        "personaje": "Daniel",
        "texto": "Yo se yo se, increible.",
        "imagen": "https://github.com/danielzarate1401-lab/yanomas/blob/main/Creig%20Toker.jpeg?raw=true",
        "siguiente": 15
    },
    15: {
        "personaje": "Daniel",
        "texto": "Oye",
        "imagen": "https://github.com/danielzarate1401-lab/yanomas/blob/main/Creig%20Toker.jpeg?raw=true",
        "siguiente": 16
    },
    16: {
        "personaje": "Daniel",
        "texto": "Me gustas",
        "imagen": "https://github.com/danielzarate1401-lab/yanomas/blob/main/Creig%20Toker.jpeg?raw=true",
        "siguiente": 17
    },
    17: {
        "personaje": "Daniel",
        "texto": "Me gustas mucho",
        "imagen": "https://github.com/danielzarate1401-lab/yanomas/blob/main/Creig%20Toker.jpeg?raw=true",
        "siguiente": 18
    },
    18: {
        "personaje": "Daniel",
        "texto": "Me gustas tanto que quiero esforzarme",
        "imagen": "https://github.com/danielzarate1401-lab/yanomas/blob/main/Creig%20Toker.jpeg?raw=true",
        "siguiente": 19
    },
    19: {
        "personaje": "Daniel",
        "texto": "Tanto como para pensar el el pasado de forma bonita ",
        "imagen": "https://github.com/danielzarate1401-lab/yanomas/blob/main/Creig%20Toker.jpeg?raw=true",
        "siguiente": 20
    },
    20: {
        "personaje": "Daniel",
        "texto": "O como para esforzarme por un buen futuro",
        "imagen": "https://github.com/danielzarate1401-lab/yanomas/blob/main/Creig%20Toker.jpeg?raw=true",
        "siguiente": 21
    },
    21: {
        "personaje": "Daniel",
        "texto": "Mi niño lindo",
        "imagen": "https://github.com/danielzarate1401-lab/yanomas/blob/main/Creig%20Toker.jpeg?raw=true",
        "siguiente": 22
    },
    22: {
        "personaje": "Daniel",
        "texto": "Feliz quinto mes ",
        "imagen": "https://github.com/danielzarate1401-lab/yanomas/blob/main/Creig%20Toker.jpeg?raw=true",
        "siguiente": 23
    },
    23: {
        "personaje": "Daniel",
        "texto": "Mi niño... Bueno, ya que me gusta ser mandoneado, me gustaría que respondas una pregunta:",
        "imagen": "https://github.com/danielzarate1401-lab/yanomas/blob/main/Creig%20Toker.jpeg?raw=true",
        "siguiente": 24
    },
    24: {
        "personaje": "Daniel",
        "texto": "¿Qué quieres hacer?",
        "imagen": "https://github.com/danielzarate1401-lab/yanomas/blob/main/Creig%20Toker.jpeg?raw=true",
        "opciones": [
            {"texto": "Recordar", "destino": 25},
            {"texto": "Planificar", "destino": 54}
        ]
    },
    # CAMINO RECORDAR
    25: {
        "personaje": "Daniel",
        "texto": "Hmmmm",
        "imagen": "https://github.com/danielzarate1401-lab/yanomas/blob/main/Creig%20Toker.jpeg?raw=true",
        "siguiente": 26
    },
    26: {
        "personaje": "Daniel",
        "texto": "Sabes, no me gustaba mucho recordar las cosas ",
        "imagen": "https://github.com/danielzarate1401-lab/yanomas/blob/main/Creig%20Toker.jpeg?raw=true",
        "siguiente": 27
    },
    27: {
        "personaje": "Daniel",
        "texto": "Nunca de hecho, es como un metodo de defenza para no deprimirme  ",
        "imagen": "https://github.com/danielzarate1401-lab/yanomas/blob/main/Creig%20Toker.jpeg?raw=true",
        "siguiente": 28
    },
    28: {
        "personaje": "Daniel",
        "texto": "Solo ",
        "imagen": "https://github.com/danielzarate1401-lab/yanomas/blob/main/Creig%20Toker.jpeg?raw=true",
        "siguiente": 29
    },
    29: {
        "personaje": "Daniel",
        "texto": "Cada que pensaba en el pasado ",
        "imagen": "https://github.com/danielzarate1401-lab/yanomas/blob/main/Creig%20Toker.jpeg?raw=true",
        "siguiente": 30
    },
    30: {
        "personaje": "Daniel",
        "texto": "Me venian a la mente malos recuerdos ",
        "imagen": "https://github.com/danielzarate1401-lab/yanomas/blob/main/Creig%20Toker.jpeg?raw=true",
        "siguiente": 31
    },
    31: {
        "personaje": "Daniel",
        "texto": "Momentos horribles",
        "imagen": "https://github.com/danielzarate1401-lab/yanomas/blob/main/Creig%20Toker.jpeg?raw=true",
        "siguiente": 32
    },
    32: {
        "personaje": "Daniel",
        "texto": "Cosas de las que me arrepiento",
        "imagen": "https://github.com/danielzarate1401-lab/yanomas/blob/main/Creig%20Toker.jpeg?raw=true",
        "siguiente": 33
    },
    33: {
        "personaje": "Daniel",
        "texto": "Dias que preferiria que no hayan existido ",
        "imagen": "https://github.com/danielzarate1401-lab/yanomas/blob/main/Creig%20Toker.jpeg?raw=true",
        "siguiente": 34
    },
    34: {
        "personaje": "Daniel",
        "texto": "Prefiero evitar los problemas, pero",
        "imagen": "https://github.com/danielzarate1401-lab/yanomas/blob/main/Creig%20Toker.jpeg?raw=true",
        "siguiente": 35
    },
    35: {
        "personaje": "Daniel",
        "texto": "Ahora hay algo que cambia, estas tu aqui conmigo :3",
        "imagen": "https://github.com/danielzarate1401-lab/yanomas/blob/main/Creig%20Toker.jpeg?raw=true",
        "siguiente": 36
    },
    36: {
        "personaje": "Daniel",
        "texto": "21 de Agosto de 2025... Justo andaba escuchando el OST de Undertale hace unos minutos. ¡Hahaha!",
        "imagen": "[EMOCIÓN: Nostálgico]",
        "siguiente": 37
    },
    37: {
        "personaje": "Daniel",
        "texto": "Jajajaj, ¿sí se escucha como Hopes and Dreams? Aún la sigo practicando. Justo el inicio se me complica un poquito.",
        "imagen": "[EMOCIÓN: Alegre]",
        "siguiente": 38
    },
    38: {
        "personaje": "Daniel",
        "texto": "Para que te hagas una idea, ya con las primeras tres notas supe que era Hopes and Dreams. Fue tan simple, pero de un momento para otro, una ligera forma de querer llamar tu atención funcionó.",
        "imagen": "[EMOCIÓN: Enamorado]",
        "siguiente": 39
    },
    39: {
        "personaje": "Daniel",
        "texto": "Me hizo feliz. Capté la atención del que no sabía que sería el mejor novio del mundo.",
        "imagen": "[EMOCIÓN: Conmovido]",
        "siguiente": 40
    },
    40: {
        "personaje": "Daniel",
        "texto": "¿Recuerdas cómo fue cuando te pregunté si querías ser mi pareja? Sonabas tan decaído en ese momento, tan triste por lo que estabas pasando...",
        "imagen": "[EMOCIÓN: Preocupado]",
        "animacion": "shake",
        "siguiente": 41
    },
    41: {
        "personaje": "Daniel",
        "texto": "Y yo, ciertamente te quería hacer feliz. Quizás es algo en lo que a veces no tengo tacto, pero me alegro de que desde ese día seamos pareja.",
        "imagen": "[EMOCIÓN: Sincero]",
        "siguiente": 42
    },
    42: {
        "personaje": "Daniel",
        "texto": "Hemos vivido muchos momentos graciosos y bonitos, como la vez que hicimos al Kris y a Ralsei, o dibujos en conjunto como Caín y Abel.",
        "imagen": "[EMOCIÓN: Muy Feliz]",
        "siguiente": 43
    },
    43: {
        "personaje": "Daniel",
        "texto": "Cuando vimos Hazbin Hotel... ¡Por ti empecé a ver South Park, por cierto! Todos los personajes con los que nos identificamos:",
        "imagen": "[EMOCIÓN: Entusiasmado]",
        "siguiente": 44
    },
    44: {
        "personaje": "Daniel",
        "texto": "Somos Ralsei y Kris, Pinkie Pie y Sunset, Tweek y Craig, Charlie y Nick, Charlie y Pim, Charlie y Vaggie, Charlie y Kirk, Trump y Satanás...",
        "imagen": "[EMOCIÓN: Divertido]",
        "siguiente": 45
    },
    45: {
        "personaje": "Daniel",
        "texto": "...Elle y Tao, Johnny y Gyro, Denji y Asa, las torres gemelas y el avión... y por supuesto que somos Sonic y Shadow. :3",
        "imagen": "[EMOCIÓN: Divertido]",
        "siguiente": 46
    },
    46: {
        "personaje": "Daniel",
        "texto": "¿Recuerdas cuando jugamos a tener una tienda? Fue tan divertido ese día. 'Te quiero presentar al oso, el amor de mi... es como un hijo para mí'.",
        "imagen": "[EMOCIÓN: Riendo]",
        "siguiente": 47
    },
    47: {
        "personaje": "Daniel",
        "texto": "'¡NOO, TÚ NO IBAS A DECIR ESO!' '¿POR QUÉ ACTUABAS COMO SI NO ME IBA A DAR CUENTA?'. Amo, amo pasar tiempo contigo. Es tan divertido cuando estamos en llamada.",
        "imagen": "[EMOCIÓN: Alegre]",
        "siguiente": 48
    },
    48: {
        "personaje": "Daniel",
        "texto": "Ciertamente, también hemos tenido malos momentos. Momentos en los que nos sentimos decaídos, con ganas de llorar por problemas adversos o incluso por el otro.",
        "imagen": "[EMOCIÓN: Triste]",
        "animacion": "shake",
        "siguiente": 49
    },
    49: {
        "personaje": "Daniel",
        "texto": "Son cosas por las que también hemos pasado. Te he hecho daño. Son malos recuerdos, pero no quiero olvidarlos.",
        "imagen": "[EMOCIÓN: Arrepentido]",
        "siguiente": 50
    },
    50: {
        "personaje": "Daniel",
        "texto": "No quiero volver a equivocarme, ni a dañarte. No quiero ser alguien más que te haga daño. No quiero actuar como si nunca hice nada malo, porque no mereces que ignore cosas que sí pasaron.",
        "imagen": "[EMOCIÓN: Serio]",
        "siguiente": 51
    },
    51: {
        "personaje": "Daniel",
        "texto": "Mereces que aprenda de mis equivocaciones, las solucione y las afronte. Porque eres alguien que vale la pena, porque me motivas a ser mejor persona.",
        "imagen": "[EMOCIÓN: Determinado]",
        "siguiente": 52
    },
    52: {
        "personaje": "Daniel",
        "texto": "Te amo. Te amo tanto.",
        "imagen": "[EMOCIÓN: Enamorado]",
        "siguiente": 53
    },
    53: {
        "personaje": "Daniel",
        "texto": "Mi niño, felices 5 mesesitos.",
        "imagen": "[EMOCIÓN: Final Feliz]",
        "siguiente": None
    },
    # CAMINO PLANIFICAR
    54: {
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
    # --- PANTALLA DE JUEGO ---
    escena = historia.get(st.session_state.paso, historia[0])
    
    # --- 2. CONTROL DE AUDIO GLOBAL ---
    # Si la escena tiene música definida, actualizamos el estado
    if "musica" in escena:
        st.session_state.musica_actual = escena["musica"]

    # Reproducimos la música actual SIEMPRE que haya una definida
    # Esto evita que se corte al cambiar de diálogo
    if st.session_state.musica_actual and st.session_state.musica_actual != "ninguna":
        st.audio(st.session_state.musica_actual, format="audio/mp3", autoplay=True, loop=True)
    
    # Si quieres una opción de silencio visual cuando no hay música
    if not st.session_state.musica_actual:
        st.write("🎵 *Silencio*")

    # --- 3. DISEÑO VISUAL ---
    c1, c2, c3 = st.columns([1, 2, 1])
    
    with c2:
        # Imagen
        clase_anim = "personaje-shake" if escena.get("animacion") == "shake" else ""
        st.markdown(f'''
            <img src="{escena["imagen"]}" 
                 class="{clase_anim}" 
                 style="width:100%; border-radius:20px; border: 5px solid white;">
        ''', unsafe_allow_html=True)
        
        # Caja de Diálogo
        st.markdown(f"""
            <div class="dialogo-box">
                <div class="nombre-personaje">{escena['personaje']}</div>
                {escena['texto']}
            </div>
        """, unsafe_allow_html=True)

        st.write("") 

        # --- 4. LÓGICA DE BOTONES ---
        if "opciones" in escena:
            cols_btn = st.columns(len(escena["opciones"]))
            for i, opt in enumerate(escena["opciones"]):
                if cols_btn[i].button(opt["texto"], key=f"btn_opt_{i}", use_container_width=True):
                    st.session_state.paso = opt["destino"]
                    st.rerun()
        else:
            sig = escena.get("siguiente")
            if sig is not None:
                if st.button("Continuar ➔", key="btn_next", use_container_width=True):
                    st.session_state.paso = sig
                    st.rerun()
            else:
                if st.button("Finalizar ❤️", key="btn_final", use_container_width=True):
                    st.balloons()
                    st.session_state.paso = 0
                    st.session_state.jugando = False
                    st.session_state.musica_actual = "ninguna"
                    st.rerun()
