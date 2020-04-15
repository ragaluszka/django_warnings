from django.contrib import admin
from django.urls import path
from .views import Warnings
from . import views


urlpatterns = [
    path('hello/', views.hello, name="hello"), # wywolanie funkcji z widoku
    path('warnings/', Warnings.as_view()) # wywolanie klasy z vidoku
]