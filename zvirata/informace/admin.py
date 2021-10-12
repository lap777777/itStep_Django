from django.contrib import admin
from .models import Zvire

# Register your models here.


class ZvireAdmin(admin.ModelAdmin):
    list_display = ("id", "jmeno", "vaha", "barva", "zije")
    list_filter = ("jmeno", "zije")
# administratorska trida ke tride Zvire
# vlastnost list_display ... upravuje, tak se bude zobrazovat tabulka v admin modu
# vlastnost list_filter ... podle ceho muzu v admin modu filtrovat

admin.site.register(Zvire, ZvireAdmin)
# tady pridam jako druhy parametr ZvireAdmin


