from django.http.response import HttpResponseNotFound
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.template.loader import render_to_string

# Create your views here.

def index(request):
    return HttpResponse("<h1>My first page in Django</h1>")

zvirata = {
    "krtek": "Krtek zije pod zemi",
    "hroch": "Hroch ma hrosi kuzi.",
    "krokodyl": "Krokodyl ma hodne zubu.",
    "slon": "Elephant has a long chobot.",
    "zirafa": "Giraffe has a long neck."
}

def info_o_zvireti(request, animal):
    # muzu zadat zvire, ktere neni ve slovniku
    # osetrim aby mi vyhodilo chybovou hlasku, kdyz nenajde zvire
    try:
        data = render_to_string("informace/info.html")  # bez templates
        return HttpResponse(data)
    except:
        return HttpResponseNotFound(f"<h2>Zvire {animal} nenalezeno.</h2>")

def ukazka(request, prvni, druhy):
    return HttpResponse(f"Prvni je {prvni}, druhy je {druhy}.")

def zvire_podle_cisla(request, animal):
    try:
        animal_name = list(zvirata.keys())[animal -1]
        return HttpResponseRedirect(animal_name)
        # presmerovani na funkci, kde uz hledam zvire podle jmena a ne cisla
    except:
        HttpResponseNotFound("Zvire s timto cislem neexistuje")
        # raise Http404()
 
# view funkce

# view trida 