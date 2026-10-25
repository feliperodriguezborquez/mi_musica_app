"""
Contenido exhaustivo para las Áreas 2, 3, 4 y 5 de Formación Litúrgica:
- Área 2: El Año Litúrgico y sus Tiempos (Matriz sinóptica + Tratados por tiempo + Antífonas de la 'O' + Triduo Pascual)
- Área 3: Biblioteca y Documentos Oficiales del Magisterio (IGMR, Musicam Sacram, Sacrosanctum Concilium, Tra le Sollecitudini, OGLH, CECh/CONALI + Antología Patrística)
- Área 4: Guía para el Músico, Coro y Compositor Litúrgico (Prosodia con ejemplos prácticos, Arquitectura de Formas Musicales, Tesitura, Instrumentación IGMR 313, Dirección y Pedagogía de Ensayo)
- Área 5: Otras Celebraciones y Liturgias (Adoración Eucarística con textos latín/español, Liturgia de las Horas con Benedictus/Magnificat/Nunc Dimittis, Exequias, Matrimonio y Confirmación)
"""

from typing import List, Dict, Any


# =============================================================================
# ÁREA 2: EL AÑO LITÚRGICO Y SUS CRITERIOS MUSICALES (EXHAUSTIVO)
# =============================================================================
MATRIZ_ANO_LITURGICO: List[Dict[str, str]] = [
    {
        "tiempo": "Adviento",
        "color_hex": "#6a4c93",
        "color_nombre": "Morado (y Rosado en III Dom. Gaudete)",
        "gloria": "No (salvo Solemnidades y Fiestas, ej. 8 y 12 dic.)",
        "aleluya": "Sí (se canta en todos los domingos y ferias)",
        "instrumentos": "Con moderación que convenga al tiempo, sin anticipar Navidad (IGMR 313)",
        "antifona_mariana": "Alma Redemptoris Mater",
    },
    {
        "tiempo": "Navidad y Epifanía",
        "color_hex": "#c99b1e",
        "color_nombre": "Blanco / Dorado",
        "gloria": "Sí (en todos los domingos, Octava de Navidad, Epifanía y Bautismo del Señor)",
        "aleluya": "Sí (solemne)",
        "instrumentos": "Plenitud festiva y coral",
        "antifona_mariana": "Alma Redemptoris Mater (hasta el 2 de febrero)",
    },
    {
        "tiempo": "Cuaresma",
        "color_hex": "#5e3c87",
        "color_nombre": "Morado (y Rosado en IV Dom. Laetare)",
        "gloria": "No (salvo Solemnidades de San José 19 mar. y Anunciación 25 mar.)",
        "aleluya": "PROHIBIDO siempre (incluso en Solemnidades). Se canta «Honor y gloria a ti, Señor Jesús»",
        "instrumentos": "SOLO para sostener el canto (prohibido tocar instrumentos solos, IGMR 313), salvo Laetare y Solemnidades",
        "antifona_mariana": "Ave Regina caelorum",
    },
    {
        "tiempo": "Triduo Pascual",
        "color_hex": "#9b2c2c",
        "color_nombre": "Blanco (Jueves y Vigilia) · Rojo (Viernes Santo)",
        "gloria": "Jueves Santo y Vigilia Pascual con repique de campanas (tras lo cual callan hasta la Vigilia)",
        "aleluya": "Se omite Jueves y Viernes; reaparece solemnemente en la Vigilia Pascual",
        "instrumentos": "Mudos desde el final del Gloria del Jueves Santo hasta el Gloria de la Vigilia Pascual (Viernes Santo a cappella)",
        "antifona_mariana": "Regina caeli (desde la Vigilia Pascual)",
    },
    {
        "tiempo": "Tiempo Pascual y Pentecostés",
        "color_hex": "#d4a72c",
        "color_nombre": "Blanco / Dorado (Rojo en Pentecostés)",
        "gloria": "Sí (todos los domingos y durante toda la Octava de Pascua)",
        "aleluya": "Sí (se añade doble Aleluya a las antífonas y al envío; Secuencias obligatorias en Pascua y Pentecostés)",
        "instrumentos": "Plenitud pascual y festiva",
        "antifona_mariana": "Regina caeli laetare",
    },
    {
        "tiempo": "Tiempo Ordinario",
        "color_hex": "#2f6b48",
        "color_nombre": "Verde",
        "gloria": "Sí en Domingos, Solemnidades y Fiestas (No en ferias ni memorias)",
        "aleluya": "Sí",
        "instrumentos": "Uso normal al servicio del canto y la dignidad del templo",
        "antifona_mariana": "Salve Regina",
    },
]

