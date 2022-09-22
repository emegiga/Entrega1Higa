from django.urls import path
from BlogBuster.views import *

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('searchvhs/', searchVhs, name="SearchVhs"),
    path('cargardatosvhs/', inputVhs, name="InputVhs"),
    path('cargardatoscds/', inputCds, name="InputCds"),
    path('cargardatosvideojuegos/', inputVideojuegos, name="InputJuegos"),
    path('resultadoVhs/', resultadoVhs)
]