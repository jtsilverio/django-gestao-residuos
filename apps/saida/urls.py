from django.urls import path
from apps.saida import views

urlpatterns = [
    path("", views.saida, name="saida"),
]
