from django.urls import path

from apps.agua import views

urlpatterns = [
    path("", views.agua_index, name="agua"),
    path("cadastro/", views.AguaCreate.as_view(), name="agua_cadastro"),
]
