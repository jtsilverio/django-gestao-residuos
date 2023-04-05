from django.shortcuts import render
from django.http import HttpResponse

def entrada(request):
    return render(request, "base.html")

