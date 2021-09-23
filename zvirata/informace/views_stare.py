from django.http.response import HttpResponseNotFound
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

# Create your views here.

def index(request):
    return HttpResponse("<h1>My first page in Django</h1>")

def info_o_slonovi(request):
    return HttpResponse("<h2>Elephant has a long chobot.</h2>")

def info_o_zirafe(request):
    return HttpResponse("<h2>Giraffe has a long neck</h2>")

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
        number = list(zvirata.keys()).index(animal) + 1 
        # vraci poradi animal ve slovniku
        response = f'<h2>{zvirata[animal]}</h2><h2> A ma cislo {number}.</h2>'
        return HttpResponse(response)
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