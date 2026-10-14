# Mi Universo — Carmen (mcpz-math)

## Sobre el proyecto
Mapa mental digital de los intereses personales de Carmen (no es material para
alumnos — es un proyecto personal, aparte del sitio de matemáticas).
Publicado gratis con GitHub Pages en: https://mcpz-math.github.io/mi-universo/

- Usuario de GitHub: `mcpz-math`
- Repositorio: `mcpz-math/mi-universo`

## Preferencias de Carmen para trabajar juntos
- Prefiere avanzar **paso a paso, una cosa a la vez**, con instrucciones claras y sin
  saltarse pasos.
- Comunicación en español.
- No tiene experiencia técnica previa con GitHub/git — explicar en lenguaje sencillo,
  sin dar por hecho conocimientos técnicos.
- Quiere que los cambios se sincronicen sobre la marcha al repositorio de GitHub.
- **Publicar siempre**: después de cada cambio, publicarlo directamente en el sitio
  (crear el pull request hacia `main` y fusionarlo uno mismo), sin preguntar, a menos
  que Carmen diga lo contrario.
- Llevar un registro de avance en [BITACORA.md](BITACORA.md) — actualizarlo cada vez
  que se agregue o cambie algo importante.
- El nombre de la práctica se escribe siempre **"ZhiNeng Qigong"** (así, con la N
  mayúscula y Qigong junto), en todas las páginas y en el mapa. Si Carmen lo escribe
  de otra forma en sus apuntes, se pasa a esta forma.
- Carmen decide qué nodos se conectan entre sí. No agregar conexiones,
  círculos u otros elementos decorativos que sugieran una relación entre
  nodos que ella no haya pedido explícitamente.

## Estilo visual
"Universo": cielo nocturno (#0b1030) + crema cálido (#f4f1e6) + acento dorado
(#f2c14e), con un fondo de estrellas. Cada interés es un planeta de color propio
alrededor del sol central ("Carmen"). Tipografías: Outfit (títulos) y Karla
(texto) — las mismas que el sitio de matemáticas, para que se sienta parte de la
misma familia. Estilos compartidos en `assets/style.css`.

## Estructura del sitio
- `index.html` — el mapa mental: el sol central ("Carmen") conectado a un planeta
  por cada interés.
- Una página HTML por interés en la raíz del repositorio (ej. `matematicas.html`,
  `musica.html`, `lectura.html`, `salud.html`, `zhineng-qigong.html`).
- Todas las páginas de interés muestran la etiqueta "Próximamente" hasta que Carmen
  comparta contenido para llenarlas.
- Para agregar un nuevo interés: se agrega un planeta más en el mapa de `index.html`
  (línea + círculo + etiqueta) y su página propia, siguiendo el mismo patrón.

## Cerebro digital en Obsidian
- La carpeta `cerebro/` es una bóveda de Obsidian con una nota por cada página del
  sitio (mismo contenido, y enlaces `[[...]]` sólo entre cada página y sus ramas, igual
  que en el mapa). Las imágenes están en `cerebro/adjuntos/`.
- Se genera desde las páginas HTML con `python3 herramientas/crear_cerebro.py` (usa
  pandoc). **Después de cada cambio al sitio, volver a correrlo** para que Obsidian
  quede igual que la página. El sitio es la fuente; no editar las notas a mano.
- `_config.yml` excluye `cerebro/` y `herramientas/` de la página publicada.

## Flujo de trabajo para agregar contenido
1. Elegir el interés a trabajar (uno de los planetas del mapa).
2. Carmen comparte el contenido (texto en el chat, fotos, notas, lo que sea).
3. Se llena la página de ese interés siguiendo el estilo "Universo".
4. Se actualiza la bóveda de Obsidian (`python3 herramientas/crear_cerebro.py`).
5. Se sincroniza automáticamente con GitHub (commit + push) y se publica (pull
   request hacia `main` fusionado).
6. Se anota el avance en [BITACORA.md](BITACORA.md).
