from django.urls import path
from . import views

urlpatterns =[
    path('sobre-mi/', views.sobreMi, name="SobreMi"),
]
