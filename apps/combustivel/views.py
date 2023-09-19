from django.shortcuts import render


# Create your views here.
def combustivel_index(request):
    return render(request, "combustivel/combustivel.html")
