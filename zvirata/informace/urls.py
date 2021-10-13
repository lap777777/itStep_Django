from django.urls import path
from . import views
# . je aktualni adresar - z aktualniho adresare naimportuj views

urlpatterns = [
    path("", views.index, name="index"),
    path("informace", views.informace_o_zvireti, name="info"),
    path("<str:jmeno>", views.info_animal, name="animal_info"),


    
    path("<int:animal>", views.zvire_podle_cisla),
    # kdyz se zvire da prevest na cislo, tak ze zobrazi vies. zivre podle cisla
    path("<str:animal>", views.info_o_zvireti, name="zvire_info"),
    # musim pouzit <> aby to bral jako parametr, ktery pouzivam ve funkci info_o_zvireti views
]

# pozor na poradi, vyhodnocuje se postupne, takze pokud vyhovuje jedno, tak uz se nespusti druhe.
# pokud bych dal <animal> na radek 7 misto slona, tak mi to vyhodi chybu, protoze slon ma jedno slovo a tak <animal vyhovuje, ale ve slovniku neni slon
# idealne kdyz mam <animal> tak uz nedavat ani slona, ani zirafu - rozcestnik musi byt jednoznacny

# path convertor: int, str, slug, uuid, path