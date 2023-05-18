from django.urls import path
from apps.classe import views

urlpatterns = [
    path("", views.classe_index, name="classe"),
    path("cadastro/", views.ClasseCreate.as_view(), name="classe_cadastro"),
    path("<int:pk>/", views.ClasseEdit.as_view(), name="classe_edit"),
    path("<int:pk>/delete/", views.classe_delete, name="classe_delete"),
]
