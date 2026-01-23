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
    
    @keyframes shake {
      0% { transform: translate(1px, 1px) rotate(0deg); }
      10% { transform: translate(-1px, -2px) rotate(-1deg); }
      30% { transform: translate(3px, 2px) rotate(0deg); }
      50% { transform: translate(-1px, 2px) rotate(-1deg); }
      100% { transform: translate(1px, -2px) rotate(-1deg); }
    }
    .personaje-shake { animation: shake 0.5s infinite; }
    
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

# --- 3. INICIALIZACIÓN DE ESTADOS ---
if 'paso' not in st.session_state:
    st.session_state.paso = 0
if 'musica_actual' not in st.session_state:
    st.session_state.musica_actual = "ninguna"
if 'jugando' not in st.session_state:
    st.session_state.jugando = False

# --- 4. BASE DE DATOS (HISTORIA) ---
# Imagen por defecto para evitar errores de carga
img_def = "https://github.com/danielzarate1401-lab/yanomas/blob/main/Creig%20Toker.jpeg?raw=true"

historia = {
    0: {
        "personaje": "Daniel",
        "texto": "Mi niño bonito, hoy cumplimos un mes más de relación y ahora que es parte de otro año quiero que sea más especial.",
        "imagen": img_def,
        "musica": "https://raw.githubusercontent.com/danielzarate1401-lab/yanomas/main/31%20minutos%20-%20Karaoke%20-%20Yo%20opino.mp3",
        "siguiente": 1
    },
    1: {
        "personaje": "Daniel",
        "texto": "Quiero dar lo mejor de mí para ti y por ambos. Por nuestro futuro y pasado, quiero aprender muchas más cosas.",
        "imagen": img_def,
        "siguiente": 2
    },
    2: {
        "personaje": "Daniel",
        "texto": "A programar, a vivir, a ser un novio tan bueno como tú.",
        "imagen": img_def,
        "siguiente": 3
    },
    3: {
        "personaje": "Daniel",
        "texto": "Porque aunque tú digas que no, eres el mejor novio del mundo.",
        "imagen": img_def,
        "animacion": "shake",
        "siguiente": 4
    },
    4: {
        "personaje": "Daniel",
        "texto": "Jamás me había sentido tan querido y correspondido por alguien.",
        "imagen": img_def,
        "siguiente": 5
    },
    5: {
        "personaje": "Daniel",
        "texto": "Haces que quiera dejar de huir de los problemas. Haces que me sienta bien conmigo mismo.",
        "imagen": img_def,
        "siguiente": 6
    },
    6: {
        "personaje": "Daniel",
        "texto": "Haces que quiera dar más de mí sin sentirme presionado. Te amo tanto, gracias por ser tú.",
        "imagen": img_def,
        "siguiente": 7
    },
    7: {
        "personaje": "Daniel",
        "texto": "Te amo tanto, gracias por ser tu",
        "imagen": img_def,
        "siguiente": 8
    },
    8: {
        "personaje": "Daniel",
        "texto": "Mi niño",
        "imagen": img_def,
        "siguiente": 9
    },
    9: {
        "personaje": "Daniel",
        "texto": "Te gusta esta novela visual?",
        "imagen": img_def,
        "siguiente": 10
    },
    10: {
        "personaje": "Daniel",
        "texto": "Tiene muchos personajes y eso, soy yo y, yo y también esta yo, y sans deltarune ",
        "imagen": img_def,
        "siguiente": 11
    },
    11: {
        "personaje": "Daniel",
        "texto": "Ah y estas tu creo ",
        "imagen": img_def,
        "siguiente": 12
    },
    12: {
        "personaje": "Daniel",
        "texto": "Bueno, como otras novelas visuales esta tiene opciones de dialogos, viste asi se bueno soy",
        "imagen": img_def,
        "siguiente": 13
    },
    13: {
        "personaje": "Daniel",
        "texto": "Que te parece?",
        "imagen": img_def,
         "opciones": [
            {"texto": "Menea la chapa remix", "destino": 14},
            {"texto": "Amarillo amarillo platano", "destino": 14}
         ] # <-- CORREGIDO AQUÍ
    },
    14: {
        "personaje": "Daniel",
        "texto": "Yo se yo se, increible.",
        "imagen": img_def,
        "siguiente": 15
    },
    15: {
        "personaje": "Daniel",
        "texto": "Oye",
        "imagen": img_def,
        "siguiente": 16
    },
    16: {
        "personaje": "Daniel",
        "texto": "Me gustas",
        "imagen": img_def,
        "siguiente": 17
    },
    17: {
        "personaje": "Daniel",
        "texto": "Me gustas mucho",
        "imagen": img_def,
        "siguiente": 18
    },
    18: {
        "personaje": "Daniel",
        "texto": "Me gustas tanto que quiero esforzarme",
        "imagen": img_def,
        "siguiente": 19
    },
    19: {
        "personaje": "Daniel",
        "texto": "Tanto como para pensar el el pasado de forma bonita ",
        "imagen": img_def,
        "siguiente": 20
    },
    20: {
        "personaje": "Daniel",
        "texto": "O como para esforzarme por un buen futuro",
        "imagen": img_def,
        "siguiente": 21
    },
    21: {
        "personaje": "Daniel",
        "texto": "Mi niño lindo",
        "imagen": img_def,
        "siguiente": 22
    },
    22: {
        "personaje": "Daniel",
        "texto": "Feliz quinto mes ",
        "imagen": img_def,
        "siguiente": 23
    },
    23: {
        "personaje": "Daniel",
        "texto": "Mi niño... Bueno, ya que me gusta ser mandoneado, me gustaría que respondas una pregunta:",
        "imagen": img_def,
        "siguiente": 24
    },
    24: {
        "personaje": "Daniel",
        "texto": "¿Qué quieres hacer?",
        "imagen": img_def,
        "musica": "ninguna",
        "opciones": [
            {"texto": "Recordar", "destino": 25},
            {"texto": "Planificar", "destino": 54}
        ]
    },
    25: {
        "personaje": "Daniel",
        "texto": "Hmmmm",
        "imagen": img_def,
        "musica": "https://raw.githubusercontent.com/danielzarate1401-lab/yanomas/main/el%20profe.mp3",
        "siguiente": 26
    },
    26: {
        "personaje": "Daniel",
        "texto": "Sabes, no me gustaba mucho recordar las cosas ",
        "imagen": img_def,
        "siguiente": 27
    },
    27: {
        "personaje": "Daniel",
        "texto": "Nunca de hecho, es como un metodo de defenza para no deprimirme  ",
        "imagen": img_def,
        "siguiente": 28
    },
    28: {
        "personaje": "Daniel",
        "texto": "Solo ",
        "imagen": img_def,
        "siguiente": 29
    },
    29: {
        "personaje": "Daniel",
        "texto": "Cada que pensaba en el pasado ",
        "imagen": img_def,
        "siguiente": 30
    },
    30: {
        "personaje": "Daniel",
        "texto": "Me venian a la mente malos recuerdos ",
        "imagen": img_def,
        "siguiente": 31
    },
    31: {
        "personaje": "Daniel",
        "texto": "Momentos horribles",
        "imagen": img_def,
        "siguiente": 32
    },
    32: {
        "personaje": "Daniel",
        "texto": "Cosas de las que me arrepiento",
        "imagen": img_def,
        "siguiente": 33
    },
    33: {
        "personaje": "Daniel",
        "texto": "Dias que preferiria que no hayan existido ",
        "imagen": img_def,
        "siguiente": 34
    },
    34: {
        "personaje": "Daniel",
        "texto": "Prefiero evitar los problemas, pero",
        "imagen": img_def,
        "siguiente": 35
    },
    35: {
        "personaje": "Daniel",
        "texto": "Ahora hay algo que cambia, estas tu aqui conmigo :3",
        "imagen": img_def,
        "siguiente": 36
    },
    36: {
        "personaje": "Daniel",
        "texto": "21 de Agosto de 2025... Justo andaba escuchando el OST de Undertale hace unos minutos. ¡Hahaha!",
        "imagen": img_def,
        "siguiente": 37
    },
    37: {
        "personaje": "Daniel",
        "texto": "Jajajaj, ¿sí se escucha como Hopes and Dreams? Aún la sigo practicando. Justo el inicio se me complica un poquito.",
        "imagen": img_def,
        "siguiente": 38
    },
    38: {
        "personaje": "Daniel",
        "texto": "Para que te hagas una idea, ya con las primeras tres notas supe que era Hopes and Dreams. Fue tan simple, pero de un momento para otro, una ligera forma de querer llamar tu atención funcionó.",
        "imagen": img_def,
        "siguiente": 39
    },
    39: {
        "personaje": "Daniel",
        "texto": "Me hizo feliz. Capté la atención del que no sabía que sería el mejor novio del mundo.",
        "imagen": img_def,
        "siguiente": 40
    },
    40: {
        "personaje": "Daniel",
        "texto": "¿Recuerdas cómo fue cuando te pregunté si querías ser mi pareja? Sonabas tan decaído en ese momento, tan triste por lo que estabas pasando...",
        "imagen": img_def,
        "animacion": "shake",
        "siguiente": 41
    },
    41: {
        "personaje": "Daniel",
        "texto": "Y yo, ciertamente te quería hacer feliz. Quizás es algo en lo que a veces no tengo tacto, pero me alegro de que desde ese día seamos pareja.",
        "imagen": img_def,
        "siguiente": 42
    },
    42: {
        "personaje": "Daniel",
        "texto": "Hemos vivido muchos momentos graciosos y bonitos, como la vez que hicimos al Kris y a Ralsei, o dibujos en conjunto como Caín y Abel.",
        "imagen": img_def,
        "siguiente": 43
    },
    43: {
        "personaje": "Daniel",
        "texto": "Cuando vimos Hazbin Hotel... ¡Por ti empecé a ver South Park, por cierto! Todos los personajes con los que nos identificamos:",
        "imagen": img_def,
        "siguiente": 44
    },
    44: {
        "personaje": "Daniel",
        "texto": "Somos Ralsei y Kris, Pinkie Pie y Sunset, Tweek y Craig, Charlie y Nick, Charlie y Pim, Charlie y Vaggie, Charlie y Kirk, Trump y Satanás...",
        "imagen": img_def,
        "siguiente": 45
    },
    45: {
        "personaje": "Daniel",
        "texto": "...Elle y Tao, Johnny y Gyro, Denji y Asa, las torres gemelas y el avión... y por supuesto que somos Sonic y Shadow. :3",
        "imagen": img_def,
        "siguiente": 46
    },
    46: {
        "personaje": "Daniel",
        "texto": "¿Recuerdas cuando jugamos a tener una tienda? Fue tan divertido ese día. 'Te quiero presentar al oso, el amor de mi... es como un hijo para mí'.",
        "imagen": img_def,
        "siguiente": 47
    },
    47: {
        "personaje": "Daniel",
        "texto": "'¡NOO, TÚ NO IBAS A DECIR ESO!' '¿POR QUÉ ACTUABAS COMO SI NO ME IBA A DAR CUENTA?'. Amo, amo pasar tiempo contigo. Es tan divertido cuando estamos en llamada.",
        "imagen": img_def,
        "siguiente": 48
    },
    48: {
        "personaje": "Daniel",
        "texto": "Ciertamente, también hemos tenido malos momentos. Momentos en los que nos sentimos decaídos, con ganas de llorar por problemas adversos o incluso por el otro.",
        "imagen": img_def,
        "animacion": "shake",
        "siguiente": 49
    },
    49: {
        "personaje": "Daniel",
        "texto": "Son cosas por las que también hemos pasado. Te he hecho daño. Son malos recuerdos, pero no quiero olvidarlos.",
        "imagen": img_def,
        "siguiente": 50
    },
    50: {
        "personaje": "Daniel",
        "texto": "No quiero volver a equivocarme, ni a dañarte. No quiero ser alguien más que te haga daño. No quiero actuar como si nunca hice nada malo, porque no mereces que ignore cosas que sí pasaron.",
        "imagen": img_def,
        "siguiente": 51
    },
    51: {
        "personaje": "Daniel",
        "texto": "Mereces que aprenda de mis equivocaciones, las solucione y las afronte. Porque eres alguien que vale la pena, porque me motivas a ser mejor persona.",
        "imagen": img_def,
        "siguiente": 52
    },
    52: {
        "personaje": "Daniel",
        "texto": "Porque eres alguien que vale la pena, porque me motivas a ser mejor persona. Te amo. Te amo tanto. Mi niño, felices 5 mesesitos.",
        "imagen": img_def,
        "siguiente": None
    },

    # --- CAMINO PLANIFICAR (FUTURO COMPLETO SIN RECORTES) ---
    54: {
        "personaje": "Daniel",
        "texto": "Hmmm futuro, es curioso. No puedo dejar de pensarte en él, sabes.",
        "imagen": img_def,
        "musica": "https://raw.githubusercontent.com/danielzarate1401-lab/yanomas/main/Weezer%20-%20Island%20In%20The%20Sun%20(Instrumental%20Original).mp3",
        "siguiente": 55
    },
    55: {
        "personaje": "Daniel",
        "texto": "Mi futuro ideal es uno donde ya estemos viviendo juntos en Chile, empezaríamos en un departamento pequeño por un tiempo.",
        "imagen": img_def,
        "siguiente": 56
    },
    56: {
        "personaje": "Daniel",
        "texto": "Algo humilde, tendríamos mis ahorros para no preocuparnos por un buen rato pero sería lindo. Tu ya todo trabajador y yo apenas entrando a la carrera. Groomer.",
        "imagen": img_def,
        "siguiente": 57
    },
    57: {
        "personaje": "Daniel",
        "texto": "Podríamos salir seguido, al parque, por sushi, al mall, a donde sea. Quiero ir contigo, quiero conocer la ciudad.",
        "imagen": img_def,
        "siguiente": 58
    },
    58: {
        "personaje": "Daniel",
        "texto": "Quiero ir a la tienda donde dijiste “1800 ah perdón es que estoy mal de la cabeza”. Quiero conocer a tus amigos y familia aunque les caiga mal.",
        "imagen": img_def,
        "siguiente": 59
    },
    59: {
        "personaje": "Daniel",
        "texto": "Luego, cuando tengamos nuestra casa propia, obtengas el trabajo que quieres... ¿Te imaginas ya con empleo? ¿No sería lindo?",
        "imagen": img_def,
        "siguiente": 60
    },
    60: {
        "personaje": "Daniel",
        "texto": "Rezo por que todo salga bien, le pido a todo y a todos por nuestro futuro. Pero creo que rezar no basta.",
        "imagen": img_def,
        "siguiente": 61
    },
    61: {
        "personaje": "Daniel",
        "texto": "Debemos esforzarnos, como pareja, para que todo nos salga bien, no quiero decepcionarte. Solo así podré estar verdaderamente orgulloso de ayudarte a cumplir tus metas.",
        "imagen": img_def,
        "siguiente": 62
    },
    62: {
        "personaje": "Daniel",
        "texto": "Imagina cuando programemos un juego buenísimo. Sé que quiero hacerlo contigo, quiero planearlo.",
        "imagen": img_def,
        "siguiente": 63
    },
    63: {
        "personaje": "Daniel",
        "texto": "Quiero que nuestros personajes sean conocidos, quiero que triunfemos en nuestro futuro. Imagina tu enorme estante de merch de Pinkie Pie.",
        "imagen": img_def,
        "siguiente": 64
    },
    64: {
        "personaje": "Daniel",
        "texto": "Al lado mi colección del manga de JoJos. Nuestras PCs al lado una de la otra para programar y jugar. En nuestra cocina un refri lleno de comida para que cocinemos lo que queramos.",
        "imagen": img_def,
        "siguiente": 65
    },
    65: {
        "personaje": "Daniel",
        "texto": "Un castillo para nuestros gatitos Nirvana y Korn. Y un cuarto para nuestros hijos. Sip ya sabes, nuestros hijos: Kurt y Frances, nuestros amores.",
        "imagen": img_def,
        "siguiente": 66
    },
    66: {
        "personaje": "Daniel",
        "texto": "Ah y nuestros otros hijos: Nirvana 2, Pinkie Pie, Shadow, Apolo, Yorkenson, Nainileven, Nirvana 3,5, Rainbow Dash, Rarity, Starlight, Sunset, Cheese Sandwich, Pelirrojo, Minipam, Minidani...",
        "imagen": img_def,
        "siguiente": 67
    },
    67: {
        "personaje": "Daniel",
        "texto": "...Mpa, Map, Pma, Vox, Charlie Kirk, Mexican Seafood, Anexorcist, Adoptado, Adoptadito, Tusk, Periwinkle, Coca de Dieta, Nuggets, Kira, Akira, Michi, Whiplash, Orion, Blackened...",
        "imagen": img_def,
        "siguiente": 68
    },
    68: {
        "personaje": "Daniel",
        "texto": "...Serv, Makima, Varka, Treintaiun Minutos, Venecolano, Venecalono, IV, Cloe, KKK, Copi-Copi, Elemento, Adjetivo, Mente en Blanco, Chaucha, Yo Soy, Calugoso, Duquesa, Reina...",
        "imagen": img_def,
        "siguiente": 69
    },
    69: {
        "personaje": "Daniel",
        "texto": "...Coliforme, Tepo-Tepo, Yo no Fui, Fierro Malo, Palmerita, Neumatex, Cortachurro, Etcétera, Maletín, Duque, Guasón, Jefe, Moneda, Cucky, Pelusa, Tía, Legui, Reality...",
        "imagen": img_def,
        "siguiente": 70
    },
    70: {
        "personaje": "Daniel",
        "texto": "...Chester, Chu, Ro, Playita, Palmera, Señor, Re Frito, Pescado, Chamuyo, Calendario, James Bond, Rata, Cabeza de Chaya, Neumático, Repetido, Añico, Rucia, Gonzo, Chino, Cortéz, Albertito.",
        "imagen": img_def,
        "siguiente": 71
    },
    71: {
        "personaje": "Daniel",
        "texto": "Bueno, ahora yendo con los que no queremos son... Ok ya paro. No sé, es lindo pensar en procrear contigo. Tener una familia. Tener cualquier cosa contigo.",
        "imagen": img_def,
        "siguiente": 72
    },
    72: {
        "personaje": "Daniel",
        "texto": "Me esforzaré porque todo salga bien, esto es una prueba de ello por ejemplo. Te amo tanto como para dejar el procrastinamiento, te amo tanto como para dar todo de mi.",
        "imagen": img_def,
        "siguiente": 73
    },
    73: {
        "personaje": "Daniel",
        "texto": "Porque al final, mi niño, al final tu mereces lo mejor de lo mejor. Mereces un mejor novio, pero yo quiero ser ese mejor novio.",
        "imagen": img_def,
        "siguiente": 74
    },
    74: {
        "personaje": "Daniel",
        "texto": "Mi wekito, felices 5 meses, te amo. Muak.",
        "imagen": img_def,
        "siguiente": None
    }
}

