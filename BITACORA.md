# Bitácora de avance — Mi Universo

## 2026-09-12 (primera versión del mapa)
- Se creó el repositorio `mcpz-math/mi-universo` y se activó GitHub Pages.
- Se armó la primera versión del mapa mental (`index.html`): el sol central
  "Carmen" conectado a 5 planetas, uno por cada interés inicial: Matemáticas,
  Música, Lectura, Salud y Zhineng Qigong.
- Se creó una página propia para cada interés (`matematicas.html`,
  `musica.html`, `lectura.html`, `salud.html`, `zhineng-qigong.html`), todas
  con la etiqueta "Próximamente" hasta que Carmen comparta contenido para
  llenarlas.
- Se definió el estilo visual "Universo" en `assets/style.css`: cielo
  nocturno, estrellas de fondo, y un color propio para cada planeta.

## 2026-09-12 (primera rama dentro de un interés: Diabetes en Salud)
- En `salud.html` se agregó un pequeño diagrama de rama que conecta el planeta
  "Salud" con un primer subtema: "Diabetes".
- Se creó su página propia `diabetes.html` (con la etiqueta "Próximamente"),
  enlazada de regreso a `salud.html`.
- Este patrón (rama dentro de la página de un interés, con su propia página)
  queda listo para repetirse cuando se agreguen más subtemas, en Salud o en
  cualquier otro interés.

## 2026-09-12 (subramas de Diabetes)
- En `diabetes.html` se agregó un diagrama con 4 subramas: Rangos y síntomas,
  Remisión de la diabetes, Cuidados y Medicamentos.
- Se creó una página propia para cada una (`rangos-sintomas.html`,
  `remision.html`, `cuidados.html`, `medicamentos.html`), todas con la
  etiqueta "Próximamente" y su enlace de regreso a Diabetes.

## 2026-09-12 (sexto planeta: Nutrición)
- Se agregó "Nutrición" como un nuevo planeta que sale directo de Carmen en
  `index.html`. Con 6 planetas el mapa se reacomodó a un hexágono parejo (antes
  eran 5 repartidos en pentágono) para que quede bien distribuido.
- Se creó su página propia `nutricion.html` con la etiqueta "Próximamente".

## 2026-09-12 (se quitó el planeta Música)
- Se eliminó el planeta "Música" del mapa (línea, planeta y `musica.html`).
- El mapa volvió a acomodarse en pentágono con los 5 planetas restantes:
  Matemáticas, Lectura, Nutrición, Salud y Zhineng Qigong.

## 2026-09-12 (toque "red neuronal")
- Carmen preguntó si convenía ver la página como una red neuronal (muchos
  nodos conectados entre sí, sin orden claro) — se le explicó que eso no
  conviene para este proyecto porque pierde la claridad jerárquica del mapa
  mental, pero que sí se podía dar ese "look" sin perder el orden.
- Se le dio un toque de red neuronal al estilo visual en `assets/style.css`:
  las líneas ahora tienen un pulso animado (como una señal viajando) y los
  planetas (y el sol "Carmen") tienen un brillo dorado alrededor, que se
  intensifica al pasar el mouse. La estructura de mapa mental (árbol con
  centro y ramas) se mantiene igual.

## 2026-09-12 (quitar el círculo que unía todos los planetas)
- Carmen notó que un círculo punteado de fondo pasaba por todos los planetas
  y daba la impresión de que estaban conectados entre sí, cuando solo están
  conectados al centro. Se quitó ese círculo de `index.html` y `diabetes.html`.
- Se anotó en CLAUDE.md que Carmen es quien decide qué nodos se conectan
  entre sí — no se deben agregar líneas, círculos u otros elementos que
  sugieran una conexión que ella no haya pedido.

## 2026-09-12 (el árbol completo de Salud en una sola imagen)
- Carmen pidió ver, en la imagen de Salud, todo lo que ya se había armado
  para ese interés. Se rehízo el diagrama de `salud.html` como un árbol de
  tres niveles en una sola imagen: Salud → Diabetes → sus 4 subtemas (Rangos
  y síntomas, Remisión, Cuidados, Medicamentos).
- Se agregó la clase `.tree-figure` en `assets/style.css` para este tipo de
  diagrama más ancho.