ANTIFONAS_MAYORES_O: List[Dict[str, str]] = [
    {
        "fecha": "17 de diciembre",
        "titulo_lat": "O Sapientia",
        "titulo_es": "¡Oh Sabiduría!",
        "cita_biblica": "Eclesiástico 24, 3; Sabiduría 8, 1",
        "texto_lat": "O Sapiéntia, quæ ex ore Altíssimi prodísti, attíngens a fine usque ad finem, fórtiter suavitérque dispónens ómnia: veni ad docéndum nos viam prudéntiæ.",
        "texto_es": "«¡Oh Sabiduría, que brotaste de los labios del Altísimo, abarcando del uno al otro confín y ordenándolo todo con firmeza y suavidad: ven y muéstranos el camino de la salvación!»",
    },
    {
        "fecha": "18 de diciembre",
        "titulo_lat": "O Adonai",
        "titulo_es": "¡Oh Adonai, Pastor de la casa de Israel!",
        "cita_biblica": "Éxodo 3, 2; 19, 16-20",
        "texto_lat": "O Adonái, et Dux domus Israël, qui Móysi in igne flammæ rubi apparuísti, et ei in Sina legem dedísti: veni ad rediméndum nos in bráchio exténto.",
        "texto_es": "«¡Oh Adonai, Pastor de la casa de Israel, que te apareciste a Moisés en la zarza ardiente y en el Sinaí le diste tu ley: ven a librarnos con el poder de tu brazo!»",
    },
    {
        "fecha": "19 de diciembre",
        "titulo_lat": "O Radix Iesse",
        "titulo_es": "¡Oh Renuevo del tronco de Jesé!",
        "cita_biblica": "Isaías 11, 1. 10; 52, 15",
        "texto_lat": "O Radix Iesse, qui stas in signum populórum, super quem continébunt reges os suum, quem Gentes deprecabúntur: veni ad liberándum nos, iam noli tardáre.",
        "texto_es": "«¡Oh Renuevo del tronco de Jesé, que te alzas como un signo para los pueblos; ante quien los reyes enmudecen y cuyo auxilio imploran las naciones: ven a librarnos, no tardes más!»",
    },
    {
        "fecha": "20 de diciembre",
        "titulo_lat": "O Clavis David",
        "titulo_es": "¡Oh Llave de David!",
        "cita_biblica": "Isaías 22, 22; 9, 6; Apocalipsis 3, 7",
        "texto_lat": "O Clavis David, et sceptrum domus Israël; qui áperis, et nemo claudit; claudis, et nemo áperit: veni, et educ vinctum de domo cárceris, sedéntem in ténebris, et umbra mortis.",
        "texto_es": "«¡Oh Llave de David y Cetro de la casa de Israel; que abres y nadie puede cerrar, cierras y nadie puede abrir: ven y libra a los cautivos que viven en tinieblas y en sombra de muerte!»",
    },
    {
        "fecha": "21 de diciembre",
        "titulo_lat": "O Oriens",
        "titulo_es": "¡Oh Sol que naces de lo alto (Oriente)!",
        "cita_biblica": "Zacarías 6, 12; Malaquías 4, 2; Lucas 1, 78-79",
        "texto_lat": "O Óriens, splendor lucis ætérnæ, et sol iustítiæ: veni, et illúmina sedéntes in ténebris, et umbra mortis.",
        "texto_es": "«¡Oh Sol que naces de lo alto, Resplandor de la luz eterna, Sol de justicia: ven ahora a iluminar a los que viven en tinieblas y en sombra de muerte!»",
    },
    {
        "fecha": "22 de diciembre",
        "titulo_lat": "O Rex Gentium",
        "titulo_es": "¡Oh Rey de las naciones y Piedra angular!",
        "cita_biblica": "Ageo 2, 7; Isaías 28, 16; Efesios 2, 14-20",
        "texto_lat": "O Rex Géntium, et desiderátus eárum, lapísque anguláris, qui facis útraque unum: veni, et salva hóminem, quem de limo formásti.",
        "texto_es": "«¡Oh Rey de las naciones y Deseado de los pueblos, Piedra angular de la Iglesia, que haces de dos pueblos uno solo: ven y salva al hombre, que formaste del barro de la tierra!»",
    },
    {
        "fecha": "23 de diciembre",
        "titulo_lat": "O Emmanuel",
        "titulo_es": "¡Oh Emmanuel, Dios con nosotros!",
        "cita_biblica": "Isaías 7, 14; 33, 22; Mateo 1, 23",
        "texto_lat": "O Emmánuel, Rex et lágifer noster, exspectátio Géntium, et Salvátor eárum: veni ad salvándum nos, Dómine, Deus noster.",
        "texto_es": "«¡Oh Emmanuel, Rey y Legislador nuestro, esperanza de las naciones y salvador de los pueblos: ven a salvarnos, Señor Dios nuestro!»",
    },
]

