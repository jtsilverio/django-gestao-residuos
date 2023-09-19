from django.urls import path

from apps.eletricidade import views

urlpatterns = [
    path("", views.eletricidade_index, name="eletricidade"),
]
