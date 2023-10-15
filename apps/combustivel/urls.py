from django.urls import path

from apps.combustivel import views

urlpatterns = [
    path("", views.combustivel_index, name="combustivel"),
    path("registro/", views.CombustivelReg.as_view(), name="combustivel_registro")
]
