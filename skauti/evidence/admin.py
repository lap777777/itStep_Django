from django.contrib import admin
from .models import Clen

# Register your models here.

class ClenAdmin(admin.ModelAdmin):
    list_display = ("jmeno", "prijmeni", "prezdivka", "vek", "prispevek")
    list_filter = ("prezdivka",)

admin.site.register(Clen, ClenAdmin)