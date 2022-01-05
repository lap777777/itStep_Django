from django import forms
from .models import Zvire

class ZvireForm(forms.ModelForm):
    class Meta:
        model = Zvire
        fields = "__all__"
        labels = {
            "jmeno": "Jmeno zvirete",
            "vaha": "kolik vazis?"
        }
        error_messages = {
            "jmeno": {
                "required": "Tohle policko musis vyplnit", 
                "max_length": "Maximalni delka jmena je 100 znaku"
            }
        }
    # kdybych chtel nejake vyhodit, tak: exclude = ["zije"]
    # nebo si nejake muzu vyjmenovat: fields = ["jmeno", "vaha"]
"""
Rozepsana trida ZvireForm s detailnimi poly

class ZvireForm(forms.Form):
    jmeno = forms.CharField(label="Jméno zvířete", max_length=100, error_messages= {"required": "Tohle policko musis vyplnit", 
     "max_length": "Maximalni delka jmena je 100 znaku"})
    vaha = forms.IntegerField()
    barva = forms.CharField()
    zije = forms.BooleanField(required=False)

# tady nemusim davat do zavorek nic, ale pokud vypisuji pole formulare for cyklem, tak pres label, tady muzu dat, jak se jmenuji policka. 
"""