from django.db import models

# Create your models here.

class Zvire(models.Model):
    jmeno = models.CharField(max_length=30)
    vaha = models.IntegerField()
    barva = models.CharField(max_length=40)
    zije = models.BooleanField(null=True)

    def __str__(self):
        return f"Jmeno: {self.jmeno}, vaha: {self.vaha}, barva: {self.barva}"