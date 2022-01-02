from django.contrib import admin
from . import models

# Register your models here.

class ClenAdmin(admin.ModelAdmin):
    list_display = ("jmeno", "prijmeni", "prezdivka", "vek", "prispevek")
    prepopulated_fields = { "slug": ("prezdivka", )}

admin.site.register(models.Clen, ClenAdmin)
admin.site.register(models.Oddil)
admin.site.register(models.Adresa)