TRATADO_TIEMPOS_DETALLADO: List[Dict[str, Any]] = [
    {
        "id": "t-adviento",
        "nombre": "1. Tiempo de Adviento",
        "color": "#6a4c93",
        "lema_latino": "Rorate, caeli, desuper · Veni, Domine Iesu",
        "estructura": "Dos etapas: 1) Desde el I Domingo hasta el 16 de diciembre (orientada a la segunda venida escatológica o Parusía del Señor); 2) Del 17 al 24 de diciembre (Feria Mayor de Adviento, orientada directamente a preparar la Natividad mediante las 7 Antífonas Mayores de la 'O').",
        "normativa_musical": "Se omite el Gloria in excelsis (NUN 53) para que el canto de los ángeles resuene como novedad en la Nochebuena; sí se canta el Aleluya antes del Evangelio. El órgano y los demás instrumentos deben emplearse con aquella moderación que conviene a la índole del tiempo, sin anticipar la alegría plena de la Navidad (IGMR 313).",
        "repertorio_clave": "Salmos 24, 79 y 84; prosas «Rorate caeli desuper», himno «Veni, veni Emmanuel» (que glosa las 7 Antífonas de la 'O', cuyo acróstico inverso en latín —Emmanuel, Rex, Oriens, Clavis, Radix, Adonai, Sapientia— forma las palabras ERO CRAS: 'Mañana estaré allí'), «Conditor alme siderum».",
    },
    {
        "id": "t-navidad",
        "nombre": "2. Tiempo de Navidad y Epifanía",
        "color": "#c99b1e",
        "lema_latino": "Verbum caro factum est · Puer natus est nobis",
        "estructura": "Desde las I Vísperas de la Natividad del Señor (24 dic. en la tarde) hasta el Domingo del Bautismo del Señor inclusive (con las cumbres de la Sagrada Familia, Santa María Madre de Dios el 1 de enero y la Epifanía del Señor).",
        "normativa_musical": "Regresa el Gloria in excelsis con máximo esplendor vocal e instrumental. En las cuatro Misas propias de la Navidad (Vigilia, Medianoche o 'del Gallo', Aurora y Día), el Credo lleva genuflexión (arrodillarse todos) en las palabras «y por obra del Espíritu Santo se encarnó de María, la Virgen, y se hizo hombre» (IGMR 275b).",
        "repertorio_clave": "Distinguir entre cantos propiamente litúrgicos del misterio de la Encarnación para la Entrada y Comunión (Salmo 97 «Canten al Señor un cántico nuevo», «Adeste fideles», «Puer natus in Bethlehem») y los villancicos folclóricos tradicionales chilenos (tonadas de Niño Dios), que encuentran su lugar ideal en la presentación de los dones, en la adoración del Niño al final de la Misa o en la salida.",
    },
    {
        "id": "t-cuaresma",
        "nombre": "3. Tiempo de Cuaresma",
        "color": "#5e3c87",
        "lema_latino": "Attende, Domine, et miserere · Parce, Domine",
        "estructura": "Desde el Miércoles de Ceniza hasta antes de la Misa Vespertina de la Cena del Señor del Jueves Santo (40 días de camino bautismal y penitencial hacia la Pascua).",
        "normativa_musical": "1) Supresión total del Aleluya en todas las celebraciones (incluidas las Solemnidades de San José y la Anunciación).\n2) Supresión del Gloria (excepto en Solemnidades y Fiestas).\n3) Prohibición de música puramente instrumental: el órgano y los instrumentos se permiten ÚNICAMENTE para sostener la afinación del canto (IGMR 313), excepto en el IV Domingo (Laetare), Solemnidades y Fiestas.",
        "repertorio_clave": "Miércoles de Ceniza (Imposición de la ceniza): Salmo 50 («Misericordia, Dios mío»), Joel 2 («Entre el vestíbulo y el altar lloren los sacerdotes: Perdona, Señor, a tu pueblo»). Domingos de Cuaresma: Salmo 90, «Attende Domine», polifonía a cappella, Kyrie y Sanctus modales.",
    },
    {
        "id": "t-triduo",
        "nombre": "4. Semana Santa y Sagrado Triduo Pascual",
        "color": "#9b2c2c",
        "lema_latino": "Crux fidelis · Christus factus est · Surrexit Dominus vere",
        "estructura": "Domingo de Ramos en la Pasión del Señor, y el Sagrado Triduo Pascual: Jueves Santo (Cena del Señor), Viernes Santo (Pasión del Señor), Sábado Santo (sepultura y silencio) y Vigilia Pascual en la Noche Santa.",
        "normativa_musical": "• Domingo de Ramos: Procesión con «Hosanna al Hijo de David» e himno «Gloria, alabanza y honor» (Gloria, laus et honor).\n• Jueves Santo: Entrada con Gálatas 6, 14 («Nosotros hemos de gloriarnos en la cruz»); en el Gloria repican las campanas y luego callan junto con el órgano hasta la Vigilia Pascual; Lavatorio de los pies (Juan 13, Mandatum novum); Ofertorio con «Ubi caritas et amor»; Procesión al Monumento con «Pange lingua / Tantum ergo».\n• Viernes Santo: Entrada en silencio absoluto (sin canto ni instrumento); Pasión según San Juan; Adoración de la Santa Cruz con los Improperia («Pueblo mío, ¿qué te he hecho? / Hagios o Theós», «Crux fidelis», Salmo 66), todo estrictamente a cappella.\n• Vigilia Pascual: Lucernario («Luz de Cristo»), Pregón Pascual (Exsultet), Salmos de las lecturas del AT, Gloria con campanas y órgano, Triple Aleluya Pascual con Salmo 117, Letanías de los Santos, «Vidi aquam» en la aspersión.",
        "repertorio_clave": "Es la cumbre de todo el año para el coro litúrgico: preparar los cantos propios de cada rito (Lavatorio, Ubi caritas, Pange lingua, Improperia, Exsultet y Vidi aquam).",
    },
    {
        "id": "t-pascua",
        "nombre": "5. Tiempo Pascual y Solemnidad de Pentecostés",
        "color": "#d4a72c",
        "lema_latino": "Haec dies quam fecit Dominus, alleluia",
        "estructura": "Los 50 días desde el Domingo de la Resurrección hasta el Domingo de Pentecostés se celebran con alegría y exultación como un solo día festivo, más aún, como «un gran Domingo» (Normas Universales del Año Litúrgico, n. 22).",
        "normativa_musical": "1) Presencia constante del Aleluya en todas las antífonas.\n2) Aspersión dominical recomendada con la antífona «Vidi aquam».\n3) Secuencias obligatorias el Domingo de Pascua (Victimae paschali laudes) y el Domingo de Pentecostés (Veni, Sancte Spiritus).\n4) Doble Aleluya en la despedida («Pueden ir en paz, aleluya, aleluya — Demos gracias a Dios, aleluya, aleluya») en la Octava de Pascua y en Pentecostés.\n5) Antífona mariana final: «Regina caeli laetare».",
        "repertorio_clave": "Salmo 117 («Éste es el día en que actuó el Señor»), Salmo 65, «O filii et filiae», «Regina caeli», Secuencias de Pascua y Pentecostés.",
    },
    {
        "id": "t-ordinario",
        "nombre": "6. Tiempo Ordinario (Per Annum)",
        "color": "#2f6b48",
        "lema_latino": "Dominus illuminatio mea · Cantate Domino",
        "estructura": "33 o 34 semanas divididas en dos etapas (desde el lunes tras el Bautismo del Señor hasta el martes antes de Ceniza, y desde el lunes tras Pentecostés hasta el sábado tras la Solemnidad de Jesucristo, Rey del Universo).",
        "normativa_musical": "Cada domingo es la Pascua semanal (con Gloria, Salmo, Aleluya y Credo). La selección de los cantos de Entrada y sobre todo de Comunión debe acompañar la lectura semicontinua del Evangelio sinóptico propio del ciclo anual: Ciclo A (San Mateo), Ciclo B (San Marcos y capítulo 6 de San Juan sobre el Pan de Vida entre los domingos XVII y XXI) y Ciclo C (San Lucas).",
        "repertorio_clave": "Salmos dominicales (18, 22, 26, 33, 62, 83, 94, 99, 102, 121, 144) y la antífona mariana «Salve Regina».",
    },
]


