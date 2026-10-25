"""
Servicio y base de conocimiento estructurada para la sección de Formación Litúrgica.
Incluye:
- Las 5 grandes áreas de Formación Litúrgica
- Las 4 partes estructurales de la Santa Misa y sus 16 momentos (100% completos en DETALLE_MOMENTOS)
- Sub-vistas dedicadas por momento (Resumen, Tratado y Documentos, Composición, Repertorio)
- Biblioteca de Documentos Oficiales del Magisterio (IGMR, Musicam Sacram, Sacrosanctum Concilium, Tra le Sollecitudini, OGLH, CONALI)
  con lector integrado y proxy hacia Vatican.va.
- Contenido profundo de Año Litúrgico, Antología Patrística, Guía del Músico y Otras Celebraciones.
"""

from typing import Dict, List, Optional, Any, Tuple
from models import Cancion
from services.tag_service import tag_matches
from services.catalog_service import sort_songs
from services.liturgy_moments_p1 import MOMENTOS_PARTE_1
from services.liturgy_moments_p2 import MOMENTOS_PARTE_2
from services.liturgy_areas_content import (
    MATRIZ_ANO_LITURGICO,
    ANTIFONAS_MAYORES_O,
    TRATADO_TIEMPOS_DETALLADO,
    ANTOLOGIA_PATRISTICA,
    GUIA_MUSICO_TRATADO,
    OTRAS_CELEBRACIONES_DETALLE,
)


# ============================================================
# 1. LAS 5 GRANDES ÁREAS DE FORMACIÓN LITÚRGICA
# ============================================================
AREAS_FORMACION: List[Dict[str, Any]] = [
    {
        "id": "santa-misa",
        "titulo": "La Santa Misa",
        "subtitulo": "Rito, Momentos, Ordinario y Propio",
        "icono": "🕊️",
        "descripcion": "Estudio mistagógico, normativo y musical de los 16 momentos de la celebración eucarística: desde los Ritos Iniciales hasta el Rito de Conclusión.",
        "url_endpoint": "ver_formacion",
        "badge": "16 momentos",
    },
    {
        "id": "ano-liturgico",
        "titulo": "Año Litúrgico y Tiempos",
        "subtitulo": "Adviento, Navidad, Cuaresma, Triduo, Pascua y T. Ordinario",
        "icono": "🗓️",
        "descripcion": "Matriz sinóptica, Antífonas de la 'O' y criterios espirituales, vocales e instrumentales propios de cada tiempo litúrgico.",
        "url_endpoint": "ver_formacion_tiempos",
        "badge": "6 tiempos",
    },
    {
        "id": "fundamentos-magisterio",
        "titulo": "Biblioteca y Documentos",
        "subtitulo": "IGMR, Musicam Sacram, Sacrosanctum Concilium, Pío X, OGLH y Padres",
        "icono": "📜",
        "descripcion": "Los documentos oficiales de la Iglesia universal y en Chile con visor embebido, los Tres Grados de participación y la antología patrística.",
        "url_endpoint": "ver_formacion_documentos",
        "badge": "6 documentos",
    },
    {
        "id": "guia-musico",
        "titulo": "Guía para el Músico y Compositor",
        "subtitulo": "Prosodia, Formas Musicales, Tesitura, Instrumentación y Ensayo",
        "icono": "🎼",
        "descripcion": "Tratado práctico de prosodia castellana con ejemplos comparados, las 5 formas musicales litúrgicas, registro congregacional y dirección coral.",
        "url_endpoint": "ver_formacion_musico",
        "badge": "5 capítulos",
    },
    {
        "id": "otras-celebraciones",
        "titulo": "Otras Celebraciones y Liturgias",
        "subtitulo": "Adoración Eucarística, Liturgia de las Horas y Sacramentos",
        "icono": "🕯️",
        "descripcion": "Estructura ritual y textos bilingües (Tantum Ergo, Benedictus, Magnificat, Nunc Dimittis, In Paradisum) para la Adoración, el Oficio Divino y los Sacramentos.",
        "url_endpoint": "ver_formacion_otras",
        "badge": "Guías rituales",
    },
]


# ============================================================
# 2. SUB-VISTAS DEDICADAS DE CADA MOMENTO DE LA MISA
# ============================================================
SUBVISTAS_MOMENTO: List[Dict[str, str]] = [
    {
        "id": "resumen",
        "titulo": "1. Resumen, Textos y Criterios Principales",
        "titulo_corto": "Resumen y Criterios",
        "descripcion": "Ficha de identidad ritual, opciones del Misal Romano, textos oficiales Latín/Español, Semáforo Parroquial y adaptación por Tiempo Litúrgico.",
    },
    {
        "id": "teologia",
        "titulo": "2. Tratado Teológico, Historia y Magisterio",
        "titulo_corto": "Tratado y Magisterio",
        "descripcion": "Mistagogía del rito, fuentes patrísticas, evolución histórica y citas oficiales desplegables con visor embebido de Vatican.va.",
    },
    {
        "id": "composicion",
        "titulo": "3. Composición, Práctica y Checklist",
        "titulo_corto": "Composición y Práctica",
        "descripcion": "Forma musical, ámbito vocal congregacional, prosodia castellana, dirección en vivo y checklist de discernimiento.",
    },
    {
        "id": "repertorio",
        "titulo": "4. Repertorio y Audios Aplicados",
        "titulo_corto": "Repertorio y Audios",
        "descripcion": "Obras del catálogo conectadas a este momento con reproductor, partituras interactivas y salmos/himnos sugeridos.",
    },
]