# --- 5. LÓGICA DE PANTALLAS ---

if not st.session_state.jugando:
    st.snow()
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.write("")
        st.write("")
        st.image(img_def, use_container_width=True)
        st.markdown("<h1 style='text-align: center; color: #d81b60; font-family: cursive;'>Nuestra Historia ❤️</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'>Un regalo especial para mi niño</p>", unsafe_allow_html=True)
        if st.button("✨ COMENZAR ✨", use_container_width=True):
            st.session_state.jugando = True
            st.rerun()
else:
    escena = historia.get(st.session_state.paso, historia[0])
    
    if "musica" in escena:
        st.session_state.musica_actual = escena["musica"]

    if st.session_state.musica_actual and st.session_state.musica_actual != "ninguna":
        st.audio(st.session_state.musica_actual, format="audio/mp3", autoplay=True, loop=True)
    
    if not st.session_state.musica_actual:
        st.write("🎵 *Silencio*")

    c1, c2, c3 = st.columns([1, 2, 1])
    with c2:
        clase_anim = "personaje-shake" if escena.get("animacion") == "shake" else ""
        st.markdown(f'''
            <img src="{escena["imagen"]}" 
                 class="{clase_anim}" 
                 style="width:100%; border-radius:20px; border: 5px solid white;">
        ''', unsafe_allow_html=True)
        
        st.markdown(f"""
            <div class="dialogo-box">
                <div class="nombre-personaje">{escena['personaje']}</div>
                {escena['texto']}
            </div>
        """, unsafe_allow_html=True)

        st.write("") 

        if "opciones" in escena:
            cols_btn = st.columns(len(escena["opciones"]))
            for i, opt in enumerate(escena["opciones"]):
                if cols_btn[i].button(opt["texto"], key=f"btn_opt_{i}_{st.session_state.paso}", use_container_width=True):
                    st.session_state.paso = opt["destino"]
                    st.rerun()
        else:
            sig = escena.get("siguiente")
            if sig is not None:
                if st.button("Continuar ➔", key=f"btn_next_{st.session_state.paso}", use_container_width=True):
                    st.session_state.paso = sig
                    st.rerun()
            else:
                if st.button("Finalizar ❤️", key="btn_final", use_container_width=True):
                    st.balloons()
                    st.session_state.paso = 0
                    st.session_state.jugando = False
                    st.session_state.musica_actual = "ninguna"
                    st.rerun()
