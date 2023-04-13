from django.urls import path
from . import views

urlpatterns = [
    path("", views.fornecedor, name="fornecedor"),
]
