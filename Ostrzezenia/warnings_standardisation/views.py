from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Warning, Voltage, Direction
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import WarningSerializer, VoltageSerializer, DirectionSerializer, WarningFullSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class WarningViewSet(viewsets.ModelViewSet):
    serializer_class = WarningSerializer
    queryset = Warning.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class WarningFullViewSet(viewsets.ModelViewSet):
    serializer_class = WarningFullSerializer
    queryset = Warning.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class VoltageViewSet(viewsets.ModelViewSet):
    serializer_class = VoltageSerializer
    queryset = Voltage.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class DirectionViewSet(viewsets.ModelViewSet):
    serializer_class = DirectionSerializer
    queryset = Direction.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class Warnings (View):

    warnings = Warning.objects.all()
    for warning in warnings:
        print(warning.name)

    warning = Warning.objects.get(id=2)
    tekst=f"warnings {warning}"

    def get(self, request):
        return HttpResponse(self.tekst)


def hello(request):
    warnings = Warning.objects.all()
    # zwrocenie zwykly tekst
    # return HttpResponse("hello")
    # Zwrocenie templates
    return render(request, "hello.html", {"warnings": warnings})