# ============================================================
# 3. BIBLIOTECA DE DOCUMENTOS MAGISTERIALES (CON EMBED / LECTOR)
# ============================================================
DOCUMENTOS_MAGISTERIALES: Dict[str, Dict[str, Any]] = {
    "igmr": {
        "id": "igmr",
        "sigla": "IGMR",
        "titulo": "Instrucción General del Misal Romano",
        "subtitulo": "Tercera Edición Típica (2002) · Congregación para el Culto Divino y la Disciplina de los Sacramentos",
        "fecha": "2002 (Adaptación CECh)",
        "url_oficial": "https://www.vatican.va/roman_curia/congregations/ccdds/documents/rc_con_ccdds_doc_20030317_ordinamento-messale_sp.html",
        "embed_proxy_allowed": True,
        "resumen": "Norma teológica, ritual y pastoral suprema para la celebración de la Eucaristía en el Rito Romano. Define la estructura de la Misa, el sentido de cada canto procesional y del Ordinario, los ministerios y el uso de los instrumentos según los tiempos litúrgicos.",
        "secciones_clave": [
            {
                "numeral": "IGMR 39–41",
                "titulo": "Importancia del canto en la celebración y primacía del canto gregoriano",
                "ancla": "#II._ESTRUCTURA_DE_LA_MISA,_SUS_ELEMENTOS_Y_SUS_PARTES",
                "extracto": "«Amonesta el Apóstol a los fieles que se reúnen esperando la venida de su Señor, que canten todos juntos con salmos, himnos y cánticos espirituales (cf. Col 3, 16), pues el canto es signo de la exultación del corazón (cf. Hch 2, 46). Por tanto, con razón decía San Agustín: 'Cantar es propio de quien ama'... Se ha de poner gran cuidado para que no falte el canto de los ministros y del pueblo en las celebraciones que se llevan a cabo los domingos y fiestas de precepto... En igualdad de circunstancias, dése el primer lugar al canto gregoriano, como propio de la Liturgia romana.»",
            },
            {
                "numeral": "IGMR 47–48",
                "titulo": "El Canto de Entrada (Introitus) y sus cuatro opciones legítimas",
                "ancla": "#B._Ritos_iniciales",
                "extracto": "«Una vez que el pueblo se ha reunido, cuando avanza el sacerdote con el diácono y los ministros, se da comienzo al canto de entrada. La finalidad de este canto es abrir la celebración, fomentar la unión de quienes se han reunido y elevar sus pensamientos a la contemplación del misterio litúrgico o de la fiesta, acompañando la procesión del sacerdote y los ministros. Se puede utilizar, o bien la antífona con su salmo como se encuentra en el Graduale Romanum o en el Graduale Simplex, o bien otro canto que sea congruente con la acción sagrada, con el día o el tiempo del año, cuyo texto haya sido aprobado por la Conferencia Episcopal.»",
            },
            {
                "numeral": "IGMR 51–53",
                "titulo": "La Aspersión Dominical, el Señor ten piedad (Kyrie) y el Gloria in excelsis",
                "ancla": "#B._Ritos_iniciales",
                "extracto": "«Los domingos, especialmente en el Tiempo Pascual, en lugar del acto penitencial acostumbrado, puede hacerse alguna vez la bendición y aspersión del agua en memoria del bautismo... Después del acto penitencial, se empieza siempre el Señor, ten piedad, a no ser que éste haya formado ya parte del mismo acto penitencial... El Gloria es un antiquísimo y venerable himno con que la Iglesia, congregada en el Espíritu Santo, glorifica a Dios Padre y al Cordero y le presenta sus súplicas. El texto de este himno no puede cambiarse por otro.»",
            },
            {
                "numeral": "IGMR 61–64, 67–71",
                "titulo": "El Salmo Responsorial, la Secuencia, el Aleluya, el Credo y la Oración Universal",
                "ancla": "#C._Liturgia_de_la_Palabra",
                "extracto": "«Después de la primera lectura sigue el salmo responsorial, que es parte integrante de la Liturgia de la Palabra y tiene gran importancia litúrgica y pastoral, porque favorece la meditación de la Palabra de Dios... Después de la lectura que precede inmediatamente al Evangelio, se canta el Aleluya u otro canto determinado por las rúbricas... La secuencia, que, fuera de los días de Pascua y de Pentecostés, es facultativa, se canta antes del Aleluya.»",
            },
            {
                "numeral": "IGMR 74, 79b, 81, 83, 86–88",
                "titulo": "Cantos de la Liturgia Eucarística (Dones, Santo, Padrenuestro, Fracción del Pan y Comunión)",
                "ancla": "#D._Liturgia_eucarística",
                "extracto": "«El canto de preparación de los dones acompaña la procesión en que se llevan los dones... En el Santo, toda la asamblea, uniéndose a las jerarquías celestiales, canta la santidad de Dios... La súplica Cordero de Dios acompaña la fracción del pan y puede repetirse cuantas veces sea necesario hasta que haya terminado el rito... Mientras el sacerdote toma el Sacramento, se inicia el canto de comunión, cuyo fin es expresar por la unidad de las voces la unión espiritual de quienes comulgan.»",
            },
            {
                "numeral": "IGMR 312–313",
                "titulo": "El Coro, el Órgano y los Instrumentos según los Tiempos Litúrgicos",
                "ancla": "#V._DISPOSICIÓN_Y_ORNATO_DE_LAS_IGLESIAS_PARA_LA_CELEBRACIÓN_EUCARÍSTICA",
                "extracto": "«En Adviento el órgano y otros instrumentos musicales deben usarse con aquella moderación que conviene a la índole del tiempo, sin que se anticipe la plena alegría de la Natividad del Señor. En Cuaresma se permite el sonido del órgano y de los otros instrumentos solamente para sostener el canto, exceptuando el domingo Laetare (IV de Cuaresma), las solemnidades y las fiestas.»",
            },
        ],
    },
    "musicam-sacram": {
        "id": "musicam-sacram",
        "sigla": "MS",
        "titulo": "Instrucción Musicam Sacram sobre la Música en la Sagrada Liturgia",
        "subtitulo": "Sagrada Congregación de Ritos · Promulgada bajo el pontificado de San Pablo VI",
        "fecha": "5 de marzo de 1967",
        "url_oficial": "https://www.vatican.va/archive/hist_councils/ii_vatican_council/documents/vat-ii_instr_19670305_musicam-sacram_lt.html",
        "url_pdf_es": "https://www.bcn.cl/obtarchivo?id=repositorio/10221/11831/1/Musicam_sacram.pdf",
        "embed_proxy_allowed": True,
        "resumen": "Carta magna postconciliar de la música litúrgica. Define qué es la música sagrada, el ministerio del coro y del salmista, la participación activa (interior y vocal) de la asamblea y los célebres Tres Grados de participación progresiva del canto en la Misa.",
        "secciones_clave": [
            {
                "numeral": "MS 4",
                "titulo": "Definición y Géneros de la Música Sagrada",
                "ancla": "",
                "extracto": "«Se entiende por música sagrada aquella que, creada para la celebración del culto divino, posee las cualidades de santidad y de perfección de formas. Con el nombre de música sagrada se designan aquí: el canto gregoriano, la polifonía sagrada antigua y moderna en sus distintos géneros, la música sagrada para órgano y otros instrumentos admitidos, y el canto sagrado popular, litúrgico y religioso.»",
            },
            {
                "numeral": "MS 7, 28–31",
                "titulo": "Los Tres Grados de Participación en la Misa Cantada",
                "ancla": "",
                "extracto": "«Para la solemnización de la Misa se seguirán tres grados de participación progresiva. El primer grado podrá emplearse solo; el segundo y el tercero no serán nunca empleados, íntegra o parcialmente, sin el primero. Así, los fieles serán siempre orientados hacia una plena participación en el canto.»",
            },
            {
                "numeral": "MS 15–17",
                "titulo": "Participación interior, escucha activa y silencio sagrado",
                "ancla": "",
                "extracto": "«La participación de los fieles debe ser ante todo interior, por la cual se unen en espíritu a lo que pronuncian o escuchan, y cooperan a la gracia divina. Pero la participación debe ser también exterior, a fin de que la unión interior se exprese por los gestos, las actitudes corporales, las aclamaciones, las respuestas y el canto. Se debe también formar a los fieles para que sepan elevar su espíritu a Dios mediante la escucha interior de lo que cantan los ministros o el coro.»",
            },
            {
                "numeral": "MS 19–24",
                "titulo": "Ministerio Litúrgico del Coro (Capilla Musical) y del Cantor",
                "ancla": "",
                "extracto": "«El coro o capilla musical o schola cantorum merece una atención especial por el ministerio litúrgico que desempeña. Su función, según las normas del Concilio Vaticano II, ha adquirido una importancia y un peso mayores: le toca asegurar la justa interpretación de las partes que le corresponden según los distintos géneros de canto y promover la participación activa de los fieles en el canto.»",
            },
            {
                "numeral": "MS 32–36",
                "titulo": "El Canto del Ordinario y del Propio de la Misa",
                "ancla": "",
                "extracto": "«Los cantos que se llaman 'Ordinario de la Misa', si son cantados a varias voces musicales, pueden ser ejecutados por el coro según las normas acostumbradas, sea a cappella, sea con acompañamiento de instrumentos, con tal de que el pueblo no quede totalmente excluido de la participación en el canto... Sin embargo, el Sanctus y el Pater Noster conviene que sean cantados por todo el pueblo junto con el sacerdote.»",
            },
        ],
    },
    "sacrosanctum-concilium": {
        "id": "sacrosanctum-concilium",
        "sigla": "SC",
        "titulo": "Constitución Sacrosanctum Concilium sobre la Sagrada Liturgia (Cap. VI)",
        "subtitulo": "Concilio Vaticano II · Promulgada por el Papa San Pablo VI",
        "fecha": "4 de diciembre de 1963",
        "url_oficial": "https://www.vatican.va/archive/hist_councils/ii_vatican_council/documents/vat-ii_const_19631204_sacrosanctum-concilium_sp.html",
        "embed_proxy_allowed": True,
        "resumen": "El Capítulo VI (nn. 112–121) de la primera Constitución del Concilio Vaticano II sienta los cimientos teológicos de la música sacra como «parte necesaria o integral de la Liturgia solemne», la participación activa del pueblo, la conservación del tesoro musical y la vocación de los compositores.",
        "secciones_clave": [
            {
                "numeral": "SC 112",
                "titulo": "Dignidad de la Música Sagrada como Parte Integral de la Liturgia",
                "ancla": "",
                "extracto": "«La tradición musical de la Iglesia universal constituye un tesoro de valor inestimable, que sobresale entre las demás expresiones artísticas, principalmente porque el canto sagrado, unido a las palabras, constituye una parte necesaria o integral de la Liturgia solemne... Por tanto, la música sagrada será tanto más santa cuanto más íntimamente esté unida a la acción litúrgica, ya sea expresando con mayor delicadeza la oración o fomentando la unanimidad, ya sea enriqueciendo de mayor solemnidad los ritos sagrados.»",
            },
            {
                "numeral": "SC 114, 116, 118",
                "titulo": "Conservación del Tesoro Coral, Canto Gregoriano, Polifonía y Canto Popular",
                "ancla": "",
                "extracto": "«Consérvese y cultívese con sumo cuidado el tesoro de la música sagrada. Foméntense diligentemente las Scholae cantorum, sobre todo en las iglesias catedrales... La Iglesia reconoce el canto gregoriano como el propio de la liturgia romana; por eso, en igualdad de circunstancias, hay que darle el primer lugar en las acciones litúrgicas. Los demás géneros de música sagrada, y en particular la polifonía, de ninguna manera han de excluirse en la celebración de los oficios divinos... Foméntese con empeño el canto religioso popular.»",
            },
            {
                "numeral": "SC 120–121",
                "titulo": "El Órgano, los Instrumentos y la Vocación de los Compositores Cristianos",
                "ancla": "",
                "extracto": "«Téngase en gran estima en la Iglesia latina el órgano de tubos, como instrumento musical tradicional, cuyo sonido puede aportar un esplendor notable a las ceremonias eclesiásticas y levantar poderosamente las almas hacia Dios... Los compositores verdaderamente cristianos deben sentirse llamados a cultivar la música sagrada y a acrecentar su tesoro. Compongan obras que presenten las características de verdadera música sagrada y que no sólo puedan ser cantadas por las mayores Scholae cantorum, sino que también estén al alcance de los coros más modestos y fomenten la participación activa de toda la asamblea de los fieles. Los textos destinados al canto sagrado deben estar de acuerdo con la doctrina católica; más aún, deben tomarse principalmente de la Sagrada Escritura y de las fuentes litúrgicas.»",
            },
        ],
    },
    "tra-le-sollecitudini": {
        "id": "tra-le-sollecitudini",
        "sigla": "TLS (Pío X)",
        "titulo": "Motu Proprio «Tra le sollecitudini» sobre la Música Sagrada",
        "subtitulo": "Papa San Pío X · En la festividad de Santa Cecilia, patrona de la música sacra",
        "fecha": "22 de noviembre de 1903",
        "url_oficial": "https://www.vatican.va/content/pius-x/es/motu_proprio/documents/hf_p-x_motu-proprio_19031122_tra-le-sollecitudini.html",
        "embed_proxy_allowed": True,
        "resumen": "Documento fundacional del movimiento litúrgico moderno. Acuñó el concepto de «participación activa» de los fieles y definió como código jurídico las tres notas esenciales de toda música litúrgica: Santidad, Bondad de las formas (perfección artística) y Universalidad.",
        "secciones_clave": [
            {
                "numeral": "TLS 1–2",
                "titulo": "Las Tres Cualidades Intrínsecas: Santidad, Bondad de las Formas y Universalidad",
                "ancla": "",
                "extracto": "«La música sagrada, como parte integrante de la liturgia solemne, participa de su fin general, que es la gloria de Dios y la santificación y edificación de los fieles... Debe, por consiguiente, poseer en grado eminente las cualidades propias de la liturgia, y en particular la santidad y la bondad de las formas, de donde nace espontáneo otro carácter suyo: la universalidad. Debe ser santa, y por lo tanto excluir todo lo profano, y no sólo en sí misma, sino en el modo en que la interpreten los mismos cantores. Debe ser arte verdadero, porque no es posible que de otro modo tenga sobre el ánimo de quien la oye aquella eficacia que la Iglesia se propone obtener al admitir en su liturgia el arte de los sonidos.»",
            },
            {
                "numeral": "TLS 7–9",
                "titulo": "Subordinación de la Música al Texto Litúrgico",
                "ancla": "",
                "extracto": "«El texto litúrgico ha de cantarse como está en los libros, sin alteración o posposición de palabras, sin vanas repeticiones, sin separar las sílabas, y siempre de modo que pueda ser entendido por los fieles que lo escuchan.»",
            },
        ],
    },
    "oglh": {
        "id": "oglh",
        "sigla": "OGLH",
        "titulo": "Ordenación General de la Liturgia de las Horas (Cap. V: El Canto en el Oficio)",
        "subtitulo": "Sagrada Congregación para el Culto Divino · Promulgada bajo San Pablo VI",
        "fecha": "2 de febrero de 1971",
        "url_oficial": "https://www.vatican.va/roman_curia/congregations/ccdds/documents/rc_con_ccdds_doc_20000630_ordinamento-liturgia-ore_lt.html",
        "embed_proxy_allowed": True,
        "resumen": "Los numerales 100–139 y 268–284 de la OGLH contienen el tratado más profundo del Magisterio sobre los modos de cantar los Salmos (en directo, antifonal y responsorial), el sentido de las antífonas y la dignidad de los Cánticos Evangélicos.",
        "secciones_clave": [
            {
                "numeral": "OGLH 268–270",
                "titulo": "El Canto de los Salmos y la Celebración Cantada del Oficio",
                "ancla": "",
                "extracto": "«En las rúbricas y normas de esta Ordenación se emplean de ordinario las palabras 'decir' o 'proclamar', tanto si la celebración se hace con canto como sin él. Sin embargo, debe recomendarse vivamente a los que rezan el Oficio en coro o en común el uso del canto, como algo que responde mejor a la naturaleza de esta oración y es indicio de mayor solemnidad y de una unión más profunda de los corazones en la alabanza divina.»",
            },
            {
                "numeral": "OGLH 279–282",
                "titulo": "Qué Elementos Tienen Prioridad para ser Cantados en Laudes y Vísperas",
                "ancla": "",
                "extracto": "«Aunque una celebración no pueda ser cantada íntegramente, es muy laudable aplicar el principio de la 'solemnización progresiva': cantar en primer lugar las aclamaciones, las respuestas al saludo del sacerdote y a las preces, y el Padre Nuestro; en segundo lugar, el himno y el Cántico Evangélico (Benedictus y Magnificat); y en tercer lugar, los salmos y cánticos con sus antífonas.»",
            },
        ],
    },
    "conali-chile": {
        "id": "conali-chile",
        "sigla": "CECh / CONALI",
        "titulo": "Orientaciones de la Conferencia Episcopal de Chile y CONALI",
        "subtitulo": "Comisión Nacional de Liturgia · Adaptaciones de la IGMR y Orientaciones Pastorales para Chile",
        "fecha": "Edición Chilena del Misal Romano",
        "url_oficial": "https://www.iglesia.cl/",
        "embed_proxy_allowed": False,
        "resumen": "Criterios pastorales y normativos propios de las diócesis de Chile sobre la aprobación de cantos litúrgicos, el respeto irrestricto de los textos del Ordinario, la formación de coros parroquiales y la inculturación sobria de nuestras expresiones musicales.",
        "secciones_clave": [
            {
                "numeral": "CECh IGMR 48 / 74 / 87",
                "titulo": "Criterio sobre el «Otro canto congruente» en las parroquias chilenas",
                "ancla": "",
                "extracto": "En la adaptación para Chile, cuando se emplea la cuarta opción en los cantos procesionales (Entrada, Dones, Comunión), debe verificarse que el texto exprese fielmente el misterio litúrgico del día y la doctrina católica, evitando sustituir los cantos rituales por canciones de temática secular, folclórica profana o meramente subjetiva.",
            },
            {
                "numeral": "Orientación Pastoral CECh",
                "titulo": "Invariabilidad del Ordinario de la Misa (Kyrie, Gloria, Credo, Santo, Padre Nuestro, Cordero)",
                "ancla": "",
                "extracto": "Los cantos del Ordinario pertenecen a la estructura misma del Misal Romano. En nuestras parroquias, colegios y movimientos debe erradicarse la práctica de alterar la letra del Gloria, del Santo, del Padre Nuestro o del Cordero de Dios para acomodarla a rimas particulares, o de reemplazar el Cordero de Dios por 'cantos de la paz' ajenos a la Fracción del Pan.",
            },
        ],
    },
}


