import streamlit as st

st.set_page_config(page_title="Felices 5 meses", layout="wide")


# ___ CSS ___ #

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@800&family=Quicksand:wght@500;700&display=swap');

    audio { display: none !important; }
    
    [data-testid="stHeader"], [data-testid="stDecoration"], footer, header {
        display: none !important;
        height: 0px !important;
        opacity: 0 !important;
    }

    .block-container {
        padding-top: 0rem !important;
        max-width: 100% !important;
    }

    /* 1. FONDO CON MOVIMIENTO DIAGONAL PERFECTO */
    .stApp { 
        background-color: #e57399; 
        background-image: url('https://raw.githubusercontent.com/danielzarate1401-lab/yanomas/main/fondoreal.png'); 
        background-repeat: repeat;
        background-size: 750px; 
        animation: moverDiagonal 60s linear infinite;
    }

    @keyframes moverDiagonal {
        from { background-position: 0 0; }
        to { background-position: -1500px 1500px; }
    }

    .caja-titulo {
        background: rgba(255, 255, 255, 0.2); /* Blanco muy transparente */
        backdrop-filter: blur(10px);        /* Efecto de desenfoque de fondo */
        border-radius: 15px;                 /* Bordes redondeados */
        border: 2px solid rgba(255, 255, 255, 0.3);
        padding: 20px;
        margin-bottom: 30px;                 /* Espacio con la consola */
        text-align: center;
        box-shadow: 0 8px 32px 0 rgba(173, 20, 87, 0.3); /* Sombra rosada sutil */
    }

    .caja-titulo h1 {
        color: white !important;
        font-family: 'Montserrat', sans-serif;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3); /* Sombra en las letras */
        margin: 0;
        font-size: 2.5rem;
    }

    /* 2. CONSOLA CON EFECTO DE BRILLO (SHINE) */
    .marco-consola {
        position: relative;
        z-index: 1000000 !important;
        background-color: #f06292;
        border: 10px solid #ad1457;
        border-radius: 20px;
        padding: 15px;
        width: 380px; 
        margin: -40px auto 0 auto; 
        box-shadow: 0px 15px 30px rgba(0,0,0,0.3);
        overflow: hidden; 
    }

    /* LA LÍNEA DE LUZ */
    .marco-consola::after {
        content: "";
        position: absolute;
        top: 0;
        left: -150%;
        width: 50%;
        height: 100%;
        background: linear-gradient(
            to right, 
            rgba(255,255,255,0) 0%, 
            rgba(255,255,255,0.4) 50%, 
            rgba(255,255,255,0) 100%
        );
        transform: skewX(-25deg); /* Inclina la línea para que se vea más natural */
        animation: relucir 8s infinite;
    }

    @keyframes relucir {
        0% { left: -150%; }
        30% { left: 150%; } /* Pasa rápido de un lado a otro */
        100% { left: 150%; } /* Se queda esperando antes de repetir */
    }

    /* 3. RESTO DE LA INTERFAZ */
    .pantalla-juego {
        background-color: #333;
        background-image: url('https://raw.githubusercontent.com/danielzarate1401-lab/yanomas/main/Cuarto.png'); 
        background-size: cover;
        background-position: center;
        height: 500px;
        border: 4px solid #333;
        border-bottom: none;
        border-radius: 10px 10px 0 0;
        display: flex;
        justify-content: flex-start; 
        align-items: flex-end;
        position: relative;
        overflow: hidden;
        z-index: 1;
    }

    .personaje-img {
        height: 85%; 
        z-index: 2;
        filter: drop-shadow(5px 5px 10px rgba(0,0,0,0.4));
    }
    .manos-overlay {
        position: absolute;
        bottom: 0;
        left: 12.5%;
        transform: translateX(-50%);
        width: 25%; /* Ajusta según el tamaño de tu imagen */
        z-index: 3;  /* Por encima del personaje que tiene z-index 2 */
        pointer-events: none; /* Para que no bloquee los clics */
    }

    .dialogo-box {
        background-color: white;
        border: 4px solid #333;
        border-radius: 0 0 10px 10px;
        padding: 15px;
        color: #333;
        font-family: 'Quicksand', sans-serif;
        min-height: 140px;
        position: relative;
        z-index: 1;
    }

    .nombre-personaje {
        font-family: 'Montserrat', sans-serif;
        color: #ad1457;
        font-size: 18px;
        margin-bottom: 5px;
    }

   .contenedor-botones {
        margin-top: 10px; /* Menos espacio con la caja de diálogo */
        display: flex;
        flex-direction: row; 
        justify-content: flex-start; /* Alinea al inicio (izquierda) */
        gap: 10px; /* Espacio pequeño entre ellos */
        width: 100%;
        padding-left: 5px; /* Pequeño ajuste para que no toque el borde del marco */
    }

    .stButton>button {
        background: #ad1457 !important;
        color: white !important;
        border-radius: 10px; /* Un poco menos redondos para que parezcan botones de consola */
        border: 2px solid #f8bbd0;
        font-family: 'Montserrat', sans-serif;
        width: auto; /* El botón se ajusta al tamaño del texto */
        min-width: 120px; 
        height: 40px;
        box-shadow: 0px 4px 0px #78002e;
        transition: all 0.1s ease;
        opacity: 1 !important;
    }

    /* EFECTO AL PASAR EL MOUSE (QUITAMOS TRANSPARENCIA) */
    .stButton>button:hover {
        background: #d81b60 !important; /* Un rosa un poco más brillante */
        border-color: white !important;
        transform: translateY(2px); /* Baja un poquito */
        box-shadow: 0px 3px 0px #78002e;
        opacity: 1 !important;
    }

    /* EFECTO AL HACER CLIC */
    .stButton>button:active {
        transform: translateY(5px); /* Se hunde totalmente */
        box-shadow: 0px 0px 0px #78002e;
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
        "texto": "Hola, mi niño, hoy cumplimos un mes más de relación y ahora que es parte de otro año quiero que sea más especial.",
        "imagen": "https://raw.githubusercontent.com/danielzarate1401-lab/yanomas/main/CerradoFrente.png",
        "manos": "https://raw.githubusercontent.com/danielzarate1401-lab/yanomas/main/shy.png",
        "musica": "https://raw.githubusercontent.com/danielzarate1401-lab/yanomas/main/31%20minutos%20-%20Karaoke%20-%20Yo%20opino.mp3",
        "siguiente": 1
    },
    1: {
        "personaje": "Daniel",
        "texto": "Quiero dar lo mejor de mí para ti y por ambos. Por nuestro futuro y pasado, quiero aprender muchas más cosas.",
        "imagen": "https://raw.githubusercontent.com/danielzarate1401-lab/yanomas/main/AbiertoFrente.png",
        "siguiente": 2
    },
    2: {
        "personaje": "Daniel",
        "texto": "Este año quiero aprender a programar, a vivir y a ser un novio tan bueno como tú.",
        "imagen": "https://raw.githubusercontent.com/danielzarate1401-lab/yanomas/main/Abiertoblush.png",
        "siguiente": 3
    },
    3: {
        "personaje": "Daniel",
        "texto": "Porque aunque tú digas lo contrario, eres el mejor novio del mundo; tan maravilloso y unico",
        "imagen": "https://raw.githubusercontent.com/danielzarate1401-lab/yanomas/main/Cerradoblush.png",
        "animacion": "shake",
        "siguiente": 4
    },
    4: {
        "personaje": "Daniel",
        "texto": "Jamás me había sentido tan querido y correspondido por alguien.",
        "imagen": "https://raw.githubusercontent.com/danielzarate1401-lab/yanomas/main/Abiertoblush.png",
        "siguiente": 5
    },
    5: {
        "personaje": "Daniel",
        "texto": "Haces que quiera dejar de huir de los problemas. Haces que me sienta bien conmigo mismo.",
        "imagen": "https://raw.githubusercontent.com/danielzarate1401-lab/yanomas/main/CerradoAbajo.png",
        "siguiente": 6
    },
    6: {
        "personaje": "Daniel",
        "texto": "Haces que quiera dar más de mí sin sentirme presionado. Te amo tanto, gracias por ser tú.",
        "imagen": "https://raw.githubusercontent.com/danielzarate1401-lab/yanomas/main/CerradoFrente.png",
        "siguiente": 7
    },
    7: {
        "personaje": "Daniel",
        "texto": "Quiero que sepas que doy lo mejor de mi, para ti, porque eres alguien que lo merece.",
        "imagen": "https://raw.githubusercontent.com/danielzarate1401-lab/yanomas/main/AbiertoFrente.png",
        "siguiente": 8
    },
    8: {
        "personaje": "Daniel",
        "texto": "Mi niño",
        "imagen": "https://raw.githubusercontent.com/danielzarate1401-lab/yanomas/main/CerradoAbajo.png",
        "siguiente": 9
    },
    9: {
        "personaje": "Daniel",
        "texto": "Te gusta esta novela visual?",
        "imagen": "https://raw.githubusercontent.com/danielzarate1401-lab/yanomas/main/AbiertoFrente.png",
        "siguiente": 10
    },
    10: {
        "personaje": "Daniel",
        "texto": "Tiene muchos personajes y eso, soy yo y... yo y.... también estoy yo... y sans deltarune ",
        "imagen": "https://raw.githubusercontent.com/danielzarate1401-lab/yanomas/main/AbiertoFrente.png",
        "siguiente": 11
    },
    11: {
        "personaje": "Daniel",
        "texto": "Ah y estas tu, creo ",
        "imagen": "https://raw.githubusercontent.com/danielzarate1401-lab/yanomas/main/CerradoFrente.png",
        "siguiente": 12
    },
    12: {
        "personaje": "Daniel",
        "texto": "Bueno, como otras novelas visuales esta tiene opciones de dialogo. Viste? Asi se bueno soy.",
        "imagen": "https://raw.githubusercontent.com/danielzarate1401-lab/yanomas/main/CerradoAbajo.png",
        "siguiente": 13
    },
    13: {
        "personaje": "Daniel",
        "texto": "Que te parece?",
        "imagen": "https://raw.githubusercontent.com/danielzarate1401-lab/yanomas/main/AbiertoFrente.png",
         "opciones": [
            {"texto": "Menea la chapa remix", "destino": 14},
            {"texto": "Amarillo amarillo platano", "destino": 14}
         ] 
    },
    14: {
        "personaje": "Daniel",
        "texto": "Yo se, increible...",
        "imagen": "https://raw.githubusercontent.com/danielzarate1401-lab/yanomas/main/CerradoFrente.png",
        "siguiente": 15
    },
    15: {
        "personaje": "Daniel",
        "texto": "Oye",
        "imagen": "https://raw.githubusercontent.com/danielzarate1401-lab/yanomas/main/Cerradoblush.png",
        "siguiente": 16
    },
    16: {
        "personaje": "Daniel",
        "texto": "Me gustas",
        "imagen": "https://raw.githubusercontent.com/danielzarate1401-lab/yanomas/main/Abiertoblush.png",
        "siguiente": 17
    },
    17: {
        "personaje": "Daniel",
        "texto": "Me gustas mucho",
        "imagen": "https://raw.githubusercontent.com/danielzarate1401-lab/yanomas/main/Abiertoblush.png",
        "siguiente": 18
    },
    18: {
        "personaje": "Daniel",
        "texto": "Me gustas tanto que quiero esforzarme",
        "imagen": "https://raw.githubusercontent.com/danielzarate1401-lab/yanomas/main/Abiertoblush.png",
        "siguiente": 19
    },
    19: {
        "personaje": "Daniel",
        "texto": "Tanto como para pensar en el pasado de forma bonita... ",
        "imagen": "https://raw.githubusercontent.com/danielzarate1401-lab/yanomas/main/Cerradoblush.png",
        "siguiente": 20
    },
    20: {
        "personaje": "Daniel",
        "texto": "...O como para esforzarme por un buen futuro.",
        "imagen": "https://raw.githubusercontent.com/danielzarate1401-lab/yanomas/main/Cerradoblush.png",
        "siguiente": 21
    },
    21: {
        "personaje": "Daniel",
        "texto": "Mi niño lindo.",
        "imagen": "https://raw.githubusercontent.com/danielzarate1401-lab/yanomas/main/AbiertoFrente.png",
        "siguiente": 22
    },
    22: {
        "personaje": "Daniel",
        "texto": "Feliz quinto mes btw.",
        "imagen": "https://raw.githubusercontent.com/danielzarate1401-lab/yanomas/main/AbiertoFrente.png",
        "siguiente": 23
    },
    23: {
        "personaje": "Daniel",
        "texto": "Mi niño... Bueno, ya que me gusta ser mandoneado, me gustaría que respondas una pregunta:",
        "imagen": "https://raw.githubusercontent.com/danielzarate1401-lab/yanomas/main/Abiertoblush.png",
        "siguiente": 24
    },
    24: {
        "personaje": "Daniel",
        "texto": "¿Qué quieres hacer?",
        "imagen": "https://raw.githubusercontent.com/danielzarate1401-lab/yanomas/main/Cerradoblush.png",
        "musica": "ninguna",
        "opciones": [
            {"texto": "Recordar", "destino": 25},
            {"texto": "Planificar", "destino": 54}
        ]
    },
    25: {
        "personaje": "Daniel",
        "texto": "Hmmmm",
        "imagen": "https://raw.githubusercontent.com/danielzarate1401-lab/yanomas/main/CerradoSerio.png",
        "musica": "https://raw.githubusercontent.com/danielzarate1401-lab/yanomas/main/el%20profe.mp3",
        "siguiente": 26
    },
    26: {
        "personaje": "Daniel",
        "texto": "Sabes, no me gustaba mucho recordar las cosas... ",
        "imagen": "https://raw.githubusercontent.com/danielzarate1401-lab/yanomas/main/AbiertoSerio.png",
        "siguiente": 27
    },
    27: {
        "personaje": "Daniel",
        "texto": "Nunca de hecho, es como un metodo de defenza para no deprimirme. ",
        "imagen": "https://raw.githubusercontent.com/danielzarate1401-lab/yanomas/main/AbiertoSerio.png",
        "siguiente": 28
    },
    28: {
        "personaje": "Daniel",
        "texto": "Solo.... ",
        "imagen": "https://raw.githubusercontent.com/danielzarate1401-lab/yanomas/main/CerradoSerio.png",
        "siguiente": 29
    },
    29: {
        "personaje": "Daniel",
        "texto": "Cada que pensaba en el pasado... ",
        "imagen": "https://raw.githubusercontent.com/danielzarate1401-lab/yanomas/main/CerradoAbajo.png",
        "siguiente": 30
    },
    30: {
        "personaje": "Daniel",
        "texto": "...Me venian a la mente malos recuerdos ",
        "imagen": "https://raw.githubusercontent.com/danielzarate1401-lab/yanomas/main/CerradoFrente.png",
        "siguiente": 31
    },
    31: {
        "personaje": "Daniel",
        "texto": "Momentos horribles",
        "imagen": "https://raw.githubusercontent.com/danielzarate1401-lab/yanomas/main/AbiertoFrente.png",
        "siguiente": 32
    },
    32: {
        "personaje": "Daniel",
        "texto": "Cosas de las que me arrepiento...",
        "imagen": "https://raw.githubusercontent.com/danielzarate1401-lab/yanomas/main/AbiertoFrente.png",
        "siguiente": 33
    },
    33: {
        "personaje": "Daniel",
        "texto": "Dias que preferiria que no hayan existido. ",
        "imagen": "https://raw.githubusercontent.com/danielzarate1401-lab/yanomas/main/CerradoFrente.png",
        "siguiente": 34
    },
    34: {
        "personaje": "Daniel",
        "texto": "Supongo que sabes como prefiero evitar los problemas, pero...",
        "imagen": "https://raw.githubusercontent.com/danielzarate1401-lab/yanomas/main/CerradoAbajo.png",
        "siguiente": 35
    },
    35: {
        "personaje": "Daniel",
        "texto": "Ahora siento que algo cambia, y eso es que tu estas aqui conmigo :3",
        "imagen": "https://raw.githubusercontent.com/danielzarate1401-lab/yanomas/main/Cerradoblush.png",
        "siguiente": 36
    },
    36: {
        "personaje": "Supuestamente Pam",
        "texto": "21 de Agosto de 2025... Justo andaba escuchando el OST de Undertale hace unos minutos. ¡Hahaha!",
        "imagen": "https://raw.githubusercontent.com/danielzarate1401-lab/yanomas/main/supuestapam.png",
        "siguiente": 37
    },
    37: {
        "personaje": "Daniel",
        "texto": "Jajajaj, ¿sí se escucha como Hopes and Dreams? Aún la sigo practicando. Justo el inicio se me complica un poquito.",
        "imagen": "https://raw.githubusercontent.com/danielzarate1401-lab/yanomas/main/AbiertoFrente.png",
        "siguiente": 38
    },
    38: {
        "personaje": "Supuestamente Pam",
        "texto": "Para que te hagas una idea, ya con las primeras tres notas supe que era Hopes and Dreams....",
        "imagen": "https://raw.githubusercontent.com/danielzarate1401-lab/yanomas/main/supuestapam.png",
        "siguiente": 39
    },
    39: {
        "personaje": "Daniel",
        "texto": "Fue tan simple, pero de un momento para otro, una ligera forma de querer llamar tu atención funcionó. Me hizo feliz. Capté la atención del que no sabía que sería el mejor novio del mundo.",
        "imagen": "https://raw.githubusercontent.com/danielzarate1401-lab/yanomas/main/Abiertoblush.png",
        "siguiente": 40
    },
    40: {
        "personaje": "Daniel",
        "texto": "¿Recuerdas cómo fue cuando te pregunté si querías ser mi pareja? Sonabas tan decaído en ese momento, tan triste por lo que estabas pasando...",
        "imagen": "https://raw.githubusercontent.com/danielzarate1401-lab/yanomas/main/Abiertoblush.png",
        "animacion": "shake",
        "siguiente": 41
    },
    41: {
        "personaje": "Daniel",
        "texto": "Y yo, ciertamente te quería hacer feliz. Quizás es algo en lo que a veces no tengo tacto, pero me alegro de que desde ese día seamos pareja.",
        "imagen": "https://raw.githubusercontent.com/danielzarate1401-lab/yanomas/main/AbiertoFrente.png",
        "siguiente": 42
    },
    42: {
        "personaje": "Daniel",
        "texto": "Hemos vivido muchos momentos graciosos y bonitos, como la vez que hicimos al Kris y a Ralsei, o dibujos en conjunto como Caín y Abel.",
        "imagen": "https://raw.githubusercontent.com/danielzarate1401-lab/yanomas/main/CerradoFrente.png",
        "siguiente": 43
    },
    43: {
        "personaje": "Daniel",
        "texto": "Cuando vimos Hazbin Hotel... ¡Por ti empecé a ver South Park, lo que me recuerda todos los personajes con los que nos identificamos:",
        "imagen": "https://raw.githubusercontent.com/danielzarate1401-lab/yanomas/main/AbiertoFrente.png",
        "siguiente": 44
    },
    44: {
        "personaje": "Daniel",
        "texto": "Somos Ralsei y Kris, Pinkie Pie y Sunset, Tweek y Craig, Charlie y Nick, Charlie y Pim, Charlie y Vaggie, Charlie y Kirk, Trump y Satanás...",
        "imagen": "https://raw.githubusercontent.com/danielzarate1401-lab/yanomas/main/Abiertoblush.png",
        "siguiente": 45
    },
    45: {
        "personaje": "Daniel",
        "texto": "...Elle y Tao, Johnny y Gyro, Denji y Asa, las torres gemelas y el avión... y por supuesto que somos Sonic y Shadow. :3",
        "imagen": "https://raw.githubusercontent.com/danielzarate1401-lab/yanomas/main/Abiertoblush.png",
        "siguiente": 46
    },
    46: {
        "personaje": "Daniel",
        "texto": "¿Recuerdas cuando jugamos a tener una tienda? Fue tan divertido ese día. 'Te quiero presentar al oso, el amor de mi... es como un hijo para mí'.",
        "imagen": "https://raw.githubusercontent.com/danielzarate1401-lab/yanomas/main/AbiertoFrente.png",
        "siguiente": 47
    },
    47: {
        "personaje": "Supuestamente Pam",
        "texto": "'¡NOO, TÚ NO IBAS A DECIR ESO!' '¿POR QUÉ ACTUABAS COMO SI NO ME IBA A DAR CUENTA?'. Amo, amo pasar tiempo contigo. Es tan divertido cuando estamos en llamada...",
        "imagen": "https://raw.githubusercontent.com/danielzarate1401-lab/yanomas/main/supuestapam.png",
        "siguiente": 75
    },
    48: {
        "personaje": "Daniel",
        "texto": "Ciertamente, también hemos tenido malos momentos. Momentos en los que nos sentimos decaídos, con ganas de llorar por problemas adversos o incluso por el otro.",
        "imagen": "https://raw.githubusercontent.com/danielzarate1401-lab/yanomas/main/AbiertoSerio.png",
        "animacion": "shake",
        "siguiente": 49
    },
    49: {
        "personaje": "Daniel",
        "texto": "Son cosas por las que también hemos pasado. Te he hecho daño. Son malos recuerdos... pero no es algo que quiera olvidar.",
        "imagen": "https://raw.githubusercontent.com/danielzarate1401-lab/yanomas/main/AbiertoSerio.png",
        "siguiente": 50
    },
    50: {
        "personaje": "Daniel",
        "texto": "No quiero volver a equivocarme, ni a dañarte. No quiero ser alguien más que te haga daño. No quiero actuar como si nunca hice nada malo, porque no mereces que ignore cosas que sí pasaron.",
        "imagen": "https://raw.githubusercontent.com/danielzarate1401-lab/yanomas/main/AbiertoFrente.png",
        "siguiente": 51
    },
    51: {
        "personaje": "Daniel",
        "texto": "Mereces que aprenda de mis equivocaciones, las solucione y las afronte. Porque eres alguien que vale la pena, porque me motivas a ser mejor persona.",
        "imagen": "https://raw.githubusercontent.com/danielzarate1401-lab/yanomas/main/AbiertoFrente.png",
        "siguiente": 52
    },
    52: {
        "personaje": "Daniel",
        "texto": "Porque eres alguien que vale la pena, porque me motivas a ser mejor persona. Te amo. Te amo tanto. Mi niño, felices 5 mesesitos.",
        "imagen": "https://raw.githubusercontent.com/danielzarate1401-lab/yanomas/main/Abiertoblush.png",
        "siguiente": None
    },

    # --- CAMINO PLANIFICAR (FUTURO COMPLETO SIN RECORTES) ---
    54: {
        "personaje": "Daniel",
        "texto": "Hmmm futuro.... es curioso. No puedo dejar de pensarte en él, Sabes?",
        "imagen": "https://raw.githubusercontent.com/danielzarate1401-lab/yanomas/main/Cerradoblush.png",
        "musica": "https://raw.githubusercontent.com/danielzarate1401-lab/yanomas/main/Weezer%20-%20Island%20In%20The%20Sun%20(Instrumental%20Original).mp3",
        "siguiente": 55
    },
    55: {
        "personaje": "Daniel",
        "texto": "Mi futuro ideal es uno donde ya estemos viviendo juntos en Chile, empezaríamos en un departamento pequeño por un tiempo.",
        "imagen": "https://raw.githubusercontent.com/danielzarate1401-lab/yanomas/main/Abiertoblush.png",
        "siguiente": 56
    },
    56: {
        "personaje": "Daniel",
        "texto": "Algo humilde, tendríamos mis ahorros para no preocuparnos por un buen rato pero sería lindo... Tu ya todo trabajador y yo apenas entrando a la carrera. Groomer.",
        "imagen": "https://raw.githubusercontent.com/danielzarate1401-lab/yanomas/main/AbiertoFrente.png",
        "siguiente": 57
    },
    57: {
        "personaje": "Daniel",
        "texto": "...Podríamos salir seguido al parque, por sushi, al mall, a donde sea. Quiero ir contigo, quiero conocer la ciudad.",
        "imagen": "https://raw.githubusercontent.com/danielzarate1401-lab/yanomas/main/CerradoAbajo.png",
        "siguiente": 58
    },
    58: {
        "personaje": "Daniel",
        "texto": "Quiero ir a la tienda donde dijiste “1800 ah perdón es que estoy mal de la cabeza”. Quiero conocer a tus amigos y familia.... aunque seguramente les caiga mal.",
        "imagen": "https://raw.githubusercontent.com/danielzarate1401-lab/yanomas/main/AbiertoFrente.png",
        "siguiente": 59
    },
    59: {
        "personaje": "Daniel",
        "texto": "Luego, en algun punto tendremos nuestra casa propia, terminare de estudiar y tu tendras el trabajo que querias... ¿Te imaginas ya con empleo? ¿No sería lindo?",
        "imagen": "https://raw.githubusercontent.com/danielzarate1401-lab/yanomas/main/AbiertoFrente.png",
        "siguiente": 60
    },
    60: {
        "personaje": "Daniel",
        "texto": "Rezo por que todo salga bien, le pido a Dios y a todo y todos porque tengamos un buen futuro... Aunque rezar no basta.",
        "imagen": "https://raw.githubusercontent.com/danielzarate1401-lab/yanomas/main/CerradoAbajo.png",
        "siguiente": 61
    },
    61: {
        "personaje": "Daniel",
        "texto": "Debemos esforzarnos, como pareja, para que todo nos salga bien, no quiero decepcionarte. Solo así podré estar verdaderamente orgulloso de ayudarte a cumplir tus metas.",
        "imagen": "https://raw.githubusercontent.com/danielzarate1401-lab/yanomas/main/CerradoFrente.png",
        "siguiente": 62
    },
    62: {
        "personaje": "Daniel",
        "texto": "Imagina cuando programemos un juego buenísimo. Sé que quiero hacerlo contigo, quiero planearlo.",
        "imagen": "https://raw.githubusercontent.com/danielzarate1401-lab/yanomas/main/AbiertoFrente.png",
        "siguiente": 63
    },
    63: {
        "personaje": "Daniel",
        "texto": "Quiero que nuestros personajes sean conocidos, quiero que triunfemos en nuestro futuro.Solo imagina tu enorme estante de merch de Pinkie Pie...",
        "imagen": "https://raw.githubusercontent.com/danielzarate1401-lab/yanomas/main/AbiertoFrente.png",
        "siguiente": 64
    },
    64: {
        "personaje": "Daniel",
        "texto": "Al lado estaria mi colección del manga de JoJos. Nuestras PCs al lado una de la otra para programar y jugar. En nuestra cocina un refri lleno de comida para que cocinemos lo que queramos.",
        "imagen": "https://raw.githubusercontent.com/danielzarate1401-lab/yanomas/main/Abiertoblush.png",
        "siguiente": 65
    },
    65: {
        "personaje": "Daniel",
        "texto": "Un castillo para nuestros gatitos Nirvana y Korn. Y un cuarto para nuestros hijos.... Sip ya sabes, nuestros hijos: Kurt y Frances, nuestros amores :3",
        "imagen": "https://raw.githubusercontent.com/danielzarate1401-lab/yanomas/main/Abiertoblush.png",
        "siguiente": 66
    },
    66: {
        "personaje": "Daniel",
        "texto": "Ah y nuestros otros hijos: Nirvana 2, Pinkie Pie, Shadow, Apolo, Yorkenson, Nainileven, Nirvana 3,5, Rainbow Dash, Rarity, Starlight, Sunset, Cheese Sandwich, Pelirrojo, Minipam, Minidani...",
        "imagen": "https://raw.githubusercontent.com/danielzarate1401-lab/yanomas/main/Abiertoblush.png",
        "siguiente": 67
    },
    67: {
        "personaje": "Daniel",
        "texto": "...Mpa, Map, Pma, Vox, Charlie Kirk, Mexican Seafood, Anexorcist, Adoptado, Adoptadito, Tusk, Periwinkle, Coca de Dieta, Nuggets, Kira, Akira, Michi, Whiplash, Orion, Blackened...",
        "imagen": "https://raw.githubusercontent.com/danielzarate1401-lab/yanomas/main/chibi.png",
        "siguiente": 68
    },
    68: {
        "personaje": "Daniel",
        "texto": "...Serv, Makima, Varka, Treintaiun Minutos, Venecolano, Venecalono, Iv, Cloe, C++,  KKK, Copi-Copi, Elemento, Adjetivo, Mente en Blanco, Chaucha, Yo Soy, Calugoso, Duquesa, Reina...",
        "imagen": "https://raw.githubusercontent.com/danielzarate1401-lab/yanomas/main/chibi.png",
        "siguiente": 69
    },
    69: {
        "personaje": "Daniel",
        "texto": "...Coliforme, Tepo-Tepo, Yo no Fui, Fierro Malo, Palmerita, Neumatex, Cortachurro, Etcétera, Maletín, Duque, Guasón, Jefe, Moneda, Cucky, Pelusa, Tía, Legui, Reality...",
        "imagen": "https://raw.githubusercontent.com/danielzarate1401-lab/yanomas/main/chibi.png",
        "siguiente": 70
    },
    70: {
        "personaje": "Daniel",
        "texto": "...Chester, Chu, Ro, Playita, Palmera, Señor, Re Frito, Pescado, Chamuyo, Calendario, James Bond, Rata, Cabeza de Chaya, Neumático, Repetido, Añico, Rucia, Gonzo, Chino, Cortéz, Albertito.",
        "imagen": "https://raw.githubusercontent.com/danielzarate1401-lab/yanomas/main/chibi.png",
        "siguiente": 71
    },
    71: {
        "personaje": "Daniel",
        "texto": "Bueno, ahora yendo con los que no queremos son... Ok ya paro. No sé, es lindo pensar en procrear contigo. Tener una familia. Tener cualquier cosa contigo.",
        "imagen": "https://raw.githubusercontent.com/danielzarate1401-lab/yanomas/main/chibi.png",
        "siguiente": 72
    },
    72: {
        "personaje": "Daniel",
        "texto": "Me esforzaré porque todo salga bien, esto es una prueba de ello por ejemplo. Te amo tanto como para dejar el procrastinamiento, te amo tanto como para dar todo de mi.",
        "imagen": "https://raw.githubusercontent.com/danielzarate1401-lab/yanomas/main/CerradoAbajo.png",
        "siguiente": 73
    },
    73: {
        "personaje": "Daniel",
        "texto": "Porque al final, mi niño, al final tu mereces lo mejor de lo mejor. Mereces un mejor novio, pero yo quiero ser ese mejor novio.",
        "imagen": "https://raw.githubusercontent.com/danielzarate1401-lab/yanomas/main/Cerradoblush.png",
        "siguiente": 74
    },
    74: {
        "personaje": "Daniel",
        "texto": "Mi amor, mi Pam, felices 5 meses y vamos por muchos mas, te amo.",
        "imagen": "https://raw.githubusercontent.com/danielzarate1401-lab/yanomas/main/Abiertoblush.png",
        "siguiente": None
    },
    75: {
        "personaje": "Daniel", # Cambia por el link de la emoción
        "texto": "hmmm...",
        "imagen": "https://raw.githubusercontent.com/danielzarate1401-lab/yanomas/main/CerradoSerio.png",
        "siguiente": 48  
    },
}

