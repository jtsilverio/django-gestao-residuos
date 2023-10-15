from django.shortcuts import render
from django.views.generic import View

# Create your views here.
def combustivel_index(request):
    return render(request, "combustivel/combustivel.html")

def CombustivelReg(request):
    return render(request, name="combustivel/combustível_registro.html")

class CombustivelReg(View):
    def get(self, request):
        return render(request, "combustivel/combustivel_registro.html")