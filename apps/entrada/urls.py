from django.urls import path
from apps.entrada import views

urlpatterns = [
    path("", views.entrada.as_view(), name="entrada"),
    path("<int:pk>/", views.entrada_edit.as_view(), name="entrada_edit"),
    path("cadastro/", views.entrada_cadastro, name="entrada_cadastro"),
    path("delete/<int:pk>/", views.delete_cadastro, name="entrada_delete"),
]