# =============================================================================
# ÁREA 3: ANTOLOGÍA HISTÓRICA Y PATRÍSTICA SOBRE LA MÚSICA SAGRADA
# =============================================================================
ANTOLOGIA_PATRISTICA: List[Dict[str, str]] = [
    {
        "autor": "San Ignacio de Antioquía († c. 107)",
        "obra": "Carta a los Efesios, IV, 1-2",
        "época": "Siglo II · Padres Apostólicos",
        "cita": "«Por eso, en la concordia de ustedes y en su amor sinfónico (symphonos agape) es cantado Jesucristo. Y cada uno de ustedes forme parte del coro, para que, siendo consonantes en la unanimidad y tomando el tono de Dios en la unidad, canten a una sola voz por medio de Jesucristo al Padre, a fin de que Él los escuche y los reconozca por sus buenas obras como miembros de su Hijo.»",
        "comentario": "Primera gran metáfora coral del cristianismo: la Iglesia unida al Obispo y a los presbíteros es una cítara afinada que canta a Cristo en una sola voz.",
    },
    {
        "autor": "San Basilio Magno (330–379)",
        "obra": "Homilía sobre el Salmo I, nn. 1–2 (PG 29, 212)",
        "época": "Siglo IV · Padres Capadocios",
        "cita": "«El Espíritu Santo, viendo que el género humano era difícil de conducir hacia la virtud y que por nuestra inclinación al placer descuidábamos la vida recta, ¿qué hizo? Mezcló la dulzura de la melodía con la doctrina, para que por medio de la suavidad y gracia de lo que escuchamos recibiéramos sin darnos cuenta la utilidad de las palabras... Por eso nos ideó estos armoniosos cantos de los Salmos, que son obra de ángeles, ciudadanía del cielo e incienso espiritual.»",
        "comentario": "Explica por qué la Palabra de Dios se canta: la belleza melódica abre el corazón humano para que penetre la medicina espiritual de la Escritura.",
    },
    {
        "autor": "San Ambrosio de Milán (340–397)",
        "obra": "Explanatio Psalmi I, 9 (PL 14, 924)",
        "época": "Siglo IV · Padre de la Himnodia Occidental",
        "cita": "«El Salmo es bendición del pueblo, alabanza de Dios, elogio de la asamblea, aclamación de todos, voz de la Iglesia, confesión armoniosa de la fe... En el canto de los salmos compiten los hombres y las mujeres, los ancianos y los niños sin distinción; y de las voces de todos se levanta como el rumor de las grandes olas del mar. ¿Qué hay más hermoso que este salmo en que resuena el vínculo de la unidad?»",
        "comentario": "San Ambrosio introdujo en Occidente (Milán, año 386) el canto antifonal de los salmos e himnos con toda la asamblea reunida.",
    },
    {
        "autor": "San Agustín de Hipona (354–430)",
        "obra": "Confesiones IX, 6, 14 y Sermón 336, 1",
        "época": "Siglos IV–V · Doctor de la Gracia",
        "cita": "«¡Cuánto lloré entre tus himnos y cánticos, profundamente conmovido por las voces de tu Iglesia que cantaba dulcemente! Aquellas voces fluían en mis oídos y tu verdad se destilaba en mi corazón, y de allí brotaba el afecto de la piedad, y corrían mis lágrimas, y me hacía bien con ellas.» — «Porque cantar es propio de quien ama (Cantare amantis est).»",
        "comentario": "La frase «Cantare amantis est» (Sermón 336, 1) fue incorporada textualmente en el numeral 39 de la Instrucción General del Misal Romano.",
    },
    {
        "autor": "San Juan Crisóstomo (347–407)",
        "obra": "In Psalmum XLI, 1 (PG 55, 156)",
        "época": "Siglo IV · Doctor de la Eucaristía",
        "cita": "«Nada eleva tanto al alma, nada le da alas y la desprende de la tierra, nada la libera de las ataduras del cuerpo y le inspira el amor a la sabiduría como el canto concorde y la melodía divina compuesta con ritmo sagrado.»",
        "comentario": "Fundamenta la dignidad estética y espiritual del canto sagrado frente a las melodías teatrales y profanas.",
    },
    {
        "autor": "Papa San Pío X (1835–1914)",
        "obra": "Motu Proprio «Tra le sollecitudini», nn. 1–2",
        "época": "22 de noviembre de 1903",
        "cita": "«La música sagrada, como parte integrante de la liturgia solemne, participa de su fin general, que es la gloria de Dios y la santificación y edificación de los fieles... Debe, por consiguiente, poseer en grado eminente las cualidades propias de la liturgia, y en particular la santidad y la bondad de las formas, de donde nace espontáneo otro carácter suyo: la universalidad.»",
        "comentario": "Documento fundacional de la renovación litúrgico-musical contemporánea que definió las tres notas de la música sacra: Santidad, Bondad de las formas (belleza artística) y Universalidad.",
    },
    {
        "autor": "Papa Benedicto XVI (Joseph Ratzinger)",
        "obra": "Exhortación Apostólica «Sacramentum Caritatis», n. 42",
        "época": "22 de febrero de 2007",
        "cita": "«En el ars celebrandi ocupa un puesto destacado el canto litúrgico. Con razón afirma san Agustín en un famoso sermón: 'El hombre nuevo conoce el cántico nuevo. Cantar es expresión de alegría y, si lo pensamos bien, expresión de amor'. El Pueblo de Dios reunido para la celebración canta las alabanzas de Dios... Efectivamente, en la liturgia no podemos decir que una canción vale igual que otra. A este respecto, hay que evitar la genérica improvisación o la introducción de géneros musicales no respetuosos del sentido de la liturgia. Como elemento litúrgico, el canto debe estar en consonancia con el misterio celebrado, así como con las diversas partes del rito.»",
        "comentario": "Síntesis magisterial reciente: en la liturgia «no vale una canción igual que otra»; el canto es parte de la acción sacramental (ars celebrandi).",
    },
]


