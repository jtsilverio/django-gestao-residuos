from django.urls import path
from apps.combustivel import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
  path("", views.combustivel_index, name="combustivel"),
  path("cadastro/", views.CombustivelReg.as_view(), name="combustivel_registro"),
  ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#  path("<int:pk>", views.CombustivelGrafico.as_view(), name="grafico"),

#urlpatterns = [
#    path("", views.combustivel_index, name="combustivel"),
#    path(
#        "cadastro/", 
#        views.CombustivelReg.as_view(),
#        name="combustivel_registro",
#        )
#]#