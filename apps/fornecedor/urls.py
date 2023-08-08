from django.urls import path

from apps.fornecedor import views

urlpatterns = [
    path("", views.fornecedor_index, name="fornecedor"),
    path(
        "fornecedor_cadastro.html",
        views.FornecedorCreate.as_view(),
        name="fornecedor_cadastro",
    ),
    path(
        "fornecedor_edit/<int:pk>",
        views.FornecedorEdit.as_view(),
        name="fornecedor_edit",
    ),
    path(
        "fornecedor_delete/<int:pk>",
        views.fornecedor_delete,
        name="fornecedor_delete",
    ),
]
