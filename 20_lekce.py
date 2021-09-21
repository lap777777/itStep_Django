"""
Jak funguje internet:
client:
- to jsem ja, zadam stranku seznam.cz 
- zadavam pozadavek: HTTP Request get site.com

server:
- tam dorazi pozadavek
- tam bezi framework a ten odpovi na pozadavek
- nabidne mi aktualni clanky, vyhledavac, zjisti, ze tam mam email, tak mi nabidne email
- bezi tam databaze - nejaky jazyk na strane serveru - ten mi sestavi stranku - vezme clanky z databaze, sahne do jine databaze pro pocasi, do jine databaze pro emaily
- na serveru sestavi stranku
- posle odpoved HTTP Response ve formatu HTML, CSS, JS, PNG/JPG
- to je frontend a to vidim a muzu se podivat do kodu
- tajne veci/knowhow bezi v backendu (python, PHP, ...)

Napln hodin:
- posilani pozadavku z klienta
- reseni pozadavku na serveru

DJANGO:

zeptat se na verzi djanga: django-admin --version

django-admin: ... utilitka, ktere ma spoustu subcommands - startapp, startproject, runserver

nastartovani projektu: 
>>django-admin startproject zvirata
takhle vytvori novy podadresar, kdybych nechtel podadresar:
>>django-admin startproject zvirata .

django vytvori slozku projektu s prednestavenymi soubory

soubor manage.py:
- spousti administrativni ulohy, nahrazuje django-admin
dale tam je:
__init__.py - balicek 
asgi.py, wsgi.py ... soubory pro deployment - aby projekt nekde bezel - na konci projektu

settings.py - nastaveni Djanga pro muj projekt - spousta prednastaveni
BASE_DIR ... vychozi adresar
DEBUG = True ... ve fazi vyvoje, False - kdyz je hotovo
INSTALLED_APPS ... casti projektu
ROOT_URLCONF ... hlavni adresa
DATABASES ... nastaveni databaze
TIME_ZONE = "UTC" ... casova zona
LANGUAGE_CODE = "cz-cs"/"en-us" ... jazyk

urls.py - bude tam souhrn stranek na zobrazeni

Projekt:
- projekt - s predvytvorenymi soubory
- aplikace - moje jednotlive podpogramy

Spusteni applikace
>>python3 manage.py startapp informace (django-admin startapp informace)
- budu pouzivat modely a views

Spustit migraci:
>>python3 manage.py migrate (django-admin migrate)

Spustit server:
>>python3 manage.py runserver (django-admin runserver)
to mi vyhodi adresu, kde mi bezi server: http://127.0.0.1:8000/ a kody:
200 ... probehlo v poradku, 404 .. chyba, nebylo nalezeno (HTTP status codes)
2xx successful
3xx redirection - to se objevi, kdyz me hodi na jinou stranku a pak prijce 2xx
4xx client error
5xx server error
server mi bezi v terminalu, (ctrl+c ho vypne), pokud vypnu terminal, server nepobezi, musim znovu dat runserver
tak si musim otevrit novy terminal, ve kterem budu psat prikazy (v prvnim bezi server a tam nic nedelam)

informace/views.py
tady budou veci, ktere urci, jak stranka bude vypadat

tam vlozim text:
>>from django.http import HttpResponse
>>def index(request):
    return HttpResponse("My first page in Django")
funkce se spusti pri pozadavku HttpResponse a vrati mi co zadam - tady text

pak si zalozim v dane aplikaci (informace) zalozim soubor urls.py a tam vlozim: 
do urlpattens informace o ceste a views, ktere se budou volat.

pak musim do urls souboru v hlavnim projektu (zvirata)



"""