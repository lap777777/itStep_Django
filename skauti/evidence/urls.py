from django.urls import path
from . import views
# . je aktualni adresar - z aktualniho adresare naimportuj views

urlpatterns = [
    
    path("", views.evidence_clenu, name="evidence"),
    path("/<str:prezdivka>", views.evidence_detail, name="detail"),

]