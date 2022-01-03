from django.contrib import admin
from . import models

# Register your models here.

class ZvireAdmin(admin.ModelAdmin):
    list_display = ("id", "jmeno", "vaha", "barva", "zije")

admin.site.register(models.Zvire, ZvireAdmin)
