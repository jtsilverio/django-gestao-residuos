from django.shortcuts import render


def fornecedor(request):
    return render(request, "fornecedor/fornecedor.html")


def destinacao(request):
    return render(request, "fornecedor/destinacao.html")