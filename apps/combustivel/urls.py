from django.urls import path

from apps.combustivel import views

urlpatterns = [
    path("", views.combustivel_index, name="combustivel"),
]
