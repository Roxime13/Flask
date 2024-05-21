from flask import Flask, request, render_template, redirect, url_for, flash
import feedparser

app = Flask(__name__)
app.secret_key = '¡3248 97320983 bkjxdlrkfj k2 r9p874989387 98p78oiyylkhçç'

def obtener_noticias(diario_nombre):
    diccionarionoticias = {
        "lavanguardia": {
            "Deportes": "https://www.lavanguardia.com/rss/deportes.xml",
            "Política": "https://www.lavanguardia.com/rss/politica.xml",
            "Vida": "https://www.lavanguardia.com/rss/vida.xml", 
            "Series": "https://www.lavanguardia.com/rss/series.xml",
            "Cultura": "https://www.lavanguardia.com/rss/cultura.xml"
        },
        "elpuntavui": {
            "Deportes": "https://www.elpuntavui.cat/rss/deportes.xml",
            "Política": "https://www.elpuntavui.cat/rss/politica.xml",
            "Vida": "https://www.elpuntavui.cat/rss/vida.xml",
            "Cultura": "https://www.elpuntavui.cat/rss/cultura.xml"
        }
    }

    noticias = []

    if diario_nombre in diccionarionoticias:
        diario_diccionarionoticias= diccionarionoticias[diario_nombre]
        for categoria, rss in diario_diccionarionoticias.items():
            feed = feedparser.parse(rss)
            for entry in feed.entries[:4]:
                noticia = {
                    "title": entry.get("title", ""),
                    "image": "", 
                }
                if "media_content" in entry:
                    noticia["image"] = entry.media_content[0]["url"]
                elif "media_thumbnail" in entry:
                    noticia["image"] = entry.media_thumbnail[0]["url"]
                noticias.append(noticia)

    return noticias

@app.route("/")
def menu_diarios():
    diarios = ['lavanguardia', 'elpuntavui'] 
    return render_template("menu.html", diaries=diarios)

@app.route("/<diario_nombre>")
def mostrar_noticias(diario_nombre):
    noticias = obtener_noticias(diario_nombre)
    return render_template("index.html", diario_nombre=diario_nombre, noticias=noticias)

@app.route('/<diario>/<seccion>')
def mostrar_noticias_por_seccion(diario, seccion):
    rss = None
    if diario == "lavanguardia":
        rss = get_rss_lavanguardia(seccion)
        if rss:
            return render_template("lavanguardia.html", diario_nombre="La Vanguardia", seccion_nombre=seccion, rss=rss)
    elif diario == "elpuntavui":
        rss = get_rss_elpuntavui(seccion)
        if rss:
            return render_template("elpuntavui.html", diario_nombre="El Punt Avui", seccion_nombre=seccion, rss=rss)
    
    return "Feed RSS no encontrado"

def get_rss_lavanguardia(seccion):
    xml = f"https://www.lavanguardia.com/rss/{seccion}.xml"
    # xml = f"./rss/lavanguardia/{seccion}.xml"
    rss = feedparser.parse(xml)
    return rss
 

def get_rss_elpuntavui(seccion):
    xml = f"http://www.elpuntavui.cat/{seccion}.feed?type=rss"
    # xml = f"./rss/elpuntavui/{seccion}.xml"
    
    rss = feedparser.parse(xml)
    
    return rss

if __name__ == "__main__":
    app.run(debug=True)