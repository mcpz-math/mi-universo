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
