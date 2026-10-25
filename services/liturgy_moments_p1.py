"""
Base de conocimiento exhaustiva de los 16 momentos de la Santa Misa (Parte 1: Momentos 1 al 9).
Incluye para cada momento:
- Ficha de identidad ritual completa (6 atributos)
- Opciones o Modos de Ejecución del Misal Romano (IGMR)
- Textos litúrgicos oficiales en paralelo (Latín / Español) o Antífonas paradigmáticas
- Semáforo Parroquial de discernimiento pastoral (Lo Esencial, Excepciones y Qué Evitar)
- Adaptación detallada según los 6 Tiempos Litúrgicos
- Tratado Teológico, Mistagógico, Patrístico e Histórico (Ordo Romanus, Padres de la Iglesia, Reforma Conciliar)
- Citas Oficiales íntegras del Magisterio con enlaces directos y visor embebido
- Criterios de Composición, Prosodia, Ámbito Vocal y Dirección en Vivo
- Checklist interactivo de discernimiento (5 preguntas de verificación)
"""

from typing import Dict, Any

MOMENTOS_PARTE_1: Dict[str, Dict[str, Any]] = {
    # =========================================================================
    # 1. CANTO DE ENTRADA (INTROITUS)
    # =========================================================================
    "entrada": {
        "slug": "entrada",
        "titulo": "Canto de Entrada",
        "nombre_latino": "Introitus / Cantus ad Introitum",
        "parte_nombre": "I. Ritos Iniciales",
        "cita_principal": "IGMR 47–48",
        "subtitulo": "El canto procesional que congrega a la multitud dispersa en un solo Cuerpo eclesial, introduce el espíritu del misterio del día y acompaña el ingreso sacramental del presidente y los ministros hacia el altar.",
        "ficha_identidad": [
            {
                "id": "id-naturaleza",
                "atributo": "Naturaleza Litúrgica",
                "valor": "Canto del Propio (Proprium Missae · Variable)",
                "detalle": "Su texto cambia cada domingo, tiempo litúrgico o solemnidad, reflejando la Antífona de Entrada del Misal Romano o del Graduale Romanum para anunciar el misterio específico del día.",
            },
            {
                "id": "id-funcion",
                "atributo": "Función Ritual",
                "valor": "Procesional (Acompaña una acción litúrgica)",
                "detalle": "Acompaña el desplazamiento real del sacerdote celebrante, diácono y ministros desde la sacristía o el pórtico hasta que el presidente llega a la sede tras venerar e incensar el altar.",
            },
            {
                "id": "id-fines",
                "atributo": "Cuatro Fines Propios (IGMR 47)",
                "valor": "1) Abrir la celebración · 2) Fomentar la unión · 3) Introducir el misterio · 4) Acompañar la procesión",
                "detalle": "No es 'música de espera' ni un mero saludo social, sino un acto sacramental eclesiológico que transforma a fieles individuales en Asamblea santa convocada por Dios.",
            },
            {
                "id": "id-ejecucion",
                "atributo": "Protagonista y Ejecución (IGMR 48)",
                "valor": "Alternado (Coro/Cantor + Pueblo), Todo el Pueblo o solo el Coro",
                "detalle": "La forma clásica y pastoralmente óptima es la responsorial: la asamblea canta el estribillo (antífona) de memoria sin depender de papeles y el coro o salmista proclama las estrofas salmódicas.",
            },
            {
                "id": "id-postura",
                "atributo": "Postura Corporal y Gesto",
                "valor": "De pie (IGMR 43)",
                "detalle": "Los fieles permanecen de pie desde que se inicia el canto de entrada, signo de la dignidad bautismal del pueblo resucitado que sale al encuentro de su Señor.",
            },
            {
                "id": "id-duracion",
                "atributo": "Inicio y Término Exacto",
                "valor": "Inicia al salir la procesión · Concluye cuando el presidente llega a la sede",
                "detalle": "Si hay incensación de la cruz y del altar (IGMR 49), el canto acompaña toda la incensación y cierra con la antífona final cuando el sacerdote se ubica en la sede para hacer la Señal de la Cruz.",
            },
        ],
        "opciones_igmr": [
            {
                "numero": "Opción 1 (Graduale Romanum)",
                "titulo": "Antífona y Salmo del Graduale Romanum",
                "descripcion": "La antífona propia del día con los versículos de su salmo según el Graduale Romanum, ya sea en canto gregoriano original o en melodías equivalentes.",
            },
            {
                "numero": "Opción 2 (Graduale Simplex)",
                "titulo": "Antífona y Salmo del Graduale Simplex",
                "descripcion": "La antífona y el salmo del Graduale Simplex (promulgado en 1967 para parroquias), que ofrece antífonas breves y accesibles por cada Tiempo Litúrgico.",
            },
            {
                "numero": "Opción 3 (Salmodia del Misal)",
                "titulo": "Antífona del Misal Romano musicalizada con su Salmo",
                "descripcion": "Poner música en lengua vernácula a la Antífona de Entrada que trae el Misal Romano para ese domingo o fiesta, alternándola con versículos del salmo respectivo.",
            },
            {
                "numero": "Opción 4 (Alius cantus aptus)",
                "titulo": "Otro canto congruente aprobado por la Conferencia Episcopal",
                "descripcion": "Otro canto que sea verdaderamente congruente con la acción sagrada, con la índole del día o del tiempo litúrgico, y cuyo texto haya sido aprobado por la Conferencia Episcopal (CECh).",
            },
        ],
        "textos_oficiales": {
            "titulo": "Estructura Clásica del Introito y Ejemplos del Misal Romano",
            "nota": "En el Rito Romano, el Introito consta de Antífona + Versículo(s) de Salmo + Doxología (Gloria Patri) + Repetición de la Antífona. Si no se canta en absoluto a la entrada, la Antífona del Misal debe ser recitada por los fieles, un lector o el sacerdote (IGMR 48).",
            "items": [
                {
                    "ocasion": "Estructura Tradicional (Ordo Romanus I)",
                    "latin": "Antiphona · Psalmus (vv. 1, 2...) · Gloria Patri et Filio et Spiritui Sancto, sicut erat in principio, et nunc, et semper, et in saecula saeculorum. Amen · Antiphona.",
                    "espanol": "Antífona (Asamblea) · Versículos del Salmo (Cantor/Coro) · Gloria al Padre y al Hijo y al Espíritu Santo, como era en el principio, ahora y siempre, por los siglos de los siglos. Amén · Antífona (Asamblea).",
                },
                {
                    "ocasion": "I Domingo de Adviento (Sal 24, 1-3)",
                    "latin": "Ad te levavi animam meam: Deus meus, in te confido, non erubescam: neque irrideant me inimici mei: etenim universi qui te exspectant, non confundentur.",
                    "espanol": "«A ti, Señor, levanto mi alma; Dios mío, en ti confío, no quede yo defraudado, que no triunfen de mí mis enemigos; pues los que esperan en ti no quedan defraudados.»",
                },
                {
                    "ocasion": "Domingo de Resurrección (Sal 138, 18. 5-6)",
                    "latin": "Resurrexi, et adhuc tecum sum, alleluia: posuisti super me manum tuam, alleluia: mirabilis facta est scientia tua, alleluia, alleluia.",
                    "espanol": "«He resucitado y aún estoy contigo, aleluya; has puesto tu mano sobre mí, aleluya; tu sabiduría ha sido maravillosa, aleluya, aleluya.»",
                },
                {
                    "ocasion": "Misa Vespertina de la Cena del Señor · Jueves Santo (Gál 6, 14)",
                    "latin": "Nos autem gloriari oportet in cruce Domini nostri Iesu Christi, in quo est salus, vita et resurrectio nostra, per quem salvati et liberati sumus.",
                    "espanol": "«Nosotros hemos de gloriarnos en la cruz de nuestro Señor Jesucristo: en él está nuestra salvación, vida y resurrección; él nos ha salvado y libertado.»",
                },
            ],
        },
        "semaforo": {
            "verde": [
                {
                    "titulo": "Cumplir las cuatro finalidades rituales (IGMR 47)",
                    "texto": "Abrir la celebración, fomentar la unión espiritual y vocal de los reunidos, introducir el espíritu en el misterio del tiempo o fiesta, y acompañar el paso real de la procesión.",
                },
                {
                    "titulo": "Inspiración bíblica y salmódica (SC 121)",
                    "texto": "Priorizar textos nacidos de los Salmos (Sal 94, 99, 121, 26, 65, 83, 149) o de las Antífonas del Misal Romano. Si no hay canto en una Misa ferial, recitar siempre la Antífona del Misal (IGMR 48).",
                },
                {
                    "titulo": "Duración subordinada a la procesión",
                    "texto": "El canto está al servicio del rito: concluye en la estrofa o antífona en curso cuando el sacerdote llega a la sede tras venerar (o incensar) el altar.",
                },
            ],
            "amarillo": [
                {
                    "titulo": "Miércoles de Ceniza y Tiempo de Cuaresma",
                    "texto": "Los instrumentos musicales se emplean exclusivamente para sostener la afinación del canto (IGMR 313). No se tocan preludios ni interludios instrumentales festivos; se omite todo 'Aleluya'.",
                },
                {
                    "titulo": "Viernes Santo (Celebración de la Pasión del Señor)",
                    "texto": "PROHIBICIÓN ABSOLUTA: El Viernes Santo no hay canto de entrada ni saludo inicial. El sacerdote y los ministros avanzan en silencio total y se postran rostro en tierra.",
                },
                {
                    "titulo": "Vigilia Pascual en la Noche Santa",
                    "texto": "No hay canto de entrada ordinario: la celebración comienza en el exterior con el Lucernario y la triple aclamación procesional «Luz de Cristo — Demos gracias a Dios» seguida del Pregón Pascual (Exsultet).",
                },
            ],
            "rojo": [
                {
                    "titulo": "El síndrome del 'canto de bienvenida social'",
                    "texto": "Sustituir la alabanza a Dios y la convocación de la Iglesia por canciones autorreferenciales ('qué alegría que viniste', 'démonos un abrazo') donde no se menciona a Dios ni el misterio pascual.",
                },
                {
                    "titulo": "Repertorio inmóvil durante todo el año",
                    "texto": "Cantar los mismos dos o tres cantos genéricos en Adviento, Navidad, Cuaresma, Pascua y Tiempo Ordinario, borrando la pedagogía del Año Litúrgico.",
                },
                {
                    "titulo": "Dejar al sacerdote esperando de pie en la sede",
                    "texto": "Seguir cantando tres estrofas más después de que el celebrante ya llegó a la sede, rompiendo el ritmo de los Ritos Iniciales.",
                },
                {
                    "titulo": "Melodías de solista inaccesibles para el pueblo",
                    "texto": "Elegir canciones con síncopas impredecibles o registros sobre Mi5 donde la asamblea queda reducida a espectadora muda.",
                },
            ],
        },
        "adaptacion_tiempos": {
            "Tiempo Ordinario": {
                "espiritu": "El Domingo como Pascua semanal: la Iglesia peregrina se congrega llamada por Cristo Resucitado.",
                "textos_sugeridos": "Salmos de convocación y alabanza: Sal 94 ('Vengan, aclamemos al Señor'), Sal 99 ('Aclamen al Señor, tierra entera'), Sal 121 ('Qué alegría cuando me dijeron'), Sal 26 ('El Señor es mi luz y mi salvación').",
                "criterio_musical": "Carácter caminante, luminoso y comunitario. Tempo moderato firme (♩ = 88–104), que invite a ponerse de pie y cantar a plena voz.",
            },
            "Adviento": {
                "espiritu": "Vigilancia esperanzada de las dos venidas del Señor (Parusía y Encarnación): '¡Maranatha, ven Señor Jesús!'.",
                "textos_sugeridos": "Isaías 45, 8 ('Cielos, destilen el rocío / Rorate caeli'), Salmo 24 ('A ti, Señor, levanto mi alma'), Salmo 79, Salmo 84 ('Muéstranos, Señor, tu misericordia'), Filipenses 4, 4-5 (Domingo Gaudete).",
                "criterio_musical": "Sobriedad contenida (IGMR 305, 313). Excelente ocasión para modos menores o dóricos, sin adelantar los villancicos de Navidad.",
            },
            "Navidad": {
                "espiritu": "Asombro y gozo por la Encarnación del Verbo: 'Un niño nos ha nacido, un hijo se nos ha dado' (Is 9, 5).",
                "textos_sugeridos": "Salmo 97 ('Canten al Señor un cántico nuevo'), Sabiduría 18, 14-15 ('Cuando un profundo silencio envolvía todas las cosas'), Isaías 60 ('Levántate y brilla, Jerusalén', Epifanía).",
                "criterio_musical": "Sonoridad amplia y radiante. En la Entrada conviene un himno teológico de la Encarnación antes que un villancico meramente costumbrista (que calza mejor al final de la Misa).",
            },
            "Cuaresma": {
                "espiritu": "Conversión del corazón, combate espiritual en el desierto con Cristo y confianza en la misericordia del Padre.",
                "textos_sugeridos": "Salmo 90 ('Me invocará y yo lo escucharé', I Domingo), Sabiduría 11, 24 ('Tú tienes compasión de todos, Señor', Ceniza), Salmo 24, Salmo 50, Joel 2.",
                "criterio_musical": "Instrumentos estrictamente limitados a sostener el canto (IGMR 313). Sin preludios ni percusión. Idealmente polifonía vocal sobria o canto congregacional austero.",
            },
            "Semana Santa": {
                "espiritu": "Ingreso mesiánico en Jerusalén (Ramos), entrega suprema en la Cena y la Cruz (Jueves Santo) y silencio pascual (Viernes Santo).",
                "textos_sugeridos": "Domingo de Ramos: 'Hosanna al Hijo de David' (Mt 21, 9) y Salmo 23 ('Portones, alzad los dinteles'). Jueves Santo: Gálatas 6, 14. Viernes Santo: Silencio absoluto.",
                "criterio_musical": "Porte majestuoso y profundamente teológico; en Jueves Santo el canto introduce todo el Triduo Sacro.",
            },
            "Pascua": {
                "espiritu": "Exultación de los cincuenta días del Gran Domingo Pascual: 'He resucitado y aún estoy contigo, aleluya'.",
                "textos_sugeridos": "Salmo 138, Salmo 65 ('Aclamen a Dios, tierra entera... aleluya'), 1 Pedro 2, 2 ('Quasi modo geniti infantes'), Sabiduría 10, 20. En Pentecostés: Sabiduría 1, 7 ('El Espíritu del Señor llena la tierra').",
                "criterio_musical": "Plenitud armónica, registro brillante de órgano/cuerdas/voces y presencia del 'Aleluya' en el estribillo.",
            },
        },
        "tratado_teologico": [
            {
                "id": "eclesiologia",
                "titulo": "1. Teología y Mistagogía: De la multitud dispersa a la Ekklesía",
                "parrafos": [
                    "En la teología litúrgica, la asamblea cristiana no es una suma casual de individuos piadosos que coinciden en un recinto, sino la epifanía visible de la Iglesia (Ekklesía: la comunidad convocada por la voz de Dios). El Canto de Entrada realiza sacramentalmente este paso: al respirar al unísono, entonar un mismo intervalo y pronunciar una misma Palabra inspirada, los fieles pasan del aislamiento de sus preocupaciones cotidianas a la comunión de un solo Cuerpo en Cristo. San Juan Crisóstomo explicaba en su Comentario al Salmo 145 que «así como las cuerdas de la cítara, siendo distintas, producen una sola sinfonía, así el canto común de los salmos ata las almas en el vínculo de la caridad».",
                    "Simultáneamente, la procesión del sacerdote celebrante (que actúa in persona Christi Capitis) y de los ministros a través de la nave hacia el altar actualiza el peregrinaje escatológico del Pueblo de Dios en la historia rumbo a la Jerusalén del cielo. El altar representa a Cristo mismo, Piedra angular y Mesa del sacrificio. Por eso San Agustín exhortaba en su célebre Sermón 256: «Cantare amantis est (Cantar es propio de quien ama)... Canta como suelen cantar los caminantes; canta para aliviar el trabajo del camino, pero camina: avanza en el bien, avanza en la fe recta».",
                    "La Instrucción General del Misal Romano (n. 47) condensa esta riqueza patrística en cuatro verbos operativos que sirven de examen para cualquier canto de entrada: 1) Abrir la celebración (marcar el umbral sagrado), 2) Fomentar la unión de los reunidos (edificar la comunión fraterna), 3) Introducir su espíritu en el misterio del tiempo litúrgico o de la festividad (mistagogía del hoy de la salvación), y 4) Acompañar la procesión de los ministros (verdad del signo en el espacio y el tiempo).",
                ],
            },
            {
                "id": "historia-introito",
                "titulo": "2. Historia Litúrgica: Del Introito antífono-salmódico romano al 'Alius cantus aptus'",
                "parrafos": [
                    "Hasta finales del siglo IV, la liturgia romana comenzaba sin ritos iniciales: apenas el obispo entraba y saludaba al pueblo ('Dominus vobiscum'), se proclamaban inmediatamente las lecturas proféticas, tal como aún hoy se conserva de manera arcaica en la liturgia del Viernes Santo. Fue en el siglo V (atribuido por el Liber Pontificalis al Papa Celestino I, 422–432, y codificado por San Gregorio Magno) cuando el crecimiento de las grandes basílicas romanas exigió acompañar la larga procesión desde el secretarium (situado junto a la puerta de entrada de la basílica) hasta el presbiterio con el canto de un salmo completo en forma antifonal.",
                    "El Ordo Romanus I (siglo VII) describe con precisión cinematográfica cómo funcionaba este rito: cuando el Papa daba la señal en la sacristía, el subdiácono avisaba al prior scholae y los cantores entonaban la Antífona del Introito seguida de los versículos del salmo. El canto avanzaba mientras el cortejo cruzaba la nave; apenas el Pontífice llegaba al altar, hacía una seña al director del coro, quien interrumpía los versículos restantes del salmo, entonaba el Gloria Patri (Doxología menor) mientras el Papa se inclinaba a besar el Evangelio y el altar, y repetía por última vez la Antífona. Esta arquitectura modular evitaba tanto que la procesión caminara en frío silencio como que el sacerdote quedara esperando inmóvil al final de una canción interminable.",
                    "Durante la Edad Media, al acortarse la procesión (pues las sacristías pasaron a construirse junto al presbiterio), el salmo del Introito se redujo a un solo versículo más el Gloria Patri. En el siglo XX, el Concilio Vaticano II y la IGMR (n. 48) restauraron la posibilidad del salmo más amplio y abrieron cuatro opciones legítimas: el Graduale Romanum, el Graduale Simplex, otro canto con texto del Misal, o 'otro canto congruente aprobado por la Conferencia Episcopal' (alius cantus aptus). El desafío pastoral contemporáneo en Chile y Latinoamérica consiste en no divorciar esa cuarta opción de la teología de la Antífona de Entrada del Misal Romano.",
                ],
            },
        ],
        "citas_magisteriales": [
            {
                "id_cita": "igmr-47",
                "doc_id": "igmr",
                "fuente": "Instrucción General del Misal Romano (IGMR)",
                "numeral": "n. 47",
                "año": "2002 / Tercera Edición Típica",
                "url_oficial": "https://www.vatican.va/roman_curia/congregations/ccdds/documents/rc_con_ccdds_doc_20030317_ordinamento-messale_sp.html#B._Ritos_iniciales",
                "texto": "«Una vez que el pueblo se ha reunido, cuando avanza el sacerdote con el diácono y los ministros, se da comienzo al canto de entrada. La finalidad de este canto es abrir la celebración, fomentar la unión de quienes se han reunido y elevar sus pensamientos a la contemplación del misterio litúrgico o de la fiesta, acompañando la procesión del sacerdote y los ministros.»",
                "comentario_pastoral": "Define los 4 criterios de discernimiento: si un canto no cumple estas cuatro funciones simultáneamente, no es apto como Canto de Entrada.",
            },
            {
                "id_cita": "igmr-48",
                "doc_id": "igmr",
                "fuente": "Instrucción General del Misal Romano (IGMR)",
                "numeral": "n. 48",
                "año": "2002 / Adaptación CECh",
                "url_oficial": "https://www.vatican.va/roman_curia/congregations/ccdds/documents/rc_con_ccdds_doc_20030317_ordinamento-messale_sp.html#B._Ritos_iniciales",
                "texto": "«Este canto lo ejecuta alternando el coro y el pueblo, o de manera análoga el cantor y el pueblo, o bien todo el pueblo, o solamente el coro. Se puede utilizar, o bien la antífona con su salmo como se encuentra en el Graduale Romanum o en el Graduale Simplex, o bien otro canto que sea congruente con la acción sagrada, con el día o el tiempo del año, cuyo texto haya sido aprobado por la Conferencia Episcopal. Si no hay canto a la entrada, la antífona propuesta en el Misal es recitada, o por los fieles, o por algunos de ellos, o por un lector, o en último caso, por el mismo sacerdote, quien también puede adaptarla a modo de monición inicial.»",
                "comentario_pastoral": "Establece los modos de ejecución, la jerarquía de las 4 opciones de repertorio y la obligación de leer la Antífona del Misal si no se canta.",
            },
            {
                "id_cita": "ms-31-32",
                "doc_id": "musicam-sacram",
                "fuente": "Instrucción Musicam Sacram (Sagrada Congregación de Ritos)",
                "numeral": "nn. 31–32",
                "año": "5 de marzo de 1967",
                "url_oficial": "https://www.vatican.va/archive/hist_councils/ii_vatican_council/documents/vat-ii_instr_19670305_musicam-sacram_lt.html",
                "texto": "«La costumbre legítimamente vigente en algunos lugares, y a veces confirmada por indultos particulares, de sustituir con otros cantos los cantos de entrada, ofertorio y comunión que se hallan en el Graduale, puede conservarse a juicio de la autoridad territorial competente, con tal de que estos cantos estén de acuerdo con las partes de la Misa, con la fiesta o con el tiempo litúrgico. Esta misma autoridad territorial debe aprobar los textos de estos cantos.»",
                "comentario_pastoral": "Recuerda que el Canto de Entrada pertenece al Tercer Grado de participación (n. 31) y que su texto exige estricta congruencia con el misterio del día.",
            },
            {
                "id_cita": "sc-112-121",
                "doc_id": "sacrosanctum-concilium",
                "fuente": "Constitución Sacrosanctum Concilium (Concilio Vaticano II)",
                "numeral": "n. 112 y n. 121",
                "año": "4 de diciembre de 1963",
                "url_oficial": "https://www.vatican.va/archive/hist_councils/ii_vatican_council/documents/vat-ii_const_19631204_sacrosanctum-concilium_sp.html",
                "texto": "«La música sagrada será tanto más santa cuanto más íntimamente esté unida a la acción litúrgica, ya sea expresando con mayor delicadeza la oración o fomentando la unanimidad, ya sea enriqueciendo de mayor solemnidad los ritos sagrados... Los textos destinados al canto sagrado deben estar de acuerdo con la doctrina católica; más aún, deben tomarse principalmente de la Sagrada Escritura y de las fuentes litúrgicas.»",
                "comentario_pastoral": "Principio teológico fundamental para compositores: la santidad de la obra radica en su unión con la acción ritual y su fuente bíblico-litúrgica.",
            },
        ],
        "criterios_musicales": [
            {
                "id": "crit-forma",
                "categoria": "Forma Musical Recomendada",
                "titulo": "Forma Responsorial (Estribillo + Estrofas) o Himno Estrófico Modular",
                "explicacion": "La forma responsorial (A – B – A – C – A) es la más eficaz pastoralmente para la Entrada y la Comunión: la asamblea aprende rápidamente un estribillo breve y pregnante (4 a 8 compases) y lo canta de memoria sin depender de hojas o pantallas, mientras el solista o el coro a voces (SATB) proclama las estrofas salmódicas. Si se compone un himno estrófico, cada estrofa debe tener cadencia conclusiva autónoma para poder cerrar el canto en cualquier estrofa apenas el sacerdote llegue a la sede.",
            },
            {
                "id": "crit-tesitura",
                "categoria": "Ámbito Melódico y Tesitura Congregacional",
                "titulo": "Registro accesible para voces aún frías (Re4 a Do5 / Re5)",
                "explicacion": "Al comenzar la Misa, la voz de los fieles aún no está temperada. La línea melódica de la asamblea debe moverse entre Do4/Re4 y Do5/Re5 (con centro de gravedad entre Mi4 y La4). Las voces de Soprano, Contralto, Tenor y Bajo del coro enriquecen armónicamente este canto, especialmente en el último estribillo, sin eclipsar la melodía principal del pueblo.",
            },
            {
                "id": "crit-prosodia",
                "categoria": "Prosodia y Acentuación Castellana",
                "titulo": "Coincidencia entre acento tónico verbal y tiempo fuerte musical",
                "explicacion": "Al musicalizar antífonas del Misal o salmos en español, las sílabas tónicas de las palabras teológicas clave (Se-ñor, pue-blo, a-le-grí-a, sal-va-ción) deben recaer sobre los tiempos fuertes o semifuertes del compás. Evitar que artículos o preposiciones átonas ('de', 'el', 'para') queden sobre notas largas o agudas en el primer tiempo.",
            },
            {
                "id": "crit-ritmo",
                "categoria": "Carácter Rítmico e Inculturación Sobria",
                "titulo": "Pulso estable, noble y procesional ('caminante')",
                "explicacion": "A diferencia del canto de meditación post-comunión, la Entrada acompaña una marcha física real por la nave. Requiere un pulso claro y acogedor (en 2/4, 4/4, 3/4 o un 6/8 noble y pausado). Si se emplean giros armónicos o rítmicos de raíz latinoamericana o chilena, deben conservar el porte solemne del rito.",
            },
            {
                "id": "crit-direccion",
                "categoria": "Práctica de Interpretación en Vivo (Gestión del Tiempo)",
                "titulo": "Sincronización visual con el Altar y el Incensario",
                "explicacion": "El director debe mantener contacto visual con la procesión:\n1. Sin incensación: Generalmente bastan Estribillo + Estrofa 1 + Estribillo + Estrofa 2 + Estribillo final (aprox. 1 min 30 s a 2 min).\n2. Con incensación del altar: Mientras el sacerdote rodea e inciensa el altar, se puede añadir una estrofa adicional o un breve interludio instrumental solemne (órgano/cuerdas), cerrando con el último estribillo justo cuando el sacerdote camina a la sede.",
            },
        ],
        "checklist_discernimiento": [
            {
                "id": "chk-ent-1",
                "pregunta": "¿El texto está tomado de los Salmos, de la Antífona del Misal o es un himno litúrgico aprobado de clara doctrina católica?",
                "pista": "Sacrosanctum Concilium 121 / IGMR 48.",
            },
            {
                "id": "chk-ent-2",
                "pregunta": "¿Introduce específicamente el Tiempo Litúrgico actual (Adviento, Navidad, Cuaresma, Pascua, T. Ordinario) o la Fiesta del día?",
                "pista": "Tercer fin del canto de entrada según IGMR 47.",
            },
            {
                "id": "chk-ent-3",
                "pregunta": "¿Expresa el sentido de Iglesia congregada que alaba a Dios (y no solo un saludo horizontal o intimista individual)?",
                "pista": "El canto de entrada une las voces de los reunidos como Cuerpo de Cristo.",
            },
            {
                "id": "chk-ent-4",
                "pregunta": "¿La estructura musical permite que la asamblea participe fácilmente (estribillo cantable en tesitura Re4–Do5)?",
                "pista": "Participación activa de todo el pueblo (IGMR 48).",
            },
            {
                "id": "chk-ent-5",
                "pregunta": "¿Se puede concluir de manera limpia al final de cualquier estrofa o estribillo apenas el sacerdote llegue a la sede?",
                "pista": "El canto acompaña la procesión; no debe dejar al presidente esperando en la sede.",
            },
        ],
    },

    # =========================================================================
    # 2. ASPERSIÓN DEL AGUA BENDITA (ASPERGES ME / VIDI AQUAM)
    # =========================================================================
    "aspersion": {
        "slug": "aspersion",
        "titulo": "Aspersión del Agua Bendita",
        "nombre_latino": "Asperges me / Vidi aquam",
        "parte_nombre": "I. Ritos Iniciales",
        "cita_principal": "IGMR 51 · Apéndice II del Misal Romano",
        "subtitulo": "El rito dominical de bendición y aspersión del agua en memoria viva del Bautismo, por el cual la asamblea purificada celebra su inserción en la Pascua de Cristo.",
        "ficha_identidad": [
            {
                "id": "asp-naturaleza",
                "atributo": "Naturaleza Litúrgica",
                "valor": "Canto del Propio Dominical (Sustituye al Acto Penitencial)",
                "detalle": "Cuando se realiza la aspersión dominical (IGMR 51), sustituye íntegramente al Acto Penitencial acostumbrado y al Kyrie eleison, pasando directamente al Gloria (si corresponde).",
            },
            {
                "id": "asp-funcion",
                "atributo": "Función Ritual",
                "valor": "Procesional / Acompaña una acción sacramental",
                "detalle": "Acompaña el recorrido del sacerdote por la nave asperjando con el hisopo a los fieles en memoria del Bautismo recibido.",
            },
            {
                "id": "asp-tiempos",
                "atributo": "Días en que se recomienda",
                "valor": "Todos los Domingos, especialmente en la cincuentena del Tiempo Pascual",
                "detalle": "El domingo es el día primordial en que la Iglesia conmemora la Resurrección y el Bautismo. En las Misas dominicales del Tiempo Pascual es sumamente recomendado.",
            },
            {
                "id": "asp-ejecucion",
                "atributo": "Protagonista y Ejecución",
                "valor": "Asamblea (Antífona) + Coro/Cantor (Versículo del Salmo 50 o 117)",
                "detalle": "Se inicia inmediatamente después de que el sacerdote concluye la oración de bendición del agua y se prolonga hasta que regresa al presbiterio.",
            },
            {
                "id": "asp-postura",
                "atributo": "Postura y Gesto de los Fieles",
                "valor": "De pie, persignándose al recibir el agua bendita",
                "detalle": "Al paso del sacerdote, los fieles cantan y trazan sobre sí mismos la Señal de la Cruz agradeciendo la gracia de su Bautismo.",
            },
            {
                "id": "asp-conclusion",
                "atributo": "Conclusión del Rito",
                "valor": "Oración conclusiva del Sacerdote desde la sede + «Amén»",
                "detalle": "Terminado el canto, el sacerdote de pie en la sede dice: «Que Dios todopoderoso nos purifique de nuestros pecados y, por la celebración de esta Eucaristía, nos haga dignos de participar del banquete de su reino. R/. Amén», e inicia enseguida el Gloria.",
            },
        ],
        "opciones_igmr": [
            {
                "numero": "Opción 1 (Fuera del T. Pascual)",
                "titulo": "Antífona «Asperges me» con Salmo 50 (51)",
                "descripcion": "Basada en el Salmo 50, 9: «Rocíame, Señor, con el hisopo y quedaré limpio; lávame y quedaré más blanco que la nieve», seguida del versículo «Misericordia, Dios mío, por tu bondad».",
            },
            {
                "numero": "Opción 2 (Tiempo Pascual)",
                "titulo": "Antífona «Vidi aquam» con Salmo 117 (118)",
                "descripcion": "Inspirada en la visión profética de Ezequiel 47, 1-2.9: «Vi brotar agua del lado derecho del templo, aleluya; y todos aquellos a quienes llegó esta agua fueron salvados y dirán: ¡Aleluya, aleluya!».",
            },
            {
                "numero": "Opción 3 (Fórmulas vernáculas del Misal)",
                "titulo": "Antífonas Bautismales del Apéndice II del Misal Romano",
                "descripcion": "Textos bíblicos propuestos por el Misal Romano en español (Ez 36, 25-26: «Derramaré sobre ustedes un agua pura...»; 1 Pe 1, 3-5; Zac 13, 1).",
            },
            {
                "numero": "Opción 4 (Canto bautismal aprobado)",
                "titulo": "Otro canto de carácter expresamente bautismal",
                "descripcion": "Un canto aprobado que exprese la purificación por el agua del Bautismo, la vida nueva en Cristo o la fuente de agua viva (no un canto genérico de entrada).",
            },
        ],
        "textos_oficiales": {
            "titulo": "Antífonas Oficiales del Rito de Aspersión (Apéndice II del Misal Romano)",
            "nota": "Estas dos antífonas constituyen el tesoro bimilenario de la Iglesia para la aspersión dominical y deben inspirar toda nueva composición para este momento.",
            "items": [
                {
                    "ocasion": "Fuera del Tiempo Pascual · Asperges me (Sal 50, 9. 3)",
                    "latin": "Asperges me, Domine, hyssopo, et mundabor: lavabis me, et super nivem dealbabor. Ps. Miserere mei, Deus, secundum magnam misericordiam tuam.",
                    "espanol": "«Rocíame, Señor, con el hisopo y quedaré limpio; lávame y quedaré más blanco que la nieve. Salmo: Misericordia, Dios mío, por tu gran bondad.»",
                },
                {
                    "ocasion": "Fuera del Tiempo Pascual · Ezequiel 36, 25-26",
                    "latin": "Effundam super vos aquam mundam, et mundabimini ab omnibus inquinamentis vestris, et dabo vobis cor novum, dicit Dominus.",
                    "espanol": "«Derramaré sobre ustedes un agua pura y quedarán purificados de todas sus manchas, y les daré un corazón nuevo, dice el Señor.»",
                },
                {
                    "ocasion": "Tiempo Pascual · Vidi aquam (Cf. Ez 47, 1-2. 9; Sal 117, 1)",
                    "latin": "Vidi aquam egredientem de templo, a latere dextro, alleluia: et omnes, ad quos pervenit aqua ista, salvi facti sunt, et dicent: alleluia, alleluia. Ps. Confitemini Domino quoniam bonus: quoniam in saeculum misericordia eius.",
                    "espanol": "«Vi brotar agua del lado derecho del templo, aleluya; y todos aquellos a quienes llegó esta agua fueron salvados, y dirán: ¡Aleluya, aleluya! Salmo: Den gracias al Señor porque es bueno, porque es eterna su misericordia.»",
                },
                {
                    "ocasion": "Vigilia Pascual y Tiempo Pascual (Cf. Zac 13, 1)",
                    "latin": "Fons aquae salientis in vitam aeternam, alleluia.",
                    "espanol": "«En aquel día manará una fuente para lavar el pecado y la impureza, aleluya. / He aquí el agua viva que brota para la vida eterna, aleluya.»",
                },
            ],
        },
        "semaforo": {
            "verde": [
                {
                    "titulo": "Claridad temática bautismal y pascual",
                    "texto": "El texto del canto debe hablar explícitamente del agua viva, del Bautismo, del costado abierto de Cristo o de la purificación del corazón (Sal 50 / Ez 47 / Ez 36).",
                },
                {
                    "titulo": "Omitir el Kyrie eleison tras la aspersión",
                    "texto": "El rito de aspersión ya cumple la función penitencial y bautismal completa; por rúbrica expresa del Misal Romano, después de la oración conclusiva del sacerdote se pasa directamente al Gloria (o a la Colecta en Adviento y Cuaresma).",
                },
                {
                    "titulo": "Destacar el «Vidi aquam» durante los 8 domingos de Pascua",
                    "texto": "Tener un canto fijo y luminoso para la aspersión durante los cincuenta días pascuales da una identidad sonora inolvidable a toda la Pascua parroquial.",
                },
            ],
            "amarillo": [
                {
                    "titulo": "Aspersión en Domingos de Adviento y Cuaresma",
                    "texto": "Aunque se asocia sobre todo a Pascua, la IGMR 51 permite hacerla en cualquier domingo (incluso en Cuaresma, evocando el camino catecumenal hacia la fuente bautismal), usando la antífona «Asperges me» o Ezequiel 36 sin Aleluya.",
                },
                {
                    "titulo": "Renovación de las Promesas Bautismales en la Vigilia Pascual",
                    "texto": "En la Noche Santa de Pascua y el Domingo de Pascua, la aspersión sigue a la solemne Renovación de las Promesas Bautismales con las velas encendidas.",
                },
            ],
            "rojo": [
                {
                    "titulo": "Cantar un canto de perdón que no menciona el agua ni el Bautismo",
                    "texto": "Usar un Señor ten piedad común o una canción genérica durante la aspersión vacía de contenido el signo visible del agua bendita.",
                },
                {
                    "titulo": "Volver a cantar el Señor ten piedad después de la aspersión",
                    "texto": "Duplicar el acto penitencial cantando el Kyrie tras la aspersión es un error ritual contrario a la IGMR 51.",
                },
            ],
        },
        "adaptacion_tiempos": {
            "Tiempo Pascual": {
                "espiritu": "Gozo bautismal por el agua y la sangre que brotaron del costado abierto de Cristo en la Cruz (Jn 19, 34; Ez 47).",
                "textos_sugeridos": "«Vidi aquam» ('Vi brotar agua del lado derecho del templo, aleluya'), «Fuentes del Señor, bendigan al Señor», Salmo 117.",
                "criterio_musical": "Tonalidad mayor radiante, ritmo fluido como corriente de agua viva y estribillo con doble Aleluya.",
            },
            "Tiempo Ordinario": {
                "espiritu": "Memoria dominical de nuestra dignidad de bautizados e hijos de Dios lavados por su gracia.",
                "textos_sugeridos": "«Asperges me» (Salmo 50, 9), Ezequiel 36, 25-26 ('Derramaré sobre ustedes un agua pura y les daré un corazón nuevo').",
                "criterio_musical": "Sereno, confiado y luminoso; alternancia ágil entre el estribillo del pueblo y los versículos del Salmo 50.",
            },
            "Cuaresma": {
                "espiritu": "Nostalgia y preparación catecumenal para la fuente bautismal de la noche de Pascua (especialmente en los Domingos de la Samaritana, el Ciego de nacimiento y Lázaro).",
                "textos_sugeridos": "Salmo 50, 9 ('Rocíame, Señor, con el hisopo'), Ezequiel 36, 25-26 (estrictamente sin Aleluya).",
                "criterio_musical": "Sobriedad modal (modo dórico o menor antiguo), acompañamiento instrumental mínimo solo para sostener las voces.",
            },
        },
        "tratado_teologico": [
            {
                "id": "teologia-agua",
                "titulo": "1. Mistagogía del Agua y del Costado Abierto de Cristo",
                "parrafos": [
                    "¿Por qué la Iglesia prefiere en los domingos —y muy especialmente en Pascua— sustituir el acto penitencial verbal por la aspersión del agua bendita? Porque el domingo es el 'Día del Señor' (Dies Domini), memorial semanal tanto de la Resurrección de Cristo como de nuestro propio Bautismo (cf. Rom 6, 3-4). Al recibir sobre nuestra frente y nuestros vestidos las gotas del agua bendecida, no realizamos un simple rito de purificación exterior, sino una anámnesis física y sensorial de la fuente bautismal que nos engendró a la vida divina.",
                    "La antífona pascual «Vidi aquam» (Ez 47, 1-2. 9) encierra una de las cumbres de la tipología patrística: el profeta Ezequiel contempló un manantial que brotaba por debajo del umbral del Templo de Jerusalén, del lado derecho (oriental), convirtiéndose en un torrente que sanaba las aguas salobres del Mar Muerto y daba vida a todo lo que tocaba. San Juan Evangelista (Jn 19, 34) y los Padres de la Iglesia (San Ambrosio, San Agustín, San Cirilo de Jerusalén) vieron cumplido este oráculo en el Cuerpo de Cristo —el verdadero Templo (Jn 2, 21)— de cuyo costado derecho, abierto por la lanza del soldado, brotó sangre y agua: los sacramentos de la Eucaristía y del Bautismo.",
                ],
            },
            {
                "id": "historia-asperges",
                "titulo": "2. Origen Histórico de la Aspersión Dominical",
                "parrafos": [
                    "La costumbre de bendecir el agua con sal y asperjar a los fieles cada domingo antes de la Misa mayor nació en el siglo IX en la Galia carolingia (documentada en los capitulares de Hincmaro de Reims y en el Pontifical Romano-Germánico de Maguncia del siglo X), inspirada en la visita procesional que en Roma se hacía al baptisterio de Letrán durante la Pascua.",
                    "Mientras en el Misal de San Pío V (1570) el Asperges me / Vidi aquam se realizaba inmediatamente antes de comenzar la Misa (con el sacerdote revestido de capa pluvial, antes de colocarse la casulla), la reforma litúrgica del Concilio Vaticano II (IGMR 51) lo integró orgánicamente dentro de los Ritos Iniciales de la Misa, inmediatamente después del saludo presidencial, otorgándole valor penitencial pleno para evitar toda duplicación con el Confiteor o el Kyrie.",
                ],
            },
        ],
        "citas_magisteriales": [
            {
                "id_cita": "igmr-51",
                "doc_id": "igmr",
                "fuente": "Instrucción General del Misal Romano (IGMR)",
                "numeral": "n. 51",
                "año": "2002 / Tercera Edición Típica",
                "url_oficial": "https://www.vatican.va/roman_curia/congregations/ccdds/documents/rc_con_ccdds_doc_20030317_ordinamento-messale_sp.html#B._Ritos_iniciales",
                "texto": "«Los domingos, especialmente en el Tiempo Pascual, en lugar del acto penitencial acostumbrado, puede hacerse alguna vez la bendición y aspersión del agua en memoria del bautismo.»",
                "comentario_pastoral": "Establece que la aspersión reemplaza al acto penitencial completo (incluido el Señor ten piedad).",
            },
            {
                "id_cita": "misal-apendice-ii",
                "doc_id": "igmr",
                "fuente": "Misal Romano · Apéndice II (Rito para la bendición y aspersión del agua)",
                "numeral": "nn. 1–6",
                "año": "Edición Típica",
                "url_oficial": "https://www.vatican.va/roman_curia/congregations/ccdds/documents/rc_con_ccdds_doc_20030317_ordinamento-messale_sp.html",
                "texto": "«El sacerdote toma el hisopo, se rocía a sí mismo y luego rocía a los ministros, al clero y al pueblo, recorriendo, si parece oportuno, la nave de la iglesia. Mientras tanto, se ejecuta un canto apropiado... Terminado el canto, el sacerdote, de pie en la sede y de cara al pueblo, con las manos juntas, dice la oración conclusiva y, a continuación, si se debe decir, se canta o se recita el himno Gloria a Dios en el cielo.»",
                "comentario_pastoral": "Detalla el orden exacto: bendición del agua → aspersión con canto → oración conclusiva en la sede → Gloria.",
            },
        ],
        "criterios_musicales": [
            {
                "id": "asp-crit-1",
                "categoria": "Estructura Formal",
                "titulo": "Antífona breve y luminosa + Versículos de Salmo (50 o 117)",
                "explicacion": "El recorrido del sacerdote asperjando la nave puede durar desde 45 segundos (capilla pequeña) hasta 3 minutos (templo parroquial lleno en Vigilia Pascual). Por eso la obra debe tener una antífona muy fácil de memorizar (ej. 'Vi brotar agua del templo, aleluya') y estrofas salmódicas flexibles que puedan sumarse o restarse según el paso del celebrante.",
            },
            {
                "id": "asp-crit-2",
                "categoria": "Pintura Musical (Madrigalismo Litúrgico)",
                "titulo": "Movimiento melódico fluido como manantial de agua viva",
                "explicacion": "En la tradición del Vidi aquam gregoriano y polifónico (como el de Tomás Luis de Victoria o Cristóbal de Morales), las líneas melódicas y el acompañamiento de arpegios sugieren el fluir cristalino del manantial que brota del templo, evitando ritmos pesados o estáticos.",
            },
        ],
        "checklist_discernimiento": [
            {
                "id": "chk-asp-1",
                "pregunta": "¿El texto del canto alude explícitamente al agua, al Bautismo o a la purificación pascual (Ez 47, Ez 36, Sal 50)?",
                "pista": "Apéndice II del Misal Romano.",
            },
            {
                "id": "chk-asp-2",
                "pregunta": "Si estamos en Tiempo Pascual, ¿incluye la aclamación «Aleluya» en su estribillo?",
                "pista": "Antífona Vidi aquam.",
            },
            {
                "id": "chk-asp-3",
                "pregunta": "¿El coro y el sacerdote están coordinados para NO cantar el «Señor, ten piedad» después de la aspersión, sino pasar directo al Gloria?",
                "pista": "IGMR 51.",
            },
        ],
    },

    # =========================================================================
    # 3. SEÑOR, TEN PIEDAD (KYRIE, ELEISON)
    # =========================================================================
    "senor-ten-piedad": {
        "slug": "senor-ten-piedad",
        "titulo": "Señor, ten piedad (Kyrie)",
        "nombre_latino": "Kyrie, eleison",
        "parte_nombre": "I. Ritos Iniciales",
        "cita_principal": "IGMR 52 · MS 30",
        "subtitulo": "La antiquísima aclamación letánica —heredada en lengua griega de la Iglesia indivisa— con la que la asamblea aclama a Cristo Kyrios e implora su misericordia salvadora.",
        "ficha_identidad": [
            {
                "id": "kyr-naturaleza",
                "atributo": "Naturaleza Litúrgica",
                "valor": "Canto del Ordinario (Ordo Missae · Texto fijo)",
                "detalle": "Es el primer canto del Ordinario de la Misa. Sus palabras pertenecen al texto oficial del Misal Romano y no pueden ser sustituidas por canciones libres sobre el perdón.",
            },
            {
                "id": "kyr-funcion",
                "atributo": "Función Ritual",
                "valor": "Es el rito en sí mismo (Aclamación cristológica implorante)",
                "detalle": "No acompaña ninguna otra acción: el canto mismo es la súplica comunitaria dirigida a Jesucristo Señor (Kyrios).",
            },
            {
                "id": "kyr-ubicacion",
                "atributo": "Ubicación y Relación con el Acto Penitencial (IGMR 52)",
                "valor": "Sigue al Acto Penitencial (Fórmulas I o II) o se integra en la Fórmula III (Tropos)",
                "detalle": "Si en el Acto Penitencial se rezó el «Yo confieso» (Fórmula I) o «Señor, ten misericordia de nosotros» (Fórmula II), a continuación se canta el Kyrie. Si se usó la Fórmula III (con invocaciones o 'tropos'), el Kyrie ya va integrado en ella y no se repite.",
            },
            {
                "id": "kyr-estructura",
                "atributo": "Estructura Litúrgica Oficial",
                "valor": "Ternaria y Binaria (3 × 2 = 6 invocaciones, o históricamente 3 × 3 = 9)",
                "detalle": "De ordinario cada una de las tres aclamaciones («Señor, ten piedad / Cristo, ten piedad / Señor, ten piedad») se dice dos veces (Cantor/Coro → Asamblea), aunque la IGMR 52 permite repetirlas más veces o insertar un breve tropo según la índole de la música.",
            },
            {
                "id": "kyr-protagonista",
                "atributo": "Protagonista y Grado (MS 30)",
                "valor": "Dialogado (Cantor/Coro + Asamblea) · Segundo Grado",
                "detalle": "Por su origen letánico, pide ser dialogado: el cantor o el coro entona cada invocación y toda la asamblea responde.",
            },
            {
                "id": "kyr-idiomas",
                "atributo": "Lenguas Litúrgicas",
                "valor": "Español («Señor, ten piedad») o Griego bíblico («Kýrie, eléison»)",
                "detalle": "Es el único texto en griego koiné que el Rito Romano conservó intacto incluso cuando toda la Misa pasó al latín en el siglo IV.",
            },
        ],
        "opciones_igmr": [
            {
                "numero": "Modo A (Independiente tras Fórmulas I o II)",
                "titulo": "Kyrie cantado después del «Yo confieso»",
                "descripcion": "Los fieles rezan el «Yo confieso» (o la fórmula II), el sacerdote dice la absolución deprecatoria («Dios todopoderoso tenga misericordia de nosotros...») y de inmediato el coro y la asamblea cantan el «Señor, ten piedad».",
            },
            {
                "numero": "Modo B (Integrado en la Fórmula III con Tropos)",
                "titulo": "Invocaciones cristológicas (Tropos) + Respuesta cantada",
                "descripcion": "El sacerdote, diácono o cantor proclama tres invocaciones dirigidas a Cristo («Tú que has sido enviado a sanar los corazones afligidos...») y la asamblea responde cantando «Señor, ten piedad / Cristo, ten piedad / Señor, ten piedad». Luego el sacerdote dice la absolución.",
            },
            {
                "numero": "Excepción (Cuando se omite)",
                "titulo": "Cuando hay Rito de Aspersión o Ritos Especiales al inicio",
                "descripcion": "Se omite el Acto Penitencial y el Kyrie cuando hay Bendición y Aspersión del agua bendita (IGMR 51), o cuando una procesión precede a la Misa (Domingo de Ramos, Candelaria, Ceniza) o en ciertas celebraciones rituales (Bautismo, Matrimonio).",
            },
        ],
        "textos_oficiales": {
            "titulo": "Texto Oficial del Kyrie (Griego / Latín / Español)",
            "nota": "A pesar de tener tres partes (Señor / Cristo / Señor), el Kyrie NO es trinitario sino íntegramente CRISTOLÓGICO: las tres invocaciones se dirigen a Jesucristo como Kyrios (Señor glorificado, cf. Flp 2, 11) y Christós (Mesías Ungido).",
            "items": [
                {
                    "ocasion": "Forma Dialogada (6 invocaciones · IGMR 52)",
                    "latin": "V/. Kýrie, eléison. R/. Kýrie, eléison.\nV/. Christe, eléison. R/. Christe, eléison.\nV/. Kýrie, eléison. R/. Kýrie, eléison.",
                    "espanol": "V/. Señor, ten piedad. R/. Señor, ten piedad.\nV/. Cristo, ten piedad. R/. Cristo, ten piedad.\nV/. Señor, ten piedad. R/. Señor, ten piedad.",
                },
                {
                    "ocasion": "Fórmula III del Acto Penitencial con Tropos (Ejemplo I del Misal)",
                    "latin": "Qui missus es sanare contritos corde: Kýrie, eléison. R/. Kýrie, eléison.\nQui peccatores vocare venisti: Christe, eléison. R/. Christe, eléison.\nQui ad dexteram Patris sedes, ad interpellandum pro nobis: Kýrie, eléison. R/. Kýrie, eléison.",
                    "espanol": "— Tú que has sido enviado a sanar los corazones afligidos: Señor, ten piedad. R/. Señor, ten piedad.\n— Tú que has venido a llamar a los pecadores: Cristo, ten piedad. R/. Cristo, ten piedad.\n— Tú que estás sentado a la derecha del Padre para interceder por nosotros: Señor, ten piedad. R/. Señor, ten piedad.",
                },
            ],
        },
        "semaforo": {
            "verde": [
                {
                    "titulo": "Respeto absoluto a la brevedad y al texto oficial",
                    "texto": "Cantar exactamente «Señor, ten piedad / Cristo, ten piedad / Señor, ten piedad» (o «Kýrie, eléison / Christe, eléison»). Si lleva tropos (Fórmula III), deben dirigirse a Cristo y no inventar estrofas moralizantes.",
                },
                {
                    "titulo": "Tono de aclamación confiada (no de angustia sombría)",
                    "texto": "La IGMR 52 define el Kyrie como «un canto con el que los fieles aclaman al Señor e imploran su misericordia». El verbo griego eleéō remite al hebreo hesed (ternura y misericordia entrañable de Dios).",
                },
                {
                    "titulo": "Protagonismo especial en Adviento y Cuaresma",
                    "texto": "Dado que en Adviento y Cuaresma no se canta el Gloria, el Kyrie pasa a ser el único canto del Ordinario en los Ritos Iniciales: conviene cantarlo siempre y con especial belleza.",
                },
            ],
            "amarillo": [
                {
                    "titulo": "Diferenciar si va con Fórmula I ('Yo confieso') o Fórmula III",
                    "texto": "El director del coro debe preguntar al sacerdote antes de la Misa qué fórmula usará: si reza el «Yo confieso», el coro espera la absolución («Dios todopoderoso tenga misericordia... Amén») y recién ahí entra con el Kyrie. Si usa la Fórmula III, el coro/asamblea responde dentro del acto penitencial antes de la absolución.",
                },
            ],
            "rojo": [
                {
                    "titulo": "Los falsos 'Kyries trinitarios' ('Padre, ten piedad / Hijo, ten piedad / Espíritu Santo...')",
                    "texto": "Es un error teológico y litúrgico muy difundido cambiar la letra a 'Dios Padre ten piedad, Dios Hijo ten piedad, Espíritu Santo ten piedad', o inventar canciones de 3 minutos tipo 'Hoy te pido perdón, Señor, porque he fallado'. El Kyrie se dirige a Cristo Mediador.",
                },
                {
                    "titulo": "Convertir el Señor ten piedad en una balada solista interminable",
                    "texto": "Los Ritos Iniciales son un pórtico breve hacia la Palabra. Un Kyrie de más de 1 minuto y medio con preludios e interludios desproporciona la arquitectura del rito.",
                },
            ],
        },
        "adaptacion_tiempos": {
            "Tiempo Ordinario": {
                "espiritu": "Aclamación serena y filial al Señor Resucitado presente en medio de su asamblea.",
                "textos_sugeridos": "Forma dialogada simple en español o griego (Misa de Angelis VIII, Misa XI Orbis Factor o composiciones vernáculas breves).",
                "criterio_musical": "Fluido, dialogado sin cortes bruscos entre cantor y pueblo.",
            },
            "Adviento": {
                "espiritu": "Clamor mesiánico por la venida del Salvador que sana y libera (ausencia del Gloria).",
                "textos_sugeridos": "Kyrie modal (ej. Misa XVII de Adviento y Cuaresma) o Fórmula III con invocaciones mesiánicas de Adviento.",
                "criterio_musical": "Al no haber Gloria, el Kyrie adquiere mayor relieve lírico y contemplativo.",
            },
            "Cuaresma": {
                "espiritu": "Súplica humilde del hijo pródigo y del publicano que confía en la misericordia del Señor.",
                "textos_sugeridos": "Kýrie, eléison en griego o español a cappella o con sostén mínimo de órgano/cuerdas (Misa XVIII o polifonía sobria).",
                "criterio_musical": "Austeridad profunda, sin adornos instrumentales (IGMR 313).",
            },
            "Navidad y Pascua": {
                "espiritu": "Aclamación gozosa a Cristo vencedor del pecado y de la muerte (cuando no se hace el Rito de Aspersión).",
                "textos_sugeridos": "Kyrie festivo (ej. Misa I Lux et Origo en Pascua) que prepare el estallido inminente del Gloria in excelsis.",
                "criterio_musical": "Luminoso y conciso, pues inmediatamente después resonará el gran himno del Gloria.",
            },
        },
        "tratado_teologico": [
            {
                "id": "kyrie-cristologia",
                "titulo": "1. Teología del «Kýrie, eléison»: Aclamación Imperial y Misericordia Mesiánica",
                "parrafos": [
                    "En el mundo grecorromano antiguo, la exclamación «Kýrie, eléison» ('¡Señor, ten misericordia!') era la aclamación oficial (acclamatio) con la que los habitantes de una ciudad salían a recibir al Emperador o al Rey triunfante cuando entraba por las puertas de la urbe, reconociendo su soberanía y pidiendo su benevolencia. Los primeros cristianos —siguiendo el himno de Filipenses 2, 9-11 («Dios le dio el Nombre sobre todo nombre, para que toda lengua proclame que Jesucristo es el Kýrios»)— transfirieron este título imperial exclusivamente a Cristo resucitado.",
                    "Al mismo tiempo, en los Evangelios sinópticos y en la versión griega de los Setenta (LXX), «Kýrie, eléison» es el grito de fe de los ciegos de Jericó (Mt 20, 30-31), de la mujer cananea (Mt 15, 22) y de los diez leprosos (Lc 17, 13) al paso de Jesús. El sustantivo éleos traduce el hebreo hesed y rahamim: no significa simplemente 'no me castigues' (clemencia judicial), sino 'derrama sobre mí tu ternura, tu aceite curativo, tu amor fiel'. Por eso la IGMR 52 recalca que en el Kyrie «los fieles aclaman al Señor e imploran su misericordia»: es primero una alabanza cristológica y luego una súplica confiada.",
                ],
            },
            {
                "id": "kyrie-historia",
                "titulo": "2. Historia Litúrgica: De la Letanía Oriental de Egeria a la Reforma de San Gregorio Magno",
                "parrafos": [
                    "El testimonio más antiguo del Kyrie litúrgico nos llega de la peregrina hispana Egeria (hacia el año 384) en su Itinerarium Egeriae (cap. 24): ella relata con asombro cómo en la basílica de la Anástasis en Jerusalén, durante el oficio vespertino del Lucernario, un diácono leía las intenciones por cada necesidad y una multitud de niños respondía incesantemente «Kýrie, eléison».",
                    "En el siglo V, el Papa Gelasio I (492–496) introdujo en Roma una letanía deprecativa similar (la Deprecatio Gelasii) al final de los ritos de entrada. Cien años más tarde, San Gregorio Magno (590–604), en su célebre Carta a Juan de Siracusa (Epist. IX, 26), explicó cómo configuró el Kyrie romano: en los días feriales se omitían las largas intenciones del diácono para dejar únicamente la respuesta pura del pueblo y del clero, pero añadiendo la invocación «Christe, eléison» (que no se cantaba en Oriente) para diferenciar el rito romano del bizantino. Así nació la simetría ternaria clásica de Roma: Kýrie eléison — Christe eléison — Kýrie eléison.",
                ],
            },
        ],
        "citas_magisteriales": [
            {
                "id_cita": "igmr-52",
                "doc_id": "igmr",
                "fuente": "Instrucción General del Misal Romano (IGMR)",
                "numeral": "n. 52",
                "año": "2002 / Tercera Edición Típica",
                "url_oficial": "https://www.vatican.va/roman_curia/congregations/ccdds/documents/rc_con_ccdds_doc_20030317_ordinamento-messale_sp.html#B._Ritos_iniciales",
                "texto": "«Después del acto penitencial, se empieza siempre el Señor, ten piedad, a no ser que éste haya formado ya parte del mismo acto penitencial. Dado que es un canto con el que los fieles aclaman al Señor e imploran su misericordia, habitualmente lo ejecutarán todos, es decir, tomarán parte en él el pueblo y el coro o un cantor. Cada aclamación de ordinario se repite dos veces, sin excluir un mayor número, según la índole de las diversas lenguas y también del arte musical o de las circunstancias. Cuando el Señor, ten piedad se canta como parte del acto penitencial, a cada una de las aclamaciones se le antepone un 'tropo'.»",
                "comentario_pastoral": "Norma fundamental: prohíbe sustituir el Kyrie por canciones ajenas y aclara cuándo lleva tropos (Fórmula III) y cuándo va después del 'Yo confieso'.",
            },
        ],
        "criterios_musicales": [
            {
                "id": "kyr-crit-1",
                "categoria": "Forma Musical Letánica",
                "titulo": "Alternancia viva: Propuesta (Cantor/Coro) y Respuesta idéntica (Asamblea)",
                "explicacion": "Para que una asamblea parroquial cante el Kyrie sin titubear, la respuesta del pueblo debe repetir exactamente el motivo melódico que acaba de entonar el cantor o el coro (eco responsorial). Mientras la asamblea repite la línea principal en unísono, el coro puede responder o acompañar a 3 o 4 voces mixtas (SATB).",
            },
            {
                "id": "kyr-crit-2",
                "categoria": "Arco Dramático-Espiritual (A – B – A')",
                "titulo": "Contraste sutil en el «Cristo, ten piedad»",
                "explicacion": "Siguiendo la tradición gregoriana y polifónica, la sección central («Cristo, ten piedad») suele elevar ligeramente el registro melódico o iluminar la armonía (por ejemplo, pasando del modo menor/dórico a su relativo mayor), regresando en el último «Señor, ten piedad» a la tónica con mayor plenitud coral.",
            },
        ],
        "checklist_discernimiento": [
            {
                "id": "chk-kyr-1",
                "pregunta": "¿El texto respeta fielmente «Señor, ten piedad / Cristo, ten piedad / Señor, ten piedad» (o «Kýrie, eléison / Christe, eléison») sin inventar letras alternativas?",
                "pista": "El Kyrie pertenece al Ordinario invariable de la Misa (IGMR 52).",
            },
            {
                "id": "chk-kyr-2",
                "pregunta": "¿Se evita el error de dirigirlo a las tres Personas de la Trinidad ('Padre... Hijo... Espíritu...'), recordando que es una aclamación cristológica?",
                "pista": "Si lleva tropos, las tres invocaciones se dirigen siempre a Jesucristo.",
            },
            {
                "id": "chk-kyr-3",
                "pregunta": "¿La estructura dialogada permite que toda la asamblea responda por imitación inmediata?",
                "pista": "Participación del pueblo y el coro/cantor (IGMR 52).",
            },
        ],
    },

    # =========================================================================
    # 4. GLORIA A DIOS EN EL CIELO (GLORIA IN EXCELSIS DEO)
    # =========================================================================
    "gloria": {
        "slug": "gloria",
        "titulo": "Gloria a Dios en el Cielo",
        "nombre_latino": "Gloria in excelsis Deo (Hymnus angelicus)",
        "parte_nombre": "I. Ritos Iniciales",
        "cita_principal": "IGMR 53 · MS 30",
        "subtitulo": "El antiquísimo y venerable himno doxológico oriental (Doxología Mayor) con que la Iglesia, congregada en el Espíritu Santo, glorifica a Dios Padre y al Cordero y le presenta sus súplicas.",
        "ficha_identidad": [
            {
                "id": "glo-naturaleza",
                "atributo": "Naturaleza Litúrgica",
                "valor": "Himno del Ordinario (Ordo Missae · Texto absolutamente invariable)",
                "detalle": "«El texto de este himno no puede cambiarse por otro» (IGMR 53). Ninguna paráfrasis métrica, canción rimada o 'gloria popular' con letra modificada es válida en la liturgia.",
            },
            {
                "id": "glo-funcion",
                "atributo": "Función Ritual",
                "valor": "Es el rito en sí mismo (Himno de alabanza trinitaria y cristológica)",
                "detalle": "Constituye la cumbre lírica de los Ritos Iniciales en los domingos y días festivos, antes de la Oración Colecta.",
            },
            {
                "id": "glo-cuando",
                "atributo": "Cuándo se Canta (IGMR 53)",
                "valor": "Domingos (fuera de Adviento y Cuaresma), Solemnidades, Fiestas y celebraciones peculiares más solemnes",
                "detalle": "Se omite estrictamente en todos los domingos y ferias de Adviento y de Cuaresma, así como en las memorias y ferias del Tiempo Ordinario.",
            },
            {
                "id": "glo-ejecucion",
                "atributo": "Modos Legítimos de Ejecución (IGMR 53)",
                "valor": "1) Todos juntos · 2) Pueblo alternando con el Coro · 3) Solo el Coro",
                "detalle": "Por ser un himno continuo en prosa rítmica (psalmus idiotikos), la Iglesia recomienda cantarlo completo todos juntos o alternando versículos entre dos coros (asamblea y schola), sin necesidad de agregarle un estribillo repetitivo.",
            },
            {
                "id": "glo-grado",
                "atributo": "Grado de Participación",
                "valor": "Segundo Grado (Musicam Sacram, n. 30)",
                "detalle": "Por ser un himno por naturaleza lírica, siempre debe preferirse cantarlo antes que recitarlo en los domingos y solemnidades.",
            },
            {
                "id": "glo-campanas",
                "atributo": "Signo Especial en el Triduo Pascual",
                "valor": "Toque solemne de campanas y órgano en Jueves Santo y en la Vigilia Pascual",
                "detalle": "Durante el canto del Gloria en la Misa de la Cena del Señor (Jueves Santo) y en la Vigilia Pascual se hacen sonar las campanas del templo; entre ambos momentos las campanas y el órgano enmudecen por completo.",
            },
        ],
        "opciones_igmr": [
            {
                "numero": "Modo 1 (Directo / Continuo)",
                "titulo": "Cantado íntegramente por toda la Asamblea y el Coro",
                "descripcion": "El sacerdote o cantor entona «Gloria a Dios en el cielo» y toda la asamblea junto con el coro canta el texto corrido de principio a fin (forma himnódica original).",
            },
            {
                "numero": "Modo 2 (Alternado / Antifonal)",
                "titulo": "Alternando versículos entre el Pueblo y el Coro (SATB)",
                "descripcion": "Forma sumamente rica y ágil: el pueblo canta un bloque o versículo en melodía sencilla y el coro responde el siguiente versículo en polifonía a 4 voces (o bien hombres y mujeres alternados).",
            },
            {
                "numero": "Modo 3 (Con aclamación intercalada)",
                "titulo": "Estribillo «Gloria a Dios en el cielo...» (Asamblea) + Estrofas literales (Coro)",
                "descripcion": "Aceptado pastoralmente siempre y cuando las estrofas cantadas por el coro o solista contengan el texto íntegro y literal del Misal Romano sin alterar ni omitir ninguna frase doctrinal.",
            },
            {
                "numero": "Modo 4 (Coral en ocasiones solemnes)",
                "titulo": "Ejecutado por el Coro polifónico (IGMR 53)",
                "descripcion": "La IGMR 53 contempla explícitamente la opción de que en grandes solemnidades sea cantado por el coro solo (repertorio polifónico sacro), siempre que la asamblea participe activamente en el Santo, las respuestas y los demás cantos.",
            },
        ],
        "textos_oficiales": {
            "titulo": "Texto Oficial Íntegro del Gloria in excelsis (Estructura Tripartita)",
            "nota": "El himno se articula en tres grandes secciones teológicas: I) El canto de los Ángeles en Belén (Lc 2, 14) y las 5 aclamaciones al Padre; II) La gran letanía cristológica al Cordero de Dios; III) La aclamación final a la gloria trinitaria.",
            "items": [
                {
                    "ocasion": "I. Aclamación Angélica y Alabanza al Padre",
                    "latin": "Glória in excélsis Deo et in terra pax homínibus bonæ voluntátis. Laudámus te, benedícimus te, adorámus te, glorificámus te, grátias ágimus tibi propter magnam glóriam tuam, Dómine Deus, Rex cæléstis, Deus Pater omnípotens.",
                    "espanol": "Gloria a Dios en el cielo, y en la tierra paz a los hombres que ama el Señor. Por tu inmensa gloria te alabamos, te bendecimos, te adoramos, te glorificamos, te damos gracias, Señor Dios, Rey celestial, Dios Padre todopoderoso.",
                },
                {
                    "ocasion": "II. Invocación y Súplica a Jesucristo, Cordero de Dios",
                    "latin": "Dómine Fili Unigénite, Iesu Christe, Dómine Deus, Agnus Dei, Fílius Patris, qui tollis peccáta mundi, miserére nobis; qui tollis peccáta mundi, súscipe deprecatiónem nostram. Qui sedes ad déxteram Patris, miserére nobis.",
                    "espanol": "Señor, Hijo único, Jesucristo; Señor Dios, Cordero de Dios, Hijo del Padre; tú que quitas el pecado del mundo, ten piedad de nosotros; tú que quitas el pecado del mundo, atiende nuestra súplica; tú que estás sentado a la derecha del Padre, ten piedad de nosotros.",
                },
                {
                    "ocasion": "III. Doxología Cristológico-Trinitaria Final",
                    "latin": "Quóniam tu solus Sanctus, tu solus Dóminus, tu solus Altíssimus, Iesu Christe, cum Sancto Spíritu: in glória Dei Patris. Amen.",
                    "espanol": "Porque solo tú eres Santo, solo tú Señor, solo tú Altísimo, Jesucristo, con el Espíritu Santo en la gloria de Dios Padre. Amén.",
                },
            ],
        },
        "semaforo": {
            "verde": [
                {
                    "titulo": "Fidelidad absoluta a cada palabra del Misal Romano (IGMR 53)",
                    "texto": "Verificar que la composición contenga íntegras las tres partes del himno oficial. El Gloria es una profesión de fe trinitaria y cristológica.",
                },
                {
                    "titulo": "Preferir la forma continua o alternada (sin estribillos redundantes)",
                    "texto": "Cuando se repite un estribillo largo cada dos líneas, el Gloria se vuelve excesivamente largo y pierde su impulso de himno corrido. La alternancia de frases entre Asamblea y Coro mantiene el texto fluido y vibrante.",
                },
                {
                    "titulo": "Silencio durante Adviento y Cuaresma para que brille en Navidad y Pascua",
                    "texto": "El ayuno del Gloria durante las cuatro semanas de Adviento y los cuarenta días de Cuaresma hace que su reaparición en la Nochebuena y en la Vigilia Pascual sea un verdadero acontecimiento espiritual.",
                },
            ],
            "amarillo": [
                {
                    "titulo": "Fiestas y Solemnidades que caen dentro de Adviento o Cuaresma",
                    "texto": "¡Atención al calendario! Sí se canta el Gloria en las Solemnidades y Fiestas que ocurren durante Adviento o Cuaresma: Inmaculada Concepción (8 dic.), Fiesta de Nuestra Señora de Guadalupe (12 dic.), Cátedra de San Pedro (22 feb.), San José (19 mar.) y Anunciación del Señor (25 mar.).",
                },
            ],
            "rojo": [
                {
                    "titulo": "Sustituir el texto oficial por 'Glorias rimados' o paráfrasis trinitarias",
                    "texto": "Reemplazar el himno del Misal por canciones cuyas estrofas dicen tres versos al Padre, tres al Hijo y tres al Espíritu omitiendo «Señor Dios, Cordero de Dios, Hijo del Padre; tú que quitas el pecado del mundo...» viola expresamente la IGMR 53.",
                },
                {
                    "titulo": "Recitar el Gloria en domingos en que se cantaron cantos secundarios",
                    "texto": "No tiene sentido litúrgico cantar un largo canto de entrada y otro de salida, y dejar rezado en frío el gran himno del Gloria in excelsis.",
                },
            ],
        },
        "adaptacion_tiempos": {
            "Adviento y Cuaresma": {
                "espiritu": "OMISIÓN NORMATIVA (salvo Solemnidades y Fiestas).",
                "textos_sugeridos": "No se canta el Gloria en los domingos de Adviento ni de Cuaresma para reservar el cántico de los ángeles a la noche de Navidad y al triunfo pascual.",
                "criterio_musical": "Terminado el Kyrie, el sacerdote dice inmediatamente «Oremos» para la Oración Colecta.",
            },
            "Navidad y Epifanía": {
                "espiritu": "El Gloria nace literalmente del Evangelio de la Nochebuena (Lc 2, 14): el coro de los ángeles anuncia a los pastores el nacimiento del Salvador.",
                "textos_sugeridos": "Texto íntegro del Misal Romano.",
                "criterio_musical": "Carácter luminoso, jubiloso y coral, con registro brillante de órgano, cuerdas e instrumentos.",
            },
            "Semana Santa y Vigilia Pascual": {
                "espiritu": "En Jueves Santo despide la sonoridad festiva antes de la Pasión; en la Vigilia Pascual anuncia la Resurrección del Señor tras las lecturas del Antiguo Testamento.",
                "textos_sugeridos": "Texto íntegro del Misal Romano acompañado del repique solemne de campanas.",
                "criterio_musical": "Debe ser la versión más solemne, majestuosa y participativa de todo el repertorio anual de la parroquia.",
            },
            "Tiempo Ordinario": {
                "espiritu": "Alabanza dominical de la Iglesia que celebra el Día del Señor.",
                "textos_sugeridos": "Texto íntegro del Misal Romano (Misa de Angelis, Misa Jubilar o composiciones en español de ejecución ágil).",
                "criterio_musical": "Fluido y directo (entre 2 y 3 minutos de duración), facilitando que toda la asamblea lo cante con soltura.",
            },
        },
        "tratado_teologico": [
            {
                "id": "gloria-origen-psalmus",
                "titulo": "1. Origen Patrístico: Los «Psalmi idiotici» y el Himno Matutino Oriental",
                "parrafos": [
                    "El Gloria in excelsis Deo pertenece al género antiquísimo de los llamados psalmi idiotici (salmos de composición eclesial privada, no bíblicos, compuestos en los siglos II y III a imitación de la poesía bíblica y de los cánticos del Apocalipsis). De la gran floración de himnos cristianos primitivos, solo dos sobrevivieron en la liturgia universal: el Phos Hilaron ('Luz gozosa', himno vespertino griego citado por San Basilio) y el Gloria in excelsis Deo (junto con el Te Deum en el Oficio Divino).",
                    "Su texto completo aparece ya en el siglo IV en las Constituciones Apostólicas (Libro VII, 47) como 'Oración de la mañana' (Hymnus matutinus) de la Liturgia de las Horas en Siria y en el Codex Alexandrinus de la Biblia griega (siglo V). Fue traducido al latín con admirable precisión teológica y rítmica muy probablemente por San Hilario de Poitiers († 367), quien conoció el himno durante su destierro en Oriente y ajustó su segunda parte para subrayar la divinidad consubstancial del Hijo frente a la herejía arriana.",
                ],
            },
            {
                "id": "gloria-historia-romana",
                "titulo": "2. De privilegio papal en la Noche de Navidad a himno dominical de toda la Asamblea",
                "parrafos": [
                    "Según el Liber Pontificalis, el Papa Telésforo (siglo II) introdujo el canto del himno angélico exclusivamente en la Misa de medianoche de la Navidad. A comienzos del siglo VI, el Papa Símaco (498–514) extendió su uso a todos los domingos y fiestas de los mártires, pero reservándolo únicamente a las Misas presididas por un Obispo; a los simples presbíteros solo se les permitía entonarlo un día al año: en la Pascua de Resurrección (como signo de que ese día todos celebraban en comunión con el Obispo). Recién hacia finales del siglo XI (Micrologus de Bernoldo de Constanza) se equiparó su uso para los presbíteros en todos los domingos y fiestas fuera de Adviento, Septuagésima y Cuaresma.",
                    "Teológicamente, el Gloria nos enseña qué es la verdadera adoración cristiana: antes de pedir cualquier cosa para nosotros ('ten piedad de nosotros, atiende nuestra súplica'), la Iglesia se olvida de sí misma para contemplar a Dios y decirle la frase más desinteresada de toda la liturgia: «Grátias ágimus tibi propter magnam glóriam tuam» ('Te damos gracias por tu inmensa gloria': te damos gracias no solo por tus beneficios hacia nosotros, sino simplemente porque Tú eres Dios).",
                ],
            },
        ],
        "citas_magisteriales": [
            {
                "id_cita": "igmr-53",
                "doc_id": "igmr",
                "fuente": "Instrucción General del Misal Romano (IGMR)",
                "numeral": "n. 53",
                "año": "2002 / Tercera Edición Típica",
                "url_oficial": "https://www.vatican.va/roman_curia/congregations/ccdds/documents/rc_con_ccdds_doc_20030317_ordinamento-messale_sp.html#B._Ritos_iniciales",
                "texto": "«El Gloria es un antiquísimo y venerable himno con que la Iglesia, congregada en el Espíritu Santo, glorifica a Dios Padre y al Cordero y le presenta sus súplicas. El texto de este himno no puede cambiarse por otro. Lo inicia el sacerdote o, según las circunstancias, el cantor o el coro, pero es cantado o por todos juntos, o por el pueblo alternando con el coro, o por el mismo coro. Si no se canta, al menos lo han de recitar todos, o juntos o en dos coros que se responden alternativamente. Se canta o se recita los domingos, fuera de los tiempos de Adviento y de Cuaresma, en las solemnidades y en las fiestas y en algunas celebraciones peculiares más solemnes.»",
                "comentario_pastoral": "Contiene la prohibición taxativa de cambiar la letra y detalla los tres modos de cantarlo y el calendario exacto de su uso.",
            },
        ],
        "criterios_musicales": [
            {
                "id": "glo-crit-1",
                "categoria": "Arquitectura en Tres Movimientos Internos",
                "titulo": "Contraste expresivo entre las tres secciones sin perder unidad de pulso",
                "explicacion": "Una buena composición del Gloria refleja musicalmente su estructura tripartita:\n1. Primera sección ('Gloria a Dios... Dios Padre todopoderoso'): Carácter luminoso, exultante y proclamativo.\n2. Segunda sección ('Señor, Hijo único... ten piedad de nosotros'): Un recogimiento lírico y suplicante más íntimo al contemplar al Cordero que quita el pecado del mundo.\n3. Tercera sección ('Porque solo tú eres Santo... Amén'): Regreso triunfal al tempo y plenitud inicial para culminar en el gran Amén.",
            },
            {
                "id": "glo-crit-2",
                "categoria": "Economía de Tiempo y Fluidez",
                "titulo": "Evitar estribillos largos que cuadrupliquen la duración",
                "explicacion": "El texto del Gloria ya es extenso por sí mismo. Si se compone en forma continua o alternada (Asamblea / Coro), dura entre 2:00 y 2:45 minutos y conserva toda su fuerza dramática.",
            },
        ],
        "checklist_discernimiento": [
            {
                "id": "chk-glo-1",
                "pregunta": "¿El texto de la obra coincide palabra por palabra con el texto oficial del Misal Romano (sin omisiones ni rimas inventadas)?",
                "pista": "«El texto de este himno no puede cambiarse por otro» (IGMR 53).",
            },
            {
                "id": "chk-glo-2",
                "pregunta": "¿Corresponde cantar el Gloria hoy según el calendario litúrgico (Domingo fuera de Adviento/Cuaresma, Solemnidad o Fiesta)?",
                "pista": "IGMR 53.",
            },
            {
                "id": "chk-glo-3",
                "pregunta": "¿Permite una ejecución ágil y festiva donde la asamblea no se agote por repeticiones innecesarias?",
                "pista": "Forma himnódica directa o alternada entre pueblo y coro.",
            },
        ],
    },

    # =========================================================================
    # 5. SALMO RESPONSORIAL (PSALMUS RESPONSORIUS)
    # =========================================================================
    "salmo-responsorial": {
        "slug": "salmo-responsorial",
        "titulo": "Salmo Responsorial",
        "nombre_latino": "Psalmus responsorius / Graduale",
        "parte_nombre": "II. Liturgia de la Palabra",
        "cita_principal": "IGMR 61 · OLM 19–22",
        "subtitulo": "Palabra de Dios poética e inspirada con la que la asamblea responde y medita la primera lectura, proclamada desde el ambón por el salmista con la respuesta cantada de todo el pueblo.",
        "ficha_identidad": [
            {
                "id": "sal-naturaleza",
                "atributo": "Naturaleza Litúrgica (IGMR 61)",
                "valor": "Canto del Propio · Parte integrante de la Liturgia de la Palabra",
                "detalle": "No es un 'interludio musical de descanso' entre dos lecturas, sino una lectura bíblica más: es Palabra de Dios inspirada por el Espíritu Santo que se proclama cantando.",
            },
            {
                "id": "sal-funcion",
                "atributo": "Función Ritual",
                "valor": "Es el rito en sí mismo (Proclamación lírica y respuesta meditativa a la Palabra)",
                "detalle": "Su selección en el Leccionario depende directamente del tema teológico de la Primera Lectura, tendiendo un puente espiritual hacia el Evangelio.",
            },
            {
                "id": "sal-lugar",
                "atributo": "Lugar Litúrgico de Proclamación",
                "valor": "Desde el Ambón (IGMR 61, 309)",
                "detalle": "Por ser Palabra de Dios, el salmista o cantor del salmo debe proclamar las estrofas desde el ambón (mesa de la Palabra), salvo que por razones acústicas o instrumentales deba hacerlo desde el facistol del coro.",
            },
            {
                "id": "sal-ejecucion",
                "atributo": "Protagonista y Forma",
                "valor": "Salmista (Versículos) + Toda la Asamblea (Respuesta / Antífona)",
                "detalle": "Preferentemente de forma responsorial (OLM 20): el salmista entona la antífona, el pueblo la repite, y luego el salmista canta las estrofas intercaladas con la respuesta de los fieles.",
            },
            {
                "id": "sal-postura",
                "atributo": "Postura Corporal",
                "valor": "Sentados en actitud de escucha y meditación (IGMR 43)",
                "detalle": "Toda la asamblea permanece sentada saboreando la Palabra proclamada.",
            },
            {
                "id": "sal-prohibicion",
                "atributo": "Invariabilidad Bíblica",
                "valor": "Prohibición absoluta de sustituirlo por cantos no bíblicos (IGMR 61)",
                "detalle": "Jamás puede reemplazarse el Salmo del Leccionario por una 'canción de meditación' o canto religioso popular.",
            },
        ],
        "opciones_igmr": [
            {
                "numero": "Opción 1 (Leccionario del Día)",
                "titulo": "El Salmo asignado por el Leccionario para ese día",
                "descripcion": "Cantar íntegramente la antífona y las estrofas del salmo propio de la Misa del día tal como figuran en el Leccionario.",
            },
            {
                "numero": "Opción 2 (Salmo Responsorial Común por Tiempo)",
                "titulo": "Antífona y Salmo común del Tiempo Litúrgico (IGMR 61)",
                "descripcion": "Para que el pueblo pueda cantar más fácilmente la respuesta, la IGMR 61 permite emplear uno de los «Salmos y antífonas comunes» que el Leccionario ofrece para cada Tiempo Litúrgico (Adviento, Navidad, Cuaresma, Pascua, T. Ordinario).",
            },
            {
                "numero": "Opción 3 (Solo la Respuesta cantada)",
                "titulo": "Antífona cantada por el pueblo y estrofas proclamadas (OLM 21)",
                "descripcion": "Si no hay un salmista capaz de cantar todas las estrofas, se debe al menos cantar la respuesta (antífona) con toda la asamblea, mientras el lector proclama los versículos con dicción pausada y poética.",
            },
            {
                "numero": "Opción 4 (Graduale Romanum / Simplex)",
                "titulo": "El Gradual del Graduale Romanum o el Salmo del Graduale Simplex",
                "descripcion": "En celebraciones en latín o con schola gregoriana, el Gradual tradicional o el salmo responsorial del Graduale Simplex.",
            },
        ],
        "textos_oficiales": {
            "titulo": "Antífonas Comunes por Tiempo Litúrgico (Ordenación de las Lecturas de la Misa, n. 19–22)",
            "nota": "La IGMR 61 autoriza que una parroquia mantenga durante varias semanas de un mismo Tiempo Litúrgico una de estas antífonas comunes cantadas para asegurar que toda la asamblea la sepa de memoria.",
            "items": [
                {
                    "ocasion": "Adviento (Salmo 24 / Salmo 84)",
                    "latin": "Ad te, Domine, levavi animam meam. / Ostende nobis, Domine, misericordiam tuam.",
                    "espanol": "«A ti, Señor, levanto mi alma.» / «Muéstranos, Señor, tu misericordia y danos tu salvación.» / «Ven, Señor, a salvarnos.»",
                },
                {
                    "ocasion": "Navidad (Salmo 97)",
                    "latin": "Viderunt omnes fines terrae salutare Dei nostri.",
                    "espanol": "«Los confines de la tierra han contemplado la victoria de nuestro Dios.» / «Hoy nos ha nacido un Salvador: el Mesías, el Señor.»",
                },
                {
                    "ocasion": "Cuaresma (Salmo 50 / Salmo 90 / Salmo 129)",
                    "latin": "Miserere mei, Deus, secundum magnam misericordiam tuam.",
                    "espanol": "«Misericordia, Señor: hemos pecado.» / «Señor, acompáñame en la tribulación.» / «Del Señor viene la misericordia y la redención copiosa.»",
                },
                {
                    "ocasion": "Tiempo Pascual (Salmo 117)",
                    "latin": "Haec dies quam fecit Dominus: exsultemus et laetemur in ea. / Alleluia, alleluia, alleluia.",
                    "espanol": "«Éste es el día en que actuó el Señor: sea nuestra alegría y nuestro gozo.» / «Aleluya, aleluya, aleluya.»",
                },
                {
                    "ocasion": "Tiempo Ordinario (Salmos 18, 26, 33, 62, 94, 102, 144)",
                    "latin": "Verba vitae aeternae habes, Domine. / Gustate et videte quoniam suavis est Dominus.",
                    "espanol": "«Señor, tú tienes palabras de vida eterna.» / «Gusten y vean qué bueno es el Señor.» / «El Señor es compasivo y misericordioso.» / «Mi alma tiene sed de ti, Dios mío.»",
                },
            ],
        },
        "semaforo": {
            "verde": [
                {
                    "titulo": "Guardar unos segundos de silencio sagrado antes de iniciar el Salmo",
                    "texto": "Terminada la Primera Lectura («Palabra de Dios — Te alabamos, Señor»), debe guardarse un breve silencio meditativo (IGMR 56) antes de que el salmista entone la antífona del Salmo.",
                },
                {
                    "titulo": "El Salmo se canta, no se lee apresuradamente como prosa informativa",
                    "texto": "Por su género literario (Tehillim: cánticos con instrumento de cuerda), el Salmo pide ser cantado. Si al menos se canta la antífona con una melodía sencilla, toda la Liturgia de la Palabra cobra vida.",
                },
                {
                    "titulo": "Claridad absoluta de dicción del Salmista",
                    "texto": "En el Salmo Responsorial la música es sierva humilde de la Palabra: cada sílaba de las estrofas debe entenderse con nitidez cristalina sin necesidad de que el pueblo tenga un folleto en las manos.",
                },
            ],
            "amarillo": [
                {
                    "titulo": "Uso del Salmo Estacional cuando no se alcanzó a musicalizar el del día",
                    "texto": "Si un domingo el salmista no pudo preparar la melodía específica del salmo propio, es cien veces preferible cantar el Salmo Común del Tiempo Litúrgico (IGMR 61) antes que leer el salmo sin música o inventar una canción ajena.",
                },
            ],
            "rojo": [
                {
                    "titulo": "Sustituir el Salmo por canciones populares ('Tu Palabra me da vida' como único canto sin leer el Salmo)",
                    "texto": "Reemplazar el Salmo bíblico del día por una canción sobre la Biblia mutila la Liturgia de la Palabra. Nadie tiene autoridad para suprimir una lectura de la Sagrada Escritura.",
                },
                {
                    "titulo": "Decir «Palabra de Dios» al terminar el Salmo",
                    "texto": "El Salmo Responsorial NO concluye con la aclamación «Palabra de Dios — Te alabamos, Señor», sino directamente con la última repetición de la antífona por parte de la asamblea.",
                },
                {
                    "titulo": "Acompañamiento instrumental ruidoso que tapa las estrofas",
                    "texto": "Rasguear con fuerza durante los versículos del salmista impide comprender el texto bíblico. Durante las estrofas el instrumento solo debe dar acordes tenidos o arpegios muy transparentes.",
                },
            ],
        },
        "adaptacion_tiempos": {
            "Tiempo Ordinario": {
                "espiritu": "Diálogo de la Esposa (la Iglesia) que medita la historia de la salvación proclamada en la Primera Lectura.",
                "textos_sugeridos": "El Salmo propio del domingo en el Leccionario (Ciclos A, B o C).",
                "criterio_musical": "Fórmulas salmódicas flexibles o composiciones responsoriales donde el estribillo sea inmediato para el pueblo.",
            },
            "Cuaresma": {
                "espiritu": "Oración penitencial y confiada de Cristo en el desierto y en su Pasión (Salmo 50 en Ceniza, Salmo 90 en el I Domingo, Salmo 21 el Domingo de Ramos).",
                "textos_sugeridos": "Salmo propio del Leccionario.",
                "criterio_musical": "Modo menor o modal (frigio/dórico), acompañamiento muy sobrio de cuerda pulsada u órgano suave.",
            },
            "Vigilia Pascual y Tiempo Pascual": {
                "espiritu": "En la Vigilia Pascual los 7 salmos responsoriales jalonan toda la historia de la salvación desde la Creación hasta el Agua viva. En el Tiempo Pascual el Salmo puede tener como respuesta «Aleluya, aleluya, aleluya».",
                "textos_sugeridos": "Salmo 117 («Éste es el día en que actuó el Señor»), Cantar de Éxodo 15, Salmo 15, Salmo 29.",
                "criterio_musical": "Luminoso y lírico; en la Vigilia Pascual conviene alternar distintos salmistas o registros para dar variedad a la gran vigilia.",
            },
        },
        "tratado_teologico": [
            {
                "id": "salmo-teologia-agustin",
                "titulo": "1. Teología Patrística del Salmo: «Christus totus» (Cristo total que ora en nosotros)",
                "parrafos": [
                    "La clave más profunda para comprender y cantar los Salmos en la Misa la formuló San Agustín en sus Enarrationes in Psalmos: cuando la Iglesia canta un salmo, quien ora allí es el Christus totus (el Cristo total, Cabeza y Cuerpo). «Si el Salmo ora, oren ustedes; si gime, giman ustedes; si se alegra, alégrense; si espera, esperen; si teme, teman; porque todo lo que aquí está escrito es nuestro espejo» (Enarr. in Ps. 30). En los Salmos escuchamos simultáneamente la voz de Dios que nos habla y nuestra propia voz humana —asumida por Cristo en su Encarnación y en la Cruz (Sal 21)— que responde al Padre.",
                    "Por eso el Orden de las Lecturas de la Misa (OLM, n. 19) enseña que el Salmo Responsorial no es un apéndice decorativo, sino «parte integrante de la Liturgia de la Palabra». En el diálogo de la Alianza, Dios toma la iniciativa hablándonos en la Primera Lectura, y la Iglesia Esposa le responde con las mismas palabras inspiradas que el Espíritu Santo puso en sus labios.",
                ],
            },
            {
                "id": "salmo-historia-gradual",
                "titulo": "2. Historia Litúrgica: Del Salmo Responsorial Patrístico al «Graduale» y su Restauración Conciliar",
                "parrafos": [
                    "El Salmo Responsorial es el canto más antiguo de toda la Misa cristiana, heredado directamente de la liturgia sinagogal judía (cf. Lc 4, 16-20; 1 Cor 14, 26). En los siglos IV y V, San Agustín en Hipona, San Ambrosio en Milán y San Juan Crisóstomo en Antioquía predicaban frecuentemente comentando el versículo del salmo que toda la asamblea acababa de cantar como respuesta al lector. El diácono o lector subía a las gradas (gradus) del ambón y desde allí entonaba el salmo completo; de ese lugar físico provino el nombre latino Graduale.",
                    "A partir del siglo VI en Roma, la schola cantorum embelleció las melodías del Gradual con melismas de extraordinaria riqueza artística, pero esto hizo que el pueblo ya no pudiera cantar la respuesta y el salmo se redujera a un solo versículo. El Concilio Vaticano II (SC 51, IGMR 61) devolvió a la Iglesia el Salmo Responsorial en su forma genuina: con varias estrofas poéticas y un estribillo accesible a toda la asamblea.",
                ],
            },
        ],
        "citas_magisteriales": [
            {
                "id_cita": "igmr-61",
                "doc_id": "igmr",
                "fuente": "Instrucción General del Misal Romano (IGMR)",
                "numeral": "n. 61",
                "año": "2002 / Tercera Edición Típica",
                "url_oficial": "https://www.vatican.va/roman_curia/congregations/ccdds/documents/rc_con_ccdds_doc_20030317_ordinamento-messale_sp.html#C._Liturgia_de_la_Palabra",
                "texto": "«Después de la primera lectura sigue el salmo responsorial, que es parte integrante de la Liturgia de la Palabra y tiene gran importancia litúrgica y pastoral, porque favorece la meditación de la Palabra de Dios. El salmo responsorial debe responder a cada lectura y habitualmente se tomará del Leccionario. Es preferible que el salmo responsorial sea cantado, al menos en lo que se refiere a la respuesta del pueblo. Así pues, el salmista, o cantor del salmo, desde el ambón o desde otro sitio oportuno, proclama las estrofas del salmo, mientras toda la asamblea escucha sentada y además participa con su respuesta, a no ser que el salmo se pronuncie de modo directo, es decir, sin respuesta. Mas, para que el pueblo pueda más fácilmente dar la respuesta salmódica, se han elegido algunos textos de respuestas y de salmos según los diversos tiempos del año o para las diversas categorías de Santos, los cuales podrán emplearse, en vez del texto que corresponde a la lectura, siempre que el salmo sea cantado.»",
                "comentario_pastoral": "Define la naturaleza bíblica del Salmo, su proclamación desde el ambón y la opción pastoral de usar los Salmos Comunes por Tiempo Litúrgico.",
            },
        ],
        "criterios_musicales": [
            {
                "id": "sal-crit-1",
                "categoria": "El Arte de la Salmodia en Español",
                "titulo": "Recitativo melódico flexible (Cuerda de recitación + Cadencia)",
                "explicacion": "Dado que los versículos de los salmos en el Leccionario no tienen métrica fija (no son octosílabos ni endecasílabos, sino paralelismo semítico de longitud variable), el compositor no debe forzar el texto metiendo diez sílabas a presión en un compás rígido. La técnica maestra es la salmodia o el recitativo lírico flexible: una nota tenida o giro melódico elástico (tenor/cuerda de recitación) que se adapta al número de sílabas de cada hemistiquio y reposa suavemente sobre el último acento tónico de la frase.",
            },
            {
                "id": "sal-crit-2",
                "categoria": "Diseño de la Antífona (Respuesta del Pueblo)",
                "titulo": "Frase breve (2 a 4 compases), diatónica y memorable en una sola escucha",
                "explicacion": "La asamblea escucha la antífona una sola vez en labios del salmista e inmediatamente debe repetirla. Por tanto, la antífona debe tener un contorno melódico natural, sin saltos disonantes ni síncopas confusas, manteniéndose entre Re4 y Si4/Do5.",
            },
        ],
        "checklist_discernimiento": [
            {
                "id": "chk-sal-1",
                "pregunta": "¿El texto corresponde exactamente al Salmo del Leccionario del día (o al Salmo Común del Tiempo Litúrgico autorizado por IGMR 61)?",
                "pista": "Jamás puede reemplazarse por un canto no salmódico.",
            },
            {
                "id": "chk-sal-2",
                "pregunta": "¿La antífona es lo bastante breve y clara para que la asamblea la repita de inmediato tras escucharla una sola vez?",
                "pista": "Participación responsorial de todo el pueblo.",
            },
            {
                "id": "chk-sal-3",
                "pregunta": "¿La música de las estrofas respeta las pausas y el paralelismo poético de los versículos sin atropellar las sílabas?",
                "pista": "Primacía de la Palabra proclamada.",
            },
        ],
    },

    # =========================================================================
    # 6. SECUENCIA (SEQUENTIA)
    # =========================================================================
    "secuencia": {
        "slug": "secuencia",
        "titulo": "Secuencia",
        "nombre_latino": "Sequentia",
        "parte_nombre": "II. Liturgia de la Palabra",
        "cita_principal": "IGMR 64",
        "subtitulo": "El himno lírico-poético de las grandes solemnidades del Señor y de la Virgen que medita dramáticamente el misterio celebrado inmediatamente antes de la aclamación del Aleluya.",
        "ficha_identidad": [
            {
                "id": "sec-naturaleza",
                "atributo": "Naturaleza Litúrgica",
                "valor": "Himno del Propio (Obligatorio en Pascua y Pentecostés · Facultativo en Corpus y Dolores)",
                "detalle": "Es una joya poética medieval conservada en el Leccionario para las cumbres del Año Litúrgico.",
            },
            {
                "id": "sec-ubicacion",
                "atributo": "Ubicación Exacta Renovada (IGMR 64)",
                "valor": "Después de la Segunda Lectura y ANTES del Aleluya",
                "detalle": "En la tercera edición típica del Misal Romano (2002), la Secuencia se trasladó antes del Aleluya para que el Aleluya acompañe directamente la procesión hacia el Evangelio.",
            },
            {
                "id": "sec-dias",
                "atributo": "Las 4 Secuencias del Misal Romano",
                "valor": "1) Pascua (Oblig.) · 2) Pentecostés (Oblig.) · 3) Corpus Christi (Facult.) · 4) Ntra. Sra. de los Dolores (Facult.)",
                "detalle": "En la Octava de Pascua (lunes a sábado) la secuencia Victimae paschali laudes es facultativa; el Domingo de Resurrección y el Domingo de Pentecostés son estrictamente obligatorias.",
            },
            {
                "id": "sec-postura",
                "atributo": "Postura Corporal de la Asamblea",
                "valor": "Sentados o de pie (poniéndose todos de pie al iniciar el Aleluya)",
                "detalle": "Como la Secuencia precede al Aleluya (que es el canto que pone de pie a la asamblea según IGMR 43), puede escucharse o cantarse sentado o de pie, pero al terminar la Secuencia todos se ponen de pie para el Aleluya.",
            },
            {
                "id": "sec-ejecucion",
                "atributo": "Protagonista y Ejecución",
                "valor": "Alternada (Coro/Solistas), toda la Asamblea o con breve estribillo intercalado",
                "detalle": "Su estructura original de estrofas pareadas (A-A, B-B, C-C) nació para ser cantada alternando dos semicoros (voces masculinas y femeninas, o solista y coro).",
            },
        ],
        "opciones_igmr": [
            {
                "numero": "Secuencia I (Pascua · Obligatoria)",
                "titulo": "Victimae paschali laudes («Ofrezcan los cristianos ofrendas de alabanza»)",
                "descripcion": "Compuesta por Wipo de Borgoña († c. 1050). Diálogo dramático con María Magdalena («¿Qué has visto de camino, María?») que culmina en la certeza: «Scimus Christum surrexisse a mortuis vere».",
            },
            {
                "numero": "Secuencia II (Pentecostés · Obligatoria)",
                "titulo": "Veni, Sancte Spiritus («Ven, Espíritu Divino»)",
                "descripcion": "Llamada la 'Secuencia Áurea' (atribuida a Esteban Langton o Inocencio III, s. XII–XIII). Diez tercetos de perfecta simetría que invocan al Padre de los pobres y Luz de los corazones.",
            },
            {
                "numero": "Secuencia III (Corpus Christi · Facultativa)",
                "titulo": "Lauda Sion Salvatorem («Alaba, Sión, al Salvador»)",
                "descripcion": "Compuesta por Santo Tomás de Aquino en 1264 a petición del Papa Urbano IV. Síntesis suprema de la teología de la transubstanciación y de la presencia real eucarística (sus últimas estrofas son el Ecce panis angelorum y el Bone Pastor).",
            },
            {
                "numero": "Secuencia IV (Virgen de los Dolores, 15 sept. · Facultativa)",
                "titulo": "Stabat Mater dolorosa («Estaba la Madre dolorosa junto a la Cruz»)",
                "descripcion": "Atribuida a Jacopone da Todi (s. XIII). Meditación lírica de la compasión de María al pie del Calvario.",
            },
        ],
        "textos_oficiales": {
            "titulo": "Las Dos Secuencias Obligatorias del Año Litúrgico (Extractos Bilingües)",
            "nota": "En la tradición del Rito Romano, las secuencias concluyen con «Amén. Aleluya», enlazando directamente con la aclamación antes del Evangelio.",
            "items": [
                {
                    "ocasion": "Domingo de Pascua de la Resurrección · Victimae paschali laudes",
                    "latin": "Víctimæ pascháli laudes ímmolent christiáni. Agnus redémit oves: Christus ínnocens Patri reconciliávit peccatóres. Mors et vita duéllo conflixére mirándo: dux vitæ mórtuus, regnat vivus. — Dic nobis María, quid vidísti in via? — Sepúlchrum Christi vivéntis, et glóriam vidi resurgéntis... Scimus Christum surrexísse a mórtuis vere: tu nobis, victor Rex, miserére. Amen. Allelúia.",
                    "espanol": "Ofrezcan los cristianos ofrendas de alabanza a gloria de la Víctima propicia de la Pascua. Cordero sin pecado que a las ovejas salva, a Dios y a los culpables unió con nueva alianza. Lucharon vida y muerte en singular batalla, y, muerto el que es la Vida, triunfante se levanta. — «¿Qué has visto de camino, María, en la mañana?» — «A mi Señor glorioso, la tumba abandonada...» Primicia de los muertos, sabemos por tu gracia que estás resucitado; la muerte en ti no manda. Rey vencedor, apiádate de la miseria humana y da a tus fieles parte en tu victoria santa.",
                },
                {
                    "ocasion": "Domingo de Pentecostés · Veni, Sancte Spiritus",
                    "latin": "Veni, Sancte Spíritus, et emítte cælitus lucis tuæ rádium. Veni, pater páuperum, veni, dator múnerum, veni, lumen córdium. Consolátor óptime, dulcis hospes ánimæ, dulce refrigérium. In labóre réquies, in æstu tempéries, in fletu solátium. O lux beatíssima, reple cordis íntima tuórum fidélium...",
                    "espanol": "Ven, Espíritu Divino, manda tu luz desde el cielo. Padre amoroso del pobre; don, en tus dones espléndido; luz que penetra las almas; fuente del mayor consuelo. Ven, dulce huésped del alma, descanso de nuestro esfuerzo, tregua en el duro trabajo, brisa en las horas de fuego, gozo que enjuga las lágrimas y reconforta en los duelos. Entra hasta el fondo del alma, divina luz, y enriquécenos...",
                },
            ],
        },
        "semaforo": {
            "verde": [
                {
                    "titulo": "Cantar la Secuencia ANTES del Aleluya (IGMR 64)",
                    "texto": "Respetar el orden ritual vigente: Segunda Lectura → Secuencia → Todos de pie para el Aleluya y procesión con el Evangeliario.",
                },
                {
                    "titulo": "Prepararla con anticipación para Pascua y Pentecostés",
                    "texto": "Dado que son obligatorias solo dos veces al año, cuando el coro prepara una versión hermosa del Victimae paschali y del Veni Sancte Spiritus realza extraordinariamente las dos mayores solemnidades del año.",
                },
            ],
            "amarillo": [
                {
                    "titulo": "En Corpus Christi (Lauda Sion) se permite la forma breve",
                    "texto": "El Leccionario permite en Corpus Christi cantar la secuencia íntegra (24 estrofas) o bien su forma breve oficial que comienza en «Ecce panis angelorum / He aquí el pan de los ángeles».",
                },
            ],
            "rojo": [
                {
                    "titulo": "Omitir la Secuencia en el Domingo de Pascua o de Pentecostés",
                    "texto": "La IGMR 64 establece que en ambos días la Secuencia es obligatoria; no debe suprimirse.",
                },
                {
                    "titulo": "Sustituir el «Veni, Sancte Spiritus» por cualquier canción carismática al Espíritu Santo",
                    "texto": "La Secuencia es un texto litúrgico oficial del Leccionario; un canto libre al Espíritu Santo puede usarse en la Entrada o Comunión, pero no reemplaza al texto de la Secuencia.",
                },
            ],
        },
        "adaptacion_tiempos": {
            "Domingo de Pascua y Octava": {
                "espiritu": "Anuncio dramático y jubiloso del triunfo de la Vida sobre la muerte y testimonio de María Magdalena.",
                "textos_sugeridos": "Victimae paschali laudes (texto oficial del Leccionario).",
                "criterio_musical": "Modo dórico luminoso; excelente para alternar solistas (en el diálogo con María Magdalena) y el tutti del coro y asamblea en el 'Sabemos que Cristo ha resucitado verdaderamente'.",
            },
            "Domingo de Pentecostés": {
                "espiritu": "Súplica ardiente e íntima para que el Espíritu Santo transforme la aridez del corazón humano.",
                "textos_sugeridos": "Veni, Sancte Spiritus (texto oficial del Leccionario).",
                "criterio_musical": "Lírico, cálido y progresivo, construyendo intensidad desde la súplica íntima hasta el septenario de dones.",
            },
            "Corpus Christi y Virgen de los Dolores": {
                "espiritu": "Adoración dogmática del Pan de los Ángeles (Corpus) y contemplación de la Madre al pie de la Cruz (15 de septiembre).",
                "textos_sugeridos": "Lauda Sion Salvatorem (o forma breve Ecce panis angelorum) y Stabat Mater dolorosa.",
                "criterio_musical": "Carácter himnódico solemne (Corpus) o recogido y expresivo (Dolores).",
            },
        },
        "tratado_teologico": [
            {
                "id": "secuencia-historia-notker",
                "titulo": "1. Origen Histórico: Del «Jubilus» del Aleluya a Notker Balbulus de Sankt Gallen",
                "parrafos": [
                    "El nacimiento de la Secuencia en el siglo IX es uno de los capítulos más fascinantes de la historia de la música occidental. En el canto gregoriano, la última sílaba de la palabra «Allelú-ia» se prolongaba en un extensísimo melisma sin texto llamado Jubilus o Sequentia ('lo que sigue' al Aleluya). Como a los monjes les resultaba difícil recordar de memoria aquellas largas cadenas de notas sin palabras, el monje Notker Balbulus ('el Tartamudo', 840–912) de la abadía suiza de Sankt Gallen —inspirado por un antifonario traído por un monje que huía de la abadía normanda de Jumièges— comenzó a escribir textos poéticos silábicos (llamados prosa ad sequentiam) colocando exactamente una sílaba debajo de cada nota del melisma.",
                    "El género tuvo tal éxito en toda Europa que durante la Edad Media se compusieron más de cinco mil secuencias. El Concilio de Trento (Misal de San Pío V, 1570), buscando depurar la liturgia de textos tardíos de desigual calidad teológica, suprimió casi todas y conservó únicamente las cuatro obras maestras universales (Victimae paschali laudes, Veni Sancte Spiritus, Lauda Sion y Dies irae, a las que Benedicto XIII sumó en 1727 el Stabat Mater). Tras el Vaticano II, el Dies irae pasó a ser himno del Oficio de Lectura de la última semana del Tiempo Ordinario y de Difuntos, quedando las cuatro secuencias actuales en el Leccionario de la Misa.",
                ],
            },
        ],
        "citas_magisteriales": [
            {
                "id_cita": "igmr-64",
                "doc_id": "igmr",
                "fuente": "Instrucción General del Misal Romano (IGMR)",
                "numeral": "n. 64",
                "año": "2002 / Tercera Edición Típica",
                "url_oficial": "https://www.vatican.va/roman_curia/congregations/ccdds/documents/rc_con_ccdds_doc_20030317_ordinamento-messale_sp.html#C._Liturgia_de_la_Palabra",
                "texto": "«La secuencia, que, fuera de los días de Pascua y de Pentecostés, es facultativa, se canta antes del Aleluya.»",
                "comentario_pastoral": "Precisa las dos solemnidades obligatorias y su colocación antes del Aleluya.",
            },
        ],
        "criterios_musicales": [
            {
                "id": "sec-crit-1",
                "categoria": "Forma de Estrofas Pareadas (Paralelismo Doble)",
                "titulo": "Alternancia de dos semicoros con estribillo congregacional opcional",
                "explicacion": "Para facilitar la participación del pueblo en un texto extenso como el Veni Sancte Spiritus o el Victimae paschali, es excelente alternar las estrofas entre voces femeninas y masculinas del coro (o solista y coro SATB), permitiendo que toda la asamblea se una cada dos o tres estrofas con una breve antífona (ej. 'Ven, Espíritu Santo, y envía desde el cielo un rayo de tu luz').",
            },
        ],
        "checklist_discernimiento": [
            {
                "id": "chk-sec-1",
                "pregunta": "¿Se utiliza el texto oficial de la Secuencia del Leccionario para Pascua o Pentecostés?",
                "pista": "IGMR 64.",
            },
            {
                "id": "chk-sec-2",
                "pregunta": "¿Está programada exactamente después de la Segunda Lectura y ANTES de entonar el Aleluya?",
                "pista": "Orden ritual de la Tercera Edición Típica del Misal Romano.",
            },
        ],
    },

    # =========================================================================
    # 7. ACLAMACIÓN ANTES DEL EVANGELIO (ALELUYA)
    # =========================================================================
    "aleluya": {
        "slug": "aleluya",
        "titulo": "Aclamación antes del Evangelio (Aleluya)",
        "nombre_latino": "Alleluia / Acclamatio ante Evangelium",
        "parte_nombre": "II. Liturgia de la Palabra",
        "cita_principal": "IGMR 62–63 · OLM 23",
        "subtitulo": "La aclamación pascual con que toda la asamblea, puesta en pie, acoge y saluda a Cristo el Señor que se hace presente para hablar a su pueblo en el Santo Evangelio.",
        "ficha_identidad": [
            {
                "id": "ale-naturaleza",
                "atributo": "Naturaleza Litúrgica (IGMR 62)",
                "valor": "Canto del Propio (con aclamación fija y versículo propio del día)",
                "detalle": "Constituye por sí mismo un rito o acto autónomo de acogida al Señor que va a hablar en el Evangelio.",
            },
            {
                "id": "ale-funcion",
                "atributo": "Doble Función Ritual",
                "valor": "1) Saludo de fe a Cristo presente · 2) Acompaña la procesión hacia el Ambón",
                "detalle": "Mientras todos cantan el Aleluya, el sacerdote impone incienso (si se usa), bendice al diácono y éste lleva en alto el Evangeliario desde el altar hasta el ambón escoltado por ciriales e incensario.",
            },
            {
                "id": "ale-ejecucion",
                "atributo": "Ejecución y Estructura (IGMR 62)",
                "valor": "Todos de pie: Asamblea (Aleluya) → Coro/Cantor (Versículo bíblico) → Asamblea (Aleluya)",
                "detalle": "Lo inicia el coro o cantor, lo repite todo el pueblo, el coro o cantor proclama el versículo propio del Evangelio del día y toda la asamblea repite el Aleluya.",
            },
            {
                "id": "ale-cuaresma",
                "atributo": "Mutación en Tiempo de Cuaresma (IGMR 62b)",
                "valor": "Supresión total del vocablo «Aleluya» · Se canta la Aclamación a Cristo",
                "detalle": "Desde el Miércoles de Ceniza hasta la Vigilia Pascual nunca se pronuncia la palabra hebrea Alleluia ('Alaben a Yahvé'): en su lugar se canta una de las aclamaciones crísticas del Leccionario («Honor y gloria a ti, Señor Jesús») más el versículo del día.",
            },
            {
                "id": "ale-omision",
                "atributo": "Norma si NO se canta (IGMR 63c)",
                "valor": "Si no se canta, el Aleluya o la aclamación antes del Evangelio PUEDE OMITIRSE",
                "detalle": "Es el único elemento del Propio que la IGMR prefiere omitir antes que recitar en frío, porque el Aleluya es intrínsecamente un canto de júbilo.",
            },
            {
                "id": "ale-grado",
                "atributo": "Grado de Participación",
                "valor": "Segundo Grado (Musicam Sacram, n. 30)",
                "detalle": "Incluso en misas feriales sin otros cantos, cantar el Aleluya de pie antes del Evangelio realza la cumbre de la Liturgia de la Palabra.",
            },
        ],
        "opciones_igmr": [
            {
                "numero": "Fuera de Cuaresma",
                "titulo": "Aleluya + Versículo propio del Leccionario + Aleluya",
                "descripcion": "Estructura tripartita obligatoria: nunca debe cantarse el 'Aleluya' solo sin su versículo bíblico interior, pues el versículo anticipa la frase clave del Evangelio que se va a proclamar.",
            },
            {
                "numero": "En Tiempo de Cuaresma",
                "titulo": "Aclamación a Cristo (Leccionario) + Versículo propio + Aclamación",
                "descripcion": "Se emplea una de las fórmulas oficiales del Leccionario en español («Honor y gloria a ti, Señor Jesús» / «Alabanza y honor a ti, Señor Jesús») enmarcando el versículo del día.",
            },
        ],
        "textos_oficiales": {
            "titulo": "Aclamaciones Oficiales antes del Evangelio (Fuera de Cuaresma y en Cuaresma)",
            "nota": "En Cuaresma se sustituye la palabra hebrea «Hallelû-Yāh» por su traducción cristológica («Alabanza a ti, oh Cristo»). Las cuatro fórmulas cuaresmales oficiales del Leccionario son las siguientes:",
            "items": [
                {
                    "ocasion": "Todo el año (excepto Cuaresma)",
                    "latin": "Allelúia, allelúia, allelúia. V/. Loquere, Domine, quia audit servus tuus... R/. Allelúia.",
                    "espanol": "R/. Aleluya, aleluya, aleluya.\nV/. Habla, Señor, que tu siervo escucha; tú tienes palabras de vida eterna (Jn 6, 68b).\nR/. Aleluya, aleluya, aleluya.",
                },
                {
                    "ocasion": "Tiempo de Cuaresma · Fórmulas Oficiales del Leccionario (OLM 23)",
                    "latin": "1) Laus tibi, Christe, Rex aeternae gloriae!\n2) Gloria et laus tibi, Christe!\n3) Gloria tibi, Verbum Dei!\n4) Salus nostra in manu tua, Domine!",
                    "espanol": "1) «¡Alabanza a ti, oh Cristo, Rey de eterna gloria!»\n2) «¡Honor y gloria a ti, Señor Jesús!»\n3) «¡Gloria a ti, Señor Jesús, Palabra del Padre!»\n4) «¡Gloria y honor a ti, Cristo Jesús!»",
                },
            ],
        },
        "semaforo": {
            "verde": [
                {
                    "titulo": "Cantar siempre el Versículo bíblico en medio del Aleluya",
                    "texto": "El Aleluya litúrgico no es un estribillo suelto: su corazón teológico es el versículo del Leccionario que introduce el Evangelio del día (Aleluya → Versículo → Aleluya).",
                },
                {
                    "titulo": "Empezar cuando el sacerdote se levanta (para acompañar toda la procesión al ambón)",
                    "texto": "No esperar a que el sacerdote ya esté en el ambón: el canto debe cubrir la imposición de incienso, la bendición al diácono y el traslado solemne del Evangeliario.",
                },
            ],
            "amarillo": [
                {
                    "titulo": "En la Vigilia Pascual: el Gran Aleluya Triple",
                    "texto": "En la Noche Santa de Pascua, tras la Epístola (Rom 6), el sacerdote o un cantor entona solemnemente tres veces el Aleluya elevando un tono cada vez, y el pueblo lo repite, seguido del Salmo 117.",
                },
            ],
            "rojo": [
                {
                    "titulo": "Cantar 'Aleluya' en Cuaresma (incluso en San José o la Anunciación)",
                    "texto": "En Cuaresma el Aleluya se suprime en TODAS las celebraciones sin excepción alguna, incluidas las Solemnidades de San José (19 mar.) y la Anunciación (25 mar.).",
                },
                {
                    "titulo": "Cantar 'Busca primero el Reino de Dios' u otra canción en vez del versículo del Evangelio",
                    "texto": "Sustituir el versículo propio del Evangelio del día por canciones populares desconectadas de la lectura evangélica empobrece la unidad de la Liturgia de la Palabra.",
                },
            ],
        },
        "adaptacion_tiempos": {
            "Tiempo Ordinario y Navidad": {
                "espiritu": "Aclamación gozosa a Cristo Maestro y Luz del mundo.",
                "textos_sugeridos": "Aleluya + Versículo propio del domingo en el Leccionario.",
                "criterio_musical": "Breve, radiante, en tonalidad mayor o modo lidio/jónico, con polifonía festiva en la repetición final.",
            },
            "Adviento": {
                "espiritu": "Expectación gozosa del Señor que viene (en Adviento SÍ se canta el Aleluya).",
                "textos_sugeridos": "Aleluya con versículos proféticos («Muéstranos, Señor, tu misericordia», «Preparen el camino del Señor», Antífonas de la 'O' del 17 al 23 de diciembre).",
                "criterio_musical": "Alegre pero contenido (ej. Aleluya gregoriano Conditor alme o modo dórico luminoso).",
            },
            "Cuaresma y Semana Santa": {
                "espiritu": "Ayuno del Aleluya; aclamación reverente a Cristo Siervo sufriente y Palabra eterna del Padre.",
                "textos_sugeridos": "«Honor y gloria a ti, Señor Jesús» + Versículo propio (en Domingo de Ramos y Viernes Santo: Filipenses 2, 8-9 «Cristo se humilló por nosotros, y por obediencia aceptó incluso la muerte, y una muerte de cruz»).",
                "criterio_musical": "Solemne, grave y recogido; el Viernes Santo se canta estrictamente a cappella.",
            },
            "Tiempo Pascual": {
                "espiritu": "El Aleluya está en su patria propia: aclamación pascual al Resucitado.",
                "textos_sugeridos": "Aleluya pascual (ej. O filii et filiae o Aleluya del Salmo 117) con el versículo propio («Cristo, nuestra Pascua, ha sido inmolado»).",
                "criterio_musical": "Máximo esplendor vocal, polifónico e instrumental.",
            },
        },
        "tratado_teologico": [
            {
                "id": "aleluya-teologia-presencia",
                "titulo": "1. Teología de la Presencia Real de Cristo en la Proclamación del Evangelio",
                "parrafos": [
                    "La Constitución Sacrosanctum Concilium (n. 7) enseña que Cristo «está presente en su palabra, pues cuando se lee en la Iglesia la Sagrada Escritura, es Él quien habla». Esta presencia alcanza su cima en la proclamación del Evangelio. Por eso la liturgia rodea al Evangeliario de los mismos signos de veneración que tributa al altar y a la Eucaristía: nos ponemos de pie (postura de los resucitados ante su Rey), se lleva en procesión entre cirios encendidos (Cristo Luz del mundo), se inciensa y es besado por el ministro al concluir.",
                    "El canto del Aleluya (del hebreo Hallelû-Yāh, grito pascual de los Salmos 113–118 y cántico de los redimidos en el cielo según Apocalipsis 19, 1-6) es la alfombra sonora que recibe al Esposo. Como explicaba San Agustín: «El Aleluya es el cántico de nuestra patria celestial; ahora lo cantamos como peregrinos en la esperanza (in spe), entonces lo cantaremos en la posesión definitiva (in re)» (Sermón 255). De ahí el sentido profundo del 'ayuno del Aleluya' durante los cuarenta días de Cuaresma: reconociéndonos en el exilio babilónico de la penitencia, guardamos silencio del cántico celestial hasta que en la noche de la Vigilia Pascual resuene de nuevo junto al sepulcro vacío.",
                ],
            },
        ],
        "citas_magisteriales": [
            {
                "id_cita": "igmr-62-63",
                "doc_id": "igmr",
                "fuente": "Instrucción General del Misal Romano (IGMR)",
                "numeral": "nn. 62–63",
                "año": "2002 / Tercera Edición Típica",
                "url_oficial": "https://www.vatican.va/roman_curia/congregations/ccdds/documents/rc_con_ccdds_doc_20030317_ordinamento-messale_sp.html#C._Liturgia_de_la_Palabra",
                "texto": "«Después de la lectura que precede inmediatamente al Evangelio, se canta el Aleluya u otro canto determinado por las rúbricas, según lo pida el tiempo litúrgico. Una aclamación de este género constituye por sí misma un rito o acto con el que la asamblea de los fieles acoge y saluda al Señor que va a hablarles en el Evangelio y profesa su fe con el canto. Es cantado por todos, de pie, iniciándolo el coro o el cantor, y si el caso lo pide, se repite; pero el versículo lo canta el coro o un cantor. a) El Aleluya se canta en todo tiempo fuera de la Cuaresma. Los versículos se toman del Leccionario o del Gradual. b) En el Tiempo de Cuaresma, en lugar del Aleluya se canta el versículo antes del Evangelio que aparece en el Leccionario... Si no se cantan, el Aleluya o el versículo antes del Evangelio pueden omitirse.»",
                "comentario_pastoral": "Define la estructura Asamblea–Cantor–Asamblea, el cambio en Cuaresma y la regla de que si no se canta es preferible omitirlo.",
            },
        ],
        "criterios_musicales": [
            {
                "id": "ale-crit-1",
                "categoria": "Fórmula de Salmodia para el Versículo Interior",
                "titulo": "Cómo cantar cualquier versículo del Leccionario sobre un mismo Aleluya",
                "explicacion": "Todo Aleluya bien compuesto debe incluir una cuerda de recitación (fórmula salmódica de dos hemistiquios en la misma tonalidad del estribillo) para que el cantor o el coro pueda entonar el versículo específico que trae el Leccionario de cada domingo sin tener que componer una canción nueva cada semana.",
            },
        ],
        "checklist_discernimiento": [
            {
                "id": "chk-ale-1",
                "pregunta": "¿Se incluye el versículo bíblico propio del Evangelio del día entre las dos aclamaciones del Aleluya?",
                "pista": "IGMR 62.",
            },
            {
                "id": "chk-ale-2",
                "pregunta": "Si estamos en Cuaresma, ¿se ha sustituido el Aleluya por «Honor y gloria a ti, Señor Jesús» u otra fórmula oficial del Leccionario?",
                "pista": "IGMR 62b.",
            },
            {
                "id": "chk-ale-3",
                "pregunta": "¿Comienza el canto a tiempo para acompañar la procesión del diácono o sacerdote hacia el ambón?",
                "pista": "Verdad del signo ritual.",
            },
        ],
    },

    # =========================================================================
    # 8. PROFESIÓN DE FE (CREDO / SYMBOLUM)
    # =========================================================================
    "credo": {
        "slug": "credo",
        "titulo": "Profesión de Fe (Credo)",
        "nombre_latino": "Symbolum Nicaeno-Constantinopolitanum / Apostolorum",
        "parte_nombre": "II. Liturgia de la Palabra",
        "cita_principal": "IGMR 67–68 · MS 30",
        "subtitulo": "El asentimiento solemne y bautismal con que todo el pueblo reunido responde a la Palabra de Dios proclamada en las lecturas y expuesta en la homilía, confesando la regla de la fe antes de celebrar la Eucaristía.",
        "ficha_identidad": [
            {
                "id": "cre-naturaleza",
                "atributo": "Naturaleza Litúrgica",
                "valor": "Canto del Ordinario (Ordo Missae · Texto dogmático invariable)",
                "detalle": "Solo existen dos textos válidos en el Misal Romano: el Símbolo Niceno-Constantinopolitano y el Símbolo de los Apóstoles. Ninguna canción sobre 'yo creo en el amor' puede reemplazar al Credo.",
            },
            {
                "id": "cre-cuando",
                "atributo": "Cuándo se Canta o Recita (IGMR 68)",
                "valor": "Todos los Domingos y Solemnidades (y celebraciones peculiares más solemnes)",
                "detalle": "A diferencia del Gloria, el Credo SÍ se dice en todos los domingos de Adviento y de Cuaresma.",
            },
            {
                "id": "cre-gesto",
                "atributo": "Gesto Corporal Prescrito (IGMR 68, 275)",
                "valor": "Inclinación profunda en la Encarnación (o Genuflexión en Navidad y la Anunciación)",
                "detalle": "A las palabras «y por obra del Espíritu Santo se encarnó de María, la Virgen, y se hizo hombre» (o «fue concebido por obra y gracia del Espíritu Santo...»), todos se inclinan profundamente; en la Anunciación (25 mar.) y en Navidad (25 dic.) todos se arrodillan.",
            },
            {
                "id": "cre-ejecucion",
                "atributo": "Protagonista y Ejecución (IGMR 68)",
                "valor": "Lo inicia el Sacerdote · Lo cantan todos juntos o alternando Pueblo y Coro",
                "detalle": "Por ser profesión personal y comunitaria de la fe («Creo / Creemos»), nunca debe ser cantado solo por el coro dejando muda a la asamblea (MS 34).",
            },
        ],
        "opciones_igmr": [
            {
                "numero": "Opción 1 (Texto Normativo)",
                "titulo": "Símbolo Niceno-Constantinopolitano (Concilios de Nicea 325 y Constantinopla 381)",
                "descripcion": "El gran Credo conciliar («Creo en un solo Dios... Dios de Dios, Luz de Luz, Dios verdadero de Dios verdadero...»), riqueza teológica suprema de la Iglesia universal.",
            },
            {
                "numero": "Opción 2 (Especialmente en Cuaresma y Pascua)",
                "titulo": "Símbolo Bautismal de la Iglesia Romana (Símbolo de los Apóstoles)",
                "descripcion": "Autorizado por la IGMR 68 especialmente durante la Cuaresma y el Tiempo Pascual por ser el símbolo propio del Bautismo romano.",
            },
            {
                "numero": "Excepción (Vigilia Pascual)",
                "titulo": "Renovación de las Promesas Bautismales («¿Creen en Dios...? — Sí, creo»)",
                "descripcion": "En la Vigilia Pascual y el Domingo de Pascua (o cuando se administra el Bautismo o la Confirmación dentro de la Misa), la Renovación dialogada de las Promesas Bautismales sustituye al Credo.",
            },
        ],
        "textos_oficiales": {
            "titulo": "Los Dos Símbolos Oficiales del Misal Romano (Extractos Centrales)",
            "nota": "En ambos textos, las palabras de la Encarnación van acompañadas de la inclinación profunda de cabeza y cuerpo.",
            "items": [
                {
                    "ocasion": "Símbolo Niceno-Constantinopolitano (Credo I / III Gregoriano)",
                    "latin": "Credo in unum Deum, Patrem omnipoténtem, factórem cæli et terræ, visibílium ómnium et invisibílium. Et in unum Dóminum Iesum Christum, Fílium Dei Unigénitum... Deum de Deo, lumen de lúmine, Deum verum de Deo vero, génitum, non factum, consubstantiálem Patri... [Hic genuflectitur / inclinatur] Et incarnátus est de Spíritu Sancto ex María Vírgine, et homo factus est...",
                    "espanol": "Creo en un solo Dios, Padre todopoderoso, Creador del cielo y de la tierra, de todo lo visible y lo invisible. Creo en un solo Señor, Jesucristo, Hijo único de Dios, nacido del Padre antes de todos los siglos: Dios de Dios, Luz de Luz, Dios verdadero de Dios verdadero, engendrado, no creado, de la misma naturaleza del Padre... [Se inclinan] y por obra del Espíritu Santo se encarnó de María, la Virgen, y se hizo hombre...",
                },
                {
                    "ocasion": "Símbolo de los Apóstoles (Especialmente en Cuaresma y Pascua)",
                    "latin": "Credo in Deum Patrem omnipoténtem, Creatórem cæli et terræ, et in Iesum Christum, Fílium eius únicum, Dóminum nostrum, [inclinatur] qui concéptus est de Spíritu Sancto, natus ex María Vírgine, passus sub Póntio Piláto...",
                    "espanol": "Creo en Dios, Padre todopoderoso, Creador del cielo y de la tierra. Creo en Jesucristo, su único Hijo, nuestro Señor, [se inclinan] que fue concebido por obra y gracia del Espíritu Santo, nació de santa María Virgen, padeció bajo el poder de Poncio Pilato...",
                },
            ],
        },
        "semaforo": {
            "verde": [
                {
                    "titulo": "Fidelidad dogmática absoluta al Símbolo Niceno o Apostólico",
                    "texto": "Cada palabra del Credo fue acuñada por los Concilios Ecuménicos y regada con la sangre de los mártires. No admite cortes ni paráfrasis.",
                },
                {
                    "titulo": "En la Vigilia Pascual o Bautismos, cantar la respuesta «¡Sí, creo!»",
                    "texto": "Cuando se hace la Renovación de las Promesas Bautismales en forma de triple pregunta, cantar con fuerza la respuesta «Sí, creo» o «Amén» tras cada artículo de fe es sumamente eficaz.",
                },
            ],
            "amarillo": [
                {
                    "titulo": "Si no se cuenta con una musicalización íntegra, es preferible proclamarlo con voz firme",
                    "texto": "Como el texto es largo, si una parroquia no conoce el Credo III gregoriano o un Credo recitativo alternado, debe recitarlo con ritmo unánime y pausado, nunca reemplazarlo por una canción.",
                },
            ],
            "rojo": [
                {
                    "titulo": "Los falsos 'Credos cantados' con letras subjetivas o incompletas",
                    "texto": "Sustituir el Símbolo de la Fe por canciones populares ('Creo, Señor, pero aumenta mi fe', 'Creo en el hombre y en la paz') que omiten los artículos trinitarios, la Encarnación virginal, la Iglesia y la Resurrección de la carne es un abuso grave.",
                },
            ],
        },
        "adaptacion_tiempos": {
            "Cuaresma y Tiempo Pascual": {
                "espiritu": "Memoria directa de la entrega del Símbolo (Redditio Symboli) a los catecúmenos en su Bautismo.",
                "textos_sugeridos": "Símbolo de los Apóstoles (más breve y conciso, ideal para musicalizar en recitativo alternado).",
                "criterio_musical": "Tono firme y sobrio; en la Vigilia Pascual se sustituye por el diálogo bautismal.",
            },
            "Grandes Solemnidades (Navidad, Epifanía, Trinidad, Cristo Rey)": {
                "espiritu": "Confesión solemne de la fe católica y apostólica en comunión con toda la Iglesia universal.",
                "textos_sugeridos": "Símbolo Niceno-Constantinopolitano (Credo III gregoriano o versión vernácula alternada).",
                "criterio_musical": "Alternancia entre dos coros (Asamblea y Schola) sobre fórmula recitativa modal, destacando con un tempo más lento y recogido la frase «Y por obra del Espíritu Santo se encarnó de María, la Virgen, y se hizo hombre».",
            },
        },
        "tratado_teologico": [
            {
                "id": "credo-historia-liturgia",
                "titulo": "1. Historia Litúrgica: Del Bautismo a la Misa (Antioquía, Toledo y Carlomagno)",
                "parrafos": [
                    "En los primeros siglos, el Credo pertenecía exclusivamente a la liturgia del Bautismo (la Traditio y Redditio Symboli en la Vigilia Pascual), pues la celebración de la Eucaristía misma ya era considerada la profesión de fe de los bautizados. Su introducción en la Misa dominical comenzó en Oriente en el siglo V (Pedro el Batanero en Antioquía hacia el 471 y Timoteo en Constantinopla hacia el 511) y pasó a Occidente a través de España en el III Concilio de Toledo (año 589), cuando el rey visigodo Recaredo y su pueblo abjuraron del arrianismo y dispusieron que el Símbolo de Nicea-Constantinopla fuese cantado en voz alta por todo el pueblo antes del Padre Nuestro como preparación a la Comunión.",
                    "A finales del siglo VIII, Carlomagno y Alcuino de York adoptaron la costumbre hispana en la capilla palatina de Aquisgrán, colocándolo inmediatamente después del Evangelio y la homilía. Finalmente, en el año 1014, durante la coronación imperial de San Enrique II en Roma, el Papa Benedicto VIII incorporó oficialmente el canto del Credo a la Misa romana, siendo por tanto el último canto del Ordinario en integrarse al Misal.",
                ],
            },
        ],
        "citas_magisteriales": [
            {
                "id_cita": "igmr-67-68",
                "doc_id": "igmr",
                "fuente": "Instrucción General del Misal Romano (IGMR)",
                "numeral": "nn. 67–68",
                "año": "2002 / Tercera Edición Típica",
                "url_oficial": "https://www.vatican.va/roman_curia/congregations/ccdds/documents/rc_con_ccdds_doc_20030317_ordinamento-messale_sp.html#C._Liturgia_de_la_Palabra",
                "texto": "«El Símbolo o profesión de fe tiende a que todo el pueblo reunido responda a la Palabra de Dios anunciada en las lecturas de la Sagrada Escritura y expuesta en la homilía, y a que, proclamando la regla de la fe con una fórmula aprobada para el uso litúrgico, recuerde y confiese los grandes misterios de la fe, antes de comenzar su celebración en la Eucaristía. El Símbolo lo debe cantar o decir el sacerdote juntamente con el pueblo en los domingos y solemnidades... Si se canta, lo inicia el sacerdote o, según las circunstancias, el cantor o el coro, pero lo cantarán o todos juntos o el pueblo alternando con el coro.»",
                "comentario_pastoral": "Exige que se use exclusivamente una «fórmula aprobada para el uso litúrgico» y que participe siempre el pueblo.",
            },
        ],
        "criterios_musicales": [
            {
                "id": "cre-crit-1",
                "categoria": "Fórmula Recitativa con Aclamación («Credo, Domine»)",
                "titulo": "Cómo componer un Credo cantable en español",
                "explicacion": "La dificultad de musicalizar el Credo radica en su extensión en prosa. Las dos soluciones históricas más logradas son:\n1) La recitación melódica silábica alternada en un solo modo (como el Credo I y el Credo III gregoriano), donde un par de fórmulas melódicas sencillas se aplican a todas las frases.\n2) El esquema responsorial donde el cantor/coro proclama en recitativo cantado cada bloque del Símbolo (Padre / Hijo / Espíritu Santo e Iglesia) y toda la asamblea ratifica con una breve aclamación («Creo, Señor» o «Creemos, Señor»), siempre que el texto proclamado sea el símbolo íntegro.",
            },
        ],
        "checklist_discernimiento": [
            {
                "id": "chk-cre-1",
                "pregunta": "¿El texto es íntegramente el Símbolo Niceno-Constantinopolitano o el Símbolo de los Apóstoles del Misal Romano?",
                "pista": "IGMR 67–68.",
            },
            {
                "id": "chk-cre-2",
                "pregunta": "¿Se prevé la pausa o inflexión musical para la inclinación profunda en «y por obra del Espíritu Santo se encarnó de María, la Virgen, y se hizo hombre»?",
                "pista": "Gesto corporal prescrito por el Misal Romano.",
            },
        ],
    },

    # =========================================================================
    # 9. ORACIÓN UNIVERSAL (ORATIO UNIVERSALIS / ORACIÓN DE LOS FIELES)
    # =========================================================================
    "oracion-universal": {
        "slug": "oracion-universal",
        "titulo": "Oración Universal (Respuesta de los Fieles)",
        "nombre_latino": "Oratio universalis / Oratio fidelium",
        "parte_nombre": "II. Liturgia de la Palabra",
        "cita_principal": "IGMR 69–71 · MS 29–30",
        "subtitulo": "La súplica sacerdotal con que la asamblea bautismal, iluminada por la Palabra escuchada, intercede por la Iglesia, el mundo, los que sufren y la comunidad local.",
        "ficha_identidad": [
            {
                "id": "oru-naturaleza",
                "atributo": "Naturaleza Litúrgica",
                "valor": "Oración dialogada de conclusión de la Liturgia de la Palabra",
                "detalle": "Es el fruto inmediato de la escucha de la Palabra: el pueblo responde a Dios ejerciendo el oficio de su sacerdocio bautismal para interceder por la salvación de todos (1 Tim 2, 1-2).",
            },
            {
                "id": "oru-actores",
                "atributo": "Actores y Jerarquía de Ministerios (IGMR 71)",
                "valor": "Sacerdote (Invitación y Oración final) + Diácono/Lector (Intenciones) + Asamblea (Respuesta)",
                "detalle": "Al sacerdote celebrante le corresponde dirigir la oración desde la sede (introducción y conclusión); el diácono (o en su defecto un cantor o lector desde el ambón) propone las intenciones, y el pueblo hace suya la súplica cantando una invocación común.",
            },
            {
                "id": "oru-orden",
                "atributo": "Orden de las 4 Intenciones (IGMR 70)",
                "valor": "1) Por la Iglesia · 2) Por los gobernantes y el mundo · 3) Por los que sufren · 4) Por la comunidad local",
                "detalle": "Esta secuencia católica (universal) abre el corazón de la asamblea desde el horizonte de toda la Iglesia y la humanidad hasta las necesidades concretas de la parroquia.",
            },
            {
                "id": "oru-grado",
                "atributo": "Grado de Participación",
                "valor": "Primer / Segundo Grado (MS 29–30)",
                "detalle": "Cantar la breve respuesta de la Oración de los Fieles toma apenas dos segundos por petición y transforma radicalmente la intensidad orante de este momento.",
            },
        ],
        "opciones_igmr": [
            {
                "numero": "Modo 1 (Respuesta cantada a cada intención)",
                "titulo": "Intención leída o cantada + Respuesta cantada por la Asamblea",
                "descripcion": "El diácono o lector proclama cada intención y termina con «Roguemos al Señor»; el cantor/coro y toda la asamblea responden cantando «Escúchanos, Señor, te rogamos» o «Kýrie, eléison».",
            },
            {
                "numero": "Modo 2 (Diácono/Cantor + Pueblo todo cantado)",
                "titulo": "Intenciones salmodiadas por el Diácono o Cantor + Respuesta cantada",
                "descripcion": "En las grandes solemnidades, el diácono o el cantor entona las intenciones en tono recitativo de letanía y el pueblo responde cantando en la misma tonalidad.",
            },
        ],
        "textos_oficiales": {
            "titulo": "Respuestas Oficiales del Misal Romano para la Oración Universal",
            "nota": "La respuesta debe ser brevísima (un solo compás o frase de 2 a 4 segundos) y dirigirse siempre a Dios Padre o a Cristo Señor.",
            "items": [
                {
                    "ocasion": "Respuestas Clásicas del Misal Romano",
                    "latin": "V/. Orémus ad Dóminum. R/. Te rogámus, audi nos. / R/. Kýrie, eléison. / R/. Exáudi nos, Dómine.",
                    "espanol": "V/. Roguemos al Señor.\nR/. «Te rogamos, óyenos.» / «Escúchanos, Señor, te rogamos.» / «Señor, ten piedad.»",
                },
                {
                    "ocasion": "Respuestas Propias por Tiempo Litúrgico",
                    "latin": "Adviento: Veni, Domine Iesu! · Pascua: Victor Rex, audi nos!",
                    "espanol": "Adviento: «¡Ven, Señor Jesús!» · Cuaresma: «Ten piedad de tu pueblo, Señor.» · Pascua: «¡Cristo resucitado, escúchanos!» / «Por tu resurrección, óyenos, Señor.»",
                },
            ],
        },
        "semaforo": {
            "verde": [
                {
                    "titulo": "Brevedad y sobriedad de la respuesta cantada",
                    "texto": "Una respuesta de 2 a 4 compases («Escúchanos, Señor, te rogamos» a una o cuatro voces) une a toda la iglesia sin alargar ni enfriar el ritmo de las peticiones.",
                },
                {
                    "titulo": "Mantener el acorde base muy suave en órgano o guitarra",
                    "texto": "Dar discretamente la nota de entrada al final del «Roguemos al Señor» permite que la asamblea entre a cantar sin vacilar en cada una de las 4 o 5 peticiones.",
                },
            ],
            "amarillo": [
                {
                    "titulo": "Viernes Santo: La Gran Oración Universal Solemne",
                    "texto": "El Viernes Santo conserva la forma más antigua de la Oración Universal (10 grandes intenciones con invitación diaconal a arrodillarse o permanecer en silencio antes de la colecta presidencial).",
                },
            ],
            "rojo": [
                {
                    "titulo": "Cantar una estrofa larga entre cada petición",
                    "texto": "Intercalar estribillos de 20 o 30 segundos después de cada intención rompe la unidad de la Oración de los Fieles y agota a la asamblea.",
                },
            ],
        },
        "adaptacion_tiempos": {
            "Todo el Año": {
                "espiritu": "Ejercicio del sacerdocio común de los bautizados intercediendo por la salvación del mundo entero.",
                "textos_sugeridos": "«Te rogamos, óyenos», «Escúchanos, Señor, te rogamos», «Kýrie, eléison».",
                "criterio_musical": "Motivo melódico de 2 compases, diatónico, en registro medio (Mi4–La4), opcionalmente armonizado a 4 voces por el coro.",
            },
        },
        "tratado_teologico": [
            {
                "id": "oracion-universal-historia",
                "titulo": "1. Teología e Historia: El Sacerdocio Bautismal y la Restauración Conciliar (SC 53)",
                "parrafos": [
                    "Ya en el año 155 d.C., San Justino Mártir describía en su Apología I (cap. 65 y 67) que, apenas concluida la lectura de las memorias de los Apóstoles y la exhortación del presidente, «todos nos levantamos a una y elevamos nuestras preces en común por nosotros mismos y por todos los demás dondequiera que estén». En la antigüedad, esta oración marcaba la despedida de los catecúmenos: solo quienes habían sido incorporados a Cristo por el Bautismo permanecían en el templo para ejercer su ministerio de intercesión sacerdotal antes de presentar las ofrendas en el altar.",
                    "Tras haber desaparecido de la Misa romana ordinaria después del siglo VI (quedando como único vestigio el «Oremos» solitario del sacerdote antes del Ofertorio y las Grandes Oraciones del Viernes Santo), el Concilio Vaticano II (Sacrosanctum Concilium, n. 53) restauró la Oración Universal u Oración de los Fieles como sello de la Liturgia de la Palabra y puente hacia la Liturgia Eucarística.",
                ],
            },
        ],
        "citas_magisteriales": [
            {
                "id_cita": "igmr-69-71",
                "doc_id": "igmr",
                "fuente": "Instrucción General del Misal Romano (IGMR)",
                "numeral": "nn. 69–71",
                "año": "2002 / Tercera Edición Típica",
                "url_oficial": "https://www.vatican.va/roman_curia/congregations/ccdds/documents/rc_con_ccdds_doc_20030317_ordinamento-messale_sp.html#C._Liturgia_de_la_Palabra",
                "texto": "«En la oración universal u oración de los fieles, el pueblo responde de alguna manera a la Palabra de Dios recibida en la fe y, ejercitando el oficio de su sacerdocio bautismal, ofrece súplicas a Dios por la salvación de todos... Las intenciones se proclaman desde el ambón o desde otro lugar conveniente, por el diácono o por un cantor o un lector, o por un fiel laico. El pueblo, por su parte, de pie, expresa su súplica, o con una invocación común después de proclamada cada intención, o bien orando en silencio.»",
                "comentario_pastoral": "Destaca que el diácono o un cantor puede proclamar las intenciones y el pueblo responde con una invocación común cantada.",
            },
        ],
        "criterios_musicales": [
            {
                "id": "oru-crit-1",
                "categoria": "Diseño de la Respuesta Cantada",
                "titulo": "Concisión absoluta (4 a 8 sílabas) y cadencia conclusiva cálida",
                "explicacion": "La respuesta debe tener un ritmo verbal idéntico al hablado («Te ro-ga-mos, ó-ye-nos» o «Es-cú-cha-nos, Se-ñor») sobre una cadencia plagal (IV–I) o auténtica suave que invite a la interioridad.",
            },
        ],
        "checklist_discernimiento": [
            {
                "id": "chk-oru-1",
                "pregunta": "¿La respuesta cantada dura entre 2 y 5 segundos para mantener vivo el ritmo del diálogo entre el lector y la asamblea?",
                "pista": "IGMR 71.",
            },
            {
                "id": "chk-oru-2",
                "pregunta": "¿El lector de las peticiones sabe cuál es el texto exacto de la respuesta que se va a cantar para anunciarlo al inicio?",
                "pista": "Coordinación previa entre el lector y el director del coro.",
            },
        ],
    },
}
