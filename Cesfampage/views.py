from django.shortcuts import render, redirect, get_object_or_404
from .forms import NoticiaForm, EventoForm, OirsForm, TrabajaConNosotrosForm
from .models import Noticia, Evento, Oirs, TrabajaConNosotros
from django.utils.timezone import now
from datetime import timedelta
from .decorators import admin_required
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib import messages

# Create your views here.

def index(request):
    noticias = Noticia.objects.all().order_by('-id')[:3]
    eventos = Evento.objects.all().order_by('fecha_inicio')[:3]
    fulleventos = Evento.objects.all()
    campañas_mensuales = Evento.objects.filter(tipo_evento__startswith="Campaña-Mensual").order_by('-id')[:1]
    campañas_semestrales = Evento.objects.filter(tipo_evento__startswith="Campaña-Semestral").order_by('-id')[:1]
    
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
        'campañas_mensuales':campañas_mensuales,
        'campañas_semestrales':campañas_semestrales,
    }
    return render(request, 'index.html', data)

def sobre_nosotros(request):
    data = {
        'JuanCarlosOchoa':'/static/img/jefatura/JuanCarlosOchoa.png',
        'JacquelineVidal':'/static/img/jefatura/JacquelineVidal.png',
        'PabloFlores':'/static/img/jefatura/PabloFlores.png',
        'YassnaVargas':'/static/img/jefatura/YassnaVargas.png',
        'NadyaFarias':'/static/img/jefatura/NadyaFarias.png',
        'CamiloDelgado':'/static/img/jefatura/CamiloDelgado.png',
        'CinthiaSoto':'/static/img/jefatura/CinthiaSoto.png',
        'MartaCifuentes':'/static/img/jefatura/MartaCifuentes.png',
        'IsabelSoto':'/static/img/jefatura/IsabelSoto.png',
        'ClaudiaQuichiyao':'/static/img/jefatura/ClaudiaQuichiyao.png',
        'CamilaCutino':'/static/img/jefatura/CamilaCutino.png',
        'GloriaJaramillo':'/static/img/jefatura/GloriaJaramillo.png',
        'RodrigoAlvarez':'/static/img/jefatura/RodrigoAlvarez.png',
        'SimonSchneider':'/static/img/jefatura/SimonSchneider.png',
        'ClaudiaFernandez':'/static/img/jefatura/ClaudiaFernandez.png',
        'LissetteGumera':'/static/img/jefatura/LissetteGumera.png',
        'DanielaAlderete':'/static/img/jefatura/DanielaAlderete.png',
        'DanielaUrrutia':'/static/img/jefatura/DanielaUrrutia.png',
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

def trabaja_con_nosotros(request):
    if request.method == 'POST':
        form = TrabajaConNosotrosForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'creacion_exitosa.html', {
                'mensaje_exito': '¡Postulación enviada correctamente!',
                'url_volver': '/'
            })
    else:
        form = TrabajaConNosotrosForm()
    
    return render(request, 'trabaja_con_nosotros.html', {'form': form})

def ver_noticias(request):
    noticias = Noticia.objects.all().order_by('-id')
    data = {
        'todas_noticias' : noticias,
    }
    return render(request, 'todas_noticias.html',data)

def ver_eventos(request):
    eventos = Evento.objects.all().order_by('-id')
    data = {
        'todos_eventos' : eventos,
    }
    return render(request, 'todos_eventos.html',data)

# VIEW ADMIN
@admin_required
def administrador(request):
    #Obtiene los eventos y filtra los que están por terminar en 3 días o menos
    eventos_por_terminar = Evento.objects.filter(fecha_termino__lte=now().date() + timedelta(days=3), fecha_termino__gte=now().date())
    #Obtiene la ultima fecha de acceso a la página 
    ultima_visita = request.session.get('ultima_visita', now())
    #Filtra los mensajes nuevos de la OIRS desde la última visita
    nuevos_oirs = Oirs.objects.filter(fecha_envio__gt=ultima_visita)
    #Actualiza la última visita con la visita actual
    postulantes = TrabajaConNosotros.objects.all().order_by('-fecha_envio')[:5]  # Obtiene los últimos 5 postulantes    
    nuevos_postulantes = TrabajaConNosotros.objects.filter(fecha_envio__gt=ultima_visita)
    request.session['ultima_visita'] = str(now())
    
    
    data = {
        'eventos_por_terminar': eventos_por_terminar,
        'nuevos_oirs': nuevos_oirs,
        'postulantes': postulantes,
        'nuevos_postulantes': nuevos_postulantes,
    }
    
    return render(request, 'admin.html', data)