# ============================================================
# 4. LAS 4 PARTES ESTRUCTURALES DE LA SANTA MISA
# ============================================================
PARTES_MISA: List[Dict[str, str]] = [
    {
        "id": "ritos-iniciales",
        "numero": "I",
        "titulo": "Ritos Iniciales",
        "cita_igmr": "IGMR 46–54",
        "proposito": "Tienen carácter de exordio, introducción y preparación: hacen que los fieles reunidos constituyan una comunión y se dispongan a escuchar debidamente la Palabra de Dios y a celebrar dignamente la Eucaristía.",
    },
    {
        "id": "liturgia-palabra",
        "numero": "II",
        "titulo": "Liturgia de la Palabra",
        "cita_igmr": "IGMR 55–71",
        "proposito": "Dios habla a su pueblo, le descubre el misterio de la redención y de la salvación, y le ofrece alimento espiritual; el pueblo responde mediante el canto salmódico, la aclamación al Evangelio, la profesión de fe y la oración universal.",
    },
    {
        "id": "liturgia-eucaristica",
        "numero": "III",
        "titulo": "Liturgia Eucarística",
        "cita_igmr": "IGMR 72–89",
        "proposito": "Centro y culmen de toda la celebración, articulada en tres momentos que actualizan los gestos de Cristo en la Última Cena: la preparación de los dones, la Plegaria Eucarística y la Fracción del Pan / Comunión.",
    },
    {
        "id": "rito-conclusion",
        "numero": "IV",
        "titulo": "Rito de Conclusión",
        "cita_igmr": "IGMR 90",
        "proposito": "Breve saludo, bendición sacerdotal y despedida diaconal o presidencial («Pueden ir en paz»), por la cual se envía a la asamblea para que cada uno regrese a sus buenas obras alabando y bendiciendo a Dios.",
    },
]


