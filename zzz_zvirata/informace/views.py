from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views import View
from django.views.generic.edit import FormView, CreateView, DeleteView, UpdateView

from .models import Zvire
from .forms import ZvireForm


# Create your views here.

def moje_funkce():
    return "vysledek_z_funkce"

# Prvni moznost pres tridy, druha moznost pres funkce. Urls.py rozhoduje o tom, ktera se pouzije:
# a) pres tridu:
class VypisZvirataView(ListView):
    model = Zvire
    template_name = "informace/index.html"
    context_object_name = "zvirata"
# b) pres funkci:
def index(request):
    zvirata = Zvire.objects.all()
    return render(request, "informace/index.html", {
        "zvirata": zvirata
    })

# Prvni moznost pres tridy, druha moznost pres funkce. Urls.py rozhoduje o tom, ktera se pouzije:
# a) pres tridu:
class InfoOZvireti(DetailView):
    model = Zvire
    template_name = "informace/info1.html"
# puvodni varianta pres funkci
def info_animal(request, jmeno):
    animal = get_object_or_404(Zvire, jmeno=jmeno)
    return render(request, "informace/info.html", {
        "jmeno": animal.jmeno,
        "barva": animal.barva[:-1] + "ou",
        "vaha": animal.vaha,
        "zije": animal.zije,
        "cislo": animal.id,
    })

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
    
def moje_funkce():
    return "vysledek_z_funkce"



# funkce pro zadavani novych zvirat:

"""
3. verze - pres zjednousenou tridu ModelForm
"""
# Prvni moznost pres tridy, druha moznost pres funkce. Urls.py rozhoduje o tom, ktera se pouzije:
# a) pres tridu:
class NoveZvireView(View):
    def get(self, request):
        form = ZvireForm()
        return self.render(form, request)
    def post(self, request):
        form = ZvireForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect("dekuji")
        return self.render(form, request)
    def render(self, form, request):
        return render(request, "informace/nove.html", {
            "form": form
        })

# b) pres funkci:
def nove_zvire(request):
    if request.method == "POST":
        form = ZvireForm(request.POST)
        # tady dochazi ke zpracovani dat
        # tato podminka zvaliduje formular na zaklade pravidel v tride ZvirataForm
        if form.is_valid():
            #zvire = Zvire(jmeno=formular.cleaned_data["jmeno"],
            #            vaha=formular.cleaned_data["vaha"],
            #            barva=formular.cleaned_data["barva"],
            #            zije=formular.cleaned_data["zije"]
            #)
            form.save()
            return HttpResponseRedirect(reverse("dekuji"))
    else:
        form = ZvireForm()
        # pokud nejprojde formular validaci, vrati se na stranku formulare s puvodnimi daty a hlaskou, co je spatne
    form = ZvireForm()
    return render(request, "informace/nove.html", { "form": form})

# c) jina trida View - FormView:
class NoveZvire2View(FormView):
    form_class = ZvireForm
    template_name = "informace/nove.html"
    succes_url = "dekuji"
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

# d) jina trida View - CreateView:
class NoveZvire3View(CreateView):
    form_class = ZvireForm
    # alternativne: fields = "__all__" ... vyberu vsechny pole z modelu, pokud bych chtel jedno vyloucit: exclude = ["zije"] ... vybere vsechny krome zije
    template_name = "informace/nove.html"
    succes_url = "dekuji"

"""
druha verze - zacatek s Djangem

def nove_zvire(request):
    if request.method == "POST":
        formular = ZvireForm(request.POST)
        if formular.is_valid():
            zvire = Zvire(jmeno=formular.cleaned_data["jmeno"],
                        vaha=formular.cleaned_data["vaha"],
                        barva=formular.cleaned_data["barva"],
                        zije=formular.cleaned_data["zije"]
            )
            zvire.save()
            # tady dochazi ke zpracovani dat
            # tato podminka zvaliduje formular na zaklade pravidel v tride ZvirataForm
            return HttpResponseRedirect(reverse("dekuji"))
    else:
        formular = ZvireForm()
        # pokud nejprojde formular validaci, vrati se na stranku formulare s puvodnimi daty a hlaskou, co je spatne
    form = ZvireForm()
    return render(request, "informace/nove.html", { "formular": form})


prvni verze jednoduchy HTML formular
def nove_zvire(request):
    if request.method == "POST":
        jmeno = request == "POST"["jmeno"]
        if len(jmeno) != 0 and len(jmeno) > 100:
            print(jmeno)
            return HttpResponseRedirect(reverse("dekuji"))
    return render(request, "informace/nove.html")

# prace s formularem - pokud je metoda post a zadam jmeno spravne, tak se data odeslou a presmeruje me to na stranku dekuji. Pokud neni splnena podminka, tak me to vrati na formular
"""

# Prvni moznost pres tridy, druha moznost pres funkce. Urls.py rozhoduje o tom, ktera se pouzije:

class DekujiView(TemplateView):
    template_name = "informace/dekuji.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["zprava"] = "ahoj tohle je zprava"
        return context

def dekuji(request):
    return render(request, "informace/dekuji.html")



"""
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

