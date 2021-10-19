from django.contrib import admin
from .models import Bobrik, Clen, Oddil, Adresa, Bobrik

# Register your models here.

class ClenAdmin(admin.ModelAdmin):
    list_display = ("jmeno", "prijmeni", "prezdivka", "vek", "prispevek")
    list_filter = ("prezdivka",)
    prepopulated_fields = { "slug": ("prezdivka", )}

class OddilAdmin(admin.ModelAdmin):
    list_display = ("jmeno", "vlajka", "sidlo")

class AdresaAdmin(admin.ModelAdmin):
    list_display = ("ulice", "cislo", "mesto")

class BobrikAdmin(admin.ModelAdmin):
    list_display = ("dovednost",)

admin.site.register(Clen, ClenAdmin)
admin.site.register(Oddil, OddilAdmin)
admin.site.register(Adresa, AdresaAdmin)
admin.site.register(Bobrik, BobrikAdmin)