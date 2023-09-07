from django.urls import path

from .views import *

urlpatterns = [
    path('test/', Test.as_view()),

    path('alif/', Alif.as_view()),
    path('nbt/', Nbt.as_view()),
    path('eskhata/', Eskhata.as_view()),
    path('spitamen/', Spitamen.as_view()),
]