# ============================================================
# 5. CATÁLOGO COMPLETO DE LOS 16 MOMENTOS DE LA MISA (TODOS DISPONIBLES)
# ============================================================
MOMENTOS_MISA: List[Dict[str, Any]] = [
    # --- I. RITOS INICIALES ---
    {
        "slug": "entrada",
        "orden": 1,
        "titulo": "Canto de Entrada",
        "nombre_latino": "Introitus",
        "parte_id": "ritos-iniciales",
        "parte_nombre": "I. Ritos Iniciales",
        "naturaleza": "Propio",
        "funcion_ritual": "Acompaña una acción (Procesión de entrada)",
        "protagonista": "Asamblea + Coro/Cantor",
        "protagonista_filtro": ["asamblea", "coro", "solista"],
        "grado_musicam_sacram": "Tercer grado (MS 31)",
        "cita_igmr": "IGMR 47–48",
        "tag_repertorio": "Santa Misa: Entrada",
        "resumen_corto": "Abre la celebración, fomenta la unión de quienes se han reunido, introduce el espíritu del tiempo litúrgico o fiesta y acompaña la procesión del sacerdote y los ministros.",
        "disponible": True,
    },
    {
        "slug": "aspersion",
        "orden": 2,
        "titulo": "Aspersión del Agua Bendita",
        "nombre_latino": "Asperges me / Vidi aquam",
        "parte_id": "ritos-iniciales",
        "parte_nombre": "I. Ritos Iniciales",
        "naturaleza": "Propio (Opcional Dominical)",
        "funcion_ritual": "Acompaña la aspersión en memoria del Bautismo",
        "protagonista": "Asamblea + Coro",
        "protagonista_filtro": ["asamblea", "coro"],
        "grado_musicam_sacram": "Segundo grado",
        "cita_igmr": "IGMR 51",
        "tag_repertorio": "Santa Misa: Aspersión",
        "resumen_corto": "Sustituye al Acto Penitencial y al Kyrie especialmente en los domingos del Tiempo Pascual; evoca la purificación bautismal por el agua y la sangre del costado de Cristo.",
        "disponible": True,
    },
    {
        "slug": "senor-ten-piedad",
        "orden": 3,
        "titulo": "Señor, ten piedad (Kyrie)",
        "nombre_latino": "Kyrie, eleison",
        "parte_id": "ritos-iniciales",
        "parte_nombre": "I. Ritos Iniciales",
        "naturaleza": "Ordinario",
        "funcion_ritual": "Es el rito en sí mismo (Aclamación implorante)",
        "protagonista": "Dialogado (Cantor/Coro + Asamblea)",
        "protagonista_filtro": ["asamblea", "coro", "solista"],
        "grado_musicam_sacram": "Segundo grado (MS 30)",
        "cita_igmr": "IGMR 52",
        "tag_repertorio": "Santa Misa: Señor ten Piedad",
        "resumen_corto": "Canto con el que los fieles aclaman a Cristo Señor (Kyrios) e imploran su misericordia. Se canta tras el 'Yo confieso' o integrado en la Fórmula III con tropos.",
        "disponible": True,
    },
    {
        "slug": "gloria",
        "orden": 4,
        "titulo": "Gloria a Dios en el Cielo",
        "nombre_latino": "Gloria in excelsis Deo",
        "parte_id": "ritos-iniciales",
        "parte_nombre": "I. Ritos Iniciales",
        "naturaleza": "Ordinario",
        "funcion_ritual": "Es el rito en sí mismo (Himno doxológico)",
        "protagonista": "Toda la Asamblea o alternado con el Coro",
        "protagonista_filtro": ["asamblea", "coro"],
        "grado_musicam_sacram": "Segundo grado (MS 30)",
        "cita_igmr": "IGMR 53",
        "tag_repertorio": "Santa Misa: Gloria",
        "resumen_corto": "Antiquísimo y venerable himno con que la Iglesia, congregada en el Espíritu Santo, glorifica a Dios Padre y al Cordero y le presenta sus súplicas. Su texto no puede sustituirse jamás.",
        "disponible": True,
    },

    # --- II. LITURGIA DE LA PALABRA ---
    {
        "slug": "salmo-responsorial",
        "orden": 5,
        "titulo": "Salmo Responsorial",
        "nombre_latino": "Psalmus responsorius",
        "parte_id": "liturgia-palabra",
        "parte_nombre": "II. Liturgia de la Palabra",
        "naturaleza": "Propio",
        "funcion_ritual": "Es el rito en sí mismo (Palabra de Dios proclamada y meditada)",
        "protagonista": "Salmista (Solista) + Asamblea (Antífona)",
        "protagonista_filtro": ["solista", "asamblea"],
        "grado_musicam_sacram": "Tercer grado / Liturgia de la Palabra (IGMR 61)",
        "cita_igmr": "IGMR 61",
        "tag_repertorio": "Cantos Bíblicos: Salmos",
        "resumen_corto": "Parte integrante de la Liturgia de la Palabra. El salmista proclama los versículos desde el ambón y toda la asamblea participa cantando la respuesta (antífona).",
        "disponible": True,
    },
    {
        "slug": "secuencia",
        "orden": 6,
        "titulo": "Secuencia",
        "nombre_latino": "Sequentia",
        "parte_id": "liturgia-palabra",
        "parte_nombre": "II. Liturgia de la Palabra",
        "naturaleza": "Propio (Solemnidades específicas)",
        "funcion_ritual": "Es el rito en sí mismo (Himno poético antes del Aleluya)",
        "protagonista": "Coro / Cantor / Asamblea",
        "protagonista_filtro": ["coro", "solista", "asamblea"],
        "grado_musicam_sacram": "Tercer grado",
        "cita_igmr": "IGMR 64",
        "tag_repertorio": "Santa Misa: Secuencia",
        "resumen_corto": "Himno litúrgico obligatorio en los días de Pascua (Victimae paschali laudes) y Pentecostés (Veni, Sancte Spiritus), y facultativo en Corpus Christi y Dolores, que se canta antes del Aleluya.",
        "disponible": True,
    },
    {
        "slug": "aleluya",
        "orden": 7,
        "titulo": "Aclamación antes del Evangelio (Aleluya)",
        "nombre_latino": "Alleluia / Acclamatio ante Evangelium",
        "parte_id": "liturgia-palabra",
        "parte_nombre": "II. Liturgia de la Palabra",
        "naturaleza": "Propio",
        "funcion_ritual": "Acompaña la procesión al ambón y constituye el saludo a Cristo que hablará",
        "protagonista": "Toda la Asamblea (de pie) + Coro/Cantor (versículo)",
        "protagonista_filtro": ["asamblea", "coro", "solista"],
        "grado_musicam_sacram": "Segundo grado (MS 30)",
        "cita_igmr": "IGMR 62–63",
        "tag_repertorio": "Santa Misa: Aleluya",
        "resumen_corto": "Rito o acto con valor propio mediante el cual la asamblea de los fieles recibe y saluda al Señor que va a hablarles en el Evangelio. En Cuaresma cambia a aclamación crística.",
        "disponible": True,
    },
    {
        "slug": "credo",
        "orden": 8,
        "titulo": "Profesión de Fe (Credo)",
        "nombre_latino": "Symbolum / Credo",
        "parte_id": "liturgia-palabra",
        "parte_nombre": "II. Liturgia de la Palabra",
        "naturaleza": "Ordinario",
        "funcion_ritual": "Es el rito en sí mismo (Asentimiento y respuesta a la Palabra)",
        "protagonista": "Toda la Asamblea o alternado con el Coro",
        "protagonista_filtro": ["asamblea", "coro"],
        "grado_musicam_sacram": "Segundo grado (MS 30)",
        "cita_igmr": "IGMR 67–68",
        "tag_repertorio": "Santa Misa: Credo",
        "resumen_corto": "El pueblo da su asentimiento y respuesta a la Palabra de Dios escuchada en las lecturas y en la homilía, confesando el Símbolo Niceno-Constantinopolitano o Apostólico.",
        "disponible": True,
    },
    {
        "slug": "oracion-universal",
        "orden": 9,
        "titulo": "Oración Universal (Respuesta de los Fieles)",
        "nombre_latino": "Oratio universalis",
        "parte_id": "liturgia-palabra",
        "parte_nombre": "II. Liturgia de la Palabra",
        "naturaleza": "Ordinario / Dialogado",
        "funcion_ritual": "Es el rito en sí mismo (Súplica sacerdotal del pueblo)",
        "protagonista": "Diácono/Lector + Asamblea (Respuesta cantada)",
        "protagonista_filtro": ["asamblea", "solista"],
        "grado_musicam_sacram": "Primer/Segundo grado (MS 29–30)",
        "cita_igmr": "IGMR 69–71",
        "tag_repertorio": "Santa Misa: Oración Universal",
        "resumen_corto": "Ejercitando el oficio de su sacerdocio bautismal, el pueblo ruega por todos los hombres mediante una breve invocación cantada (ej. 'Te rogamos, óyenos' o 'Kyrie, eleison').",
        "disponible": True,
    },

    # --- III. LITURGIA EUCARÍSTICA ---
    {
        "slug": "presentacion-dones",
        "orden": 10,
        "titulo": "Presentación de los Dones (Ofertorio)",
        "nombre_latino": "Cantus ad Offertorium",
        "parte_id": "liturgia-eucaristica",
        "parte_nombre": "III. Liturgia Eucarística",
        "naturaleza": "Propio",
        "funcion_ritual": "Acompaña la procesión y preparación del pan y el vino en el altar",
        "protagonista": "Asamblea + Coro, solo Coro, o música instrumental / silencio",
        "protagonista_filtro": ["asamblea", "coro"],
        "grado_musicam_sacram": "Tercer grado (MS 31)",
        "cita_igmr": "IGMR 74",
        "tag_repertorio": "Santa Misa: Ofertorio",
        "resumen_corto": "Acompaña la procesión en que se llevan los dones al altar. Puede ser cantado por la asamblea, solo por el coro polifónico, o bien dejar espacio al órgano/instrumentos o al diálogo 'Bendito seas por siempre, Señor'.",
        "disponible": True,
    },
    {
        "slug": "santo",
        "orden": 11,
        "titulo": "Santo (Sanctus)",
        "nombre_latino": "Sanctus, Sanctus, Sanctus",
        "parte_id": "liturgia-eucaristica",
        "parte_nombre": "III. Liturgia Eucarística",
        "naturaleza": "Ordinario",
        "funcion_ritual": "Es el rito en sí mismo (Parte de la Plegaria Eucarística)",
        "protagonista": "Toda la Asamblea unida al Sacerdote y al Coro",
        "protagonista_filtro": ["asamblea", "coro"],
        "grado_musicam_sacram": "Primer grado (MS 29 — Prioridad absoluta)",
        "cita_igmr": "IGMR 79b",
        "tag_repertorio": "Santa Misa: Santo",
        "resumen_corto": "Aclamación con que toda la asamblea, uniéndose a las jerarquías celestiales tras el Prefacio, canta la santidad de Dios. Debe ser cantado por todo el pueblo junto con el sacerdote.",
        "disponible": True,
    },
    {
        "slug": "aclamaciones-eucaristicas",
        "orden": 12,
        "titulo": "Aclamación Memorial y Gran Amén",
        "nombre_latino": "Mysterium fidei & Doxologia finalis (Amen)",
        "parte_id": "liturgia-eucaristica",
        "parte_nombre": "III. Liturgia Eucarística",
        "naturaleza": "Ordinario",
        "funcion_ritual": "Es el rito en sí mismo (Aclamaciones dentro de la Plegaria Eucarística)",
        "protagonista": "Sacerdote + Toda la Asamblea",
        "protagonista_filtro": ["asamblea"],
        "grado_musicam_sacram": "Primer grado (MS 29 — Prioridad absoluta)",
        "cita_igmr": "IGMR 79c, 79h, 151",
        "tag_repertorio": "Santa Misa: Amén",
        "resumen_corto": "La aclamación pascual de los fieles tras la consagración ('Anunciamos tu muerte...') y el Gran Amén que ratifica la Doxología final ('Por Cristo, con Él y en Él').",
        "disponible": True,
    },
    {
        "slug": "padre-nuestro",
        "orden": 13,
        "titulo": "Padre Nuestro y Doxología",
        "nombre_latino": "Pater Noster",
        "parte_id": "liturgia-eucaristica",
        "parte_nombre": "III. Liturgia Eucarística",
        "naturaleza": "Ordinario",
        "funcion_ritual": "Es el rito en sí mismo (Oración del Señor previa a la Comunión)",
        "protagonista": "Sacerdote + Toda la Asamblea",
        "protagonista_filtro": ["asamblea"],
        "grado_musicam_sacram": "Primer grado (MS 29 — Prioridad absoluta)",
        "cita_igmr": "IGMR 81",
        "tag_repertorio": "Santa Misa: Padre Nuestro",
        "resumen_corto": "Oración dominical con que comienza el rito de la Comunión. Si se canta, debe hacerse con el texto exacto e íntegro del Misal Romano, seguido del embolismo y la aclamación 'Tuyo es el reino...'.",
        "disponible": True,
    },
    {
        "slug": "cordero-de-dios",
        "orden": 14,
        "titulo": "Cordero de Dios (Agnus Dei)",
        "nombre_latino": "Agnus Dei",
        "parte_id": "liturgia-eucaristica",
        "parte_nombre": "III. Liturgia Eucarística",
        "naturaleza": "Ordinario",
        "funcion_ritual": "Acompaña la Fracción del Pan (no el saludo de la paz)",
        "protagonista": "Cantor/Coro (invocación) + Asamblea (respuesta) o todos",
        "protagonista_filtro": ["asamblea", "coro", "solista"],
        "grado_musicam_sacram": "Segundo grado (MS 30)",
        "cita_igmr": "IGMR 83",
        "tag_repertorio": "Santa Misa: Cordero de Dios",
        "resumen_corto": "Súplica letánica que acompaña el gesto de partir el Pan consagrado y dejar caer una partícula en el cáliz. Puede repetirse cuantas veces sea necesario hasta que concluya la fracción, cerrando con 'danos la paz'.",
        "disponible": True,
    },
    {
        "slug": "comunion",
        "orden": 15,
        "titulo": "Canto de Comunión y Acción de Gracias",
        "nombre_latino": "Cantus ad Communionem",
        "parte_id": "liturgia-eucaristica",
        "parte_nombre": "III. Liturgia Eucarística",
        "naturaleza": "Propio",
        "funcion_ritual": "Acompaña la procesión de los fieles a comulgar (comienza cuando comulga el sacerdote)",
        "protagonista": "Asamblea + Coro/Cantor (forma responsorial) o Coro solo",
        "protagonista_filtro": ["asamblea", "coro", "solista"],
        "grado_musicam_sacram": "Tercer grado (MS 31)",
        "cita_igmr": "IGMR 86–88",
        "tag_repertorio": "Santa Misa: Comunión",
        "resumen_corto": "Expresa por la unidad de las voces la unión espiritual de quienes comulgan, manifiesta el gozo del corazón y esclarece el carácter comunitario de la procesión para recibir la Eucaristía.",
        "disponible": True,
    },

    # --- IV. RITO DE CONCLUSIÓN ---
    {
        "slug": "salida",
        "orden": 16,
        "titulo": "Canto de Salida / Envío",
        "nombre_latino": "Recessus (Ad libitum)",
        "parte_id": "rito-conclusion",
        "parte_nombre": "IV. Rito de Conclusión",
        "naturaleza": "Extralitúrgico / Opcional",
        "funcion_ritual": "Acompaña la retirada del sacerdote y los ministros tras el 'Pueden ir en paz'",
        "protagonista": "Asamblea / Coro / Instrumental",
        "protagonista_filtro": ["asamblea", "coro"],
        "grado_musicam_sacram": "Opcional (No prescrito en la IGMR)",
        "cita_igmr": "IGMR 90 (MS 36)",
        "tag_repertorio": "Santa Misa: Salida",
        "resumen_corto": "Aunque no está prescrito en las rúbricas del Misal Romano, es una costumbre legítima acompañar la retirada de los ministros con una antífona mariana, himno de alabanza o postludio instrumental.",
        "disponible": True,
    },
]


