from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    #parametrosGet = request.GET["dato"]
    #return HttpResponse("Pasamos como parámetro... " + parametrosGet)
    return HttpResponse("Pasamos como parámetro... ")
def verHeaders(request):
    hds = request.META
    return HttpResponse(hds)