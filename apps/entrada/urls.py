from django.urls import path
from apps.entrada import views

urlpatterns = [
    path("", views.entrada, name="entrada"),
]