# =============================================================================
# ÁREA 4: GUÍA COMPLETA PARA EL MÚSICO, CORO Y COMPOSITOR LITÚRGICO
# =============================================================================
GUIA_MUSICO_TRATADO: List[Dict[str, Any]] = [
    {
        "id": "mus-prosodia",
        "numero": "I",
        "titulo": "Prosodia Castellana y Primacía de la Palabra («Logos»)",
        "cita": "Sacrosanctum Concilium 112, 121",
        "resumen": "En la música litúrgica cristiana la melodía nace de la Palabra revelada. Cuando un compositor respeta las leyes prosódicas del idioma español, la asamblea comprende el texto al instante y lo canta con naturalidad.",
        "principios": [
            {
                "regla": "1. Ley de coincidencia entre Acento Tónico e Ictus Musical",
                "explicacion": "Toda palabra significativa en español (sustantivos, verbos, adjetivos, adverbios) tiene una sílaba tónica. Esa sílaba tónica DEBE coincidir con el tiempo fuerte (1.er tiempo) o semifuerte del compás, o bien con una nota de mayor duración o altura melódica.",
                "ejemplo_incorrecto": "❌ INCORRECTO: Poner en tiempo fuerte artículos, preposiciones o conjunciones átonas («EL Se-ñor es LA luz DE mi vi-DA»).",
                "ejemplo_correcto": "✅ CORRECTO: Dar anacrusa (tiempo débil previo) a las sílabas átonas para que el primer tiempo caiga sobre la sílaba tónica («El Se-[ÑOR] es mi [LUZ] y mi [SAL]-va-[CIÓN]»).",
            },
            {
                "regla": "2. Tratamiento de palabras Agudas, Graves y Esdrújulas en las Cadencias",
                "explicacion": "• Palabras AGUDAS (Se-ñor, pie-dad, bon-dad, cruz, paz): piden resolver directamente sobre el tiempo fuerte del compás final (cadencia masculina).\n• Palabras GRAVES o LLANAS (glo-ria, san-to, cie-lo, vi-da): piden apoyar la penúltima sílaba en el tiempo fuerte y relajar suavemente la última sílaba átona (cadencia femenina).\n• Palabras ESDRÚJULAS (Es-pí-ri-tu, u-ní-so-no, cá-li-ces): exigen que la antepenúltima sílaba reciba el acento principal y las dos sílabas finales desciendan con ligereza sin alargar la última.",
                "ejemplo_incorrecto": "❌ INCORRECTO: Cantar «Es-pi-ri-TÚ San-TÓ» alargando la última sílaba en el primer tiempo.",
                "ejemplo_correcto": "✅ CORRECTO: «Es-[PÍ]-ri-tu [SAN]-to» (tresillo o corchea con puntillo sobre -pí-).",
            },
            {
                "regla": "3. Sinalefas Naturales del Español Cantado",
                "explicacion": "En español, cuando una palabra termina en vocal y la siguiente comienza en vocal átona o 'h' muda, se unen en una sola emisión métrica (sinalefa), salvo que haya una coma o cesura lógica de sentido.",
                "ejemplo_incorrecto": "❌ INCORRECTO: Separar artificialmente con hipos cada vocal («Por-que / a-mor / es / Dios»).",
                "ejemplo_correcto": "✅ CORRECTO: Unir con fluidez vocal las sinalefas («Cuan-do_el Se-ñor nos ha-bla_al co-ra-zón»).",
            },
        ],
    },
    {
        "id": "mus-formas",
        "numero": "II",
        "titulo": "Las 5 Formas Musicales Litúrgicas y Cuándo Emplear Cada Una",
        "cita": "IGMR 39–41 · Musicam Sacram 16–21",
        "resumen": "Un error frecuente en la composición parroquial es escribir todos los cantos de la Misa con la misma estructura de 'canción estrofa-estribillo'. Cada rito tiene su propia arquitectura formal:",
        "principios": [
            {
                "regla": "1. Forma Dialogada / Acclamatio (Diálogos, Amén, Aclamación Memorial, Oración Universal)",
                "explicacion": "Fórmulas breves (1 a 4 compases), directas y unánimes. No llevan preludios instrumentales: responden inmediatamente a la voz del presidente o del diácono.",
            },
            {
                "regla": "2. Forma Letánica (Kyrie eleison, Agnus Dei, Letanías de los Santos)",
                "explicacion": "Invocaciones reiteradas donde el cantor o el coro lanza el título cristológico («Cordero de Dios, que quitas el pecado del mundo») y toda la asamblea responde con la súplica constante («ten piedad de nosotros» / «danos la paz»).",
            },
            {
                "regla": "3. Forma Himnódica Continua o In Directum (Gloria in excelsis, Sanctus, Credo, Te Deum)",
                "explicacion": "El texto se desarrolla de principio a fin sin volver atrás a un estribillo. Se ejecuta por todos juntos o alternando bloques entre dos coros (Asamblea y Coro polifónico SATB).",
            },
            {
                "regla": "4. Forma Responsorial Salmódica (Salmo Responsorial, Canto de Entrada, Canto de Comunión)",
                "explicacion": "La asamblea canta una antífona breve y memorable (A), y el salmista o el coro canta los versículos del salmo (B, C, D) sobre una cuerda de recitación o melodía estrófica.",
            },
            {
                "regla": "5. Motete Coral o Pieza Instrumental (Ofertorio, Post-Comunión tras el silencio)",
                "explicacion": "Obras donde la schola o coro polifónico a 3 o 4 voces canta sola para favorecer la contemplación interior de la asamblea (permitido en el Ofertorio, en la Entrada/Comunión ocasionalmente, y tras la Comunión).",
            },
        ],
    },
    {
        "id": "mus-tesitura-coro",
        "numero": "III",
        "titulo": "Ámbito Vocal Congregacional y el Ministerio del Coro Polifónico (SATB)",
        "cita": "Musicam Sacram 19–23 · IGMR 103",
        "resumen": "El Concilio Vaticano II no contrapone el Coro a la Asamblea: el coro es parte de la asamblea y ejerce un ministerio litúrgico propio e insustituible.",
        "principios": [
            {
                "regla": "1. Registro de Oro para la Asamblea (Re4 a Do5 / Re5)",
                "explicacion": "Una asamblea parroquial mixta (hombres y mujeres cantando a la octava) sin calentamiento vocal previo canta con plenitud y sin fatiga entre el Re4 (o Do4 grave de paso) y el Do5/Re5, manteniendo la tessitura media (notas más frecuentes) entre Mi4 y La4. Si un canto sube reiteradamente a Mi5 o Fa5, la asamblea dejará de cantar.",
            },
            {
                "regla": "2. Cómo Armonizar a 4 Voces (SATB) sin Tapar al Pueblo",
                "explicacion": "Cuando toda la asamblea canta el estribillo o el Santo, la voz de Soprano (o Tenor) lleva con firmeza la melodía principal que canta el pueblo, mientras Contraltos, Tenores y Bajos tejen el sostén armónico. En el último estribillo, una voz de descanto (discantus) de sopranos agudas sobre el canto firme del pueblo eleva enormemente la solemnidad.",
            },
            {
                "regla": "3. Cuándo Canta el Coro Solo y Cuándo Canta con el Pueblo",
                "explicacion": "• SIEMPRE CON EL PUEBLO: Santo, Padre Nuestro, Aclamaciones Eucarísticas, Respuestas de los diálogos y Antífona del Salmo Responsorial.\n• ALTERNANDO CON EL PUEBLO: Estrofas del Canto de Entrada y de Comunión, versículos del Gloria y del Credo, invocaciones del Kyrie y del Cordero de Dios.\n• PUEDE CANTAR EL CORO SOLO: Presentación de los Dones (Ofertorio), un motete post-comunión tras el silencio sagrado o, en ocasiones solemnes, el Gloria o la Comunión.",
            },
        ],
    },
    {
        "id": "mus-instrumentos",
        "numero": "IV",
        "titulo": "Órgano, Guitarra, Cuerdas e Instrumentación en la Liturgia",
        "cita": "Sacrosanctum Concilium 120 · IGMR 313 · Musicam Sacram 62–67",
        "resumen": "En la liturgia católica la voz humana tiene siempre el primado sobre cualquier instrumento, porque solo la voz pronuncia el Logos (la Palabra). Los instrumentos sostienen, embellecen y nunca ahogan el canto.",
        "principios": [
            {
                "regla": "1. Primacía del Órgano y de los Instrumentos de Aliento/Arco Sostenido",
                "explicacion": "La Iglesia tiene en altísima estima el órgano de tubos (o litúrgico) y las cuerdas frotadas (violín, violonchelo) o maderas dulces (flauta, oboe) porque sostienen el aliento largo de la frase vocal humana y envuelven el canto colectivo de la nave.",
            },
            {
                "regla": "2. Uso Noble de la Guitarra en la Liturgia",
                "explicacion": "Cuando se acompaña con guitarra acústica/clásica, debe distinguirse entre momentos líricos y contemplativos (Salmo Responsorial, Cordero de Dios, Comunión), que piden arpegios limpios, acordes plaqué y bajos cantábiles en vez de rasgueos percusivos constantes.",
            },
            {
                "regla": "3. Balance Acústico y Amplificación en el Templo",
                "explicacion": "El volumen de los instrumentos amplificados nunca debe superar a la voz natural de la asamblea reunida. Si los fieles en los bancos no escuchan la voz de quienes están a su lado porque los parlantes del coro aturden el recinto, dejan de cantar.",
            },
        ],
    },
    {
        "id": "mus-ensayo",
        "numero": "V",
        "titulo": "Espiritualidad del Músico Litúrgico y Metodología del Ensayo Parroquial",
        "cita": "Sacrosanctum Concilium 115 · IGMR 103",
        "resumen": "El músico de iglesia no es un artista que ofrece un espectáculo en el templo, sino un ministro litúrgico que ora dos veces y ayuda a orar a sus hermanos.",
        "principios": [
            {
                "regla": "1. Preparar a partir del Leccionario y del Misal (no al azar 10 minutos antes)",
                "explicacion": "La programación musical de cada domingo comienza leyendo la Antífona de Entrada, las tres lecturas bíblicas, el Salmo Responsorial y la Antífona de Comunión del domingo siguiente.",
            },
            {
                "regla": "2. Estructura de un Ensayo Coral Eficaz (60–75 minutos)",
                "explicacion": "1) Oración breve inicial leyendo el Evangelio del domingo (5 min).\n2) Vocalización, respiración diafragmática y afinación de acordes puros (10 min).\n3) Asegurar primero lo propio del domingo: Salmo Responsorial y Versículo del Aleluya (15 min).\n4) Ordinario del Tiempo Litúrgico (Kyrie, Gloria, Santo, Amén, Cordero) a voces (15 min).\n5) Cantos procesionales de Entrada, Comunión y obra nueva en estudio (20 min).",
            },
            {
                "regla": "3. Cómo Enseñar un Canto Nuevo a la Asamblea sin Interrumpir la Misa",
                "explicacion": "Cinco minutos antes de que comience la Misa (nunca cortando la celebración ya iniciada), el director invita amablemente a la asamblea a repasar una o dos veces el estribillo de 4 compases del Salmo Responsorial o del Canto de Entrada/Comunión.",
            },
        ],
    },
]


