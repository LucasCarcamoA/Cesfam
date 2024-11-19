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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Cesfampage.views import index, trabaja_con_nosotros, ver_postulantes, sobre_nosotros, ubicacion, oirs, administrador, noticias, crear_noticia, eventos, crear_evento, ver_noticias, leer_noticia, leer_evento, oirs_inbox, modificar_noticia, eliminar_noticia, modificar_evento, eliminar_evento

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('sobrenosotros/', sobre_nosotros),
    path('ubicacion/', ubicacion),
    path('oirs/', oirs),
    path('administrador/', administrador, name='administrador'),
    path('noticias/', noticias, name='noticias'),
    path('crear_noticia/', crear_noticia),
    path('eventos/', eventos, name='eventos'),
    path('crear_evento/', crear_evento),
    path('todas_noticias/', ver_noticias),
    path('leer_noticia/<int:id>/', leer_noticia, name='leer_noticia'),
    path('leer_evento/<int:id>/', leer_evento, name='leer_evento'),
    path('oirs_inbox/', oirs_inbox, name='oirs_inbox'),
    path('modificar_noticia/<int:id>/', modificar_noticia),
    path('eliminar_noticia/<int:id>/', eliminar_noticia),
    path('modificar_evento/<int:id>/', modificar_evento),
    path('eliminar_evento/<int:id>/', eliminar_evento),
    path('trabaja-con-nosotros/', trabaja_con_nosotros, name='trabaja_con_nosotros'),
    path('administrador/postulantes/', ver_postulantes, name='ver_postulantes'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# Agrega las imagenes de la base de datos para ser mostradas en noticias.html y eventos.html