# --- 4. LÓGICA DE PANTALLAS ---
if st.session_state.jugando:
    # Obtenemos la escena actual
    escena = historia.get(st.session_state.paso, historia[0])
    
    # Manejo de manos (Overlay)
    manos_html = ""
    if "manos" in escena:
        manos_html = f'<img src="{escena["manos"]}" class="manos-overlay">'
    
    # Marco de la Consola
    st.markdown('<div class="marco-consola">', unsafe_allow_html=True)
    st.markdown(f'''
        <div class="pantalla-juego">
            <img src="{escena["imagen"]}" class="personaje-img">
            {manos_html}
        </div>
        <div class="dialogo-box">
            <div class="nombre-personaje">{escena["personaje"]}</div>
            <div style="font-size: 16px; line-height: 1.3;">{escena["texto"]}</div>
        </div>
    ''', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True) 

    # Contenedor de Botones
    st.markdown('<div class="contenedor-botones">', unsafe_allow_html=True)
    if "opciones" in escena:
        for i, opcion in enumerate(escena["opciones"]):
            # Key única por paso y opción para evitar errores de duplicados
            if st.button(opcion["texto"], key=f"btn_{st.session_state.paso}_{i}"):
                st.session_state.paso = opcion["destino"]
                st.rerun()
    else:
        # Botón único de continuar
        if st.button("Continuar", key=f"btn_next_{st.session_state.paso}"):
            if escena.get("siguiente") is not None:
                st.session_state.paso = escena["siguiente"]
                st.rerun()
            else:
                st.session_state.jugando = False
                st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    # Audio
    if "musica" in escena:
        if escena["musica"] != st.session_state.musica_actual:
            st.session_state.musica_actual = escena["musica"]
    
    if st.session_state.musica_actual and st.session_state.musica_actual != "ninguna":
        st.audio(st.session_state.musica_actual, format="audio/mp3", autoplay=True, loop=True)

else:
    # --- PANTALLA DE INICIO (RESTABLECIDA) ---
    st.markdown("""
        <div class="caja-titulo">
            <h1> Felices 5 Meses amor</h1>
        </div>
    """, unsafe_allow_html=True)

    # El marco de la consola
    st.markdown('<div class="marco-consola" style="text-align:center; min-height: 200px; display:flex; flex-direction:column; justify-content:center;">', unsafe_allow_html=True)
    st.markdown('<p style="color:white; font-family:Quicksand; font-size: 18px;">Para el mejor novio del mundo</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # El botón para empezar
    st.markdown('<div class="contenedor-botones">', unsafe_allow_html=True)
    if st.button("Empezar", key="btn_start"):
        st.session_state.jugando = True
        st.session_state.paso = 0
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
