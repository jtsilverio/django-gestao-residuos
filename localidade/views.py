from django.shortcuts import render
from django.http import HttpResponse

def localidade(request):
    return HttpResponse("Hello, world. You're at the localidade index.")