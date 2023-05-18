from django.urls import path
from . import views

urlpatterns = [
    path("", views.localidade_index, name="localidade"),
    path("cadastro/", views.LocalidadeCreate.as_view(), name="localidade_cadastro"),
    path("<int:pk>/", views.LocalidadeEdit.as_view(), name="localidade_edit"),
    path("<int:pk>/delete/", views.localidade_delete, name="localidade_delete"),
]
