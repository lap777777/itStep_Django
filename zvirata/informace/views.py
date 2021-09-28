from django.http.response import HttpResponseNotFound
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

# Create your views here.

def moje_funkce():
    return "vysledek_z_funkce"

def index(request):
    return render(request, "informace/index.html",{
        "text": "Ahoj, ja jsem uvodni text",
        "abeceda": "abcdefghijklmnopqrstuvwxyz",
        "kratky_text": "bflmpsvz",
        "cislo": 5645454545454545,
        "cislo_jako_string": "56",
        "dvojka": 2,
        "ano": True,
        "ne": False,
        "dvojka_jako_string": "2",
        "moje_funkce": moje_funkce,
        "seznam": ["jablko", "hruska", "tresen", "svestka"],
        "slovnik": {
            "a": "hodnota pod klicem a",
            "b": "hodnota pod klicem b",
            "c": "hodnota pod klicem c"
        }
    })

def informace_o_zvireti(request):
    return render(request, "informace/informace.html",{
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


zvirata = {
    "krtek": "krtek zije pod zemi",
    "hroch": "hroch ma hrosi kuzi.",
    "krokodyl": "krokodyl ma hodne zubu.",
    "slon": "elephant has a long chobot.",
    "zirafa": "giraffe has a long neck."
}


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