from django.shortcuts import render
from django.http import HttpResponse


def localidade(request):
    return render(request, "localidade/localidade.html")
