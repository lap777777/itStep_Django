from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.template.loader import render_to_string

# Create your views here.

zvirata = {
    "krtek" : "krtek zije pod zemi",
    "hroch" : "hroch ma hrosi kuzi",
    "krokodyl" : "krokodyl ma hodne zubu",
    "slon" : "slon ma dlouhy chobot",
    "zirafa" : "zirafa ma dlouhy krk",
    "pes" : "pes smrdi",
}

def moje_funkce():
    return "vysledek_z_funkce"

def index(request):
    return render(request, "informace/index.html", {
        "zvirata": zvirata
    })

def info_o_zvireti(request, animal):
    # muzu zadat zvire, ktere neni ve slovniku
    # osetrim aby mi vyhodilo chybovou hlasku, kdyz nenajde zvire
    try:
        number = list(zvirata.keys()).index(animal) + 1 
        return render(request, "informace/info.html",{
            "zvire_v_sablone": animal,
            "informace": zvirata[animal].capitalize(),
            "cislo": number
        })
    except:
        return HttpResponseNotFound(f"<h2>Zvire {animal} nenalezeno.</h2>")

def zvire_podle_cisla(request, animal):
    try:
        animal_name = list(zvirata.keys())[animal - 1]
        return HttpResponseRedirect(animal_name)
    except:
        return HttpResponseNotFound(f"<h2>Zvire s timto cislem neexistuje</h2>")

def filtry(request):
    return render(request, "informace/filtry.html", {
        "text": "Ahoj, ja jsem uvodni text",
        "abeceda": "abcdefghijeklmnopqrstuvwyz",
        "kratky_text": "bflm37psvz", 
        "dlouhy text": "Sla Nanynka do zeli a tam natrhala lupeni.",
        "cislo": 56,
        "dvojka": 2,
        "ano": True,
        "ne": False,
        "dvojka_string": "2",
        "cislo_jako_string": "56",
        "velke_cislo": 45674755445454,
        "moje_funkce": moje_funkce,
        "seznam": ["jablko", "hruska", "tresen", "svestka"],
        "slovnik": { 
            "a": "hodnota pod klicem a",
            "b": "hodnota pod klicem b"
        }
    })

"""
# dle metody render_to_string:
def info_o_zvireti(request, animal):
    try:
        data = render_to_string("informace/info.html")
        return HttpResponse(data)
    except:
        return HttpResponseNotFound(f"Zvire {animal} nebylo nalezeno.")

# zakladni HttpResponse:
def info_o_zvireti(request, animal):
    try:
        cislo = list(zvirata.keys()).index(animal) + 1
        response = f"<h1>Informace {zvirata[animal]}</h1><h2>A ma cislo {cislo}</h2>"
        return HttpResponse(response)
    except:
        return HttpResponseNotFound(f"<h2>Zvire {animal} nenalezeno</h2>")

def demonstrace(request, prvni, druhy):
    return HttpResponse(f"Prvni je {prvni}, druhy je {druhy}.")

"""

