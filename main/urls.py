from django.urls import path
from . import views

urlpatterns=[
    #path('holamundo/', views.holaMundo, name="HolaMundo" )
    path('', views.main_view, name="MainIndex"),
    path('inicio/', views.main_view, name="MainIndex")
]