- De paso se corrigió un error: la regla de color de las etiquetas de texto
  (`.node-label-out`) solo aplicaba dentro de un planeta del mapa principal,
  así que en los diagramas de rama ("Salud", "Diabetes", etc.) el texto no
  tomaba el color correcto. Ahora aplica en todos los diagramas por igual.

## 2026-09-12 (primera imagen en Nutrición)
- Carmen subió una imagen (la pirámide de la dieta mediterránea) directamente
  a GitHub. Se guardó en `materiales/piramide-mediterranea.png` y se agregó
  a `nutricion.html` dentro de un marco a juego con el estilo del sitio.
- Se agregó la clase `.topic-image` en `assets/style.css` para mostrar
  imágenes dentro de la página de un interés.

## 2026-09-12 (arreglo real de las etiquetas de texto)
- El arreglo anterior a `.node-label-out` (para que se vieran los nombres en
  Salud y Diabetes) sin querer rompió las etiquetas del mapa principal: ahí
  compite con otra regla más específica que las pintaba oscuras. Se corrigió
  para que `.node-label-out` siempre gane y las etiquetas se vean en todas
  las páginas por igual.

## 2026-09-12 (título "Dieta Mediterránea")
- Se agregó el título "Dieta Mediterránea" justo antes de la imagen de la
  pirámide en `nutricion.html`.

## 2026-09-12 (lista de grasas antes de la pirámide)
- Se agregó, antes de la pirámide, una lista con las grasas de la dieta
  mediterránea: aceite de oliva, frutos secos y pescados.
- Se agregó estilo para listas dentro de la página de un interés en
  `assets/style.css`.
- Se agregó también la frase "Los cereales y los vegetales son la base de
  los platillos."
- Y la frase "Las carnes y similares son ahora la guarnición."
- Y la frase "Se añaden factores socioculturales y actividad física."
- Y la frase "Tomar de 1.5 a 2 litros de agua."

## 2026-09-13 (primer subtema de Nutrición: Minicurso para contar carbohidratos)
- Carmen compartió una fotografía de sus apuntes de un minicurso sobre cómo contar
  carbohidratos, y pidió que fuera un subtema de Nutrición (mismo patrón que
  Salud → Diabetes), en vez de una sección dentro de `nutricion.html`.
- Se agregó en `nutricion.html` un diagrama de rama (`.branch-figure`) que conecta
  "Nutrición" con su primer subtema, "Minicurso para contar carbohidratos", con un color
  propio (`--c-nutricion-branch` en `assets/style.css`).
- Se creó la página propia `carbohidratos.html` (enlazada de regreso a Nutrición) con el
  contenido del minicurso: qué es un carbohidrato y en qué alimentos se encuentra,
  macronutrientes y micronutrientes, y cómo medir porciones (taza medidora de 240 ml,
  media taza ≈ una porción, 15 g ≈ una porción para alimentos formados como una
  tortilla).

## 2026-09-13 (Dieta Mediterránea también como subtema)
- Carmen pidió que, al entrar a Nutrición, se vieran dos ramas: "Dieta Mediterránea" y
  "Minicurso para contar carbohidratos", cada una con su propio contenido en su página.
- Se sacó el contenido de la Dieta Mediterránea (que antes vivía directo en
  `nutricion.html`) a su propia página `dieta-mediterranea.html`, con el mismo patrón que
  `carbohidratos.html`.
- `nutricion.html` ahora solo muestra el diagrama de rama con los dos subtemas de
  Nutrición (Dieta Mediterránea y Minicurso para contar carbohidratos), igual que
  `salud.html` muestra sus subtemas.

## 2026-09-13 (ajustes al Minicurso para contar carbohidratos)
- "Macronutrientes" y "Micronutrientes" eran subtítulos dentro del texto; se cambiaron de
  párrafo normal a encabezado (`<h2>`) en `carbohidratos.html` para que se vean
  diferenciados en tamaño y en negritas.
- Se agregó al final la nota sobre las frutas: una pieza de fruta equivale a una porción
  (solo cuando no se pide medir con taza), y debe verse del tamaño del puño de la mano.

## 2026-09-20 (más contenido en el Minicurso para contar carbohidratos)
- Se agregó el título "Recomendaciones para el conteo de carbohidratos" en
  `carbohidratos.html`, justo antes de los párrafos sobre la taza medidora y las
  porciones (para separar esa parte del resto del contenido).
