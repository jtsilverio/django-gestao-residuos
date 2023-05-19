from django.urls import path
from apps.fornecedor import views

urlpatterns = [
    path("", views.fornecedor, name="fornecedor"),
    path("fornecedor_cadastro.html", views.fornecedor_cadastro, name="fornecedor_cadastro"),
]