# ============================================================
# 6. RESUMEN DE TIEMPOS LITÚRGICOS Y GRADOS DE PARTICIPACIÓN
# ============================================================
TIEMPOS_LITURGICOS_RESUMEN: List[Dict[str, str]] = [
    {
        "nombre": "Adviento",
        "color": "#5c3d7a",
        "caracter": "Espera piadosa, gozosa y sobria de las dos venidas del Señor (Parusía y Natividad).",
        "reglas_clave": "Se omite el Gloria (salvo solemnidades como la Inmaculada). Se conserva el Aleluya. Los instrumentos y flores se usan con la moderación que conviene al carácter del tiempo, sin anticipar la alegría plena de la Navidad (IGMR 305, 313). Del 17 al 23 de diciembre brillan las 7 Antífonas Mayores de la 'O'.",
    },
    {
        "nombre": "Navidad y Epifanía",
        "color": "#b89020",
        "caracter": "Alegría desbordante por el misterio de la Encarnación y manifestación del Verbo hecho carne.",
        "reglas_clave": "Vuelve el Gloria con carácter festivo. En las Misas del día de Navidad todos se arrodillan en el Credo al decir «y por obra del Espíritu Santo se encarnó...» (IGMR 275b). Uso pleno de instrumentos; cuidar que en la Entrada y Comunión predomine el sentido teológico del misterio.",
    },
    {
        "nombre": "Cuaresma",
        "color": "#6b3fa0",
        "caracter": "Conversión penitencial, desierto con Cristo, preparación bautismal y memoria de la Pasión.",
        "reglas_clave": "Se suprime el Gloria y se prohíbe absolutamente el Aleluya en todas las celebraciones (incluidas solemnidades). Se prohíbe el sonido del órgano y de otros instrumentos musicales 'solo para tocar': se permiten únicamente para sostener el canto (IGMR 313), excepto el domingo Laetare y solemnidades.",
    },
    {
        "nombre": "Semana Santa y Triduo Pascual",
        "color": "#8b2626",
        "caracter": "Culmen de todo el año litúrgico: Pasión, Muerte, Sepultura y Resurrección del Señor.",
        "reglas_clave": "En el Jueves Santo resuena el Gloria con campanas, tras lo cual el órgano y los instrumentos callan por completo hasta el Gloria de la Vigilia Pascual (el Viernes Santo es estrictamente sin canto de entrada y con cantos a cappella en la Adoración de la Cruz).",
    },
    {
        "nombre": "Tiempo Pascual y Pentecostés",
        "color": "#c99b1e",
        "caracter": "Cincuenta días celebrados como un solo 'gran Domingo' en el gozo del Resucitado.",
        "reglas_clave": "El Aleluya se añade a las antífonas y al envío. Se recomienda la aspersión dominical con el canto 'Vidi aquam' ('Vi brotar agua del lado derecho del templo'). Obligatorias las secuencias de Pascua (Victimae paschali laudes) y Pentecostés (Veni, Sancte Spiritus).",
    },
    {
        "nombre": "Tiempo Ordinario",
        "color": "#2f6b48",
        "caracter": "Celebración del misterio de Cristo en su plenitud, especialmente cada domingo como Pascua semanal.",
        "reglas_clave": "Se canta el Gloria y el Credo todos los domingos. La elección de cantos (especialmente la Comunión) debe acompañar la lectura semicontinua del Evangelio sinóptico propio del ciclo (A: Mateo, B: Marcos, C: Lucas).",
    },
]

GRADOS_PARTICIPACION_MS: List[Dict[str, Any]] = [
    {
        "grado": "Primer Grado (Prioridad Absoluta)",
        "cita": "Musicam Sacram, n. 29",
        "explicacion": "Debe emplearse antes que cualquier otro: son los diálogos entre el sacerdote y la asamblea, y las aclamaciones que pertenecen a todo el pueblo. Es un contrasentido litúrgico que un coro prepare cuatro canciones largas con guitarra y deje rezados el Santo, el Amén o las respuestas del diálogo presidencial.",
        "elementos": [
            "Saludos del sacerdote y respuestas de los fieles en los Ritos Iniciales y en la Oración Colecta.",
            "Aclamar en los diálogos del Evangelio.",
            "Diálogo del Prefacio, el Santo (Sanctus), la Aclamación Memorial y el Gran Amén de la Doxología.",
            "Padre Nuestro con su invitación, embolismo y doxología final («Tuyo es el reino...»).",
            "Saludo de la Paz, Bendición final y despedida («Pueden ir en paz — Demos gracias a Dios»).",
        ],
    },
    {
        "grado": "Segundo Grado",
        "cita": "Musicam Sacram, n. 30",
        "explicacion": "Nunca debe emplearse sin el Primer Grado. Comprende los demás cantos del Ordinario y la Oración Universal.",
        "elementos": [
            "Kyrie (Señor, ten piedad), Gloria in excelsis y Cordero de Dios (Agnus Dei).",
            "Profesión de fe (Credo).",
            "Oración Universal de los Fieles (respuesta cantada del pueblo).",
        ],
    },
    {
        "grado": "Tercer Grado",
        "cita": "Musicam Sacram, n. 31",
        "explicacion": "Comprende los cantos procesionales y variables del Propio de la Misa y de la Liturgia de la Palabra.",
        "elementos": [
            "Canto de Entrada (Introitus) y Canto Procesional de Comunión.",
            "Salmo Responsorial después de la primera lectura y Aclamación antes del Evangelio (Aleluya).",
            "Canto en la Presentación de los Dones (Ofertorio) y proclamación cantada de las lecturas bíblicas.",
        ],
    },
]


