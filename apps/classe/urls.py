from django.urls import path
from apps.classe import views

urlpatterns = [
    path("", views.classe, name="classe"),
]
