from django.shortcuts import get_object_or_404, redirect, render


def fornecedor(request):
    return render(request, "fornecedor/fornecedor.html")


def fornecedor_cadastro(request):
    return render(request, "fornecedor/fornecedor_cadastro.html")
