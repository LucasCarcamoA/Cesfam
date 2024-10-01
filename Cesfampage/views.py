from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def sobre_nosotros(request):
    return render(request, 'sobre_nosotros.html')