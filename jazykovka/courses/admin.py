from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Course)
admin.site.register(models.Branch)
admin.site.register(models.Person)
admin.site.register(models.Category)

