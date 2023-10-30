from django.urls import path

from apps.combustivel import views

app_name = "combustivel"

urlpatterns = [
    path("", views.index, name="index"),
    path(
        "cadastro/",
        views.Create.as_view(),
        name="create",
    ),
]
