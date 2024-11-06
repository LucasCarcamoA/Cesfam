from django.shortcuts import render, redirect, get_object_or_404
from .forms import NoticiaForm, EventoForm
from .models import Noticia, Evento

# Create your views here.

def index(request):
    noticias = Noticia.objects.all().order_by('-id')[:3]
    eventos = Evento.objects.all().order_by('fecha_inicio')[:3]
    fulleventos = Evento.objects.all()
    
    data = {
        'logosamu':'/static/img/logosamu.png',
        'logobomberos':'/static/img/logobomberos.png',
        'logocarabineros':'/static/img/logocarabineros.png',
        'logopdi':'/static/img/logopdi.png',
        'logodrogas':'/static/img/logodrogas.png',
        'logorescatemar':'/static/img/logorescatemar.png',
        'noticias': noticias,
        'eventos' : eventos,
        'fulleventos': fulleventos,
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

def ver_noticias(request):
    noticias = Noticia.objects.all().order_by('-id')
    data = {
        'todas_noticias' : noticias,
    }
    return render(request, 'todas_noticias.html',data)

# VIEW ADMIN
def administrador(request):
    return render(request, 'admin.html')

def noticias(request):
    noticias = Noticia.objects.all().order_by('-fecha_creacion')  # Obtener las noticias y ordenarlas por fecha de creacion
    return render(request, 'noticias.html', {'noticias': noticias})

def crear_noticia(request):
    if request.method == 'POST':
        form = NoticiaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'creacion_exitosa.html', {
                'mensaje_exito': '¡Noticia creada correctamente!',
                'url_volver': '/noticias/'  # Redirige a la página de noticias exitosa despues de la página de creación exitosa
            })
    else:
        form = NoticiaForm()
    return render(request, 'crear_noticia.html', {'form': form})

def eventos(request):
    eventos = Evento.objects.all().order_by('-fecha_creacion')  # Obtener los eventos y ordenarlas por fecha de creacion
    return render(request, 'eventos.html', {'eventos': eventos})

def crear_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'creacion_exitosa.html', {
                'mensaje_exito': '¡Evento creado correctamente!',
                'url_volver': '/eventos/'  # Redirige a la página de eventos exitosa despues de la página de creación exitosa
            })
    else:
        form = EventoForm()
    return render(request, 'crear_evento.html', {'form': form})

def leer_noticia(request, id):
    noticia = get_object_or_404(Noticia, id=id)
    ultimas_noticias = Noticia.objects.exclude(id=id).order_by('-fecha_creacion')[:5]
    return render(request, 'leer_noticia.html', {'noticia': noticia, 'ultimas_noticias': ultimas_noticias})

def leer_evento(request, id):
    evento = get_object_or_404(Evento, id=id)
    ultimos_eventos = Evento.objects.exclude(id=id).order_by('-fecha_creacion')[:5]
    return render(request, 'leer_evento.html', {'evento': evento, 'ultimos_eventos': ultimos_eventos})