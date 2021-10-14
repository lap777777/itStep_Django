from django.shortcuts import render
from django.shortcuts import get_object_or_404, render

from .models import Clen

# Create your views here.

def evidence_clenu(request):
    clenove = Clen.objects.all()
    return render(request, "evidence/evidence.html", {"clenove": clenove})


def evidence_detail(request, prezdivka):
    clen = get_object_or_404(Clen, prezdivka=prezdivka)
    return render(request, "evidence/clen_detail.html", {
        "jmeno": clen.jmeno,
        "prijmeni": clen.prijmeni,
        "prezdivka": clen.prezdivka,
        "vek": clen.vek,
        "prispevek": clen.prispevek,
})


