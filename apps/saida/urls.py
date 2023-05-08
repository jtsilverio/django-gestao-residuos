from django.urls import path
from apps.saida import views

urlpatterns = [
    path("", views.saida_index, name="saida"),
]
