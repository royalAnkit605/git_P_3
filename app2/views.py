from django.shortcuts import render
from django.http import HttpResponse
def real(request):
    return HttpResponse('<h1> Real Madrid is worst club </h1>')