# ============================================================
# 7. DICCIONARIO UNIFICADO DE LOS 16 MOMENTOS DE LA MISA
# ============================================================
DETALLE_MOMENTOS: Dict[str, Dict[str, Any]] = {}
DETALLE_MOMENTOS.update(MOMENTOS_PARTE_1)
DETALLE_MOMENTOS.update(MOMENTOS_PARTE_2)


# ============================================================
# 8. FUNCIONES DE CONSULTA Y CONEXIÓN CON EL REPERTORIO
# ============================================================
def get_all_areas() -> List[Dict[str, Any]]:
    """Retorna las 5 grandes áreas de Formación Litúrgica."""
    return AREAS_FORMACION


def get_subvistas_momento() -> List[Dict[str, str]]:
    """Retorna las 4 sub-vistas dedicadas de estudio para cada momento."""
    return SUBVISTAS_MOMENTO


def get_documentos_magisteriales() -> List[Dict[str, Any]]:
    """Retorna todos los documentos de la biblioteca magisterial."""
    return list(DOCUMENTOS_MAGISTERIALES.values())


def get_documento_by_id(doc_id: str) -> Optional[Dict[str, Any]]:
    """Retorna un documento magisterial por su ID ('igmr', 'musicam-sacram', etc.)."""
    return DOCUMENTOS_MAGISTERIALES.get(doc_id)


def get_partes_misa() -> List[Dict[str, str]]:
    """Retorna las 4 partes estructurales de la Santa Misa."""
    return PARTES_MISA


def get_momentos_misa() -> List[Dict[str, Any]]:
    """Retorna la lista ordenada de los 16 momentos de la Misa."""
    return sorted(MOMENTOS_MISA, key=lambda m: m["orden"])


def get_momento_by_slug(slug: str) -> Optional[Dict[str, Any]]:
    """Busca los metadatos de índice de un momento por su slug."""
    for m in MOMENTOS_MISA:
        if m["slug"] == slug:
            return m
    return None


def get_detalle_momento(slug: str) -> Optional[Dict[str, Any]]:
    """
    Retorna el diccionario con el desarrollo exhaustivo de un momento (todos los 16 momentos
    cuentan con su estudio completo en DETALLE_MOMENTOS).
    """
    meta = get_momento_by_slug(slug)
    if not meta:
        return None
    if slug in DETALLE_MOMENTOS:
        merged = dict(meta)
        merged.update(DETALLE_MOMENTOS[slug])
        return merged
    return meta


def get_datos_areas_extra() -> Dict[str, Any]:
    """
    Retorna el contenido estructurado completo para las Áreas 2, 3, 4 y 5:
    - matriz_ano_liturgico, antifonas_o, tratado_tiempos
    - antologia_patristica
    - guia_musico_tratado
    - otras_celebraciones_detalle
    """
    return {
        "matriz_ano_liturgico": MATRIZ_ANO_LITURGICO,
        "antifonas_o": ANTIFONAS_MAYORES_O,
        "tratado_tiempos": TRATADO_TIEMPOS_DETALLADO,
        "antologia_patristica": ANTOLOGIA_PATRISTICA,
        "guia_musico_tratado": GUIA_MUSICO_TRATADO,
        "otras_celebraciones_detalle": OTRAS_CELEBRACIONES_DETALLE,
    }


def get_repertorio_for_momento(slug: str) -> Tuple[List[Cancion], List[Cancion]]:
    """
    Retorna (canciones_especificas, canciones_sugeridas) para cualquiera de los 16 momentos de la Misa.
    """
    meta = get_momento_by_slug(slug)
    if not meta:
        return [], []

    all_songs = Cancion.query.all()
    tag_objetivo = meta.get("tag_repertorio", "")

    especificas = [s for s in all_songs if tag_objetivo and tag_matches(tag_objetivo, s.tags)]
    especificas = sort_songs(especificas, sort_by="cronologico")

    sugeridas: List[Cancion] = []
    ids_especificas = {s.id for s in especificas}

    tags_afines_map: Dict[str, List[str]] = {
        "entrada": ["Cantos Bíblicos: Salmos", "Tiempos Litúrgicos", "Himnos"],
        "aspersion": ["Cantos Bíblicos: Salmos", "Tiempos Litúrgicos: Pascua", "Tiempos Litúrgicos: Cuaresma"],
        "salmo-responsorial": ["Cantos Bíblicos: Salmos", "Cantos Bíblicos"],
        "secuencia": ["Tiempos Litúrgicos: Pascua", "Himnos"],
        "aleluya": ["Cantos Bíblicos: Salmos", "Tiempos Litúrgicos"],
        "presentacion-dones": ["Cantos Bíblicos: Salmos", "Himnos", "Tiempos Litúrgicos"],
        "comunion": ["Cantos Bíblicos: Salmos", "Adoración y Meditación", "Himnos"],
        "salida": ["Virgen María", "Himnos", "Tiempos Litúrgicos: Navidad"],
    }

    afines = tags_afines_map.get(slug, [])
    if afines:
        for s in all_songs:
            if s.id in ids_especificas:
                continue
            if any(tag_matches(t, s.tags) for t in afines):
                if not any(
                    tag_matches(fijo, s.tags)
                    for fijo in [
                        "Santa Misa: Señor ten Piedad",
                        "Santa Misa: Santo",
                        "Santa Misa: Cordero de Dios",
                    ]
                ):
                    sugeridas.append(s)
        sugeridas = sort_songs(sugeridas, sort_by="cronologico")[:6]

    return especificas, sugeridas


