from django.db import models
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

    def seznam_skautu(self):
        # return Clen.objects.filter(oddil__jmeno=self.jmeno)
        # __ dve podtrzitka pro spojovani modelu a pole pro dotazy (misto tecky)
        return ", ".join(str(clen.prezdivka) for clen in Clen.objects.filter(oddil__jmeno=self.jmeno))
        # hezky vypis seznamu na admin strance

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
    bobrik = models.ManyToManyField(Bobrik, null=True)
    
    """
    def save(self, *args, **kwargs):
        self.slug = slugify(self.prezdivka)
        super().save(*args, **kwargs)
        # kdyz jsem si prepsal save, tak musim pro save zavolat predka
        # kdyz jsem v admin pouzil prepopulated fields, tak uz nepotrebuji tuto funkci na vytvareni funkci slugify
    """

    def __str__(self):
        return f"Skaut {self.jmeno} {self.prijmeni} s prezdivkou {self.prezdivka} ma {self.vek} let."
        
    class Meta():
        verbose_name_plural = "Clenove"
        ordering = ["prezdivka"]



