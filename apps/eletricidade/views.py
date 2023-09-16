from django.shortcuts import render


def eletricidade_index(request):
    return render(request, "eletricidade/eletricidade.html")
