# Index
1. ## Instal.lació Flask i entorn
2. ### Creació entorn
3. ### Qué es Pip?


## Instal.lació Flask i entorn

### Creació entorn
### ¿Qué és Flask?
### Jinja
### Resum instal.lació
## Git (Preparació entorn repositori i comandes importants)
## RSS
## FeedParser i Modes
## Enllaços d'Interés

** Windows **
- .prova/Scripts/activate
- Per desactivar: desactivate

** Linux **
- Per activar: source .prova/Scripts/activate
- Per desactivar: desactivate

Per poder crear l'entorn virtual, es ha de fer servir l'eina virtualenv que el que fa és instal·lar llibreries python de manera privada a un projecte, i per això facilita la recreació de l'entorn amb màquines diferents de la que vam utilitzar per iniciar el projecte.
per instal·lar-lo s'ha de fer servir: `python install virtualenv`

### Qué es Pip?

Pip és un instal·lador de paquets de python i serveix per gestionar les dependències, inclòs la de virtualenv.

#### Instal.lar pip (python package Index)

1. pip install (nompaquet)
2. -U (nompaquet) actualitzar paquet a l'última versió
3. freeze per veure tots els paquets que s'han instal·lat.


```python 

Per instal·lar pip install (nompaquet)

pip uninstall (nompaquet)

U (nompaquet) actualitzar paquet a l'última versió

freeze per veure tots els paquets que s'han instal·lat

```

```python
$ pip freeze
beautifulsoup4==4.12.3
blinker==1.7.0
bs4==0.0.2
click==8.1.7
colorama==0.4.6
feedparser==6.0.11
Flask==3.0.3
importlib_metadata==7.1.0
itsdangerous==2.2.0
Jinja2==3.1.3
lxml==5.1.0
MarkupSafe==2.1.5
mysql-connector-python==8.3.0     
sgmllib3k==1.0.0
soupsieve==2.5
zipp==3.18.1
```
---

Si ja s'ha instal·lat l'entorn es pot guardar els paquets que surten amb la comanda pip Freeze a l'arxiu de requirements.txt e instal·lar d'una tots els paquets necessaris amb: `install -r requirements.txt`

---

### ¿Qué és Flask?

Flask és un framework escrit en Python que permet crear aplicacions de forma senzilla i ràpida.

Després del pip, forma inicial s'ha d'instal·lar flask amb: `pip install Flask`.

En aquest cas, pel treball per començar a treballar, i la comanda per posar en marxa l'entorn i que es desplegui l'aplicació web seria: `Flask run --debug`

```python 
import flask

@app.route("/demo1")
def demo1():
    return render_template("exemples/demo/hola.html")

@app.route("/demo2")
def demo2():
    return render_template("exemples/demo/edat.html", nom="Alfonso", edat=26)

@app.route("/demo3/<nom_usuari>/<int:edat>")
def demo3(nom_usuari, edat):
    return render_template("exemples/demo/edat.html", nom = nom_usuari, edat = edat)

@app.route("/demo4")
def demo4():
    nom = request.args.get('nom', default = "Desconegut/a", type = str)
    edat = request.args.get('edat', default = 0, type = int)
    return render_template("exemples/demo/edat.html", nom = nom, edat = edat)


```
---

### Jinja

Jinja treballa amb Flask i es una llibreria que permet generar documents HTML de manera rápida i sencilla. 

#### Sintaxi

- Expressions: Les expressions s'encapsulen amb dobles claudàtors {{ }}. Aquestes s'utilitzen per avaluacions d'expressions, com accedir a variables o cridar funcions.

- Estructures de control: Les estructures de control, com les instruccions if, for, elif, i else, s'encapsulen amb claudàtors i signes de percentatge {% %}.

Un exemple seria el següent:

```jinja
{{% if %}}
{{% elif %}}
{{% else %}}
{{% endif %}}


```

---

### Resum instal.lació

