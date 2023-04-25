from django.shortcuts import render
from django.http import HttpResponse


def classe(request):
    return render(request, "classe/classe.html")