def get_citas_popover_dictionary() -> Dict[str, Dict[str, str]]:
    """
    Construye un diccionario unificado de citas magisteriales (IGMR, MS, SC, TLS, OGLH, CECh)
    para mostrar previsualizaciones flotantes (Hover Cards / Popovers) al pasar el mouse
    o hacer clic sobre cualquier referencia normativa en el estudio.
    """
    citas: Dict[str, Dict[str, str]] = {
        "IGMR 16": {
            "ref": "IGMR 16",
            "fuente": "Instrucción General del Misal Romano",
            "doc_id": "igmr",
            "url": DOCUMENTOS_MAGISTERIALES["igmr"]["url_oficial"],
            "texto": "«La celebración de la Misa, como acción de Cristo y del Pueblo de Dios ordenado jerárquicamente, constituye el centro de toda la vida cristiana para la Iglesia, tanto universal como local, y para cada uno de los fieles.»",
        },
        "IGMR 39–41": {
            "ref": "IGMR 39–41",
            "fuente": "Instrucción General del Misal Romano",
            "doc_id": "igmr",
            "url": DOCUMENTOS_MAGISTERIALES["igmr"]["url_oficial"],
            "texto": "«Cantar es propio de quien ama... Se ha de poner gran cuidado para que no falte el canto de los ministros y del pueblo en las celebraciones que se llevan a cabo los domingos y fiestas de precepto.»",
        },
        "IGMR 40": {
            "ref": "IGMR 40",
            "fuente": "Instrucción General del Misal Romano",
            "doc_id": "igmr",
            "url": DOCUMENTOS_MAGISTERIALES["igmr"]["url_oficial"],
            "texto": "«Al elegir las partes que de hecho se van a cantar, se dará la preferencia a las que tienen mayor importancia, y sobre todo a las que deben cantar el sacerdote, el diácono o el lector, con respuesta del pueblo, o el sacerdote y el pueblo al mismo tiempo.»",
        },
        "IGMR 46–54": {
            "ref": "IGMR 46–54",
            "fuente": "Instrucción General del Misal Romano · Ritos Iniciales",
            "doc_id": "igmr",
            "url": DOCUMENTOS_MAGISTERIALES["igmr"]["url_oficial"] + "#B._Ritos_iniciales",
            "texto": "«Los ritos que preceden a la Liturgia de la Palabra, es decir, la entrada, el saludo, el acto penitencial, el Kyrie, el Gloria y la oración colecta, tienen carácter de exordio, introducción y preparación: hacen que los fieles reunidos constituyan una comunión.»",
        },
        "IGMR 47": {
            "ref": "IGMR 47",
            "fuente": "Instrucción General del Misal Romano · Canto de Entrada",
            "doc_id": "igmr",
            "url": DOCUMENTOS_MAGISTERIALES["igmr"]["url_oficial"] + "#B._Ritos_iniciales",
            "texto": "«La finalidad de este canto es abrir la celebración, fomentar la unión de quienes se han reunido y elevar sus pensamientos a la contemplación del misterio litúrgico o de la fiesta, acompañando la procesión del sacerdote y los ministros.»",
        },
        "IGMR 48": {
            "ref": "IGMR 48",
            "fuente": "Instrucción General del Misal Romano · Elección del Canto de Entrada",
            "doc_id": "igmr",
            "url": DOCUMENTOS_MAGISTERIALES["igmr"]["url_oficial"] + "#B._Ritos_iniciales",
            "texto": "«Puede emplearse la antífona con su salmo del Graduale Romanum o del Graduale Simplex, o bien otro canto que sea congruente con la acción sagrada, el carácter del día o del tiempo, cuyo texto haya sido aprobado por la Conferencia de Obispos.»",
        },
        "IGMR 47–48": {
            "ref": "IGMR 47–48",
            "fuente": "Instrucción General del Misal Romano · Canto de Entrada",
            "doc_id": "igmr",
            "url": DOCUMENTOS_MAGISTERIALES["igmr"]["url_oficial"] + "#B._Ritos_iniciales",
            "texto": "«Abre la celebración, fomenta la unión de quienes se han reunido, introduce el espíritu en el misterio del tiempo o fiesta y acompaña la procesión del sacerdote y los ministros hacia el altar.»",
        },
        "IGMR 51": {
            "ref": "IGMR 51",
            "fuente": "Instrucción General del Misal Romano · Aspersión Dominical",
            "doc_id": "igmr",
            "url": DOCUMENTOS_MAGISTERIALES["igmr"]["url_oficial"] + "#B._Ritos_iniciales",
            "texto": "«Los domingos, especialmente en el Tiempo Pascual, en lugar del acto penitencial acostumbrado, puede hacerse alguna vez la bendición y aspersión del agua en memoria del bautismo.»",
        },
        "IGMR 52": {
            "ref": "IGMR 52",
            "fuente": "Instrucción General del Misal Romano · Señor, ten piedad (Kyrie)",
            "doc_id": "igmr",
            "url": DOCUMENTOS_MAGISTERIALES["igmr"]["url_oficial"] + "#B._Ritos_iniciales",
            "texto": "«Después del acto penitencial, se empieza siempre el Señor, ten piedad, a no ser que éste haya formado ya parte del mismo acto penitencial. Es un canto con el que los fieles aclaman al Señor e imploran su misericordia.»",
        },
        "IGMR 53": {
            "ref": "IGMR 53",
            "fuente": "Instrucción General del Misal Romano · Gloria in excelsis",
            "doc_id": "igmr",
            "url": DOCUMENTOS_MAGISTERIALES["igmr"]["url_oficial"] + "#B._Ritos_iniciales",
            "texto": "«El Gloria es un antiquísimo y venerable himno con que la Iglesia, congregada en el Espíritu Santo, glorifica a Dios Padre y al Cordero y le presenta sus súplicas. El texto de este himno no puede cambiarse por otro.»",
        },
        "IGMR 55–71": {
            "ref": "IGMR 55–71",
            "fuente": "Instrucción General del Misal Romano · Liturgia de la Palabra",
            "doc_id": "igmr",
            "url": DOCUMENTOS_MAGISTERIALES["igmr"]["url_oficial"] + "#C._Liturgia_de_la_Palabra",
            "texto": "«En las lecturas, que luego desarrolla la homilía, Dios habla a su pueblo, le descubre el misterio de la redención y salvación, y le ofrece alimento espiritual; y el mismo Cristo, por su palabra, se hace presente en medio de los fieles.»",
        },
        "IGMR 61": {
            "ref": "IGMR 61",
            "fuente": "Instrucción General del Misal Romano · Salmo Responsorial",
            "doc_id": "igmr",
            "url": DOCUMENTOS_MAGISTERIALES["igmr"]["url_oficial"] + "#C._Liturgia_de_la_Palabra",
            "texto": "«Después de la primera lectura sigue el salmo responsorial, que es parte integrante de la Liturgia de la Palabra y tiene gran importancia litúrgica y pastoral, porque favorece la meditación de la Palabra de Dios.»",
        },
        "IGMR 62–63": {
            "ref": "IGMR 62–63",
            "fuente": "Instrucción General del Misal Romano · Aleluya",
            "doc_id": "igmr",
            "url": DOCUMENTOS_MAGISTERIALES["igmr"]["url_oficial"] + "#C._Liturgia_de_la_Palabra",
            "texto": "«Después de la lectura que precede inmediatamente al Evangelio, se canta el Aleluya u otro canto determinado por las rúbricas, según lo pida el tiempo litúrgico. Una aclamación de este género constituye por sí misma un rito o acto con el que la asamblea de los fieles acoge y saluda al Señor que va a hablarles en el Evangelio.»",
        },
        "IGMR 64": {
            "ref": "IGMR 64",
            "fuente": "Instrucción General del Misal Romano · Secuencia",
            "doc_id": "igmr",
            "url": DOCUMENTOS_MAGISTERIALES["igmr"]["url_oficial"] + "#C._Liturgia_de_la_Palabra",
            "texto": "«La secuencia, que, fuera de los días de Pascua y de Pentecostés, es facultativa, se canta antes del Aleluya.»",
        },
        "IGMR 67–68": {
            "ref": "IGMR 67–68",
            "fuente": "Instrucción General del Misal Romano · Profesión de Fe (Credo)",
            "doc_id": "igmr",
            "url": DOCUMENTOS_MAGISTERIALES["igmr"]["url_oficial"] + "#C._Liturgia_de_la_Palabra",
            "texto": "«El Símbolo o profesión de fe tiende a que todo el pueblo reunido responda a la Palabra de Dios anunciada en las lecturas de la Sagrada Escritura y expuesta en la homilía.»",
        },
        "IGMR 69–71": {
            "ref": "IGMR 69–71",
            "fuente": "Instrucción General del Misal Romano · Oración Universal",
            "doc_id": "igmr",
            "url": DOCUMENTOS_MAGISTERIALES["igmr"]["url_oficial"] + "#C._Liturgia_de_la_Palabra",
            "texto": "«En la oración universal u oración de los fieles, el pueblo, ejercitando su oficio sacerdotal, ruega por todos los hombres.»",
        },
        "IGMR 72–89": {
            "ref": "IGMR 72–89",
            "fuente": "Instrucción General del Misal Romano · Liturgia Eucarística",
            "doc_id": "igmr",
            "url": DOCUMENTOS_MAGISTERIALES["igmr"]["url_oficial"] + "#D._Liturgia_eucarística",
            "texto": "«Cristo tomó el pan y el cáliz, dio gracias, lo partió y lo dio a sus discípulos... La Iglesia ha ordenado toda la celebración de la Liturgia eucarística con estas partes que corresponden a las palabras y acciones de Cristo: preparación de los dones, Plegaria Eucarística y rito de Comunión.»",
        },
        "IGMR 74": {
            "ref": "IGMR 74",
            "fuente": "Instrucción General del Misal Romano · Preparación de los Dones",
            "doc_id": "igmr",
            "url": DOCUMENTOS_MAGISTERIALES["igmr"]["url_oficial"] + "#D._Liturgia_eucarística",
            "texto": "«El canto de preparación de los dones acompaña la procesión en que se llevan los dones y se prolonga por lo menos hasta que los dones han sido depositados sobre el altar. Las normas sobre el modo de cantar son las mismas que para el canto de entrada (n. 48).»",
        },
        "IGMR 79b": {
            "ref": "IGMR 79b",
            "fuente": "Instrucción General del Misal Romano · El Santo (Sanctus)",
            "doc_id": "igmr",
            "url": DOCUMENTOS_MAGISTERIALES["igmr"]["url_oficial"] + "#D._Liturgia_eucarística",
            "texto": "«Aclama toda la asamblea, uniéndose a las jerarquías celestiales, con el canto del Santo. Esta aclamación, que constituye parte de la misma Plegaria Eucarística, la pronuncia todo el pueblo con el sacerdote.»",
        },
        "IGMR 79": {
            "ref": "IGMR 79",
            "fuente": "Instrucción General del Misal Romano · Aclamaciones Eucarísticas",
            "doc_id": "igmr",
            "url": DOCUMENTOS_MAGISTERIALES["igmr"]["url_oficial"] + "#D._Liturgia_eucarística",
            "texto": "«Los fieles expresan su participación mediante las aclamaciones, entre las que sobresalen la aclamación conmemorativa después de la consagración y el Amén final de la doxología.»",
        },
        "IGMR 81": {
            "ref": "IGMR 81",
            "fuente": "Instrucción General del Misal Romano · Oración del Señor (Padrenuestro)",
            "doc_id": "igmr",
            "url": DOCUMENTOS_MAGISTERIALES["igmr"]["url_oficial"] + "#D._Liturgia_eucarística",
            "texto": "«En la Oración del Señor se pide el pan de cada día, con lo que para los cristianos se evoca principalmente el pan eucarístico, y se implora la purificación de los pecados.»",
        },
        "IGMR 83": {
            "ref": "IGMR 83",
            "fuente": "Instrucción General del Misal Romano · Fracción del Pan (Agnus Dei)",
            "doc_id": "igmr",
            "url": DOCUMENTOS_MAGISTERIALES["igmr"]["url_oficial"] + "#D._Liturgia_eucarística",
            "texto": "«La súplica Cordero de Dios la canta de ordinario el coro o el cantor con la respuesta del pueblo; o la dice al menos en voz alta. Esta invocación acompaña la fracción del pan y, por eso, puede repetirse cuantas veces sea necesario hasta que haya terminado el rito; la última vez se concluye con las palabras danos la paz.»",
        },
        "IGMR 86–88": {
            "ref": "IGMR 86–88",
            "fuente": "Instrucción General del Misal Romano · Canto de Comunión y Silencio Sagrado",
            "doc_id": "igmr",
            "url": DOCUMENTOS_MAGISTERIALES["igmr"]["url_oficial"] + "#D._Liturgia_eucarística",
            "texto": "«Mientras el sacerdote toma el Sacramento, se inicia el canto de comunión, cuyo fin es expresar por la unidad de las voces la unión espiritual de quienes comulgan, demostrar la alegría del corazón y manifestar más claramente el carácter 'comunitario' de la procesión para recibir la Eucaristía.»",
        },
        "IGMR 90": {
            "ref": "IGMR 90",
            "fuente": "Instrucción General del Misal Romano · Rito de Conclusión",
            "doc_id": "igmr",
            "url": DOCUMENTOS_MAGISTERIALES["igmr"]["url_oficial"],
            "texto": "«Al rito de conclusión pertenecen los breves avisos si fuere necesario, el saludo y la bendición del sacerdote, la despedida del pueblo por parte del diácono o del sacerdote, para que cada uno regrese a sus buenas obras alabando y bendiciendo a Dios, y el beso al altar.»",
        },
        "IGMR 305, 313": {
            "ref": "IGMR 305, 313",
            "fuente": "Instrucción General del Misal Romano · Moderación Instrumental en Adviento y Cuaresma",
            "doc_id": "igmr",
            "url": DOCUMENTOS_MAGISTERIALES["igmr"]["url_oficial"],
            "texto": "«En Adviento el órgano y otros instrumentos musicales deben usarse con moderación... En Cuaresma se permite el sonido del órgano y de los otros instrumentos solamente para sostener el canto, exceptuando el domingo Laetare, las solemnidades y las fiestas.»",
        },
        "MS 4": {
            "ref": "MS 4",
            "fuente": "Instrucción Musicam Sacram (1967)",
            "doc_id": "musicam-sacram",
            "url": DOCUMENTOS_MAGISTERIALES["musicam-sacram"]["url_oficial"],
            "texto": "«Se entiende por música sagrada aquella que, creada para la celebración del culto divino, posee las cualidades de santidad y de perfección de formas.»",
        },
        "MS 28–31": {
            "ref": "MS 28–31",
            "fuente": "Instrucción Musicam Sacram · Los 3 Grados de Participación",
            "doc_id": "musicam-sacram",
            "url": DOCUMENTOS_MAGISTERIALES["musicam-sacram"]["url_oficial"],
            "texto": "«Para la solemnización de la Misa se seguirán tres grados de participación progresiva: 1.º Diálogos, Santo y Padrenuestro; 2.º Kyrie, Gloria, Agnus Dei, Credo y Oración de los fieles; 3.º Cantos procesionales (Entrada, Dones, Comunión) y lecturas/Salmo.»",
        },
        "SC 112": {
            "ref": "SC 112",
            "fuente": "Constitución Sacrosanctum Concilium (Vaticano II)",
            "doc_id": "sacrosanctum-concilium",
            "url": DOCUMENTOS_MAGISTERIALES["sacrosanctum-concilium"]["url_oficial"],
            "texto": "«El canto sagrado, unido a las palabras, constituye una parte necesaria o integral de la Liturgia solemne... La música sagrada será tanto más santa cuanto más íntimamente esté unida a la acción litúrgica.»",
        },
        "SC 121": {
            "ref": "SC 121",
            "fuente": "Constitución Sacrosanctum Concilium (Vaticano II)",
            "doc_id": "sacrosanctum-concilium",
            "url": DOCUMENTOS_MAGISTERIALES["sacrosanctum-concilium"]["url_oficial"],
            "texto": "«Los textos destinados al canto sagrado deben estar de acuerdo con la doctrina católica; más aún, deben tomarse principalmente de la Sagrada Escritura y de las fuentes litúrgicas.»",
        },
        "TLS 1–2": {
            "ref": "TLS 1–2",
            "fuente": "San Pío X · Motu Proprio Tra le sollecitudini (1903)",
            "doc_id": "tra-le-sollecitudini",
            "url": DOCUMENTOS_MAGISTERIALES["tra-le-sollecitudini"]["url_oficial"],
            "texto": "«La música sagrada debe poseer en grado eminente las cualidades propias de la liturgia: la santidad y la bondad de las formas, de donde nace espontáneo otro carácter suyo: la universalidad.»",
        },
        "OGLH 268–284": {
            "ref": "OGLH 268–284",
            "fuente": "Ordenación General de la Liturgia de las Horas",
            "doc_id": "oglh",
            "url": DOCUMENTOS_MAGISTERIALES["oglh"]["url_oficial"],
            "texto": "«Se recomienda vivamente a los que rezan el Oficio en coro o en común el uso del canto, como algo que responde mejor a la naturaleza de esta oración y es indicio de mayor solemnidad y de una unión más profunda de los corazones.»",
        },
    }
    return citas


