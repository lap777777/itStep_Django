from django.urls import path
from . import views
# . je aktualni adresar - z aktualniho adresare naimportuj views

urlpatterns = [
    path("", views.index),
    path("slon", views.info_o_slonovi),
    path("zirafa", views.info_o_zirafe),
    path("<animal>", views.info_o_zvireti),
    # musim pouzit <> aby to bral jako parametr, ktery pouzivam ve funkci info_o_zvireti
    path("<prvni>/<druhy>", views.ukazka),
]

# pozor na poradi, vyhodnocuje se postupne, takze pokud vyhovuje jedno, tak uz se nespusti druhe.
# pokud bych dal <animal> na radek 7 misto slona, tak mi to vyhodi chybu, protoze slon ma jedno slovo a tak <animal vyhovuje, ale ve slovniku neni slon
# idealne kdyz mam <animal> tak uz nedavat ani slona, ani zirafu - rozcestnik musi byt jednoznacny