from django.urls import path

from apps.fornecedor import views

urlpatterns = [
    path("", views.fornecedor_index, name="fornecedor"),
    path(
        "cadastro/",
        views.FornecedorCreate.as_view(),
        name="fornecedor_cadastro",
    ),
    path(
        "<int:pk>/",
        views.FornecedorEdit.as_view(),
        name="fornecedor_edit",
    ),
    path(
        "<int:pk>/delete/",
        views.fornecedor_delete,
        name="fornecedor_delete",
    ),
]
