from urllib import request
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index (request):
    return render(request, 'shop/index.html')

def contacto(request):
    return render(request, 'shop/contacto.html')