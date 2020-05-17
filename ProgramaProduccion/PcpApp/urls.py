from django.urls import path

from PcpApp import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('cliente', views.cliente, name="Clente"),
    path('materiaprima', views.materiaPrima, name="Materia Prima"),
    path('setup', views.setup, name="Setup"),
    path('fichatecnica', views.fichaTecnica, name="Ficha Tecnica"),
]