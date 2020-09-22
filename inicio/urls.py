from django.urls import path

from inicio import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('servicios/', views.servicios, name="servicios"),
    path('acerca/', views.acerca, name="acerca"),
    path('horarios/', views.calendario, name="calendario"),
    path('gracias/', views.gracias, name="gracias"),
    path('portafolio/', views.portafolio, name="portafolio"),
]