En resum, les passes a seguir serien les següents per crear per primer cop l'entorn virtual serien les següents: 
1. `python  -m pip install virtualenv`
2. virtualenv venv
3. Activar l'entorn on tenim la carpeta. Windows: venv\Scripts\activate y Linux/macos: source venv/bin/activate
4. Instal.lar pip amb `pip install` 
5. pip install Flask  (si no s'ha isntal.lat)
6. Flask run --debug 


En aquest cas, com ja tenim la carpeta amb el codi base de l'aplicació només caldria instalar els requirements amb `install -r requirements.txt` i  fer l'últim pas que seria `Flask run --debug`. 

---

## Git (Preparació entorn repositori i comandes importants)

A continuació, explico les passes per iniciar el repositori del projecte:

1. git init: Inicialitzara un repositori buit
2. git branch -m master main: Es canvia el nom de la branca, per a que no hi hagi problemes de compatibilitat en un futur.
3. Git status: Per comprovar que estic a la branca que vull, en aquest cas, main. Si hi ha arxius amb modificacions sortirà una llista amb els pendents.
4. git add *: S'utilitza per afegir tots els arxius o carpetes pendents a la vegada.
5. git commit -m "comentari a posar": És per guardar els arxius per poder-ho pujar.
6. Git status: Comprovar que s'han afegit bé els que en vull
7. git remode add origin + ruta repositori: Per vincular un repositori local amb un repositori remot.
8. git remote -v: Mostra llista dels remots associats al repositori local, junt amb les URLs.
9. git push origin main: Pujar els arxius afegits al repositori remot.

Una altra comanda important seria git branch --list que serveix per veure la llista de les branques existents en el repositori.

```bash
sanru@Sandra MINGW64 ~/Escritorio/M04, llenguatge de marques/projecteflask (master)
$ git branch -m master main

sanru@Sandra MINGW64 ~/Escritorio/M04, llenguatge de marques/projecteflask (main)
$ git branch --list

sanru@Sandra MINGW64 ~/Escritorio/M04, llenguatge de marques/projecteflask (main)
$ git branch

sanru@Sandra MINGW64 ~/Escritorio/M04, llenguatge de marques/projecteflask (main)
$ git branch -r

sanru@Sandra MINGW64 ~/Escritorio/M04, llenguatge de marques/projecteflask (main)
$ git status
On branch main

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
    	.gitignore
    	README.md
    	app.py
    	requirements.txt
    	rss/
    	static/
    	templates/

nothing added to commit but untracked files present (use "git add" to track)

sanru@Sandra MINGW64 ~/Escritorio/M04, llenguatge de marques/projecteflask (main)
$ git add *
warning: in the working copy of 'README.md', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'app.py', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'requirements.txt', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'rss/lavanguardia/deportes.xml', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'rss/lavanguardia/politica.xml', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'rss/lavanguardia/vida.xml', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'static/css/style.css', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'templates/exemples/demo/boostrap.html', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'templates/exemples/demo/edat.html', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'templates/exemples/demo/hola.html', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'templates/exemples/hola/salutacio_form.html', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'templates/exemples/hola/salutacio_resultat.html', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'templates/exemples/insert/insert_form.html', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'templates/index.html', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'templates/lavanguardia.html', LF will be replaced by CRLF the next time Git touches it

sanru@Sandra MINGW64 ~/Escritorio/M04, llenguatge de marques/projecteflask (main)
$ git status
On branch main

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
    	new file:   README.md
    	new file:   app.py
    	new file:   requirements.txt
    	new file:   rss/lavanguardia/deportes.xml
    	new file:   rss/lavanguardia/politica.xml
    	new file:   rss/lavanguardia/vida.xml
    	new file:   static/css/style.css
    	new file:   static/img/diaris.jpg
    	new file:   static/img/gat.jpg
    	new file:   templates/exemples/demo/boostrap.html
    	new file:   templates/exemples/demo/edat.html
    	new file:   templates/exemples/demo/hola.html
    	new file:   templates/exemples/hola/salutacio_form.html
    	new file:   templates/exemples/hola/salutacio_resultat.html
    	new file:   templates/exemples/insert/insert_form.html
    	new file:   templates/index.html
    	new file:   templates/lavanguardia.html

Untracked files:
  (use "git add <file>..." to include in what will be committed)
    	.gitignore


sanru@Sandra MINGW64 ~/Escritorio/M04, llenguatge de marques/projecteflask (main)
$ git commit -m "El meu primer commit"
[main (root-commit) 0ae289a] El meu primer commit
 17 files changed, 5482 insertions(+)
 create mode 100644 README.md
 create mode 100644 app.py
 create mode 100644 requirements.txt
 create mode 100644 rss/lavanguardia/deportes.xml
 create mode 100644 rss/lavanguardia/politica.xml
 create mode 100644 rss/lavanguardia/vida.xml
 create mode 100644 static/css/style.css
 create mode 100644 static/img/diaris.jpg
 create mode 100644 static/img/gat.jpg
 create mode 100644 templates/exemples/demo/boostrap.html
 create mode 100644 templates/exemples/demo/edat.html
 create mode 100644 templates/exemples/demo/hola.html
 create mode 100644 templates/exemples/hola/salutacio_form.html
 create mode 100644 templates/exemples/hola/salutacio_resultat.html
 create mode 100644 templates/exemples/insert/insert_form.html
 create mode 100644 templates/index.html
 create mode 100644 templates/lavanguardia.html

sanru@Sandra MINGW64 ~/Escritorio/M04, llenguatge de marques/projecteflask (main)
$ git status
On branch main
Untracked files:
  (use "git add <file>..." to include in what will be committed)
    	.gitignore

nothing added to commit but untracked files present (use "git add" to track)

sanru@Sandra MINGW64 ~/Escritorio/M04, llenguatge de marques/projecteflask (main)
$ git remote add origin https://github.com/Roxime13/Flask.git

sanru@Sandra MINGW64 ~/Escritorio/M04, llenguatge de marques/projecteflask (main)
$ git remote --v
origin  https://github.com/Roxime13/Flask.git (fetch)
origin  https://github.com/Roxime13/Flask.git (push)

sanru@Sandra MINGW64 ~/Escritorio/M04, llenguatge de marques/projecteflask (main)
$ git push origin main
info: please complete authentication in your browser...
Enumerating objects: 29, done.
Counting objects: 100% (29/29), done.
Delta compression using up to 20 threads
Compressing objects: 100% (26/26), done.
Writing objects: 100% (29/29), 236.61 KiB | 5.03 MiB/s, done.
Total 29 (delta 3), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (3/3), done.
To https://github.com/Roxime13/Flask.git
 * [new branch]  	main -> main



```
---
## RSS
RSS ve de les sigles Really Simple Syndication. És un http (acabar de veure l'RSS), S'utilitza el feedparser llegeix el contingut del fitxer rss i recupera les dades. L'objectiu és actualitzar un lloc web dins d'un "feed" similar al que s'fa servir a les xarxes socials.

els avantatges que té utilitzar un Feed RSS en un lloc web són les següents:

- ***Actualitzacions en temps real*** : S'actualitza quasi de forma simultània amb el lloc web. Això assegura que les noves publicacions es vegi a l'instant.

-***Senzillesa***:
És discret i intrusiva, fent que sigui visual i atractiu pel públic.

-***SEO***:
RSS informa Google i a altres motors de cerca dels canvis recents del lloc, fent que s'indexi de manera ràpida i que el contingut estigui actualitzat.

```xml
<rss xmlns:media="http://search.yahoo.com/mrss/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:atom="http://www.w3.org/2005/Atom" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:content="http://purl.org/rss/1.0/modules/content/" xmlns:og="https://ogp.me/ns#" version="2.0">
    <channel>
        <title>Series</title>
        <description>Series</description>
        <image>
            <url>https://www.lavanguardia.com/images/logo.png</url>
            <title>Series</title>
            <link>https://www.lavanguardia.com/series</link>
            <description>Logo LV</description>
        </image>
        <link>https://www.lavanguardia.com/series</link>
        <atom:link rel="self" type="application/rss+xml" href="https://www.lavanguardia.com/rss/series.xml"/>
        
<item>
     <guid isPermaLink="true">https://www.lavanguardia.com/series/20240507/9616481/donde-rodado-shogun-exitosa-serie-disney-mundo-habla-mmn.html</guid>
     <title>
         Dónde se ha rodado &#039;Shogun&#039;, la exitosa serie de Disney+ de la que todo el mundo habla
     </title>
     <description>
         Los 10 capítulos de la ficción se encuentran ya disponibles en la plataforma de streaming&amp;nbsp;
     </description>
     <pubDate>07 May 2024 11:09:14 +0200</pubDate>
     <link>https://www.lavanguardia.com/series/20240507/9616481/donde-rodado-shogun-exitosa-serie-disney-mundo-habla-mmn.html</link>
             <enclosure type="image/jpeg" length="323145" url="https://www.lavanguardia.com/files/og_thumbnail/uploads/2024/02/22/65d7ab39143f5.jpeg"/>
         <category>Series</category>
     <dcterms:modified>2024-05-07T11:09:14+02:00</dcterms:modified>
     <dc:creator>Nerea Parraga Frutos</dc:creator>
             <content:encoded>&lt;![CDATA[&lt;p&gt;&lt;i&gt;&lt;a href=&quot;https://www.lavanguardia.com/andro4all/series/el-final-de-shogun-explicado-por-uno-de-sus-protagonistas-hiroyuki-sanada-lord-toranaga&quot; target=&quot;_blank&quot;&gt;Shogun&lt;/a&gt;&lt;/i&gt; ha sido sin duda uno de los grandes estrenos de esta primera mitad del año. La ficción, basada en el&amp;nbsp;best-seller de 1975 del mismo nombre y escrito por James Clavell, se estrenó en Disney + el pasado 27 de febrero. Desde entonces, la serie fue estrenando semana a semana capítulos en la plataforma hasta culminar con su décimo episodio el pasado 23 de abril.&amp;nbsp;&lt;/p&gt;&lt;p&gt;&lt;a href=&quot;https://www.lavanguardia.com/series/20240507/9616481/donde-rodado-shogun-exitosa-serie-disney-mundo-habla-mmn.html&quot;&gt;Seguir leyendo...&lt;/a&gt;&lt;/p]]&gt;</content:encoded>
                 <media:content type="image/jpeg" medium="image" url="https://www.lavanguardia.com/files/og_thumbnail/uploads/2024/02/22/65d7ab39143f5.jpeg"/>
     </item>



```

---
## FeedParser i Modes

Feedparser és un paquet de python. La seva utilitat resideix en que pot extreure informació sobre un lloc web específic o  una publicació amb feed RSS. Es fa servir per llegir feeds RSS. 

A continuació, explico els dos modes per poder conectar-se al RSS d'un lloc web, en aquest cas, La Vanguardia. Per els dos casos, es necessari importar la llibreria de feedparser, aquest són: Remot i Local. 

Per extreure informació, en aquest cas de la descripció, logo, author,categoria, data de publicació i data d'última modificiació 

```python 
import feeedparser
<h1>La Vanguardia - <small><a href="/">{{rss.feed.title}}</a></small></h1>
    <img src="{{rss.feed.image.url}}" alt="{{rss.feed.image.description}}"/>
    {% for item in rss.entries %}
        <p>
            <a href="{{item.link}}">{{item.title}}</a>
            {% for media in item.media_content %}
                <p><img src="{{media.url}}" alt="{{item.title}}" /></p>
                <p><b>Autor: </b>{{item.author}}</p>
                <p><b>Categoría:</b>{{item.category}}</p>
                <p><b>Fecha de publicación:</b>{{item.published}}</p>
                <p><b>Última actualitzación:</b> {{item.updated}} </p>
            {% endfor %}
        </p>
    {% endfor %}

```

### Mode Remot

En el mode remot, FeedParser accedeix directament a l'URL del feed RSS a través d'Internet. és una opció útil per tal d'obtenir les últimes actualitzacions d'un feed sense descarregar i guardar l'XML manualment en el sistema. 

Per enllaçar amb el feed remot s'ha de seguir el següent pas: 

```python 
import feedparser
def get_rss_lavanguardia(seccio):
    # MODE REMOT: versió on descarrega l'XML de la web
    xml = f"https://www.lavanguardia.com/rss/{seccio}.xml" 

```

### Mode local

En el mode local, FeedParser utilitza un fitxer XML que ja s'ha descarregat i guardat localment al sistema. És útil utilitzar-ho si es vol treballar amb un feed RSS sense haver de fer peticions en xarxa cada vegada que es necessiti accedir. 

El següent fragment indica com fer-ho: 

```python 
import feedparser

def get_rss_lavanguardia(seccio):
    xml = f"./rss/lavanguardia/{seccio}.xml"
    
    rss = feedparser.parse(xml)
    return rss


```

## Enllaços d'Interés
* [Feedparser](https://mr-destructive.github.io/techstructive-blog/python-feedparser/)

* [RSS](https://rockcontent.com/es/blog/feed-rss/)

* [Flask](https://www.ionos.es/digitalguide/paginas-web/desarrollo-web/flask/)

