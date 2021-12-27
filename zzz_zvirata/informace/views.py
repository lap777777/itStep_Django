from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

# Create your views here.

zvirata = {
    "krtek" : "krtek zije pod zemi",
    "hroch" : "hroch ma hrosi kuzi",
    "krokodyl" : "krokodyl ma hodne zubu",
    "slon" : "slon ma dlouhy chobot",
    "zirafa" : "zirafa ma dlouhy krk"
}

def index(request):
    return HttpResponse("<h1>Moje prvni stranka v Djangu!</h1>")

def info_o_zvireti(request, animal):
    try:
        cislo = list(zvirata.keys()).index(animal) + 1
        response = f"<h1>Informace {zvirata[animal]}</h1><h2>A ma cislo {cislo}</h2>"
        return HttpResponse(response)
    except:
        return HttpResponseNotFound(f"<h2>Zvire {animal} nenalezeno</h2>")

def zvire_podle_cisla(request, animal):
    try:
        animal_name = list(zvirata.keys())[animal - 1]
        return HttpResponseRedirect(animal_name)
    except:
        return HttpResponseNotFound(f"<h2>Zvire s timto cislem neexistuje</h2>")
def demonstrace(request, prvni, druhy):
    return HttpResponse(f"Prvni je {prvni}, druhy je {druhy}.")



