from django.urls import path
from . import views

urlpatterns=[
    path('proyectos/', views.proyectos, name="Proyectos"),
    path('proyectos/proyecto/<int:id>', views.proyecto, name="Proyecto")
]