"""Crea (o vuelve a crear) la bóveda de Obsidian `cerebro/` a partir de las
páginas HTML del sitio. Cada página se vuelve una nota, y cada nota enlaza a la
página de la que depende y a sus ramas, igual que en el mapa.

Uso (desde la raíz del repositorio):  python3 herramientas/crear_cerebro.py
"""
import re
import shutil
import subprocess
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
CEREBRO = RAIZ / "cerebro"
ADJUNTOS = CEREBRO / "adjuntos"
SITIO = "https://mcpz-math.github.io/mi-universo/"
# Páginas que sólo redirigen a otra y no son una nota propia.
OMITIR = {"carbohidratos.html"}


def titulo(html):
    h1 = re.search(r"<h1>(.*?)</h1>", html, re.S).group(1).strip()
    partes = h1.split(" ", 1)
    # Las páginas de interés empiezan con un emoji: "🥗 Nutrición".
    if len(partes) == 2 and not partes[0][0].isascii():
        return partes[0], partes[1]
    return "☀️", h1


def padre(html):
    m = re.search(r'class="back-link" href="([^"]+)"', html)
    return m.group(1) if m else None


def cuerpo_markdown(html, imagenes):
    m = re.search(r'<section class="topic-body">(.*?)</section>', html, re.S)
    if not m:
        m = re.search(r'<header class="site-header wrap">.*?</h1>(.*?)</header>', html, re.S)
    parte = m.group(1)
    # Los mapas (SVG) se representan con los enlaces de la nota.
    parte = re.sub(r'<figure class="(tree|orbit)-figure">.*?</figure>', "", parte, flags=re.S)
    # La lámina dibujada a mano sólo se puede ver en la página web.
    parte = re.sub(r'<figure class="topic-image puntos-figure">.*?</figure>',
                   "<p><em>(La lámina propia de Los puntos se ve en la página web.)</em></p>",
                   parte, flags=re.S)

    def img(m):
        src = m.group(1)
        imagenes.append(src)
        return f"<p>IMAGEN:{Path(src).name}</p>"

    parte = re.sub(r'<img src="([^"]+)"[^>]*>', img, parte)
    md = subprocess.run(["pandoc", "-f", "html", "-t", "gfm", "--wrap=none"],
                        input=parte, capture_output=True, text=True, check=True).stdout
    md = re.sub(r"IMAGEN:(\S+)", r"![[\1]]", md)
    md = re.sub(r"<[^>]+>", "", md)  # restos de etiquetas (figure, figcaption)
    return re.sub(r"\n{3,}", "\n\n", md).strip()


def main():
    paginas = sorted(p for p in RAIZ.glob("*.html") if p.name not in OMITIR)
    datos = {}
    for p in paginas:
        html = p.read_text(encoding="utf-8")
        emoji, nombre = titulo(html)
        if p.name == "index.html":
            nombre = "Carmen"
        datos[p.name] = dict(html=html, emoji=emoji, nombre=nombre, padre=padre(html))

    # El sol "Carmen" es el padre de los planetas.
    for d in datos.values():
        if d["padre"] == "index.html" or (d["padre"] is None and d["nombre"] != "Carmen"):
            d["padre"] = "index.html"

    hijos = {k: [] for k in datos}
    orden = {}
    for k, d in datos.items():
        # El orden de las ramas es el mismo que en el mapa de la página padre.
        if d["padre"] in datos:
            hijos[d["padre"]].append(k)
    for k, d in datos.items():
        posiciones = {h: i for i, h in enumerate(re.findall(r'href="([a-z-]+\.html)"', d["html"]))}
        hijos[k].sort(key=lambda h: posiciones.get(h, 999))

    if CEREBRO.exists():
        for nota in CEREBRO.glob("*.md"):
            nota.unlink()
    ADJUNTOS.mkdir(parents=True, exist_ok=True)

    for k, d in datos.items():
        imagenes = []
        lineas = []
        if d["padre"]:
            lineas.append(f"Parte de: [[{datos[d['padre']]['nombre']}]]\n")
        lineas.append(f"# {d['emoji']} {d['nombre']}\n")
        if "Próximamente" in d["html"]:
            lineas.append("*Próximamente*\n")
        cuerpo = cuerpo_markdown(d["html"], imagenes)
        if cuerpo:
            lineas.append(cuerpo + "\n")
        if hijos[k]:
            lineas.append("## Ramas\n")
            lineas += [f"- [[{datos[h]['nombre']}]]" for h in hijos[k]]
            lineas.append("")
        lineas.append(f"---\n[Ver en la página web]({SITIO}{'' if k == 'index.html' else k})\n")
        (CEREBRO / f"{d['nombre']}.md").write_text("\n".join(lineas), encoding="utf-8")
        for src in imagenes:
            shutil.copy(RAIZ / src, ADJUNTOS / Path(src).name)


if __name__ == "__main__":
    main()
