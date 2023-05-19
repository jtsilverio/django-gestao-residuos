from django.urls import path
from apps.destinacao import views

urlpatterns = [
    path("", views.destinacao_index, name="destinacao"),
    path("cadastro/", views.DestinacaoCreate.as_view(), name="destinacao_cadastro"),
    path("<int:pk>/", views.DestinacaoEdit.as_view(), name="destinacao_edit"),
    path("<int:pk>/delete/", views.destinacao_delete, name="destinacao_delete"),
]
