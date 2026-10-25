"""
Base de conocimiento exhaustiva de los 16 momentos de la Santa Misa (Parte 2: Momentos 10 al 16).
Incluye Liturgia Eucarística y Rito de Conclusión:
10. Presentación de los Dones (Ofertorio)
11. Santo (Sanctus)
12. Aclamación Memorial y Gran Amén
13. Padre Nuestro y Doxología
14. Cordero de Dios (Agnus Dei)
15. Canto de Comunión y Acción de Gracias
16. Canto de Salida / Envío (Recessus)
"""

from typing import Dict, Any

MOMENTOS_PARTE_2: Dict[str, Dict[str, Any]] = {
    # =========================================================================
    # 10. PRESENTACIÓN DE LOS DONES / OFERTORIO (CANTUS AD OFFERTORIUM)
    # =========================================================================
    "presentacion-dones": {
        "slug": "presentacion-dones",
        "titulo": "Presentación de los Dones (Ofertorio)",
        "nombre_latino": "Cantus ad Offertorium / Praeparatio donorum",
        "parte_nombre": "III. Liturgia Eucarística",
        "cita_principal": "IGMR 73–74 · MS 31",
        "subtitulo": "El canto procesional que acompaña el traslado del pan, el vino y las ofrendas para los pobres hacia el altar, mientras el sacerdote prepara la mesa del sacrificio.",
        "ficha_identidad": [
            {
                "id": "ofe-naturaleza",
                "atributo": "Naturaleza Litúrgica",
                "valor": "Canto del Propio (Variable y Facultativo)",
                "detalle": "Acompaña la procesión y preparación de los dones. A diferencia de la Entrada o la Comunión, la IGMR 74 contempla explícitamente la opción de no cantar en voz alta para permitir que el sacerdote pronuncie en voz alta las hermosas bendiciones berakhot («Bendito seas, Señor, Dios del universo...»).",
            },
            {
                "id": "ofe-funcion",
                "atributo": "Función Ritual",
                "valor": "Procesional / Acompaña la preparación del altar y de las ofrendas",
                "detalle": "Acompaña la procesión de los fieles que llevan el pan, el vino y los dones para la Iglesia y los pobres, la colocación de los corporales y la eventual incensación de las ofrendas, de la cruz, del altar, del sacerdote y del pueblo.",
            },
            {
                "id": "ofe-ejecucion",
                "atributo": "Cuatro Modos Legítimos en este Momento (IGMR 74, 142)",
                "valor": "1) Canto Asamblea/Coro · 2) Solo el Coro (polifonía) · 3) Música instrumental · 4) Bendición en voz alta + Respuesta",
                "detalle": "Es el momento por excelencia donde la schola o coro puede interpretar un motete polifónico a voces solas, o el organista/instrumentistas tocar una pieza sacra meditativa.",
            },
            {
                "id": "ofe-postura",
                "atributo": "Postura Corporal (IGMR 43)",
                "valor": "Sentados (poniéndose de pie a la invitación «Oren, hermanos...»)",
                "detalle": "Los fieles permanecen sentados durante la presentación de los dones y se levantan cuando el sacerdote dice «Oren, hermanos, para que este sacrificio, mío y de ustedes...».",
            },
            {
                "id": "ofe-duracion",
                "atributo": "Inicio y Término Exacto",
                "valor": "Inicia al comenzar la procesión/preparación · Termina antes de «Oren, hermanos»",
                "detalle": "Se prolonga «por lo menos hasta que los dones han sido depositados sobre el altar» (IGMR 74) o hasta concluir la incensación del pueblo y el lavabo de manos.",
            },
            {
                "id": "ofe-terminologia",
                "atributo": "Precisión Teológica del Nombre",
                "valor": "«Preparación de los Dones» (no anticipar verbalmente la Consagración)",
                "detalle": "El verdadero ofrecimiento sacrificial de Cristo al Padre ocurre dentro de la Plegaria Eucarística después de la Consagración («Unde et memores... te ofrecemos el Pan de vida y el Cáliz de salvación»). Aquí presentamos los dones de la creación y de nuestro trabajo para que sean consagrados.",
            },
        ],
        "opciones_igmr": [
            {
                "numero": "Opción 1 (Antífona con Salmo)",
                "titulo": "Antífona del Graduale Romanum o del Graduale Simplex",
                "descripcion": "Canto de la antífona de ofertorio tradicional del día según el Graduale Romanum o el Graduale Simplex (IGMR 74 remite a las 4 opciones de IGMR 48).",
            },
            {
                "numero": "Opción 2 (Canto Congregacional o Coral)",
                "titulo": "Otro canto congruente con el rito y el tiempo litúrgico",
                "descripcion": "Un canto aprobado de presentación de dones, de alabanza por la creación y el trabajo, o un motete coral propio del Tiempo Litúrgico (incluso cuando no haya procesión de ofrendas por la nave).",
            },
            {
                "numero": "Opción 3 (Música Instrumental o Silencio)",
                "titulo": "Pieza de órgano / instrumentos admitidos o silencio meditativo",
                "descripcion": "Especialmente fecundo para descansar la voz de la asamblea tras la Liturgia de la Palabra y prepararla para cantar con toda su fuerza el Diálogo del Prefacio y el Santo.",
            },
            {
                "numero": "Opción 4 (Diálogo «Bendito seas por siempre, Señor»)",
                "titulo": "Oraciones de presentación en voz alta por el Sacerdote (IGMR 142)",
                "descripcion": "Si no hay canto de ofertorio ni toca el órgano, el sacerdote dice en voz alta las dos bendiciones sobre el pan y el vino, y todo el pueblo aclama (o canta): «Bendito seas por siempre, Señor».",
            },
        ],
        "textos_oficiales": {
            "titulo": "Fórmulas Litúrgicas de la Preparación de los Dones y Antífonas Clásicas",
            "nota": "Si el coro NO canta durante la presentación del pan y el vino, puede musicalizar la respuesta del pueblo «Bendito seas por siempre, Señor» a las oraciones del sacerdote (IGMR 142).",
            "items": [
                {
                    "ocasion": "Diálogo cuando no hay canto de Ofertorio (IGMR 142)",
                    "latin": "V/. Benedictus es, Domine, Deus universi, quia de tua largitate accepimus panem (vinum)...\nR/. Benedictus Deus in saecula.",
                    "espanol": "V/. Bendito seas, Señor, Dios del universo, por este pan (vino), fruto de la tierra (de la vid) y del trabajo del hombre, que recibimos de tu generosidad y ahora te presentamos; él será para nosotros pan de vida (bebida de salvación).\nR/. «Bendito seas por siempre, Señor.»",
                },
                {
                    "ocasion": "Jueves Santo · Misa Vespertina de la Cena del Señor",
                    "latin": "Ubi cáritas et amor, Deus ibi est. Congregávit nos in unum Christi amor...",
                    "espanol": "«Donde hay caridad y amor, allí está Dios. Nos congregó y nos unió el amor de Cristo...» (Himno propio prescrito por el Misal Romano para la procesión de dones del Jueves Santo).",
                },
                {
                    "ocasion": "Antífona del Graduale Romanum · Domingo de Pentecostés (Sal 67, 29-30)",
                    "latin": "Confirma hoc, Deus, quod operatus es in nobis: a templo tuo, quod est in Ierusalem, tibi offerent reges munera, alleluia.",
                    "espanol": "«Confirma, oh Dios, lo que has realizado en nosotros; desde tu santo templo en Jerusalén, los reyes te ofrecerán dones, aleluya.»",
                },
            ],
        },
        "semaforo": {
            "verde": [
                {
                    "titulo": "Distinguir entre presentar el pan y el vino y la Consagración futura",
                    "texto": "Los buenos textos de presentación de dones hablan del fruto de la tierra, de la vid y del trabajo humano que ponemos en las manos de Dios para que Él los transforme («él será para nosotros pan de vida»), o bien son salmos de alabanza y entrega de la propia vida (Rom 12, 1).",
                },
                {
                    "titulo": "Aprovechar este momento para la polifonía coral, el instrumento solista o el silencio",
                    "texto": "No es obligatorio que toda la asamblea cante a plena voz en el ofertorio todos los domingos: dejar que aquí cante solo el coro a voces, o toque una cuerda/órgano suave, permite que la asamblea reserve su energía vocal para el Santo (que sí es de Primer Grado).",
                },
                {
                    "titulo": "Terminar puntualmente cuando el sacerdote se lava las manos",
                    "texto": "El canto debe concluir apenas el sacerdote regresa al centro del altar tras el lavabo («Lávame, Señor, de mis culpas...») para no retrasar el «Oren, hermanos».",
                },
            ],
            "amarillo": [
                {
                    "titulo": "En Cuaresma: prohibido tocar instrumentos solos sin canto (IGMR 313)",
                    "texto": "Mientras en Tiempo Ordinario, Navidad o Pascua es hermoso tocar una pieza instrumental de órgano o violín en el ofertorio, en Cuaresma los instrumentos solo pueden sonar para sostener el canto. Si no se canta en Cuaresma, se guarda silencio o el sacerdote dice en voz alta el «Bendito seas, Señor».",
                },
            ],
            "rojo": [
                {
                    "titulo": "Textos que hablan como si el pan y el vino YA estuvieran consagrados",
                    "texto": "Evitar cantos de ofertorio que dicen 'aquí en el altar ya está el Cuerpo y la Sangre del Señor' antes de la Plegaria Eucarística: la transubstanciación ocurre en la Consagración, no en el ofertorio.",
                },
                {
                    "titulo": "Reducir todo el repertorio a 'Te ofrecemos este pan y este vino'",
                    "texto": "En el Graduale Romanum ningún canto de ofertorio describe literalmente el pan y el vino materiales: todos son grandes salmos que prolongan el misterio del día o el Evangelio recién proclamado. Reducir los 52 domingos del año a tres canciones de 'pan y vino' empobrece enormemente la liturgia.",
                },
                {
                    "titulo": "Tapar con el canto el «Bendito seas, Señor» dicho en voz alta por el sacerdote",
                    "texto": "La IGMR 142 prohíbe expresamente la superposición: si hay canto de ofertorio, el sacerdote reza las oraciones de presentación en secreto; solo si NO hay canto las pronuncia en voz alta.",
                },
            ],
        },
        "adaptacion_tiempos": {
            "Tiempo Ordinario": {
                "espiritu": "Entrega del trabajo semanal, de la creación y de la propia existencia en unión con Cristo.",
                "textos_sugeridos": "Salmos de acción de gracias y confianza (Sal 115 '¿Cómo pagaré al Señor todo el bien que me ha hecho?', Sal 137 'Te doy gracias, Señor, de todo corazón', Oración de San Ignacio 'Tomad, Señor, y recibid').",
                "criterio_musical": "Sereno, lírico y contemplativo; ideal para alternar coro a voces o intervención instrumental.",
            },
            "Adviento y Navidad": {
                "espiritu": "En Adviento: la tierra que se abre para recibir al Salvador (Sal 84). En Navidad: los dones de los pastores y de los Magos de Oriente (Sal 71).",
                "textos_sugeridos": "Adviento: «Ave Maria» (Lc 1, 28, antífona propia del IV Domingo de Adviento). Navidad/Epifanía: «Los reyes de Tarsis y de las islas le ofrecerán dones» (Sal 71), villancicos contemplativos de adoración.",
                "criterio_musical": "Recogido y transparente en Adviento; luminoso y cálido en Navidad.",
            },
            "Cuaresma y Semana Santa": {
                "espiritu": "El sacrificio verdadero es un espíritu quebrantado y un corazón contrito (Sal 50, 19; Dan 3, 39-40).",
                "textos_sugeridos": "Oración de Azarías (Dan 3, 39-40: «Con espíritu humilde y corazón contrito seamos recibidos por ti, Señor»), y en Jueves Santo el himno «Ubi caritas et amor».",
                "criterio_musical": "En Cuaresma: motete coral a cappella, canto sobrio o silencio con respuesta cantada al «Bendito seas por siempre, Señor».",
            },
            "Tiempo Pascual": {
                "espiritu": "La creación renovada por la Resurrección del Señor.",
                "textos_sugeridos": "Salmos pascuales con Aleluya (Sal 65, Sal 117) o himnos pascuales.",
                "criterio_musical": "Luminoso y festivo.",
            },
        },
        "tratado_teologico": [
            {
                "id": "ofertorio-teologia-ireneo",
                "titulo": "1. Teología Patrística de los Dones: San Ireneo y las Primicias de la Creación",
                "parrafos": [
                    "Ya en el siglo II, San Ireneo de Lyon (Adversus Haereses IV, 17-18) defendió contra el dualismo gnóstico la bondad de la creación material señalando precisamente la presentación del pan y del vino en la Eucaristía: al llevar al altar los frutos de la tierra y del cultivo humano, la Iglesia proclama que el Creador del cosmos y el Padre de Jesucristo son el mismo Dios. Y San Agustín añadía a los neófitos en la noche de Pascua un pensamiento de hondura sobrecogedora: «Allí sobre la mesa del Señor están ustedes mismos: ustedes son el grano que fue molido por el ayuno y el exorcismo, amasado con el agua del Bautismo y cocido con el fuego del Espíritu Santo. Sean lo que ven y reciban lo que son» (Sermón 272).",
                    "La reforma litúrgica del Vaticano II (IGMR 73–74) enriqueció este momento recuperando las dos oraciones de bendición inspiradas en la berakhah judía de la mesa («Bendito seas, Señor, Dios del universo...»). En ellas se expresa la teología exacta de la Praeparatio donorum: no ofrecemos a Dios algo que Él necesite, sino que le devolvemos con gratitud lo que primero «recibimos de tu generosidad» para que, por la acción del Espíritu Santo en la Plegaria Eucarística, llegue a ser para nosotros el Cuerpo y la Sangre de Cristo.",
                ],
            },
            {
                "id": "ofertorio-historia-procesion",
                "titulo": "2. Historia Litúrgica: De la Procesión de Ofrendas de San Agustín al Motete Polifónico",
                "parrafos": [
                    "El canto de Ofertorio fue introducido en el norte de África en tiempos de San Agustín (quien en su tratado Retractationes II, 11 cuenta que defendió con un libro entero la nueva costumbre de cantar himnos del Libro de los Salmos mientras el pueblo llevaba sus ofrendas al altar en Cartago). En la Roma antigua (Ordo Romanus I), toda la asamblea —encabezada por la nobleza, los hombres y las mujeres— se acercaba procesionalmente a entregar panes (coronae) y ánforas de vino, no solo para la comunión del día sino para el sustento de los pobres y huérfanos de la ciudad, mientras la schola cantaba un salmo responsorial de gran riqueza melismática.",
                    "Cuando a partir del siglo XI desapareció la procesión general de los fieles con panes naturales y se introdujo el pan ácimo ya preparado en la credencia, el salmo del ofertorio perdió sus versículos y quedó solo la antífona breve; ese espacio temporal fue ocupado entonces por el órgano (versets de órgano) o por el motete polifónico renacentista y barroco (como los grandes Offertoria de Palestrina). La IGMR 74 actual integra armónicamente toda esta historia: permite el canto procesional con la asamblea, el canto coral, la música de órgano o la proclamación en voz alta de las bendiciones presidenciales.",
                ],
            },
        ],
        "citas_magisteriales": [
            {
                "id_cita": "igmr-73-74",
                "doc_id": "igmr",
                "fuente": "Instrucción General del Misal Romano (IGMR)",
                "numeral": "nn. 73–74",
                "año": "2002 / Tercera Edición Típica",
                "url_oficial": "https://www.vatican.va/roman_curia/congregations/ccdds/documents/rc_con_ccdds_doc_20030317_ordinamento-messale_sp.html#D._Liturgia_eucarística",
                "texto": "«Al comienzo de la Liturgia eucarística se llevan al altar los dones que se convertirán en el Cuerpo y la Sangre de Cristo... Es laudable que el pan y el vino sean presentados por los fieles... El canto de preparación de los dones acompaña la procesión en que se llevan los dones y se prolonga por lo menos hasta que los dones han sido depositados sobre el altar. Las normas sobre el modo de cantar son las mismas que para el canto de entrada (n. 48). El canto puede asociarse siempre al rito para la preparación de los dones, incluso sin la procesión con los dones.»",
                "comentario_pastoral": "Aclara que los dones 'se convertirán' (futuro) en el Cuerpo y la Sangre de Cristo y que el canto es válido incluso cuando no hay procesión por el pasillo.",
            },
            {
                "id_cita": "igmr-142",
                "doc_id": "igmr",
                "fuente": "Instrucción General del Misal Romano (IGMR)",
                "numeral": "n. 142",
                "año": "2002 / Tercera Edición Típica",
                "url_oficial": "https://www.vatican.va/roman_curia/congregations/ccdds/documents/rc_con_ccdds_doc_20030317_ordinamento-messale_sp.html",
                "texto": "«Si no se realiza el canto de preparación de los dones ni se toca el órgano, en la presentación del pan y del vino el sacerdote puede decir en voz alta las fórmulas de bendición, a las cuales el pueblo aclama: Bendito seas por siempre, Señor.»",
                "comentario_pastoral": "Regla de oro contra la superposición: si hay canto o música instrumental, el sacerdote dice las fórmulas en voz secreta; si hay silencio, las dice en voz alta.",
            },
        ],
        "criterios_musicales": [
            {
                "id": "ofe-crit-1",
                "categoria": "Economía Energética dentro de la Misa",
                "titulo": "Preparar el oído y la voz para la cumbre de la Plegaria Eucarística",
                "explicacion": "En una buena arquitectura musical de la Misa, el Ofertorio actúa como un valle de serenidad lírica entre la cima de la Liturgia de la Palabra (Evangelio y Credo) y la cima suprema de la Plegaria Eucarística (Prefacio y Sanctus). Un canto de ofertorio estridente o demasiado largo resta frescura e impacto al Santo que vendrá un minuto después.",
            },
        ],
        "checklist_discernimiento": [
            {
                "id": "chk-ofe-1",
                "pregunta": "¿El texto respeta la verdad teológica del momento (presentación de dones que SERÁN transformados, alabanza o entrega espiritual) sin hablar como si ya hubiera ocurrido la Consagración?",
                "pista": "IGMR 73.",
            },
            {
                "id": "chk-ofe-2",
                "pregunta": "¿Su duración se ajusta al tiempo real de la preparación del altar (e incensación, si la hay) para terminar antes del «Oren, hermanos»?",
                "pista": "IGMR 74.",
            },
            {
                "id": "chk-ofe-3",
                "pregunta": "Si hoy no se canta en el ofertorio, ¿está preparado el coro/pueblo para responder (o cantar) «Bendito seas por siempre, Señor» a las bendiciones del sacerdote?",
                "pista": "IGMR 142.",
            },
        ],
    },

    # =========================================================================
    # 11. SANTO (SANCTUS, SANCTUS, SANCTUS)
    # =========================================================================
    "santo": {
        "slug": "santo",
        "titulo": "Santo (Sanctus)",
        "nombre_latino": "Sanctus, Sanctus, Sanctus & Benedictus",
        "parte_nombre": "III. Liturgia Eucarística",
        "cita_principal": "IGMR 79b, 148 · MS 29 (Primer Grado)",
        "subtitulo": "El himno seráfico y mesiánico de Primer Grado con el que toda la asamblea terrena, unida al sacerdote y a los coros de los ángeles, irrumpe en la liturgia del Cielo dentro de la Plegaria Eucarística.",
        "ficha_identidad": [
            {
                "id": "san-naturaleza",
                "atributo": "Naturaleza Litúrgica (IGMR 79b)",
                "valor": "Canto del Ordinario · Parte integrante de la misma Plegaria Eucarística",
                "detalle": "No es un canto externo que interrumpe la oración del sacerdote, sino la primera gran intervención de toda la iglesia dentro de la Anáfora o Plegaria Eucarística.",
            },
            {
                "id": "san-grado",
                "atributo": "Prioridad Normativa",
                "valor": "PRIMER GRADO de Participación (Musicam Sacram, n. 29)",
                "detalle": "Es el canto congregacional más importante de toda la Misa junto con las respuestas y el Gran Amén. Si en una Misa solo pudiera cantarse una pieza en absoluto, esa pieza debe ser el Santo.",
            },
            {
                "id": "san-protagonista",
                "atributo": "Protagonista Obligatorio (IGMR 79b, 148)",
                "valor": "TODO EL PUEBLO juntamente con el Sacerdote (nunca el coro solo)",
                "detalle": "Musicam Sacram 34 e IGMR 79b establecen que el Santo jamás puede ser reservado exclusivamente al coro polifónico dejando callada a la asamblea: debe ser cantado por todos.",
            },
            {
                "id": "san-texto",
                "atributo": "Invariabilidad Absoluta del Texto",
                "valor": "Texto bíblico-litúrgico estricto (Isaías 6, 3 + Mateo 21, 9)",
                "detalle": "Está terminantemente prohibido alterar, recortar, parafrasear o añadir estrofas ajenas al texto oficial del Misal Romano (Redemptionis Sacramentum, n. 53).",
            },
            {
                "id": "san-postura",
                "atributo": "Postura Corporal (IGMR 43)",
                "valor": "De pie (arrodillándose al terminar el Santo para la Epíclesis y Consagración)",
                "detalle": "Toda la asamblea canta el Santo de pie, en actitud de alabanza celestial, y se arrodilla al concluir el «Hosanna en el cielo» cuando el sacerdote extiende las manos sobre las ofrendas.",
            },
        ],
        "opciones_igmr": [
            {
                "numero": "Regla Única de Texto",
                "titulo": "Texto literal e íntegro del Misal Romano (Sanctus + Benedictus sin cortes)",
                "descripcion": "Desde la reforma de San Pío X y del Concilio Vaticano II, el Sanctus y el Benedictus forman una sola unidad indivisible que se canta completa inmediatamente después de la conclusión del Prefacio, antes de que el sacerdote inicie la Epíclesis.",
            },
            {
                "numero": "Continuidad Modal con el Prefacio",
                "titulo": "Enlace directo con el Diálogo y el Prefacio cantado por el Sacerdote",
                "descripcion": "Cuando el sacerdote canta el Diálogo inicial («El Señor esté con ustedes / Levantemos el corazón / Demos gracias al Señor, nuestro Dios») y el Prefacio, el Santo brota sin interrupción de las últimas palabras del sacerdote («...cantamos sin cesar el himno de tu gloria: Santo, Santo, Santo...»).",
            },
        ],
        "textos_oficiales": {
            "titulo": "Texto Oficial Íntegro del Sanctus (Diálogo del Prefacio + Sanctus + Benedictus)",
            "nota": "El himno une la visión del profeta Isaías en el Templo celestial (Is 6, 3; Ap 4, 8) con la aclamación mesiánica de la entrada de Jesús en Jerusalén (Sal 117, 26; Mt 21, 9).",
            "items": [
                {
                    "ocasion": "Diálogo Inicial del Prefacio (Primer Grado · IGMR 147)",
                    "latin": "V/. Dóminus vobíscum. R/. Et cum spíritu tuo.\nV/. Sursum corda. R/. Habémus ad Dóminum.\nV/. Grátias agámus Dómino Deo nostro. R/. Dignum et iustum est.",
                    "espanol": "V/. El Señor esté con ustedes. R/. Y con tu espíritu.\nV/. Levantemos el corazón. R/. Lo tenemos levantado hacia el Señor.\nV/. Demos gracias al Señor, nuestro Dios. R/. Es justo y necesario.",
                },
                {
                    "ocasion": "I. El Trisagio Seráfico (Isaías 6, 3 · Apocalipsis 4, 8)",
                    "latin": "Sanctus, Sanctus, Sanctus Dóminus Deus Sábaoth. Pleni sunt cæli et terra glória tua. Hosánna in excélsis.",
                    "espanol": "Santo, Santo, Santo es el Señor, Dios del Universo. Llenos están el cielo y la tierra de tu gloria. Hosanna en el cielo.",
                },
                {
                    "ocasion": "II. Aclamación Mesiánica (Salmo 117, 26 · Mateo 21, 9)",
                    "latin": "Benedíctus qui venit in nómine Dómini. Hosánna in excélsis.",
                    "espanol": "Bendito el que viene en nombre del Señor. Hosanna en el cielo.",
                },
            ],
        },
        "semaforo": {
            "verde": [
                {
                    "titulo": "Letra 100 % idéntica al Misal Romano",
                    "texto": "Verificar las seis frases exactas: 1) Santo, Santo, Santo es el Señor, Dios del Universo; 2) Llenos están el cielo y la tierra de tu gloria; 3) Hosanna en el cielo; 4) Bendito el que viene en nombre del Señor; 5) Hosanna en el cielo.",
                },
                {
                    "titulo": "Entrar inmediatamente después de «...cantamos sin cesar el himno de tu gloria»",
                    "texto": "El organista o guitarrista debe tener el acorde listo durante las últimas líneas del Prefacio para que no haya un bache de silencio ni una introducción larga: el Santo continúa la frase misma del sacerdote.",
                },
                {
                    "titulo": "Grandeza, solemnidad y participación unánime",
                    "texto": "La melodía debe ser majestuosa, radiante y cantada a plena voz por toda la iglesia, con las cuatro voces del coro (SATB) sosteniendo la armonía.",
                },
            ],
            "amarillo": [
                {
                    "titulo": "Repeticiones musicales legítimas dentro del texto oficial",
                    "texto": "Por razones estrictamente musicales de fraseo simétrico, es legítimo repetir «Hosanna, hosanna en el cielo» o las palabras del propio texto oficial, siempre que no se agreguen palabras inventadas ni se suprima ninguna frase del Misal.",
                },
            ],
            "rojo": [
                {
                    "titulo": "Los falsos 'Santos' con letra alterada ('Santo dicen los querubines', 'Santo porque mi Dios es santo')",
                    "texto": "En Chile y Latinoamérica se popularizaron canciones llamadas 'Santo de los querubines', 'Santo marinera' o paráfrasis que omiten 'Llenos están el cielo y la tierra' o agregan 'porque mi Dios es grande'. Su uso está prohibido porque alteran la Plegaria Eucarística misma.",
                },
                {
                    "titulo": "Dejar el Santo rezado en una Misa donde sí se cantaron otros cantos",
                    "texto": "Si hay coro o cantor en la Misa, dejar rezado el Santo mientras sí se cantó el Ofertorio invierte por completo la jerarquía de Musicam Sacram (n. 29).",
                },
            ],
        },
        "adaptacion_tiempos": {
            "Todos los Tiempos Litúrgicos": {
                "espiritu": "El Santo se canta en TODAS las Misas de todos los tiempos del año (incluida la Cuaresma y las Misas de Difuntos).",
                "textos_sugeridos": "Texto único e invariable del Misal Romano.",
                "criterio_musical": "Conviene que la parroquia tenga 2 o 3 musicalizaciones oficiales del Santo según el tiempo litúrgico: uno muy solemne y festivo para Navidad y Pascua, uno luminoso para los domingos del Tiempo Ordinario, y uno más sobrio o modal (como el Sanctus XVIII gregoriano o versión modal en español) para Adviento y Cuaresma.",
            },
        },
        "tratado_teologico": [
            {
                "id": "santo-teologia-cosmica",
                "titulo": "1. Teología Cósmica del Sanctus: El Cielo y la Tierra en una sola Liturgia",
                "parrafos": [
                    "El canto del Sanctus es el instante en que se rasga el velo entre la Iglesia peregrina en la tierra y la Jerusalén celestial (cf. Heb 12, 22; Ap 4, 8). En la visión inaugural del profeta Isaías en el Templo (Is 6, 1-3), los serafines de seis alas clamaban el uno al otro: «Qādôš, Qādôš, Qādôš YHWH Ṣĕbā’ôt, mĕlō’ kol-hā’āreṣ kĕbôdô» ('Santo, Santo, Santo es el Señor de los Ejércitos; toda la tierra está llena de su gloria'). En la gramática hebrea, la triple repetición de un adjetivo constituye el grado superlativo absoluto (el Tres Veces Santo, la Trascendencia infinita de Dios), en la cual los Padres de la Iglesia contemplaron desde el principio el misterio de la Santísima Trinidad.",
                    "Pero la liturgia cristiana introduce dos transformaciones admirables respecto al texto de Isaías: primero, dice «llenos están EL CIELO Y la tierra de tu gloria» (porque en Cristo resucitado la alabanza abarca todo el cosmos visible e invisible); y segundo, añade el «Benedictus qui venit in nomine Domini. Hosanna in excelsis» (Sal 117, 26; Mt 21, 9). Así, el Dios infinitamente trascendente ante quien los serafines se cubren el rostro ('Santo, Santo, Santo') es reconocido como el Emmanuel cercano que viene a nosotros bajo las especies sacramentales del pan y del vino ('Bendito el que viene en nombre del Señor').",
                ],
            },
            {
                "id": "santo-historia-liturgia",
                "titulo": "2. Antigüedad Apostólica y Patrística del Sanctus en la Anáfora",
                "parrafos": [
                    "Después del Salmo y del Aleluya, el Sanctus es la aclamación más antigua de la Eucaristía: ya hacia el año 96 d.C., el Papa San Clemente Romano alude a él en su Primera Carta a los Corintios (cap. 34, 6), exhortando a la asamblea a «reunirse en concordia para clamar como de una sola boca» el himno de los ángeles.En el siglo IV está atestiguado en todas las grandes familias litúrgicas de Oriente y Occidente (Anáfora de Serapión en Egipto, Catequesis Mistagógicas de San Cirilo de Jerusalén, Constituciones Apostólicas en Siria y Canon Romano).",
                ],
            },
        ],
        "citas_magisteriales": [
            {
                "id_cita": "igmr-79b",
                "doc_id": "igmr",
                "fuente": "Instrucción General del Misal Romano (IGMR)",
                "numeral": "n. 79b y n. 148",
                "año": "2002 / Tercera Edición Típica",
                "url_oficial": "https://www.vatican.va/roman_curia/congregations/ccdds/documents/rc_con_ccdds_doc_20030317_ordinamento-messale_sp.html#D._Liturgia_eucarística",
                "texto": "«Aclama toda la asamblea, uniéndose a las jerarquías celestiales, con el canto del Santo. Esta aclamación, que constituye parte de la misma Plegaria Eucarística, la pronuncia todo el pueblo con el sacerdote.»",
                "comentario_pastoral": "Subraya que pertenece a la Plegaria Eucarística misma y debe ser cantado por todo el pueblo con el sacerdote.",
            },
            {
                "id_cita": "rs-53",
                "doc_id": "igmr",
                "fuente": "Instrucción Redemptionis Sacramentum (Congregación para el Culto Divino)",
                "numeral": "n. 53",
                "año": "25 de marzo de 2004",
                "url_oficial": "https://www.vatican.va/roman_curia/congregations/ccdds/documents/rc_con_ccdds_doc_20040423_redemptionis-sacramentum_sp.html",
                "texto": "«Mientras el mismo sacerdote pronuncia la Plegaria Eucarística, no se realizarán otras oraciones o cantos, y estarán en silencio el órgano y los otros instrumentos musicales, salvo en las aclamaciones del pueblo, debidamente aprobadas... El Santo, que es parte de la Plegaria Eucarística, debe ser cantado o dicho por todos juntamente con el sacerdote.»",
                "comentario_pastoral": "Recuerda tanto la obligatoriedad del texto oficial del Santo como el silencio instrumental durante las palabras consecratorias.",
            },
        ],
        "criterios_musicales": [
            {
                "id": "san-crit-1",
                "categoria": "Impulso Inicial sin Introducción Larga",
                "titulo": "Ataque inmediato del triple «Santo, Santo, Santo»",
                "explicacion": "El sacerdote termina el Prefacio diciendo: «...cantando sin cesar el himno de tu gloria:». Si el coro mete allí una introducción instrumental de 8 compases, el enlace dramático con el Prefacio se rompe. El acuerdo ideal es dar un único acorde breve de llamada (1 tiempo o 1 compás) y entrar directamente con «Santo, Santo, Santo...».",
            },
            {
                "id": "san-crit-2",
                "categoria": "Progresión Sonora hacia el «Hosanna en el cielo»",
                "titulo": "Del asombro reverente a la exultación mesiánica",
                "explicacion": "Las tres primeras invocaciones («Santo, Santo, Santo») suelen ascender por grados conjuntos o arpegio tónico, abriéndose con amplitud luminosa en «Llenos están el cielo y la tierra de tu gloria» y culminando con plenitud polifónica (SATB + Asamblea) en el «Hosanna en el cielo».",
            },
        ],
        "checklist_discernimiento": [
            {
                "id": "chk-san-1",
                "pregunta": "¿Contiene las palabras exactas e íntegras del Misal Romano sin agregados ni omisiones?",
                "pista": "IGMR 79b.",
            },
            {
                "id": "chk-san-2",
                "pregunta": "¿Puede cantarlo toda la asamblea unida al sacerdote (tesitura accesible y ritmo claro)?",
                "pista": "Primer Grado de Musicam Sacram (n. 29).",
            },
            {
                "id": "chk-san-3",
                "pregunta": "¿Entra sin demora apenas el sacerdote concluye el Prefacio?",
                "pista": "Continuidad orgánica de la Plegaria Eucarística.",
            },
        ],
    },

    # =========================================================================
    # 12. ACLAMACIÓN MEMORIAL Y GRAN AMÉN (MYSTERIUM FIDEI & AMEN)
    # =========================================================================
    "aclamaciones-eucaristicas": {
        "slug": "aclamaciones-eucaristicas",
        "titulo": "Aclamación Memorial y Gran Amén",
        "nombre_latino": "Acclamatio anamnetica (Mysterium fidei) & Doxologia finalis (Amen)",
        "parte_nombre": "III. Liturgia Eucarística",
        "cita_principal": "IGMR 79c, 79h, 150–151 · MS 29 (Primer Grado)",
        "subtitulo": "Las dos aclamaciones pascuales de Primer Grado con las que el pueblo proclama el Misterio de la Fe tras la Consagración y sella con el Gran Amén la Doxología trinitaria de toda la Plegaria Eucarística.",
        "ficha_identidad": [
            {
                "id": "acl-naturaleza",
                "atributo": "Naturaleza Litúrgica",
                "valor": "Aclamaciones del Ordinario dentro de la Plegaria Eucarística",
                "detalle": "Son las dos intervenciones del pueblo tras el Santo: la Aclamación Memorial (después de la consagración del cáliz) y el Amén solemne al final de «Por Cristo, con Él y en Él».",
            },
            {
                "id": "acl-grado",
                "atributo": "Prioridad Normativa",
                "valor": "PRIMER GRADO de Participación (Musicam Sacram, n. 29)",
                "detalle": "Cuando el sacerdote canta «Éste es el Sacramento de nuestra fe» y «Por Cristo, con Él y en Él...», la respuesta cantada del pueblo es de máxima prioridad litúrgica.",
            },
            {
                "id": "acl-formulas",
                "atributo": "Las 3 Fórmulas Oficiales del Memorial",
                "valor": "1) «Anunciamos tu muerte...» · 2) «Cada vez que comemos...» · 3) «Salvador del mundo, sálvanos...»",
                "detalle": "Las dos primeras están inspiradas en 1 Corintios 11, 26; la tercera se dirige a Cristo Redentor por su Cruz y Resurrección.",
            },
            {
                "id": "acl-doxologia",
                "atributo": "Reserva Exclusiva de la Doxología al Sacerdote (IGMR 151)",
                "valor": "«Por Cristo, con Él y en Él...» lo dice/canta SOLO el Sacerdote · El Pueblo canta el «Amén»",
                "detalle": "La Doxología final es oración estrictamente presidencial; la asamblea no debe recitar ni cantar 'Por Cristo, con Él y en Él', sino responder unánimemente con el Gran Amén.",
            },
        ],
        "opciones_igmr": [
            {
                "numero": "Aclamación Memorial · Fórmula 1 (La más universal)",
                "titulo": "«Anunciamos tu muerte, proclamamos tu resurrección. ¡Ven, Señor Jesús!»",
                "descripcion": "Responde a la monición del sacerdote «Éste es el Misterio (Sacramento) de la fe». Abarca pasado (muerte), presente (resurrección) y futuro escatológico (¡Ven, Señor Jesús! · 1 Cor 11, 26; Ap 22, 20).",
            },
            {
                "numero": "Aclamación Memorial · Fórmula 2",
                "titulo": "«Cada vez que comemos de este pan y bebemos de este cáliz, anunciamos tu muerte, Señor, hasta que vuelvas.»",
                "descripcion": "Cita literal de San Pablo en 1 Corintios 11, 26.",
            },
            {
                "numero": "Aclamación Memorial · Fórmula 3",
                "titulo": "«Salvador del mundo, sálvanos, tú que nos has liberado por tu cruz y resurrección.»",
                "descripcion": "En la edición chilena y española del Misal Romano se introduce con «Cristo se entregó por nosotros» o «Aclamen el Misterio de la redención».",
            },
            {
                "numero": "El Gran Amén de la Doxología (IGMR 79h, 151)",
                "titulo": "«Amén» (Simple, doble o triple solemne)",
                "descripcion": "Ratificación solemne de toda la Plegaria Eucarística tras el canto presidencial «Por Cristo, con Él y en Él...». Puede amplificarse musicalmente (Amén, amén, amén) a 4 voces.",
            },
        ],
        "textos_oficiales": {
            "titulo": "Textos Oficiales de la Aclamación Memorial y de la Doxología Final",
            "nota": "En el Rito Romano, estas dos aclamaciones deben compartir preferentemente el mismo lenguaje modal o tonal que el Prefacio y el Santo (Misa cíclica).",
            "items": [
                {
                    "ocasion": "Aclamación Conmemorativa tras la Consagración (IGMR 150)",
                    "latin": "Sac.: Mystérium fídei.\nPop.: 1) Mortem tuam annuntiámus, Dómine, et tuam resurrectiónem confitémur, donec vénias.\n2) Quotiescúmque manducámus panem hunc et cálicem bíbimus, mortem tuam annuntiámus, Dómine, donec vénias.\n3) Salvátor mundi, salva nos, qui per crucem et resurrectiónem tuam liberásti nos.",
                    "espanol": "Sac.: Éste es el Sacramento (Misterio) de nuestra fe.\nPueblo:\n1) «Anunciamos tu muerte, proclamamos tu resurrección. ¡Ven, Señor Jesús!»\n2) «Cada vez que comemos de este pan y bebemos de este cáliz, anunciamos tu muerte, Señor, hasta que vuelvas.»\n3) «Por tu cruz y resurrección nos has salvado, Señor.» / «Salvador del mundo, sálvanos, tú que nos has liberado por tu cruz y resurrección.»",
                },
                {
                    "ocasion": "Doxología Final de la Plegaria Eucarística y Gran Amén (IGMR 79h, 151)",
                    "latin": "Sac.: Per ipsum, et cum ipso, et in ipso, est tibi Deo Patri omnipoténti, in unitáte Spíritus Sancti, omnis honor et glória per ómnia sǽcula sæculórum.\nPop.: Amen.",
                    "espanol": "Sac. (solo con los concelebrantes): Por Cristo, con él y en él, a ti, Dios Padre todopoderoso, en la unidad del Espíritu Santo, todo honor y toda gloria por los siglos de los siglos.\nPueblo: «¡Amén!»",
                },
            ],
        },
        "semaforo": {
            "verde": [
                {
                    "titulo": "Silencio absoluto de instrumentos durante la Consagración (IGMR 32, RS 53)",
                    "texto": "Desde que termina el Santo hasta que el sacerdote canta «Éste es el Sacramento de nuestra fe», el órgano y las guitarras deben guardar silencio total: no se toca 'música de fondo' debajo de las palabras de Cristo en la Consagración.",
                },
                {
                    "titulo": "Tomo directo de la nota del Sacerdote en la Doxología",
                    "texto": "Si el sacerdote canta «Por Cristo, con Él y en Él...», el director o instrumentista debe captar la nota final de «por los siglos de los siglos» para que el Gran Amén entre exactamente en la misma tonalidad.",
                },
            ],
            "amarillo": [
                {
                    "titulo": "Coordinar qué fórmula de Aclamación Memorial dice el Sacerdote",
                    "texto": "En el Misal Romano cada una de las 3 respuestas corresponde a su invitación específica; de ordinario «Éste es el Sacramento de nuestra fe» pide la respuesta «Anunciamos tu muerte, proclamamos tu resurrección. ¡Ven, Señor Jesús!».",
                },
            ],
            "rojo": [
                {
                    "titulo": "Cantar canciones ajenas tras la Consagración ('Bendito, bendito sea Dios', 'Señor mío y Dios mío')",
                    "texto": "Sustituir la Aclamación Memorial oficial por cantos de adoración eucarística interrumpe la Plegaria Eucarística (que aún no ha terminado: faltan la Anámnesis, la Oblación, las Intercesiones y la Doxología).",
                },
                {
                    "titulo": "Que el coro o el pueblo cante «Por Cristo, con Él y en Él» junto con el sacerdote",
                    "texto": "La IGMR 147 y 151 y Redemptionis Sacramentum 52 recuerdan que la Doxología es oración estrictamente presidencial; el pueblo participa respondiendo con el Gran Amén.",
                },
            ],
        },
        "adaptacion_tiempos": {
            "Todos los Tiempos Litúrgicos": {
                "espiritu": "Síntesis pascual de la fe de la Iglesia (Memorial) y sello de la alianza (Amén).",
                "textos_sugeridos": "«Anunciamos tu muerte, proclamamos tu resurrección. ¡Ven, Señor Jesús!» y «Amén».",
                "criterio_musical": "Usar el mismo tono del Misal Romano o una composición polifónica breve y rotunda para el Gran Amén.",
            },
        },
        "tratado_teologico": [
            {
                "id": "amen-san-jeronimo",
                "titulo": "1. Teología Patrística del «Gran Amén»: San Justino y el Trueno de las Basílicas de Roma",
                "parrafos": [
                    "La palabra hebrea ’Āmēn (de la raíz ’mn: estar firme, ser sólido, digno de fe, verdadero) es la firma con la que el Pueblo de Dios suscribe y hace suya la Plegaria Eucarística pronunciada por el presidente. Ya en el año 155, San Justino Mártir explicaba al emperador Antonino Pío en su Apología I (cap. 65): «Cuando el que preside ha terminado las oraciones y la acción de gracias [la Eucaristía], todo el pueblo presente aclama diciendo: Amén. Y 'Amén' en lengua hebrea significa: 'Así sea'».",
                    "Dos siglos más tarde, San Jerónimo dejaba este testimonio inolvidable sobre la fuerza con que los cristianos de Roma cantaban el Amén de la Doxología eucarística: «En las basílicas de Roma, el Amén del pueblo retumba como el trueno del cielo (ad similitudinem caelestis tonitrui Amen reboat), mientras los templos vacíos de los ídolos tiemblan» (In Epist. ad Galatas, II, Prólogo). Por su parte, San Agustín afirmaba: «El Amén de ustedes es su firma, es su consentimiento, es su compromiso» (Sermón 272).",
                ],
            },
        ],
        "citas_magisteriales": [
            {
                "id_cita": "igmr-79ch-151",
                "doc_id": "igmr",
                "fuente": "Instrucción General del Misal Romano (IGMR)",
                "numeral": "nn. 79c, 79h, 150–151",
                "año": "2002 / Tercera Edición Típica",
                "url_oficial": "https://www.vatican.va/roman_curia/congregations/ccdds/documents/rc_con_ccdds_doc_20030317_ordinamento-messale_sp.html#D._Liturgia_eucarística",
                "texto": "«A la monición del sacerdote, el pueblo aclama recordando la muerte y resurrección del Señor y esperando su venida gloriosa... La doxología final: Por la cual se expresa la glorificación de Dios, y que es confirmada y concluida con la aclamación Amén del pueblo.»",
                "comentario_pastoral": "Muestra que el Gran Amén es la conclusión y confirmación de toda la Plegaria Eucarística.",
            },
        ],
        "criterios_musicales": [
            {
                "id": "acl-crit-1",
                "categoria": "Diseño del Gran Amén",
                "titulo": "Triple Amén ascendente con armonización coral SATB",
                "explicacion": "Un simple 'Amén' hablado después de una Plegaria Eucarística solemne resulta anticlimático. Componer un triple «Amén, amén, amén» donde la melodía de la asamblea asciende por grados conjuntos (ej. Do–Re–Mi / Re–Mi–Fa / Mi–Re–Do) mientras el coro despliega acordes plenos a 4 voces devuelve al Amén el 'sonido de trueno celestial' que describía San Jerónimo.",
            },
        ],
        "checklist_discernimiento": [
            {
                "id": "chk-acl-1",
                "pregunta": "¿Se guarda silencio absoluto de instrumentos durante la Consagración, entrando recién tras «Éste es el Sacramento de nuestra fe»?",
                "pista": "Redemptionis Sacramentum 53 / IGMR 32.",
            },
            {
                "id": "chk-acl-2",
                "pregunta": "¿Se deja que el sacerdote cante o diga solo «Por Cristo, con Él y en Él...», entrando todos con fuerza en el Gran Amén?",
                "pista": "IGMR 151.",
            },
        ],
    },

    # =========================================================================
    # 13. PADRE NUESTRO Y DOXOLOGÍA (PATER NOSTER)
    # =========================================================================
    "padre-nuestro": {
        "slug": "padre-nuestro",
        "titulo": "Padre Nuestro y Doxología",
        "nombre_latino": "Oratio Dominica (Pater Noster)",
        "parte_nombre": "III. Liturgia Eucarística (Rito de la Comunión)",
        "cita_principal": "IGMR 81, 152–153 · MS 29 (Primer Grado)",
        "subtitulo": "La Oración del Señor con que se abre el Rito de la Comunión, pidiendo el Pan cotidiano y eucarístico y el perdón fraterno, seguida del Embolismo presidencial y la doxología final del pueblo.",
        "ficha_identidad": [
            {
                "id": "pat-naturaleza",
                "atributo": "Naturaleza Litúrgica (IGMR 81)",
                "valor": "Oración del Ordinario (Texto evangélico y litúrgico absolutamente invariable)",
                "detalle": "Pórtico del Rito de la Comunión. Sus palabras son las que Cristo mismo entregó a sus Apóstoles (Mt 6, 9-13) según la traducción litúrgica oficial del Misal Romano.",
            },
            {
                "id": "pat-grado",
                "atributo": "Prioridad Normativa",
                "valor": "PRIMER GRADO de Participación (Musicam Sacram, n. 29)",
                "detalle": "Cuando se canta, debe usarse una melodía que todo el pueblo conozca y cante juntamente con el sacerdote celebrante.",
            },
            {
                "id": "pat-estructura",
                "atributo": "Estructura Tripartita Completa (IGMR 81, 152–153)",
                "valor": "1) Invitación y Padre Nuestro (Sacerdote + Pueblo) → 2) Embolismo (Sacerdote) → 3) Doxología (Pueblo)",
                "detalle": "El Padre Nuestro en la Misa NO termina con la palabra «Amén» después de «líbranos del mal», porque el sacerdote prolonga inmediatamente esa última petición con el Embolismo («Líbranos de todos los males, Señor...») y el pueblo cierra con «Tuyo es el reino, tuyo el poder y la gloria, por siempre, Señor».",
            },
            {
                "id": "pat-postura",
                "atributo": "Postura Corporal (IGMR 43, 152)",
                "valor": "De pie · El Sacerdote extiende las manos (gesto presidencial)",
                "detalle": "El Misal indica que el sacerdote extiende las manos; en cuanto a los fieles, se desaconseja darse las manos en cadena (anticipando el rito de la paz que viene después).",
            },
        ],
        "opciones_igmr": [
            {
                "numero": "Opción 1 (Tono oficial del Misal Romano)",
                "titulo": "Melodía tradicional del Misal Romano (adaptación hispanoamericana del Pater Noster gregoriano)",
                "descripcion": "La melodía modal universal del Misal Romano es un tesoro de sobriedad y nobleza que une a todas las parroquias y diócesis sin necesidad de ensayos previos.",
            },
            {
                "numero": "Opción 2 (Musicalización aprobada con texto literal)",
                "titulo": "Otra melodía congregacional aprobada con el texto exacto e íntegro del Misal",
                "descripcion": "Solo es legítima si mantiene el texto oficial palabra por palabra («Padre nuestro, que estás en el cielo... no nos dejes caer en la tentación, y líbranos del mal») sin añadir palabras ni rimas.",
            },
        ],
        "textos_oficiales": {
            "titulo": "Texto Oficial Íntegro del Rito del Padre Nuestro (Invitación, Oración, Embolismo y Doxología)",
            "nota": "Si se canta el Padre Nuestro, es sumamente recomendable que el sacerdote cante también el Embolismo y toda la asamblea cante la Doxología final «Tuyo es el reino...».",
            "items": [
                {
                    "ocasion": "1. Invitación y Oración del Señor (Sacerdote + Pueblo)",
                    "latin": "Sac.: Præcéptis salutáribus móniti, et divína institutióne formáti, audémus dícere:\nOmnes: Pater noster, qui es in cælis: sanctificétur nomen tuum; advéniat regnum tuum; fiat volúntas tua, sicut in cælo, et in terra. Panem nostrum cotidiánum da nobis hódie; et dimítte nobis débita nostra, sicut et nos dimíttimus debitóribus nostris; et ne nos indúcas in tentatiónem; sed líbera nos a malo.",
                    "espanol": "Sac.: Fieles a la recomendación del Salvador y siguiendo su divina enseñanza, nos atrevemos a decir:\nTodos: Padre nuestro, que estás en el cielo, santificado sea tu Nombre; venga a nosotros tu reino; hágase tu voluntad en la tierra como en el cielo. Danos hoy nuestro pan de cada día; perdona nuestras ofensas, como también nosotros perdonamos a los que nos ofenden; no nos dejes caer en la tentación, y líbranos del mal.",
                },
                {
                    "ocasion": "2. Embolismo Presidencial (Sacerdote solo)",
                    "latin": "Sac.: Líbera nos, quǽsumus, Dómine, ab ómnibus malis, da propítius pacem in diébus nostris, ut, ope misericórdiæ tuæ adiúti, et a peccáto simus semper líberi et ab omni perturbatióne secúri: exspectántes beátam spem et advéntum Salvatóris nostri Iesu Christi.",
                    "espanol": "Sac.: Líbranos de todos los males, Señor, y concédenos la paz en nuestros días, para que, ayudados por tu misericordia, vivamos siempre libres de pecado y protegidos de toda perturbación, mientras esperamos la gloriosa venida de nuestro Salvador Jesucristo.",
                },
                {
                    "ocasion": "3. Doxología Final (Aclama el Pueblo · Didaché 8, 2)",
                    "latin": "Pop.: Quia tuum est regnum, et potéstas, et glória in sǽcula.",
                    "espanol": "Pueblo: «Tuyo es el reino, tuyo el poder y la gloria, por siempre, Señor.»",
                },
            ],
        },
        "semaforo": {
            "verde": [
                {
                    "titulo": "Privilegiar la melodía oficial del Misal Romano",
                    "texto": "La melodía oficial del Misal Romano permite que cualquier fiel, sacerdote o visitante cante el Padre Nuestro con unción y unidad, enlazando además con la música del Embolismo y del «Tuyo es el reino».",
                },
                {
                    "titulo": "Cantar también la aclamación «Tuyo es el reino, tuyo el poder y la gloria, por siempre, Señor»",
                    "texto": "Incluso cuando el Padre Nuestro y el Embolismo se hayan rezado, o más aún cuando se han cantado, responder cantando la Doxología final cierra con majestad la oración dominical.",
                },
            ],
            "amarillo": [
                {
                    "titulo": "No decir «Amén» al terminar «y líbranos del mal»",
                    "texto": "La melodía del Padre Nuestro en la Misa debe concluir directamente en «y líbranos del mal» (sin agregar «Amén»), dejando abierta la cadencia para que el sacerdote inicie el Embolismo «Líbranos de todos los males, Señor...».",
                },
            ],
            "rojo": [
                {
                    "titulo": "PROHIBICIÓN TAXATIVA: Los falsos 'Padrenuestros' adaptados a melodías profanas ('The Sound of Silence', etc.)",
                    "texto": "Está estrictamente prohibido en la liturgia católica cantar versiones como 'Padre nuestro tú que estás en los que aman la verdad' (sobre la música de Simon & Garfunkel) o dejar rezando al pueblo en voz baja mientras el coro canta otra letra encima.",
                },
            ],
        },
        "adaptacion_tiempos": {
            "Todos los Tiempos Litúrgicos": {
                "espiritu": "Oración de los hijos de Dios antes de acercarse a la mesa del Pan sobresustancial.",
                "textos_sugeridos": "Texto único e invariable del Evangelio y del Misal Romano.",
                "criterio_musical": "Canto llano o acompañado discretamente; en Viernes Santo se canta o reza sin acompañamiento instrumental.",
            },
        },
        "tratado_teologico": [
            {
                "id": "pater-teologia-pan",
                "titulo": "1. Teología Patrística: El «Pan Epiousios» y el Perdón antes de Comulgar",
                "parrafos": [
                    "¿Por qué la Iglesia coloca el Padre Nuestro inmediatamente antes de la Comunión? Los Padres de la Iglesia (Tertuliano, San Cipriano de Cartago, San Agustín y San Jerónimo) señalaban que las dos peticiones centrales de la segunda parte del Padre Nuestro son la preparación directa e indispensable para recibir el Cuerpo de Cristo:",
                    "1) «Danos hoy nuestro pan de cada día (panem nostrum cotidianum / epiousion)»: San Jerónimo tradujo el adjetivo griego epiousios de Mateo 6, 11 como «supersubstantialem» ('nuestro pan sobresustancial'), viendo en él en primer lugar el Pan Eucarístico que alimenta la vida divina en nosotros.\n2) «Perdona nuestras ofensas, como también nosotros perdonamos a los que nos ofenden»: cumpliendo el mandato de Jesús en Mateo 5, 23-24 (reconciliarse con el hermano antes de acercarse al altar), la asamblea pide ser purificada de las faltas cotidianas antes de comulgar.",
                ],
            },
            {
                "id": "pater-historia-embolismo",
                "titulo": "2. Historia Litúrgica: San Gregorio Magno, el Embolismo y la Doxología de la Didaché",
                "parrafos": [
                    "En su Carta a Juan de Siracusa (Epist. IX, 26), San Gregorio Magno explicó que él mismo trasladó el Pater Noster a su lugar actual (inmediatamente después del Canon o Plegaria Eucarística), porque «me parecía muy impropio que dijéramos sobre la oblación una plegaria compuesta por un estudioso y no dijéramos sobre su Cuerpo y su Sangre la misma oración que compuso nuestro Redentor».",
                    "El término griego Embolismós significa 'desarrollo insertado': retoma la séptima y última petición del Padre Nuestro («y líbranos del mal») y la despliega litúrgicamente. Finalmente, la reforma del Vaticano II restauró al final del Embolismo la antiquísima doxología judeocristiana documentada ya en el siglo I en la Didaché (Doctrina de los Doce Apóstoles, cap. 8, 2): «Porque tuyo es el poder y la gloria por los siglos».",
                ],
            },
        ],
        "citas_magisteriales": [
            {
                "id_cita": "igmr-81",
                "doc_id": "igmr",
                "fuente": "Instrucción General del Misal Romano (IGMR)",
                "numeral": "n. 81",
                "año": "2002 / Tercera Edición Típica",
                "url_oficial": "https://www.vatican.va/roman_curia/congregations/ccdds/documents/rc_con_ccdds_doc_20030317_ordinamento-messale_sp.html#D._Liturgia_eucarística",
                "texto": "«En la Oración del Señor se pide el pan de cada día, con lo que para los cristianos se evoca principalmente el pan eucarístico, y se implora la purificación de los pecados, de modo que, en realidad, las cosas santas se den a los santos. El sacerdote hace la invitación a la oración, y todos los fieles dicen la oración juntamente con el sacerdote; el sacerdote solo añade el embolismo, que el pueblo concluye con la doxología. El embolismo, que desarrolla la última petición de la misma Oración del Señor, pide con ardor para toda la comunidad de los fieles la liberación del poder del mal. La invitación, la oración misma, el embolismo y la doxología con que el pueblo concluye todo esto, se cantan o se dicen en voz alta.»",
                "comentario_pastoral": "Muestra la unidad de los cuatro elementos: Invitación, Padre Nuestro, Embolismo y Doxología.",
            },
        ],
        "criterios_musicales": [
            {
                "id": "pat-crit-1",
                "categoria": "Prosodia y Ritmo de Oración",
                "titulo": "Respetar las siete peticiones sin deformar los acentos con síncopas pop",
                "explicacion": "El Padre Nuestro es la oración que todo bautizado lleva grabada en el alma desde niño. Si una melodía altera la prosodia natural del texto o introduce silencios caprichosos donde la gente entra a destiempo, genera incomodidad en la asamblea. El canto llano o recitativo silábico fluido es insuperable aquí.",
            },
        ],
        "checklist_discernimiento": [
            {
                "id": "chk-pat-1",
                "pregunta": "¿El texto cantado es 100 % idéntico a la oración oficial del Padre Nuestro sin una sola palabra cambiada ni agregada?",
                "pista": "IGMR 81.",
            },
            {
                "id": "chk-pat-2",
                "pregunta": "¿Termina en «y líbranos del mal» (sin decir «Amén») para dar paso directo al Embolismo del sacerdote?",
                "pista": "IGMR 81, 153.",
            },
        ],
    },

    # =========================================================================
    # 14. CORDERO DE DIOS (AGNUS DEI · FRACCIÓN DEL PAN)
    # =========================================================================
    "cordero-de-dios": {
        "slug": "cordero-de-dios",
        "titulo": "Cordero de Dios (Agnus Dei)",
        "nombre_latino": "Fractio Panis · Agnus Dei",
        "parte_nombre": "III. Liturgia Eucarística (Rito de la Comunión)",
        "cita_principal": "IGMR 82–83 · MS 30 · Notificación CDDS (2014)",
        "subtitulo": "La súplica letánica dirigida a Cristo Cordero Pascual inmolado (Jn 1, 29; Ap 5, 6) que acompaña el gesto apostólico de la Fracción del Pan consagrado.",
        "ficha_identidad": [
            {
                "id": "cor-naturaleza",
                "atributo": "Naturaleza Litúrgica (IGMR 83)",
                "valor": "Canto del Ordinario (Ordo Missae · Texto letánico invariable)",
                "detalle": "Sus palabras pertenecen al Ordinario de la Misa («Cordero de Dios, que quitas el pecado del mundo, ten piedad de nosotros... danos la paz») y no pueden sustituirse.",
            },
            {
                "id": "cor-funcion",
                "atributo": "Función Ritual Exacta (¡Ojo con el Saludo de la Paz!)",
                "valor": "Acompaña la FRACCIÓN DEL PAN y la Inmixtión (NO el saludo de la paz)",
                "detalle": "El saludo de la paz debe ser sobrio y breve (sin 'canto de la paz'); apenas los fieles se dan la paz a quienes tienen más cerca y el sacerdote toma la Hostia sobre la patena para partirla, se inicia el canto del Cordero de Dios.",
            },
            {
                "id": "cor-repeticion",
                "atributo": "Número de Invocaciones (IGMR 83)",
                "valor": "Habitualmente 3 veces (o más si la Fracción del Pan se prolonga)",
                "detalle": "«Puede repetirse cuantas veces sea necesario hasta que haya terminado el rito; la última vez se concluye con las palabras danos la paz» (IGMR 83).",
            },
            {
                "id": "cor-ejecucion",
                "atributo": "Protagonista y Ejecución (IGMR 83)",
                "valor": "Cantor o Coro (Invocación) + Pueblo (Respuesta) o toda la Asamblea",
                "detalle": "Por su estructura de letanía, la IGMR 83 destaca el diálogo: el coro o cantor entona «Cordero de Dios, que quitas el pecado del mundo» y todo el pueblo responde «ten piedad de nosotros» / «danos la paz».",
            },
            {
                "id": "cor-postura",
                "atributo": "Postura al Concluir",
                "valor": "De pie durante el canto · De rodillas en «Éste es el Cordero de Dios...» (IGMR 43)",
                "detalle": "Concluido el «danos la paz», los fieles se arrodillan para la ostensión de la Hostia («Éste es el Cordero de Dios... Dichosos los invitados a la cena del Señor»).",
            },
        ],
        "opciones_igmr": [
            {
                "numero": "Forma Normativa (3 invocaciones)",
                "titulo": "Dos veces «ten piedad de nosotros» y la última «danos la paz»",
                "descripcion": "En las Misas parroquiales ordinarias donde la fracción del pan toma entre 30 y 45 segundos, las tres invocaciones tradicionales calzan con exactitud matemática con el gesto del sacerdote.",
            },
            {
                "numero": "En Grandes Concelebraciones (IGMR 83)",
                "titulo": "Repetición de «ten piedad de nosotros» hasta terminar de partir las Hostias",
                "descripcion": "Si hay varios copones o una Hostia magna que requiere más tiempo de fracción, se repite «Cordero de Dios... ten piedad de nosotros» las veces necesarias y, cuando el sacerdote deja caer la partícula en el cáliz (Inmixtión), se canta la última con «danos la paz».",
            },
        ],
        "textos_oficiales": {
            "titulo": "Texto Oficial del Agnus Dei y la Invitación a la Comunión",
            "nota": "Observemos la conexión teológica: el canto aclama al Cordero invisiblemente presente en la fracción, e inmediatamente después el sacerdote levanta la Hostia partida y dice: «Éste es el Cordero de Dios...» (Jn 1, 29; Ap 19, 9).",
            "items": [
                {
                    "ocasion": "Letanía de la Fracción del Pan (IGMR 83)",
                    "latin": "Agnus Dei, qui tollis peccáta mundi: miserére nobis.\nAgnus Dei, qui tollis peccáta mundi: miserére nobis.\nAgnus Dei, qui tollis peccáta mundi: dona nobis pacem.",
                    "espanol": "Cordero de Dios, que quitas el pecado del mundo, ten piedad de nosotros.\nCordero de Dios, que quitas el pecado del mundo, ten piedad de nosotros.\nCordero de Dios, que quitas el pecado del mundo, danos la paz.",
                },
                {
                    "ocasion": "Ostensión e Invitación a la Comunión (IGMR 84 · Jn 1, 29; Ap 19, 9; Mt 8, 8)",
                    "latin": "Sac.: Ecce Agnus Dei, ecce qui tollit peccáta mundi. Beáti qui ad cenam Agni vocáti sunt.\nOmnes: Dómine, non sum dignus, ut intres sub tectum meum, sed tantum dic verbo, et sanábitur ánima mea.",
                    "espanol": "Sac.: Éste es el Cordero de Dios, que quita el pecado del mundo. Dichosos los invitados a la cena del Señor.\nTodos: Señor, no soy digno de que entres en mi casa, pero una palabra tuya bastará para sanarme.",
                },
            ],
        },
        "semaforo": {
            "verde": [
                {
                    "titulo": "NO tocar ningún 'canto de la paz' para poder iniciar el Cordero de Dios a tiempo",
                    "texto": "La Carta Circular de la Congregación para el Culto Divino sobre el significado ritual del don de la paz en la Misa (2014, aprobada por el Papa Francisco) reitera que en el Rito Romano NO existe un 'canto de la paz': tras el saludo breve a quienes están al lado, se canta inmediatamente el Cordero de Dios mientras el sacerdote parte la Hostia.",
                },
                {
                    "titulo": "Terminar junto con la Fracción del Pan (sin obligar al sacerdote a esperar con la Hostia en alto)",
                    "texto": "El Cordero de Dios debe ser conciso y recogido (40 a 60 segundos), de modo que concluya cuando el sacerdote prepara la genuflexión previa al «Éste es el Cordero de Dios».",
                },
            ],
            "amarillo": [
                {
                    "titulo": "Cuidar que la primera invocación no quede tapada por el murmullo del saludo de la paz",
                    "texto": "Entonar con firmeza y claridad la primera invocación del «Cordero de Dios» ayuda pastoralmente a que la asamblea concluya el saludo de la paz y vuelva la mirada hacia el altar para contemplar la Fracción del Pan.",
                },
            ],
            "rojo": [
                {
                    "titulo": "ABUSO GRAVE: Reemplazar o retrasar el Cordero de Dios por 'cantos de la paz' ('La paz esté con nosotros', 'Paz en la tierra', etc.)",
                    "texto": "Cantar una canción de la paz convierte el rito en un recreo ruidoso de abrazos por toda la iglesia, hace que el sacerdote parta el Pan en solitario mientras nadie mira al altar y termina suprimiendo o atropellando el Agnus Dei.",
                },
                {
                    "titulo": "Alterar la letra ('Cordero de Dios que quitas el pecado DE LOS HOMBRES')",
                    "texto": "El texto bíblico de Juan 1, 29 y del Misal Romano es en singular cósmico: «que quitas el pecado DEL MUNDO» (peccatum mundi).",
                },
            ],
        },
        "adaptacion_tiempos": {
            "Todos los Tiempos Litúrgicos": {
                "espiritu": "Contemplación reverente del Cuerpo de Cristo que se parte por nosotros como en Emaús (Lc 24, 30-35).",
                "textos_sugeridos": "Texto único e invariable del Misal Romano (en español o en latín Agnus Dei).",
                "criterio_musical": "Carácter íntimo, suplicante y profundamente eucarístico; el último «danos la paz» debe resolverse en una cadencia de serena paz interior.",
            },
        },
        "tratado_teologico": [
            {
                "id": "cordero-teologia-fraccion",
                "titulo": "1. Teología de la «Fractio Panis»: Emaús, San Pablo y el Cordero del Apocalipsis",
                "parrafos": [
                    "En la Iglesia apostólica, toda la celebración de la Eucaristía se llamaba simplemente «la Fracción del Pan» (Fractio panis; cf. Hch 2, 42; Lc 24, 35). Como enseña la IGMR 83 citando a San Pablo (1 Cor 10, 17): «El gesto de la fracción del pan, realizado por Cristo en la Última Cena, que en el tiempo apostólico designó a toda la acción eucarística, significa que los fieles, siendo muchos, en la Comunión de un solo pan de vida, que es Cristo muerto y resucitado para la salvación del mundo, se hacen un solo cuerpo».",
                    "El canto del Agnus Dei une el testimonio del Bautista en el Jordán («He ahí el Cordero de Dios que quita el pecado del mundo», Jn 1, 29) con la liturgia celestial del Apocalipsis, donde el Cordero «de pie, como degollado» (Ap 5, 6) recibe la adoración de los redimidos. Al partirse el Pan consagrado y dejar caer una partícula del Cuerpo en el Cáliz de la Sangre (el rito de la Inmixtión o Commixtio, que simboliza la unión del Cuerpo y el Alma de Cristo en su gloriosa Resurrección), cantamos al Cordero Pascual cuya sangre nos libra de la muerte.",
                ],
            },
            {
                "id": "cordero-historia-sergio",
                "titulo": "2. Historia Litúrgica: El Papa San Sergio I (687–701) y la Notificación de 2014",
                "parrafos": [
                    "Según el Liber Pontificalis, fue el Papa San Sergio I (de origen sirio-antioqueno, pontífice entre 687 y 701) quien estableció que «en el momento de la fracción del Cuerpo del Señor, el clero y el pueblo canten Agnus Dei, qui tollis peccata mundi, miserere nobis». En aquella época se partían sobre el altar grandes panes fermentados para la comunión de toda la asamblea y para enviar el Fermentum a las iglesias titulares de Roma, por lo que la letanía se repetía con «miserere nobis» mientras duraba la fracción. En los siglos X–XI, cuando los disturbios feudales asolaban Europa, se sustituyó el tercer «miserere nobis» por la súplica «dona nobis pacem» ('danos la paz').",
                    "En julio de 2014, la Congregación para el Culto Divino y la Disciplina de los Sacramentos publicó con aprobación del Papa Francisco la Carta Circular «La expresión ritual del don de la paz en la Misa», pidiendo erradicar definitivamente los abusos que desvirtúan este momento (como introducir un 'canto de la paz' inexistente en el Rito Romano o desplazarse de los lugares) para devolver todo su relieve mistagógico a la Fracción del Pan y al canto del Cordero de Dios.",
                ],
            },
        ],
        "citas_magisteriales": [
            {
                "id_cita": "igmr-83",
                "doc_id": "igmr",
                "fuente": "Instrucción General del Misal Romano (IGMR)",
                "numeral": "n. 83",
                "año": "2002 / Tercera Edición Típica",
                "url_oficial": "https://www.vatican.va/roman_curia/congregations/ccdds/documents/rc_con_ccdds_doc_20030317_ordinamento-messale_sp.html#D._Liturgia_eucarística",
                "texto": "«El sacerdote parte el pan eucarístico, con la ayuda, si es el caso, del diácono o de un concelebrante. El gesto de la fracción del pan, realizado por Cristo en la Última Cena, que en el tiempo apostólico designó a toda la acción eucarística, significa que los fieles, siendo muchos, en la Comunión de un solo pan de vida, que es Cristo muerto y resucitado para la salvación del mundo, se hacen un solo cuerpo (1 Cor 10, 17). La fracción comienza después de haberse dado la paz y se lleva a cabo con la debida reverencia... La súplica Cordero de Dios la canta de ordinario el coro o el cantor con la respuesta del pueblo; o la dice al menos en voz alta. Esta invocación acompaña la fracción del pan y, por eso, puede repetirse cuantas veces sea necesario hasta que haya terminado el rito; la última vez se concluye con las palabras danos la paz.»",
                "comentario_pastoral": "Norma central sobre el sentido teológico de la Fracción del Pan y el modo dialogado de cantar el Cordero de Dios.",
            },
            {
                "id_cita": "cdds-paz-2014",
                "doc_id": "conali-chile",
                "fuente": "Congregación para el Culto Divino · Carta Circular sobre el Don de la Paz en la Misa",
                "numeral": "n. 6a",
                "año": "8 de junio de 2014",
                "url_oficial": "https://www.vatican.va/roman_curia/congregations/ccdds/documents/rc_con_ccdds_doc_20140607_circolare-pace-messa_sp.html",
                "texto": "«En todo caso, será necesario que en el momento del intercambio de la paz se eviten definitivamente algunos abusos tales como: la introducción de un 'canto para la paz', inexistente en el Rito romano; los desplazamientos de los fieles para intercambiar la paz; que el sacerdote abandone el altar para dar la paz a algunos fieles.»",
                "comentario_pastoral": "Documento definitivo de la Santa Sede que prohíbe introducir un 'canto de la paz' antes del Cordero de Dios.",
            },
        ],
        "criterios_musicales": [
            {
                "id": "cor-crit-1",
                "categoria": "Tempo, Dinámica y Duración",
                "titulo": "Recogimiento contemplativo (45 a 60 segundos en total)",
                "explicacion": "A diferencia del Gloria o del Santo (que son himnos de plenitud sonora), el Cordero de Dios pide un tempo Andante sereno y una dinámica mezzo-piano a piano que conduzca al silencio de adoración cuando el sacerdote muestra la Hostia consagrada.",
            },
        ],
        "checklist_discernimiento": [
            {
                "id": "chk-cor-1",
                "pregunta": "¿Se ha eliminado cualquier 'canto de la paz' para que el Cordero de Dios comience apenas el sacerdote toma la Hostia para partirla?",
                "pista": "IGMR 83 y Carta Circular CDDS (2014) n. 6a.",
            },
            {
                "id": "chk-cor-2",
                "pregunta": "¿El texto dice exactamente «Cordero de Dios, que quitas el pecado del mundo, ten piedad de nosotros... danos la paz»?",
                "pista": "Ordinario de la Misa.",
            },
            {
                "id": "chk-cor-3",
                "pregunta": "¿Su duración permite concluir junto con la fracción del pan sin hacer esperar al sacerdote antes del «Éste es el Cordero de Dios»?",
                "pista": "Subordinación del canto a la acción ritual.",
            },
        ],
    },

    # =========================================================================
    # 15. CANTO DE COMUNIÓN Y ACCIÓN DE GRACIAS (CANTUS AD COMMUNIONEM)
    # =========================================================================
    "comunion": {
        "slug": "comunion",
        "titulo": "Canto de Comunión y Acción de Gracias",
        "nombre_latino": "Cantus ad Communionem & Post Communionem",
        "parte_nombre": "III. Liturgia Eucarística (Rito de la Comunión)",
        "cita_principal": "IGMR 86–88 · MS 31–32",
        "subtitulo": "El canto procesional que comienza mientras comulga el sacerdote para expresar por la unidad de las voces la unión espiritual de quienes reciben el Cuerpo del Señor, seguido del silencio sagrado o salmo de alabanza.",
        "ficha_identidad": [
            {
                "id": "com-naturaleza",
                "atributo": "Naturaleza Litúrgica (IGMR 86)",
                "valor": "Canto del Propio (Proprium Missae · Variable y Eucarístico-Evangélico)",
                "detalle": "En la tradición romana, la Antífona de Comunión toma una frase directa del Evangelio proclamado ese mismo día o un versículo eucarístico de los Salmos (especialmente el Salmo 33).",
            },
            {
                "id": "com-inicio",
                "atributo": "Momento Exacto de Inicio y Término (IGMR 86)",
                "valor": "Inicia MIENTRAS el sacerdote toma el Sacramento · Dura mientras comulgan los fieles",
                "detalle": "No se espera a que comulguen los ministros o el primer fiel de la fila: apenas termina el «Señor, no soy digno...» y el sacerdote comulga el Cuerpo de Cristo, comienza el canto de comunión.",
            },
            {
                "id": "com-fines",
                "atributo": "Tres Fines Propios (IGMR 86)",
                "valor": "1) Expresar por la unidad de las voces la unión espiritual · 2) Mostrar la alegría del corazón · 3) Esclarecer el carácter comunitario de la procesión",
                "detalle": "La Comunión no es una devoción privada aislada, sino el banquete pascual de los hermanos que caminan juntos hacia el altar.",
            },
            {
                "id": "com-ejecucion",
                "atributo": "Forma Óptima de Ejecución (IGMR 87)",
                "valor": "Responsorial sin papeles (Asamblea canta antífona breve + Coro/Cantor estrofas) o solo el Coro",
                "detalle": "Como los fieles van caminando en fila con las manos ocupadas o recogidas, no pueden sostener un cancionero: necesitan un estribillo breve que puedan cantar de memoria mientras avanzan.",
            },
            {
                "id": "com-post",
                "atributo": "Después de la Distribución: Silencio Sagrado o Himno de Alabanza (IGMR 88)",
                "valor": "El canto procesional termina con la distribución · Sigue el Silencio Sagrado (o himno de acción de gracias)",
                "detalle": "La IGMR 86 advierte que si después de la comunión se va a cantar un himno de alabanza, el canto procesional de comunión debe terminar a tiempo para garantizar un intervalo de silencio sagrado.",
            },
        ],
        "opciones_igmr": [
            {
                "numero": "Opción 1 (Graduale Romanum)",
                "titulo": "Antífona del Graduale Romanum (con o sin Salmo)",
                "descripcion": "Canto de la antífona propia del Graduale Romanum, que suele musicalizar las palabras mismas de Jesús en el Evangelio del día.",
            },
            {
                "numero": "Opción 2 (Graduale Simplex / Salmo 33)",
                "titulo": "Antífona con Salmo del Graduale Simplex (especialmente el Salmo 33)",
                "descripcion": "El Salmo 33 con la antífona «Gusten y vean qué bueno es el Señor» es el canto de comunión por excelencia de toda la tradición cristiana de Oriente y Occidente.",
            },
            {
                "numero": "Opción 3 (Antífona del Misal Romano)",
                "titulo": "Musicalización de la Antífona de Comunión del Misal Romano con Salmo",
                "descripcion": "Poner melodía en español a la Antífona de Comunión impresa en el Misal Romano para ese domingo, alternándola con versículos del Salmo 33, 22, 62, 83 o 144.",
            },
            {
                "numero": "Opción 4 (Alius cantus aptus)",
                "titulo": "Otro canto congruente aprobado por la Conferencia Episcopal",
                "descripcion": "Un canto de carácter verdaderamente eucarístico o evangélico acorde al Tiempo Litúrgico. Si no hay canto en absoluto, la Antífona de Comunión del Misal debe ser leída por los fieles, un lector o el sacerdote (IGMR 87).",
            },
        ],
        "textos_oficiales": {
            "titulo": "Antífonas Paradigmáticas de Comunión e Himnos Eucarísticos de la Tradición",
            "nota": "En el Misal Romano, cuando no hay canto de comunión, la Antífona de Comunión se recita después de que el sacerdote ha comulgado y antes de distribuir la Comunión a los fieles (IGMR 87).",
            "items": [
                {
                    "ocasion": "El Salmo Eucarístico Universal · Salmo 33, 9 (San Cirilo de Jerusalén)",
                    "latin": "Gustáte et vidéte quóniam suávis est Dóminus: beátus vir, qui sperat in eo.",
                    "espanol": "«Gusten y vean qué bueno es el Señor; dichoso el que se acoge a él.»",
                },
                {
                    "ocasion": "Discurso del Pan de Vida · Juan 6, 56. 54",
                    "latin": "Qui mandúcat meam carnem et bibit meum sánguinem, in me manet et ego in eo, dicit Dóminus.",
                    "espanol": "«El que come mi carne y bebe mi sangre permanece en mí y yo en él, dice el Señor.»",
                },
                {
                    "ocasion": "Fracción del Pan · 1 Corintios 10, 16-17",
                    "latin": "Calix benedictiónis, cui benedícimus, nonne communicátio Sánguinis Christi est? Et panis, quem frángimus, nonne participátio Córporis Dómini est?",
                    "espanol": "«El cáliz de bendición que bendecimos, ¿no es comunión con la Sangre de Cristo? Y el pan que partimos, ¿no es comunión con el Cuerpo del Señor?»",
                },
                {
                    "ocasion": "Himnos Clásicos de Acción de Gracias Post-Comunión (IGMR 88)",
                    "latin": "Anima Christi, sanctifica me... · Adoro te devote, latens Deitas... · Ave verum Corpus natum de Maria Virgine... · Panis angelicus...",
                    "espanol": "«Alma de Cristo, santifícame; Cuerpo de Cristo, sálvame; Sangre de Cristo, embriágame...» · «Te adoro con devoción, Dios escondido...» · «Salve, verdadero Cuerpo nacido de María Virgen...»",
                },
            ],
        },
        "semaforo": {
            "verde": [
                {
                    "titulo": "Empezar inmediatamente cuando comulga el Sacerdote (IGMR 86)",
                    "texto": "No dejar un vacío de silencio mientras comulgan el sacerdote, el diácono y los ministros: el canto comienza apenas el sacerdote comulga para unir desde el primer instante a toda la asamblea.",
                },
                {
                    "titulo": "Textos centrados en el misterio Eucarístico y en el Evangelio del día",
                    "texto": "En el Rito Romano existe la llamada 'ley del eco evangélico en la Comunión': la Comunión es el momento en que la Palabra escuchada en el Evangelio se hace Carne que recibimos. Un canto que recoja la parábola o el Evangelio del día junto con el misterio del Pan de Vida es el ideal supremo.",
                },
                {
                    "titulo": "Garantizar siempre el Silencio Sagrado después de la Comunión (IGMR 88)",
                    "texto": "Cuando el sacerdote o acólito guarda el copón en el Sagrario y termina de purificar el cáliz en el altar, la música debe callar por completo durante al menos un minuto para que cada fiel converse íntimamente en el silencio de su corazón con el Señor recibido.",
                },
            ],
            "amarillo": [
                {
                    "titulo": "Distinguir entre el Canto Procesional de Comunión (IGMR 86) y el Canto Post-Comunión (IGMR 88)",
                    "texto": "No hay que encadenar 3 o 4 canciones seguidas sin pausa hasta el «Oremos»: es mucho mejor cantar un buen canto procesional mientras la gente comulga y luego dejar silencio sagrado (o un breve canto meditativo tipo Anima Christi tras el silencio).",
                },
            ],
            "rojo": [
                {
                    "titulo": "Canciones en la Comunión que no mencionan a Cristo ni a la Eucaristía",
                    "texto": "Usar en la sagrada Comunión canciones genéricas de valores humanos, de la naturaleza o cantos marianos que ignoran por completo la presencia real del Cuerpo y la Sangre de Cristo que se está recibiendo en ese preciso instante.",
                },
                {
                    "titulo": "Eliminar el silencio post-comunión por horror al vacío ('horror vacui')",
                    "texto": "Seguir cantando y tocando sin parar hasta que el sacerdote se pone de pie y dice «Oremos» priva a los fieles del momento más íntimo de oración personal con Jesús Eucaristía.",
                },
            ],
        },
        "adaptacion_tiempos": {
            "Tiempo Ordinario": {
                "espiritu": "Alimento del peregrino y comunión con la Palabra del Evangelio dominical.",
                "textos_sugeridos": "Salmo 33 ('Gusten y vean qué bueno es el Señor'), Salmo 22 ('El Señor es mi pastor', preparar la mesa), Discurso del Pan de Vida (Jn 6), Emaús ('Quédate con nosotros, Señor').",
                "criterio_musical": "Responsorial cálido, luminoso y caminante durante la procesión; recogimiento interior al concluir.",
            },
            "Adviento y Navidad": {
                "espiritu": "En Adviento: el anhelo del Emmanuel que viene a habitar en nosotros. En Navidad: Belén ('Casa del Pan'), donde adoramos al Verbo hecho carne.",
                "textos_sugeridos": "Adviento: Isaías 7, 14 ('La Virgen concebirá y dará a luz un hijo'), Salmo 84. Navidad: Juan 1, 14 ('Y el Verbo se hizo carne y vimos su gloria'), himnos de adoración del Misterio de la Encarnación.",
                "criterio_musical": "Tierno, contemplativo y profundamente teológico.",
            },
            "Cuaresma y Semana Santa": {
                "espiritu": "En los domingos de Cuaresma, las antífonas de comunión del Ciclo A dialogan directamente con los grandes Evangelios bautismales (la Samaritana y el Agua viva, el Ciego de nacimiento y la Luz, Lázaro y la Resurrección).",
                "textos_sugeridos": "Juan 4, 13-14 ('El que beba del agua que yo le daré...'), Juan 9, Salmo 90. Jueves Santo: 1 Corintios 11, 24-25 ('Esto es mi Cuerpo, que se entrega por ustedes'). Viernes Santo: Salmo 21 o Adoración de la Cruz.",
                "criterio_musical": "Sobrio, hondo y expresivo; el Viernes Santo con suma austeridad vocal.",
            },
            "Tiempo Pascual": {
                "espiritu": "Banquete con el Resucitado (como en Emaús y a orillas del lago de Tiberíades): «Cristo, nuestra Pascua, ha sido inmolado; celebremos el banquete con el Señor resucitado, aleluya» (1 Cor 5, 7-8).",
                "textos_sugeridos": "1 Corintios 5, 7-8; Juan 20, 27 ('Acerca tu mano y toca el lugar de los clavos'); Juan 10, 14 ('Yo soy el Buen Pastor, aleluya').",
                "criterio_musical": "Gozoso y pascual, incluyendo el «Aleluya» en la antífona de comunión.",
            },
        },
        "tratado_teologico": [
            {
                "id": "comunion-teologia-cirilo",
                "titulo": "1. Mistagogía Patrística de la Comunión: San Cirilo de Jerusalén y el Salmo 33",
                "parrafos": [
                    "En el año 348, el obispo San Cirilo de Jerusalén pronunció sus célebres Catequesis Mistagógicas ante los recién bautizados en la basílica del Santo Sepulcro. En la Catequesis V (n. 20) nos dejó la descripción más conmovedora de la procesión y del canto de Comunión en la Iglesia antigua: «Después de esto, ustedes oyen al cantor que con melodía divina los invita a la comunión de los Santos Misterios diciendo: 'Gusten y vean qué bueno es el Señor' (Sal 33, 9). No confíen el juicio al paladar corporal, sino a la fe indudable; porque al gustar no se les manda gustar pan y vino, sino el antítipo del Cuerpo y de la Sangre de Cristo. Al acercarse, pues, no vayan con las palmas de las manos extendidas ni con los dedos separados, sino haciendo con la mano izquierda un trono para la derecha, como quien va a recibir a un Rey».",
                    "Observemos cómo la IGMR 86 recoge intacta esta teología: el canto de comunión no es música ambiental para rellenar el tiempo que tarda la fila, sino el sacramento sonoro de la koinonía (comunión): mientras recibimos el único Cuerpo eucarístico de Cristo, nuestras voces múltiples se funden en una sola voz para manifestar que hemos llegado a ser un solo Cuerpo eclesial.",
                ],
            },
            {
                "id": "comunion-ley-evangelio",
                "titulo": "2. La «Ley del Eco Evangélico» en la Antífona de Comunión y el Silencio Sagrado",
                "parrafos": [
                    "Los liturgistas han observado una ley fascinante en la composición de las Antífonas de Comunión del Misal Romano y del Graduale: mientras el Introito mira hacia el misterio general del día y el Gradual medita el Antiguo Testamento, la Antífona de Comunión retoma casi siempre las palabras textuales pronunciadas por Jesús en el Evangelio proclamado media hora antes. ¿Por qué? Porque las dos mesas de la Misa (la Mesa de la Palabra y la Mesa de la Eucaristía, SC 56) son un solo banquete: la misma Palabra eterna del Padre que entró por nuestros oídos en el Evangelio es la que ahora recibimos sustancialmente en nuestros labios en la Comunión.",
                    "Y una vez concluida la procesión, el rito alcanza su reposo en el Silencio Sagrado (IGMR 45, 88). Como enseñaba el Papa Benedicto XVI en la Exhortación Apostólica Sacramentum Caritatis (n. 50 y 55), el silencio tras la Comunión no es una pausa vacía, sino el espacio interior donde el alma conversa corazón a corazón con su Señor antes de que el sacerdote recoja las preces de todos en la Oración después de la Comunión.",
                ],
            },
        ],
        "citas_magisteriales": [
            {
                "id_cita": "igmr-86",
                "doc_id": "igmr",
                "fuente": "Instrucción General del Misal Romano (IGMR)",
                "numeral": "n. 86",
                "año": "2002 / Tercera Edición Típica",
                "url_oficial": "https://www.vatican.va/roman_curia/congregations/ccdds/documents/rc_con_ccdds_doc_20030317_ordinamento-messale_sp.html#D._Liturgia_eucarística",
                "texto": "«Mientras el sacerdote toma el Sacramento, se inicia el canto de comunión, cuyo fin es expresar por la unidad de las voces la unión espiritual de quienes comulgan, demostrar la alegría del corazón y manifestar más claramente el carácter 'comunitario' de la procesión para recibir la Eucaristía. El canto se prolonga mientras se administra el Sacramento a los fieles. Pero si se ha de tener un himno después de la Comunión, el canto para la Comunión debe ser terminado oportunamente. Procura que también los cantores puedan comulgar cómodamente.»",
                "comentario_pastoral": "Define el momento exacto de inicio, los 3 fines teológicos y el deber de facilitar que los músicos del coro también comulguen con recogimiento.",
            },
            {
                "id_cita": "igmr-87-88",
                "doc_id": "igmr",
                "fuente": "Instrucción General del Misal Romano (IGMR)",
                "numeral": "nn. 87–88",
                "año": "2002 / Adaptación CECh",
                "url_oficial": "https://www.vatican.va/roman_curia/congregations/ccdds/documents/rc_con_ccdds_doc_20030317_ordinamento-messale_sp.html#D._Liturgia_eucarística",
                "texto": "«El canto lo ejecuta o el coro solo, o el coro o el cantor con el pueblo. Si no hay canto, se puede decir la antífona propuesta en el Misal... Terminada la distribución de la Comunión, si resulta oportuno, el sacerdote y los fieles oran en silencio por algún intervalo de tiempo. Si se quiere, toda la asamblea puede también cantar un salmo o algún otro canto de alabanza o un himno.»",
                "comentario_pastoral": "Distingue nítidamente el canto procesional durante la distribución (n. 86-87) del silencio sagrado y el eventual himno de acción de gracias posterior (n. 88).",
            },
        ],
        "criterios_musicales": [
            {
                "id": "com-crit-1",
                "categoria": "Forma Responsorial para Caminantes sin Cancionero",
                "titulo": "Antífona breve en labios de todos + Estrofas salmódicas/evangélicas por el Coro",
                "explicacion": "Durante la Comunión nadie lleva una hoja en la mano mientras camina por el pasillo central. Si se canta una canción de 4 estrofas distintas sin estribillo claro, solo cantará el coro. En cambio, cuando el estribillo es una antífona bíblica corta y luminosa (ej. «Gusten y vean qué bueno es el Señor» o «El Señor es mi pastor, nada me puede faltar»), toda la fila va cantando mientras camina hacia el altar.",
            },
            {
                "id": "com-crit-2",
                "categoria": "Organización Práctica para que Comulgue el Coro (IGMR 86)",
                "titulo": "Cómo distribuir el turno de comunión de los cantores e instrumentistas",
                "explicacion": "La IGMR 86 pide expresamente: «Procúrese que también los cantores puedan comulgar cómodamente». Existen dos modos excelentes:\n1) Que un ministro extraordinario o el diácono se acerque a dar la Comunión al coro al final de la fila mientras un instrumento suave o un solista mantiene la última estrofa.\n2) Que el coro comulgue en el primer o último turno de la procesión dejando unos compases de interludio instrumental suave antes de cerrar con la última antífona y entrar al silencio sagrado.",
            },
        ],
        "checklist_discernimiento": [
            {
                "id": "chk-com-1",
                "pregunta": "¿El texto tiene un contenido claramente Eucarístico (Pan de Vida, Cuerpo y Sangre de Cristo, Banquete Pascual) o toma las palabras del Evangelio del día?",
                "pista": "IGMR 86–87.",
            },
            {
                "id": "chk-com-2",
                "pregunta": "¿Comienza el canto apenas comulga el sacerdote y permite que los fieles respondan un estribillo breve de memoria mientras caminan en la fila?",
                "pista": "IGMR 86.",
            },
            {
                "id": "chk-com-3",
                "pregunta": "¿Se detiene la música al terminar la distribución de la Comunión para respetar el tiempo de Silencio Sagrado antes del «Oremos»?",
                "pista": "IGMR 88.",
            },
        ],
    },

    # =========================================================================
    # 16. CANTO DE SALIDA / ENVÍO (RECESSUS AD LIBITUM)
    # =========================================================================
    "salida": {
        "slug": "salida",
        "titulo": "Canto de Salida / Envío",
        "nombre_latino": "Recessus (Cantus ad dimissionem · Ad libitum)",
        "parte_nombre": "IV. Rito de Conclusión",
        "cita_principal": "IGMR 90 · MS 36",
        "subtitulo": "El canto o pieza instrumental facultativa que acompaña la retirada del sacerdote y los ministros tras la bendición y el envío misionero («Pueden ir en paz — Demos gracias a Dios»).",
        "ficha_identidad": [
            {
                "id": "sal-out-naturaleza",
                "atributo": "Naturaleza Litúrgica",
                "valor": "Facultativo / Costumbre legítima (No prescrito por las rúbricas del Misal)",
                "detalle": "Litúrgicamente la Misa concluye con el diálogo de envío: «Pueden ir en paz — Demos gracias a Dios» (IGMR 90). Por eso el Misal Romano no trae una 'Antífona de Salida'; sin embargo, acompañar la retirada procesional de los ministros con un canto o pieza de órgano es una tradición laudable (MS 36).",
            },
            {
                "id": "sal-out-prioridad",
                "atributo": "Verdadera Prioridad del Rito de Conclusión (MS 29)",
                "valor": "El Saludo, la Bendición y el «Pueden ir en paz — Demos gracias a Dios» (Primer Grado)",
                "detalle": "Antes que preocuparse del canto de salida, lo propiamente litúrgico y de Primer Grado (MS 29) es responder cantando al saludo final, a la bendición sacerdotal y a la despedida diaconal.",
            },
            {
                "id": "sal-out-repertorio",
                "atributo": "Repertorio Ideal",
                "valor": "1) Antífonas Marianas · 2) Himnos de alabanza o envío · 3) Postludio instrumental",
                "detalle": "Es el lugar privilegiado para el canto a la Santísima Virgen María (especialmente las 4 Antífonas Marianas del año litúrgico), un himno breve de acción de gracias/misión o un postludio solemne de órgano.",
            },
            {
                "id": "sal-out-duracion",
                "atributo": "Duración Recomendada",
                "valor": "Breve y conclusiva (1 estrofa con estribillo o antífona mariana)",
                "detalle": "Acompaña la veneración final del altar y el regreso de los ministros a la sacristía.",
            },
        ],
        "opciones_igmr": [
            {
                "numero": "Opción 1 (Tradición Universal)",
                "titulo": "Las Cuatro Antífonas Marianas según el Tiempo Litúrgico",
                "descripcion": "Cantar la antífona mariana propia de la estación: Alma Redemptoris Mater (Adviento y Navidad), Ave Regina caelorum (hasta Miércoles Santo), Regina caeli (Tiempo Pascual) o Salve Regina (Tiempo Ordinario), o un canto mariano vernáculo digno.",
            },
            {
                "numero": "Opción 2 (Canto de Alabanza o Envío Misionero)",
                "titulo": "Himno breve de alabanza trinitaria o de misión apostólica",
                "descripcion": "Un salmo breve de alabanza (Sal 116 'Alaben al Señor todas las naciones', Sal 150) o un himno que prolongue en la vida cotidiana la misión recibida.",
            },
            {
                "numero": "Opción 3 (Postludio Instrumental)",
                "titulo": "Postludio de órgano o instrumentos sacros",
                "descripcion": "En los domingos y solemnidades (fuera de Cuaresma), una pieza instrumental festiva mientras los ministros se retiran a la sacristía.",
            },
            {
                "numero": "Opción 4 (Silencio en Cuaresma y Viernes Santo)",
                "titulo": "Retirada en silencio reverente",
                "descripcion": "En Cuaresma (donde no se tocan instrumentos solos, IGMR 313) es muy expresivo retirarse en silencio o cantando a cappella una breve antífona penitencial o mariana; en Jueves y Viernes Santo la retirada es en silencio absoluto.",
            },
        ],
        "textos_oficiales": {
            "titulo": "Fórmulas Oficiales de Despedida del Misal Romano y las 4 Antífonas Marianas",
            "nota": "En el Tiempo Pascual (desde la Vigilia Pascual hasta el Domingo de Pentecostés inclusive, y en la Octava de Pascua), a la despedida y a su respuesta se añade el doble «Aleluya, aleluya».",
            "items": [
                {
                    "ocasion": "Diálogo de Envío (Primer Grado · IGMR 90, 168)",
                    "latin": "Diac. / Sac.: Ite, missa est. (En Pascua: Ite, missa est, allelúia, allelúia.)\nPop.: Deo grátias. (En Pascua: Deo grátias, allelúia, allelúia.)",
                    "espanol": "Diác. / Sac.: Pueden ir en paz. (O bien: Anuncien a todos la alegría del Señor; pueden ir en paz / Glorifiquen al Señor con su vida; pueden ir en paz.)\nPueblo: «Demos gracias a Dios.» (En Pascua: «Demos gracias a Dios, aleluya, aleluya.»)",
                },
                {
                    "ocasion": "Tiempo Pascual · Antífona Mariana «Regina caeli»",
                    "latin": "Regína cæli, lætáre, allelúia; quia quem meruísti portáre, allelúia, resurréxit, sicut dixit, allelúia: ora pro nobis Deum, allelúia.",
                    "espanol": "«Reina del cielo, alégrate, aleluya; porque el Señor, a quien has merecido llevar, aleluya, ha resucitado, según su palabra, aleluya. Ruega al Señor por nosotros, aleluya.»",
                },
                {
                    "ocasion": "Tiempo Ordinario · Antífona Mariana «Salve Regina»",
                    "latin": "Salve, Regína, Mater misericórdiæ, vita, dulcédo, et spes nostra, salve... O clemens, O pia, O dulcis Virgo María.",
                    "espanol": "«Dios te salve, Reina y Madre de misericordia, vida, dulzura y esperanza nuestra, Dios te salve... ¡Oh clemente, oh piadosa, oh dulce Virgen María!»",
                },
            ],
        },
        "semaforo": {
            "verde": [
                {
                    "titulo": "Esperar siempre a que el pueblo responda «Demos gracias a Dios» antes de iniciar el canto",
                    "texto": "Jamás empezar a rasguear o tocar encima de la bendición del sacerdote ni antes de que la asamblea haya respondido «Demos gracias a Dios» al envío.",
                },
                {
                    "titulo": "Privilegiar a la Santísima Virgen María como estrella del envío misionero",
                    "texto": "Despedir la asamblea dominical con un canto mariano sobrio y bello (la Salve Regina, el Regina Caeli en Pascua o los cantos marianos tradicionales de la piedad chilena) une la Eucaristía con la Madre de la Iglesia.",
                },
            ],
            "amarillo": [
                {
                    "titulo": "Jueves Santo y Viernes Santo: Prohibido el canto de salida",
                    "texto": "El Jueves Santo termina con la procesión al Monumento con el himno Pange lingua / Tantum ergo y luego todos se retiran en silencio; el Viernes Santo concluye con la Oración sobre el pueblo y todos se retiran en silencio absoluto sin bendición ni canto.",
                },
                {
                    "titulo": "En Navidad: el momento ideal para los Villancicos tradicionales",
                    "texto": "Mientras se adora la imagen del Niño Jesús al final de la Misa de Nochebuena o de Navidad, el canto de salida es el espacio más natural y festivo para los villancicos tradicionales chilenos y universales.",
                },
            ],
            "rojo": [
                {
                    "titulo": "Tapar la bendición o el «Pueden ir en paz» con la introducción musical",
                    "texto": "El Rito de Conclusión es el envío apostólico de la Iglesia al mundo; interrumpirlo por apuro musical resta solemnidad a la bendición sacerdotal.",
                },
                {
                    "titulo": "Cantar 4 estrofas largas obligando a la gente a quedarse de pie cuando la Misa ya terminó",
                    "texto": "Una sola estrofa con su estribillo (45 a 60 segundos) basta para acompañar la veneración del altar y la retirada del sacerdote a la sacristía.",
                },
            ],
        },
        "adaptacion_tiempos": {
            "Adviento y Navidad": {
                "espiritu": "Con María la Virgen esperamos al Salvador (Adviento) y adoramos al Niño nacido en Belén (Navidad).",
                "textos_sugeridos": "Adviento: Alma Redemptoris Mater, 'Santa María de la Esperanza', 'El Ángelus'. Navidad: Villancicos tradicionales ('Adeste fideles', 'Noche de paz', 'Señora Doña María').",
                "criterio_musical": "Gozoso y familiar.",
            },
            "Cuaresma y Semana Santa": {
                "espiritu": "Recogimiento penitencial camino a la Pascua.",
                "textos_sugeridos": "Ave Regina caelorum, Stabat Mater (1 estrofa), canto penitencial breve a cappella o retirada en silencio reverente (IGMR 313).",
                "criterio_musical": "Sin postludios instrumentales festivos; en Jueves y Viernes Santo silencio absoluto.",
            },
            "Tiempo Pascual": {
                "espiritu": "Envío misionero de los testigos de la Resurrección con el doble Aleluya («Pueden ir en paz, aleluya, aleluya»).",
                "textos_sugeridos": "Regina caeli laetare ('Reina del cielo, alégrate, aleluya'), himnos pascuales de triunfo.",
                "criterio_musical": "Radiante y glorioso.",
            },
            "Tiempo Ordinario": {
                "espiritu": "La Iglesia sale al mundo para santificar las realidades temporales alabando y bendiciendo a Dios (IGMR 90).",
                "textos_sugeridos": "Salve Regina, cantos marianos o salmos breves de alabanza (Sal 116).",
                "criterio_musical": "Vital, noble y conciso.",
            },
        },
        "tratado_teologico": [
            {
                "id": "salida-teologia-missa",
                "titulo": "1. Teología del «Ite, missa est»: Por qué la Eucaristía se llama «Misa»",
                "parrafos": [
                    "En el latín tardío de la cancillería romana, el sustantivo missa (forma tardía de missio, del verbo mittere: enviar, despedir) significaba el acto solemne de despedida y envío de una asamblea. Tan decisivo consideraban los primeros cristianos este envío misionero al mundo que la fórmula final del diácono —«Ite, missa est»— terminó dando nombre a todo el sacrificio eucarístico: «la Misa».",
                    "Como profundizó el Papa Benedicto XVI en la Exhortación Apostólica Sacramentum Caritatis (n. 51): «En la antigüedad 'missa' significaba simplemente 'dimissio', despedida. Sin embargo, en el uso cristiano ha adquirido un sentido cada vez más profundo. La expresión 'dimissio' se transforma en realidad en 'missio' (misión). Este saludo expresa sintéticamente la naturaleza misionera de la Iglesia». La Eucaristía no se encierra en las paredes del templo: terminada la celebración sacramental, comienza la 'liturgia de la vida cotidiana' en la caridad, el trabajo y el anuncio del Evangelio.",
                ],
            },
        ],
        "citas_magisteriales": [
            {
                "id_cita": "igmr-90",
                "doc_id": "igmr",
                "fuente": "Instrucción General del Misal Romano (IGMR)",
                "numeral": "n. 90",
                "año": "2002 / Tercera Edición Típica",
                "url_oficial": "https://www.vatican.va/roman_curia/congregations/ccdds/documents/rc_con_ccdds_doc_20030317_ordinamento-messale_sp.html#E._Rito_de_conclusión",
                "texto": "«Al rito de conclusión pertenecen: a) Breves avisos, si fuere necesario. b) El saludo y la bendición del sacerdote, que en ciertos días y ocasiones se enriquece y se expresa con la oración sobre el pueblo o con otra fórmula más solemne. c) La despedida del pueblo por parte del diácono o del sacerdote, para que cada uno regrese a sus buenas obras alabando y bendiciendo a Dios. d) El beso del altar por parte del sacerdote y del diácono y después la inclinación profunda al altar de parte del sacerdote, del diácono y de los demás ministros.»",
                "comentario_pastoral": "Muestra que el rito oficial concluye con el envío y la veneración del altar; cualquier canto de salida acompaña únicamente esta retirada.",
            },
        ],
        "criterios_musicales": [
            {
                "id": "sal-out-crit-1",
                "categoria": "Economía y Sobriedad",
                "titulo": "Una estrofa bien cantada vale más que tres estrofas con el templo vaciándose",
                "explicacion": "El Canto de Salida cumple su función ritual durante los 30 a 50 segundos que el sacerdote tarda en besar el altar, hacer la inclinación ante el Crucifijo y caminar hacia la sacristía. Elegir una sola estrofa luminosa (o una antífona mariana completa) permite que toda la asamblea la cante de pie hasta el último acorde antes de retirarse.",
            },
        ],
        "checklist_discernimiento": [
            {
                "id": "chk-sal-out-1",
                "pregunta": "¿Se espera a que el pueblo haya respondido «Demos gracias a Dios» al envío antes de iniciar el canto de salida?",
                "pista": "IGMR 90 / MS 29.",
            },
            {
                "id": "chk-sal-out-2",
                "pregunta": "Si estamos en Cuaresma o Semana Santa, ¿se respeta la sobriedad del tiempo (evitando cantos festivos o postludios instrumentales, y guardando silencio absoluto el Jueves y Viernes Santo)?",
                "pista": "IGMR 313.",
            },
        ],
    },
}
