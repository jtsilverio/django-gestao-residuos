from django.urls import path

from apps.unidade_consumo import views

app_name = "unidade_consumo"

urlpatterns = [
    path("", views.index, name="index"),
    path("cadastro/", views.Create.as_view(), name="create"),
    path("edit/<int:pk>/", views.Edit.as_view(), name="edit"),
    path("delete/<int:pk>/", views.delete, name="delete"),
]