- Carmen pidió buscar en la red qué son los micronutrientes y agregar un resumen
  breve. Se agregó, debajo del título "Micronutrientes", un párrafo explicando que
  son las vitaminas y minerales que el cuerpo necesita en pequeñas cantidades pero
  son esenciales, y que deben obtenerse de la alimentación porque el cuerpo no los
  produce por sí solo.
- Carmen compartió, en 4 fotos, la "Tabla de raciones de hidratos de carbono" de la
  Dra. Zuraima Corona (especialista en diabetes). Se guardaron las 4 páginas en
  `materiales/` (`tabla-raciones-hidratos-carbono.png`, `-2.png`, `-3.png`, `-4.png`)
  y se agregaron a `carbohidratos.html`, al final, después del párrafo sobre la
  fruta y el puño de la mano.
- Se convirtieron en lista las notas que estaban debajo de "Recomendaciones para el
  conteo de carbohidratos" en `carbohidratos.html` (antes eran párrafos sueltos).
- Se agregó a esa misma lista la nota "Podemos preguntar a Google cuántos gramos de
  carbohidratos hay en la porción que vamos a comer."
- Se agregó, en la lista de dónde se encuentran los carbohidratos, la nota "Los
  vegetales son los alimentos que menos carbohidratos tienen", justo antes de
  "Entre otros...".
- Carmen pidió quitar las imágenes de la tabla de raciones de hidratos de carbono; se
  quitaron de `carbohidratos.html` y se borraron los 4 archivos de `materiales/`.
- Se simplificó la frase sobre dónde están los carbohidratos: "Están en todas las
  frutas, cereales, granos, tubérculos, leche y yogurt."
- Se agregó la sección "Lectura de etiquetas" con 3 notas en lista: observar la
  porción de la etiqueta, que toda la información corresponde a esa porción, y no
  olvidar que el conteo es por porción.
- Se agregó la sección "Índice glucémico" con 3 notas en lista: qué es el índice
  glucémico (capacidad de un alimento para elevar la glucosa en la sangre), que el
  mismo número de carbohidratos en diferentes alimentos no da el mismo índice
  glucémico, y que los alimentos con fibra suben la glucosa más lento (índice
  glucémico más bajo).

## 2026-09-20 (primeras 9 sesiones de Zhineng Qigong)
- Carmen pidió crear nodos llamados "sesiones" dentro de Zhineng Qigong, para irlos
  agregando poco a poco. Se armaron los primeros 9: Preparación, Qué es el Zhineng
  Qigong, Principios fundamentales, Zu Chang Fa, Método para levantar y verter el Qi,
  Método de las sentadillas de pared, Du Quian Fa, La Qi y Conclusión.
- En `zhineng-qigong.html` se agregó un diagrama de árbol con Zhineng Qigong al centro
  y las 9 sesiones en una columna a la derecha, cada una con su línea de conexión
  (mismo patrón que Salud → Diabetes, pero con 9 ramas en vez de 4).
- Se creó una página propia para cada sesión (`preparacion.html`,
  `que-es-zhineng-qigong.html`, `principios-fundamentales.html`, `zu-chang-fa.html`,
  `levantar-verter-qi.html`, `sentadillas-pared.html`, `du-quian-fa.html`, `la-qi.html`,
  `conclusion.html`), todas con la etiqueta "Próximamente" y su enlace de regreso a
  Zhineng Qigong.
- Se agregó el color `--c-qigong-branch` en `assets/style.css` para estas 9 ramas.

## 2026-09-20 (primer contenido de Zhineng Qigong: Preparación)
- Carmen compartió 6 fotos de sus apuntes a mano del curso de Zhineng Qigong
  (módulo "Bienvenida e introducción", 1/11).
- Se llenó `preparacion.html` con todo el contenido de esas fotos, organizado en
  secciones: la lista de indicaciones de Preparación, sobre la instrucción que se
  va a recibir, aprender a acomodar el cuerpo, cuerpo/postura/emociones, cómo
  sentarnos en una silla, el Ming Men, los tres aspectos de la instrucción (Xing
  Chuan, Kou Chuan, Xin Chuan), sobre sanar y recibir la instrucción, cómo recibir
  adecuadamente la instrucción, no comparar/no interpretar, sensaciones y
  reacciones, atención en nosotros mismos y el Qi, y bibliografía.
- Se quitó la etiqueta "Próximamente" de `preparacion.html` ya que ahora tiene
  contenido.