@admin_required
def ver_postulantes(request):
    postulantes = TrabajaConNosotros.objects.all().order_by('-fecha_envio')
    return render(request, 'postulantes.html', {'postulantes': postulantes})

@admin_required
def noticias(request):
    noticias = Noticia.objects.all().order_by('-fecha_creacion')  # Obtener las noticias y ordenarlas por fecha de creacion
    return render(request, 'noticias.html', {'noticias': noticias})

def oirs(request):
    data = {
        'oirslogo':'/static/img/oirs.png'
    }
    if request.method == 'POST':
        form = OirsForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'creacion_exitosa.html', {
                'mensaje_exito': '¡Mensaje enviado correctamente!',
                'url_volver': '/'  # Redirige a la página de OIRS exitosa despues de la página de creación exitosa
                })
    else:
        form = OirsForm()
    return render(request, 'oirs.html', {'form': form, 'data': data})

def crear_noticia(request):
    if request.method == 'POST':
        form = NoticiaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'creacion_exitosa.html', {
                'mensaje_exito': '¡Noticia creada correctamente!',
                'url_volver': '/administrador/noticias'  # Redirige a la página de noticias exitosa despues de la página de creación exitosa
            })
    else:
        form = NoticiaForm()
    return render(request, 'crear_noticia.html', {'form': form})

def modificar_noticia(request, id):
    noticia = Noticia.objects.get(id=id)
    form = NoticiaForm(instance=noticia)
    if request.method == 'POST':
        form = NoticiaForm(request.POST, request.FILES, instance=noticia)
        if form.is_valid():
            form.save()
        return render(request, 'creacion_exitosa.html', {
            'mensaje_exito': 'Noticia modificada correctamente!',
            'url_volver': '/administrador/noticias'  # Redirige a la página de noticias exitosa despues de la página de creación exitosa
            })
    data={
        'form':form,
        'editar': True
    }
    return render(request,'crear_noticia.html', data)

def eliminar_noticia(request, id):
    noticia = Noticia.objects.get(id=id)
    noticia.delete()
    return render(request, 'creacion_exitosa.html', {
        'mensaje_exito': 'Noticia eliminada correctamente!',
        'url_volver': '/administrador/noticias'  # Redirige a la página de noticias exitosa despues de la página de creación exitosa
        })

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
                'url_volver': '/administrador/eventos/'  # Redirige a la página de eventos exitosa despues de la página de creación exitosa
            })
    else:
        form = EventoForm()
    return render(request, 'crear_evento.html', {'form': form})

@admin_required
def modificar_evento(request, id):
    evento = Evento.objects.get(id=id)
    form = EventoForm(instance=evento)
    if request.method == 'POST':
        form = EventoForm(request.POST, request.FILES, instance=evento)
        if form.is_valid():
            form.save()
        return render(request, 'creacion_exitosa.html', {
            'mensaje_exito': 'Evento modificado correctamente!',
            'url_volver': '/administrador/eventos/'  # Redirige a la página de eventos exitosa despues de la página de creación exitosa
            })
    data={
        'form':form,
        'editar': True
    }
    return render(request,'crear_evento.html', data)

@admin_required
def eliminar_evento(request, id):
    evento = Evento.objects.get(id=id)
    evento.delete()
    return render(request, 'creacion_exitosa.html', {
        'mensaje_exito': 'Evento eliminado correctamente!',
        'url_volver': '/administrador/eventos/'  # Redirige a la página de eventos exitosa despues de la página de creación exitosa
        })

def leer_noticia(request, id):
    noticia = get_object_or_404(Noticia, id=id)
    ultimas_noticias = Noticia.objects.exclude(id=id).order_by('-fecha_creacion')[:5]
    return render(request, 'leer_noticia.html', {'noticia': noticia, 'ultimas_noticias': ultimas_noticias})

def leer_evento(request, id):
    evento = get_object_or_404(Evento, id=id)
    ultimos_eventos = Evento.objects.exclude(id=id).order_by('-fecha_creacion')[:5]
    return render(request, 'leer_evento.html', {'evento': evento, 'ultimos_eventos': ultimos_eventos})


@admin_required
def oirs_inbox(request):
    oirs = Oirs.objects.all().order_by('-fecha_envio')
    return render(request, 'oirs_inbox.html', {'oirs': oirs})
                
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and (user.is_staff or user.is_superuser):
            login(request, user)
            return redirect(reverse('administrador'))
        else:
            return render(request, 'login.html', {'error': 'Credenciales inválidas o usuario no autorizado'})
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'Has cerrado sesión exitosamente.')
    return redirect('login')
