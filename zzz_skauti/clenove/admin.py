from django.contrib import admin
from . import models

# Register your models here.

class ClenAdmin(admin.ModelAdmin):
    list_display = ("jmeno", "prijmeni", "prezdivka", "vek", "prispevek")
    prepopulated_fields = { "slug": ("prezdivka", )}

class OddilAdmin(admin.ModelAdmin):
    list_display = ("jmeno", "vlajka", "sidlo", "seznam_skautu")

class AdresaAdmin(admin.ModelAdmin):
    list_display = ("ulice", "cislo", "mesto")

admin.site.register(models.Clen, ClenAdmin)
admin.site.register(models.Oddil, OddilAdmin)
admin.site.register(models.Adresa, AdresaAdmin)

