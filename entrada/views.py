from django.shortcuts import render
from django.http import HttpResponse

def entrada(request):
    return HttpResponse("Hello, world. You're at the entrada index.")

