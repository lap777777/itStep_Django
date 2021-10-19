from django.db import models
from django.db.models.fields.related import OneToOneField
from django.utils.text import slugify

# Create your models here.

class Adresa(models.Model):
    ulice = models.CharField(max_length=30)
    cislo = models.IntegerField()
    mesto = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "Adresy"

    def __str__(self):
        return f"{self.ulice} {self.cislo}, {self.mesto}"

class Oddil(models.Model):
    jmeno = models.CharField(max_length=30)
    vlajka = models.BooleanField()
    sidlo = models.OneToOneField(Adresa, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name_plural = "Oddily"

    def __str__(self):
        return self.jmeno

class Bobrik(models.Model):
    dovednost = models.CharField(max_length=200)

    class Meta():
        verbose_name_plural = "Bobrici"

    def __str__(self) -> str:
        return self.dovednost

class Clen(models.Model):
    jmeno = models.CharField(max_length=30)
    prijmeni = models.CharField(max_length=30)
    prezdivka = models.CharField(max_length=30)
    vek = models.IntegerField(null=True)
    prispevek = models.BooleanField(null=True)
    slug = models.SlugField(blank="True", default="", null=False, primary_key=True)
    oddil = models.ForeignKey(Oddil, on_delete=models.SET_NULL, null=True)
    bobrik = models.ManyToManyField(Bobrik)
    
    """
    def save(self, *args, **kwargs):
        self.slug = slugify(self.prezdivka)
        super().save(*args, **kwargs)
        # kdyz jsem si prepsal save, tak musim pro save zavolat predka
        """

    def __str__(self):
        text = f"jmeno: {self.jmeno}, prijmeni: {self.prijmeni}, prezdivka: {self.prezdivka}, vek: {self.vek}, zaplacene prispevky: {self.prispevek}"
        return text

    class Meta():
        verbose_name_plural = "Clenove"
        ordering = ["prezdivka"]   # razeni v tabulkce, pokud dam pred - "-prezdivka", tak je to sestupne




