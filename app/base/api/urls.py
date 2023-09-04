from django.urls import path

from .views import Test, Alif

urlpatterns = [
    path('test/', Test.as_view()),

    path('alif/', Alif.as_view()),
]
