from django.urls import path
from . import views

urlpatterns = [
    # prvni moznost pres tridy, druha pres funkce - prvni ma prednost:
    path("", views.VypisZvirataView.as_view(), name="index"),
    path("", views.index, name="index"),

    path("filtry", views.filtry, name="filtr"),
    # path("<int:animal>", views.zvire_podle_cisla),

    # prvni moznost pres tridy, druha pres funkce - prvni ma prednost:
    path("nove_zvire", views.NoveZvire2View.as_view(), name="nove_zvire"),
    path("nove_zvire", views.nove_zvire, name="nove_zvire"),

    # prvni moznost pres tridy, druha pres funkce - prvni ma prednost:
    path("dekuji", views.DekujiView.as_view(), name="dekuji"),
    path("dekuji", views.dekuji, name="dekuji"),
    
    # prvni moznost pres tridy, druha pres funkce - prvni ma prednost
    path("<int:pk>", views.InfoOZvireti.as_view(), name="animal_info"),
    path("<str:jmeno>", views.info_animal, name="animal_info"),
    # path("<str:animal>", views.info_o_zvireti, name="zvire_info"),
    # path("<prvni>/<druhy>", views.demonstrace)
    
]
# path converter - int, str, slug, uuid




