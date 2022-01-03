from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("filtry", views.filtry, name="filtr"),
    # path("<int:animal>", views.zvire_podle_cisla),
    path("nove_zvire", views.nove_zvire, name="nove_zvire"),
    path("<str:jmeno>", views.info_animal, name="animal_info"),
    # path("<str:animal>", views.info_o_zvireti, name="zvire_info"),
    # path("<prvni>/<druhy>", views.demonstrace)
    
]
# path converter - int, str, slug, uuid
