from django.contrib import admin
from django.urls import path, include
from .views import Warnings, WarningViewSet, VoltageViewSet, DirectionViewSet, WarningFullViewSet
from . import views
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token


router = routers.DefaultRouter()
router.register('warnings-serializer', WarningViewSet, basename='Warning')
router.register('voltages-serializer', VoltageViewSet, basename='Voltage')
router.register('directions-serializer', DirectionViewSet, basename='Direction')
router.register('warningsfull-serializer', WarningFullViewSet, basename='WarningFull')

urlpatterns = [
    path('', include(router.urls)), # zaimporutj domyslne path z router
    path('hello/', views.hello, name="hello"), # wywolanie funkcji z widoku
    path('warnings/', Warnings.as_view()), # wywolanie klasy z vidoku
    path('auth/',obtain_auth_token),
]