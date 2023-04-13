from django.shortcuts import render
from django.http import HttpResponse


def fornecedor(request):
    return render(request, "fornecedor/fornecedor.html")
