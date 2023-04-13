from django.shortcuts import render
from django.http import HttpResponse


def saida(request):
    return render(request, "saida/saida.html")
