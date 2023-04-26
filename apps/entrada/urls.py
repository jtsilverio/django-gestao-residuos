from django.urls import path
from apps.entrada import views

urlpatterns = [
    path("", views.entrada.as_view(), name="entrada"),
    path("cadastro/", views.entrada_cadastro, name="entrada_cadastro"),
]
