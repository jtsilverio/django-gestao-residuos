from django.shortcuts import render
from django.http import HttpResponse

def classe(request):
    return HttpResponse("Hello, world. You're at the classe index.")