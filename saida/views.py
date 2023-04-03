from django.shortcuts import render
from django.http import HttpResponse

def saida(request):
    return HttpResponse("Hello, world. You're at the saida index.")