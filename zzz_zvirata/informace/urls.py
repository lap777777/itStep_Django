from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("<int:animal>", views.zvire_podle_cisla),
    path("<str:animal>", views.info_o_zvireti),
    path("<prvni>/<druhy>", views.demonstrace)
]

# path converter - int, str, slug, uuid