def get_buscador_estudio_index() -> List[Dict[str, str]]:
    """
    Construye el índice completo de navegación para el Buscador / Paleta de Comandos (Ctrl+K).
    Incluye los 16 momentos de la Misa y sus 4 sub-páginas (64 vistas), los 6 documentos magisteriales,
    las Antífonas de la 'O', los Padres de la Iglesia, la Guía del Músico y las Otras Celebraciones.
    """
    items: List[Dict[str, str]] = [
        {
            "categoria": "Módulo",
            "titulo": "La Santa Misa — Estructura y 16 Momentos",
            "subtitulo": "Índice general, tabla compacta, secuencia y filtro por participación",
            "keywords": "misa rito ordinario propio estructura indice",
            "url": "/formacion",
        },
        {
            "categoria": "Módulo",
            "titulo": "Año Litúrgico, Matriz Sinóptica y Antífonas de la 'O'",
            "subtitulo": "Adviento, Navidad, Cuaresma, Triduo Pascual, Pascua y Tiempo Ordinario",
            "keywords": "adviento navidad cuaresma pascua triduo ordinario organo gloria aleluya antifonas o sapientia emmanuel",
            "url": "/formacion/tiempos",
        },
        {
            "categoria": "Módulo",
            "titulo": "Guía para el Músico, Coro y Compositor",
            "subtitulo": "Prosodia castellana, 5 formas musicales, tesitura Re4–Do5, instrumentación y ensayo",
            "keywords": "compositor coro direccion prosodia tesitura registro satb organo guitarra ensayo",
            "url": "/formacion/musico",
        },
        {
            "categoria": "Módulo",
            "titulo": "Otras Celebraciones: Adoración, Liturgia de las Horas y Sacramentos",
            "subtitulo": "Tantum Ergo, Benedictus, Magnificat, Nunc Dimittis, Matrimonios y Exequias (In Paradisum)",
            "keywords": "adoracion santisimo tantum ergo laudes visperas completas horas benedictus magnificat matrimonio exequias",
            "url": "/formacion/otras",
        },
    ]

    # Documentos Magisteriales
    for doc in DOCUMENTOS_MAGISTERIALES.values():
        items.append({
            "categoria": f"Magisterio · {doc['sigla']}",
            "titulo": f"{doc['sigla']} — {doc['titulo']}",
            "subtitulo": doc["subtitulo"],
            "keywords": f"{doc['sigla'].lower()} {doc['titulo'].lower()} vatican documento norma",
            "url": f"/formacion/documentos/{doc['id']}",
        })
        for sec in doc.get("secciones_clave", []):
            items.append({
                "categoria": f"Numeral · {sec['numeral']}",
                "titulo": f"{sec['numeral']}: {sec['titulo']}",
                "subtitulo": sec["extracto"][:110] + "…",
                "keywords": f"{sec['numeral'].lower()} {sec['titulo'].lower()} {sec['extracto'].lower()}",
                "url": f"/formacion/documentos/{doc['id']}",
            })

    # Los 16 Momentos de la Misa + Sus 4 Sub-páginas
    for m in MOMENTOS_MISA:
        items.append({
            "categoria": f"Misa #{m['orden']} · Resumen",
            "titulo": f"{m['orden']}. {m['titulo']} ({m['nombre_latino']})",
            "subtitulo": f"{m['naturaleza']} · {m['cita_igmr']} · Textos Latín/Español y Semáforo",
            "keywords": f"{m['titulo'].lower()} {m['nombre_latino'].lower()} {m['cita_igmr'].lower()} {m['naturaleza'].lower()} {m['resumen_corto'].lower()}",
            "url": f"/formacion/misa/{m['slug']}/resumen",
        })
        items.append({
            "categoria": f"Misa #{m['orden']} · Tratado",
            "titulo": f"{m['titulo']} — Tratado Teológico, Historia y Fuentes",
            "subtitulo": f"Mistagogía patrística, evolución histórica y citas de {m['cita_igmr']}",
            "keywords": f"{m['titulo'].lower()} teologia tratado historia padres igmr vatican",
            "url": f"/formacion/misa/{m['slug']}/teologia",
        })
        items.append({
            "categoria": f"Misa #{m['orden']} · Composición",
            "titulo": f"{m['titulo']} — Composición, Práctica y Checklist",
            "subtitulo": "Forma musical, prosodia, dirección en vivo y lista de verificación",
            "keywords": f"{m['titulo'].lower()} composicion practica checklist tesitura prosodia",
            "url": f"/formacion/misa/{m['slug']}/composicion",
        })
        items.append({
            "categoria": f"Misa #{m['orden']} · Repertorio",
            "titulo": f"{m['titulo']} — Repertorio y Audios Aplicados",
            "subtitulo": f"Obras con etiqueta {m['tag_repertorio']} y salmos sugeridos",
            "keywords": f"{m['titulo'].lower()} repertorio audios partituras canciones",
            "url": f"/formacion/misa/{m['slug']}/repertorio",
        })

    return items
