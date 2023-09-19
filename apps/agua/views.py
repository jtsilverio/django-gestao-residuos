from django.shortcuts import render

# Create your views here.


def agua_index(request):
    return render(request, "agua/agua.html")
