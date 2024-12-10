"""
URL configuration for Cesfam project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from Cesfampage.views import index, logout_view ,login_view, trabaja_con_nosotros, ver_postulantes, sobre_nosotros, ubicacion, oirs, administrador, noticias, crear_noticia, eventos, crear_evento, ver_noticias, ver_eventos, leer_noticia, leer_evento, oirs_inbox, modificar_noticia, eliminar_noticia, modificar_evento, eliminar_evento
from django.contrib.auth.decorators import login_required
from Cesfampage.decorators import admin_required

urlpatterns = [
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('sobrenosotros/', sobre_nosotros),
    path('ubicacion/', ubicacion),
    path('oirs/', oirs),
    path('administrador/', admin_required(administrador), name='administrador'),
    path('administrador/noticias/', admin_required(noticias), name='noticias'),
    path('administrador/noticias/crear_noticia/', admin_required(crear_noticia), name='crear_noticia'),
    path('administrador/eventos/', admin_required(eventos), name='eventos'),
    path('administrador/eventos/crear_evento/', admin_required(crear_evento), name='crear_evento'),
    path('todas_noticias/', ver_noticias),
    path('todos_eventos/', ver_eventos),
    path('leer_noticia/<int:id>/', leer_noticia, name='leer_noticia'),
    path('leer_evento/<int:id>/', leer_evento, name='leer_evento'),
    path('administrador/oirs_inbox/', admin_required(oirs_inbox), name='oirs_inbox'),
    path('administrador/noticia/modificar_noticia/<int:id>/', admin_required(modificar_noticia), name='modificar_noticia'),
    path('administrador/noticia/eliminar_noticia/<int:id>/', admin_required(eliminar_noticia), name='eliminar_noticia'),
    path('administrador/evento/modificar_evento/<int:id>/', admin_required(modificar_evento), name='modificar_evento'),
    path('administrador/evento/eliminar_evento/<int:id>/', admin_required(eliminar_evento), name='eliminar_evento'),
    path('administrador/postulantes/', admin_required(ver_postulantes), name='ver_postulantes'),
    path('trabaja-con-nosotros/', trabaja_con_nosotros, name='trabaja_con_nosotros'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path("ckeditor5/", include('django_ckeditor_5.urls')),
    path('captcha/', include('captcha.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# Agrega las imagenes de la base de datos para ser mostradas en noticias.html y eventos.html

