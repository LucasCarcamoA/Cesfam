from django.shortcuts import render

# Create your views here.

def index(request):
    data = {
        'logosamu':'/static/img/logosamu.png',
        'logobomberos':'/static/img/logobomberos.png',
        'logocarabineros':'/static/img/logocarabineros.png',
        'logopdi':'/static/img/logopdi.png',
        'logodrogas':'/static/img/logodrogas.png',
        'logorescatemar':'/static/img/logorescatemar.png',
    }
    return render(request, 'index.html', data)

def sobre_nosotros(request):
    data = {
        'logosamu':'/static/img/logosamu.png',
        'logobomberos':'/static/img/logobomberos.png',
        'logocarabineros':'/static/img/logocarabineros.png',
        'logopdi':'/static/img/logopdi.png',
        'logodrogas':'/static/img/logodrogas.png',
        'logorescatemar':'/static/img/logorescatemar.png',
    }    
    return render(request, 'sobre_nosotros.html', data)

def ubicacion(request):
    data = {
        'logosamu':'/static/img/logosamu.png',
        'logobomberos':'/static/img/logobomberos.png',
        'logocarabineros':'/static/img/logocarabineros.png',
        'logopdi':'/static/img/logopdi.png',
        'logodrogas':'/static/img/logodrogas.png',
        'logorescatemar':'/static/img/logorescatemar.png',
    }
    return render(request, 'ubicacion.html', data)

def oirs(request):
    data = {
        'oirslogo':'/static/img/oirs.png',
        'logosamu':'/static/img/logosamu.png',
        'logobomberos':'/static/img/logobomberos.png',
        'logocarabineros':'/static/img/logocarabineros.png',
        'logopdi':'/static/img/logopdi.png',
        'logodrogas':'/static/img/logodrogas.png',
        'logorescatemar':'/static/img/logorescatemar.png',
    }
    return render(request, 'oirs.html', data)