from django.urls import path

from apps.agua import views

urlpatterns = [
    path("", views.agua_index, name="agua"),
]
