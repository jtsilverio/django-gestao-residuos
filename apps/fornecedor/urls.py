from django.urls import path
from apps.fornecedor import views

urlpatterns = [
    path("", views.fornecedor, name="fornecedor"),
    path("destinacao", views.destinacao, name="destinacao"),
    path("fornecedor_cadastro.html", views.cadastro, name="fornecedor_cadastro")
]