# =============================================================================
# ÁREA 5: OTRAS CELEBRACIONES, LITURGIA DE LAS HORAS Y SACRAMENTOS
# =============================================================================
OTRAS_CELEBRACIONES_DETALLE: List[Dict[str, Any]] = [
    {
        "id": "cel-adoracion",
        "titulo": "1. Exposición y Bendición con el Santísimo Sacramento (Adoración Eucarística)",
        "cita": "Ritual de la Sagrada Comunión y del Culto a la Eucaristía fuera de la Misa (nn. 82–100)",
        "descripcion": "La Adoración Eucarística prolonga la gracia del sacrificio de la Misa y conduce a los fieles a reconocer en la Hostia consagrada la presencia real y sustancial de Cristo Señor.",
        "estructura_ritual": [
            "1. Exposición: Mientras el ministro trae el Santísimo y lo coloca en la custodia sobre el altar (e inciensa de rodillas), se canta un himno eucarístico de adoración (ej. «Cantemos al Amor de los amores», «O salutaris Hostia», «Altísimo Señor»).",
            "2. Tiempo de Adoración: Se alternan lecturas bíblicas, salmos, cánticos meditativos (Taizé, himnos eucarísticos) y amplios espacios de SILENCIO CONTEMPLATIVO (que nunca debe ser ahogado por música ininterrumpida).",
            "3. Antes de la Bendición: De rodillas, el ministro inciensa el Santísimo mientras se canta el himno «Tantum ergo Sacramentum» (las dos últimas estrofas del Pange lingua de Santo Tomás de Aquino) o otro canto eucarístico venerado.",
            "4. Oración Presidencial y Bendición Eucarística: El ministro de pie canta o dice «Les diste el pan del cielo / Que contiene en sí todo deleite» y la oración «Oh Dios, que en este sacramento admirable...»; luego toma el paño humeral y traza la señal de la Cruz con la custodia en silencio solemne.",
            "5. Reserva y Aclamaciones (Alabanzas de Desagravio): «Bendito sea Dios...» y canto final («Alabado sea el Santísimo» o antífona mariana).",
        ],
        "textos_bilingues": [
            {
                "titulo": "Himno «Tantum ergo Sacramentum» (Santo Tomás de Aquino, 1264)",
                "latin": "Tantum ergo Sacraméntum venerémur cérnui, et antíquum documéntum novo cedat rítui; præstet fides suppleméntum sénsuum deféctui.\nGenitóri, Genitóque laus et iubilátio, salus, honor, virtus quoque sit et benedíctio; procedénti ab utróque compar sit laudátio. Amen.\nV/. Panem de cælo præstitísti eis. (T.P. Allelúia.)\nR/. Omne delectaméntum in se habéntem. (T.P. Allelúia.)",
                "espanol": "Adoremos reverentes tan augusto Sacramento; ceda el antiguo testamento ante el nuevo rito, y la fe supla la incapacidad de los sentidos.\nAl Padre y al Hijo sean dados alabanza y júbilo, salud, honor, poder y bendición; una gloria igual sea dada al que de ambos procede. Amén.\nV/. Les diste el pan del cielo. (T.P. Aleluya.)\nR/. Que contiene en sí todo deleite. (T.P. Aleluya.)",
            },
            {
                "titulo": "Himno «Adoro te devote» (Santo Tomás de Aquino)",
                "latin": "Adóro te devóte, latens Déitas, quæ sub his figúris vere látitas: tibi se cor meum totum súbicit, quia te contémplans totum déficit.\nVisus, tactus, gustus in te fállitur, sed audítu solo tuto créditur; credo quidquid dixit Dei Fílius: nil hoc verbo Veritátis vérius.",
                "espanol": "Te adoro con devoción, Dios escondido, oculto verdaderamente bajo estas apariencias; a ti se somete mi corazón por completo, y se rinde totalmente al contemplarte.\nLa vista, el tacto y el gusto se equivocan en ti, pero solo con el oído se cree con firmeza; creo todo lo que ha dicho el Hijo de Dios: nada es más verdadero que esta palabra de la Verdad.",
            },
        ],
    },
    {
        "id": "cel-horas",
        "titulo": "2. Liturgia de las Horas (Laudes, Vísperas y Completas)",
        "cita": "Ordenación General de la Liturgia de las Horas (OGLH nn. 268–284)",
        "descripcion": "La oración pública de la Iglesia para la santificación del tiempo diario, articulada en sus dos goznes principales: Laudes (al amanecer, memoria de la Resurrección) y Vísperas (al atardecer, sacrificio vespertino de alabanza).",
        "estructura_ritual": [
            "1. Invocación inicial: «Dios mío, ven en mi auxilio / Señor, date prisa en socorrerme. Gloria al Padre... Aleluya» (en Laudes precedida por el Invitatorio Salmo 94 si es la primera hora del día).",
            "2. Himno propio del Tiempo y de la Hora (da el color lírico de la celebración).",
            "3. Salmodia: En Laudes (Salmo matutino + Cántico del Antiguo Testamento + Salmo de alabanza); en Vísperas (Dos Salmos + Cántico del Nuevo Testamento: Flp 2, Col 1, Ef 1 o Apocalipsis), cada uno con su antífona.",
            "4. Lectura breve de la Escritura y Responsorio breve.",
            "5. Cántico Evangélico (Cumbre de la Hora, siempre de pie y santiguándose al inicio): en Laudes el «Benedictus» (Lc 1, 68-79); en Vísperas el «Magnificat» (Lc 1, 46-55); en Completas el «Nunc dimittis» (Lc 2, 29-32).",
            "6. Preces, Padre Nuestro, Oración conclusiva y Bendición (en Completas concluye con la Antífona final a la Santísima Virgen).",
        ],
        "textos_bilingues": [
            {
                "titulo": "Cántico de Zacarías · «Benedictus» (Laudes · Lucas 1, 68-79)",
                "latin": "Benedíctus Dóminus, Deus Israël, quia visitávit et fecit redemptiónem plebi suæ, et eréxit cornu salútis nobis in domo David púeri sui... Per víscera misericórdiæ Dei nostri, in quibus visitávit nos Óriens ex alto, illumináre his, qui in ténebris et in umbra mortis sedent, ad dirigéndos pedes nostros in viam pacis.",
                "espanol": "Bendito sea el Señor, Dios de Israel, porque ha visitado y redimido a su pueblo, suscitándonos una fuerza de salvación en la casa de David, su siervo... Por la entrañable misericordia de nuestro Dios, nos visitará el Sol que nace de lo alto, para iluminar a los que viven en tinieblas y en sombra de muerte, para guiar nuestros pasos por el camino de la paz.",
            },
            {
                "titulo": "Cántico de la Virgen María · «Magnificat» (Vísperas · Lucas 1, 46-55)",
                "latin": "Magníficat ánima mea Dóminum, et exsultávit spíritus meus in Deo salvatóre meo, quia respéxit humilitátem ancíllæ suæ: ecce enim ex hoc beátam me dicent omnes generatiónes. Quia fecit mihi magna qui potens est, et sanctum nomen eius...",
                "espanol": "Proclama mi alma la grandeza del Señor, se alegra mi espíritu en Dios, mi salvador; porque ha mirado la humillación de su esclava. Desde ahora me felicitarán todas las generaciones, porque el Poderoso ha hecho obras grandes por mí: su nombre es santo...",
            },
            {
                "titulo": "Cántico de Simeón · «Nunc dimittis» (Completas · Lucas 2, 29-32)",
                "latin": "Nunc dimíttis servum tuum, Dómine, secúndum verbum tuum in pace: quia vidérunt óculi mei salutáre tuum, quod parásti ante fáciem ómnium populórum: lumen ad revelatiónem géntium, et glóriam plebis tuæ Israël.",
                "espanol": "Ahora, Señor, según tu promesa, puedes dejar a tu siervo irse en paz. Porque mis ojos han visto a tu Salvador, a quien has presentado ante todos los pueblos: luz para alumbrar a las naciones y gloria de tu pueblo Israel.",
            },
        ],
    },
    {
        "id": "cel-sacramentos-exequias",
        "titulo": "3. Celebración de los Sacramentos (Matrimonio, Confirmación) y Exequias Cristianas",
        "cita": "Rituales de los Sacramentos · IGMR 379–385",
        "descripcion": "Criterios esenciales para evitar la secularización musical en bodas y funerales, preservando el sentido pascual de los sacramentos.",
        "estructura_ritual": [
            "• Sacramento del Matrimonio: La boda católica es un Sacramento de la Iglesia y no un evento social privado. Deben excluirse de dentro de la acción litúrgica canciones de películas, baladas pop románticas o arias operísticas de texto profano (como las marchas nupciales teatrales de óperas de Wagner o Mendelssohn si desplazan el canto litúrgico). Textos propios admirables: Salmo 127 («Dichosos los que temen al Señor»), Salmo 33, Salmo 144, Himno a la Caridad de 1 Corintios 13 y Cantar de los Cantares.",
            "• Sacramento de la Confirmación: Destacar los cantos pentecostales durante la imposición de manos y la crismación («Veni, Creator Spiritus», «Veni, Sancte Spiritus», Salmo 103 «Envía tu Espíritu, Señor, y repuebla la faz de la tierra»).",
            "• Misa de Exequias y Funerales (IGMR 379–385): En las exequias cristianas los cantos deben expresar el misterio pascual de la esperanza en la Resurrección y la intercesión por el alma del difunto (Salmo 22 «El Señor es mi pastor», Salmo 129 «Desde lo hondo a ti grito, Señor / De profundis», Salmo 114, «Yo soy la Resurrección y la Vida»). En la Última Encomendación y Despedida (Responsory) brillan las dos antífonas bimilenarias del Ritual de Exequias: «Subvenite, Sancti Dei» y «In paradisum deducant te Angeli».",
        ],
        "textos_bilingues": [
            {
                "titulo": "Antífona de Despedida en las Exequias · «In paradisum» (Ritual de Exequias)",
                "latin": "In paradísum dedúcant te Ángeli; in tuo advéntu suscípiant te Mártyres, et perdúcant te in civitátem sanctam Ierúsalem. Chorus Angelórum te suscípiat, et cum Lázaro quondam páupere ætérnam hábeas réquiem.",
                "espanol": "«Al paraíso te lleven los ángeles, a tu llegada te reciban los mártires y te introduzcan en la ciudad santa de Jerusalén. El coro de los ángeles te reciba y, con Lázaro, pobre en esta vida, tengas eterno descanso.»",
            },
        ],
    },
]