- Quedaron pendientes dos frases que se cortaban en el borde de las fotos, y el
  inicio de un tema nuevo ("Testimonio 2/11") del que solo se veía el título sin
  notas — para completar cuando Carmen tenga esa información.

## 2026-10-03 (primer contenido de "Qué es el Zhineng Qigong")
- Se agregó en `que-es-zhineng-qigong.html` la frase: "El Zhineng Qigong es una
  ciencia avalada por el Buró Nacional de Ciencias, el gobierno chino y el
  Ministerio de Salud Pública."
- Se quitó la etiqueta "Próximamente" de esa página, ya que ahora tiene contenido.
- Se agregó el párrafo: "Es una ciencia milenaria y es una práctica que nos enseña
  a manejar el Qi. Todos sus movimientos tienen por objetivo ayudar a que el Qi se
  mueva de manera más eficiente en nuestro cuerpo."
- Se agregó el párrafo: "El entrenamiento está diseñado para mejorar la salud
  física, mental y emocional, pues todo lo que hacemos desequilibra el Qi. La única
  práctica correcta para equilibrar el Qi es el Qigong."
- Carmen pidió poner lo escrito como lista: los tres párrafos de
  `que-es-zhineng-qigong.html` se convirtieron en una lista con viñetas.
- Carmen compartió una foto de sus apuntes (dos columnas). Se agregó a la lista la
  nota "Todos los deportes desequilibran nuestro Qi." y una sección nueva,
  "Zhi 智 (Sabiduría)", con sus notas en lista: sabiduría ≠ inteligencia, la
  sabiduría se despierta (no se aprende), la sabiduría del cuerpo, las emociones y
  la mente, el cuerpo como mecanismo de frecuencias, y por qué los medicamentos
  tienen efectos secundarios. Las frases que Carmen resaltó en verde en sus
  apuntes se pusieron en negritas.
- Carmen compartió otra foto de sus apuntes. Se agregaron 4 notas más a la sección
  "Zhi 智 (Sabiduría)" (el cultivo del silencio, desde la paz todo puede florecer, y
  Zhi como despertar de la sabiduría) y tres secciones nuevas, una por cada parte
  del nombre: "Neng 能 (Talento)", "Qi 气" (qué es el Qi, por qué practicamos, los
  dos aspectos del Qi) y "Gong 功" (trabajo y esfuerzo realizado con el corazón).
  Lo resaltado en verde va en negritas.
- Carmen compartió una tercera foto. Se agregaron dos secciones más: "Qi Gong"
  (trabajar con nuestro Qi; cómo las posturas, los movimientos, los sonidos y la
  mente influyen en el Qi; buscar respuestas en el silencio) y "Zhi Neng Qi Gong"
  ("Trabajar con nuestro Qi para despertar nuestra sabiduría").
- Carmen compartió la foto de sus apuntes del módulo "Antecedentes históricos y
  anatomía sutil" (4/11) y eligió que fueran en esta misma página (no como sesión
  nueva). Se agregaron dos secciones: "Antecedentes históricos y anatomía sutil" y
  "Diferencias con otras formas de Qi Gong".
- Carmen compartió otra foto. Se agregaron 6 notas más a "Diferencias con otras
  formas de Qi Gong" (seguridad, profundidad, Pang Ming como creador, impacto
  económico, sinergia, no requiere diagnóstico) y tres secciones nuevas:
  "Anatomía del Qi" (los dos sistemas, interno y externo), "Sistema interno de Qi"
  (canales o meridianos) y "Dan Tian" (qué son, sus funciones, y el primero de los
  tres: el Dan Tian bajo). Los otros dos Dan Tian quedan pendientes para la
  siguiente foto.
- Carmen compartió otra foto. Se completaron los tres Dan Tian (medio y alto), se
  agregaron 4 notas más a "Dan Tian" (el ser humano: cuerpo, emociones y mente;
  arraigarnos hacia abajo; el Qi tiende a subir; verterlo en el Dan Tian bajo) y una
  sección nueva, "Sistema externo" (el campo, la entrada y salida del Qi, la
  sustitución celular).
- Pendientes: la frase "Todo cuerpo tiene un campo, cada átomo de tu cuerpo tiene
  un campo, cada molécula de tu…" se corta al final de la foto, y hay que confirmar
  con Carmen si el Dan Tian alto se relaciona con el aspecto "emocional" (como se
  leyó en sus apuntes) o con otro aspecto.
