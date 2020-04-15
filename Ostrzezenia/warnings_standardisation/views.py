from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Warning
from django.shortcuts import render
# Create your views here.

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
