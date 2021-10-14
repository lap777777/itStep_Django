from django.db import models

# Create your models here.

class Clen(models.Model):
    jmeno = models.CharField(max_length=30)
    prijmeni = models.CharField(max_length=30)
    prezdivka = models.CharField(max_length=30)
    vek = models.IntegerField(null=True)
    prispevek = models.BooleanField(null=True)

    def __str__(self):
        text = f"jmeno: {self.jmeno}, prijmeni: {self.prijmeni}, prezdivka: {self.prezdivka}, vek: {self.vek}, zaplacene prispevky: {self.prispevek}"
        return text