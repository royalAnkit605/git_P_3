from django.shortcuts import render
from django.http import HttpResponse
def barcelona(request):
    return HttpResponse('<h1> BARCA FOREVER </h1>')


