from django.urls import path

from apps.saida import views

urlpatterns = [
    path("", views.saida_index, name="saida"),
    path("cadastro/", views.saida_cadastro, name="saida_cadastro"),
    path("<int:pk>/", views.SaidaEdit.as_view(), name="saida_edit"),
    path("delete/<int:pk>/", views.saida_delete, name="saida_delete"),
]
