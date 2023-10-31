# Create your views here.

from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import CreateView
from .models import Combustivel
from django.contrib.messages.views import SuccessMessageMixin
from apps.combustivel.models import Combustivel

def combustivel_index(request):
    combustivel = None
    combustivel = combustivel
    return render(request, "combustivel/combustivel.html", {"combustivel": combustivel})


class CombustivelReg(CreateView, SuccessMessageMixin):
    model = Combustivel
    fields = '__all__'
    success_message = "Combustível registrado com sucesso!"
    
    def get(self, request):
        return render(request, "combustivel/combustivel_registro.html")

    def post(self, request):
        quantidade = request.POST.get("quantidade")
        combustivel = Combustivel(quantidade=quantidade)
        combustivel.save()
        messages.success(request, f"Combustível {quantidade} adicionado com sucesso!")
        return redirect("combustivel_index")