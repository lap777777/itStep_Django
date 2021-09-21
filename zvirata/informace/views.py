from django.shortcuts import render
from django.http import HttpResponse

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
    "krokodyl": "Krokodyl ma hodne zubu."
}

def info_o_zvireti(request, animal):
    response = "<h2>" + zvirata[animal] + "</h2>"
    return HttpResponse(response)

def ukazka(request, prvni, druhy):
    return HttpResponse(f"Prvni je {prvni}, druhy je {druhy}.")


 
# view funkce

# view trida 