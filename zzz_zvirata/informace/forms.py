from django import forms

class ZvireForm(forms.Form):
    jmeno = forms.CharField(label="Jméno zvířete", max_length=100)
    vaha = forms.IntegerField()
    barva = forms.CharField()
    zije = forms.BooleanField()

# tady nemusim davat do zavorek nic, ale pokud vypisuji pole formulare for cyklem, tak pres label, tady muzu dat, jak se jmenuji policka. 
