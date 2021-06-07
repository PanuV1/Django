from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def newApp(request):
    return render(request,'templates/newApp.html')

def home(request):
    return HttpResponse('<h1>Esta es otra pagina<h1/>')

def otra_pagina(request):
    return HttpResponse('<h1>Esta es otra pagina<h1/>')