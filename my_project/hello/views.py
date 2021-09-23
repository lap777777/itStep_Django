from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime as dt
import random

# Create your views here.
def index(request): 
    text = "<h1>Hello World!</h1>"
    text += '<p><a href="/day.html">Aktualni den</a><br>'
    text += '<a href="/day.html">Citaty</a></p>'
    return HttpResponse(text)

def current_day(request):
    now = dt.now()
    day = dt.weekday(now)
    text = f"<h2>Dnes je:</h2>" 
    text += f"<p>{now}<br>"
    text += f'Aktualne je {day}. den v tydnu.</p>'
    text += "<br>"
    text += '<a href="../index.html">Zpet na hlavni stranku</a>'
    return HttpResponse(text)

def quote_day(request):
    selection = random.randint(1,len(my_dict))
    quote = my_dict[selection]
    text = f"<h2>Citat dne: </h2>"
    text += f"<h3>{quote}</h3>"
    text += "<br>"
    text += '<a href="../index.html">Zpet na hlavni stranku</a>'
    return HttpResponse(text)

my_dict = {
    1: "Jak se do lesa vola, tak se z lesa ozyva.",
    2: "Unor bily, pole sili.",
    3: "Brezen za kamna vlezem.",
    4: "Duben jeste tam budem.",
    5: "Tak dlouho se chodi se dzbanem  pro vodu, az se ucho utrhne.",
    6: "Pozde bycha honit.",
    7: "Nestahuj kalhoty, kdyz brod je jeste daleko."
}