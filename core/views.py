# Create your views here.
from django.shortcuts import render # Usado para renderizar templates
from django.http import HttpResponse # Usado para retornar uma resposta HTTP

#View baseada em função (tem como ser baseada em classe)
def index(request):
    # return HttpResponse("Hello, world! - Index")
    return render(request, 'index.html', {'titulo':'Olá mundo com variável \"global\"'})

def ola(request):
    return HttpResponse("Olá Django! (SOU A VIEW VIA URL)")