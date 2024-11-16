from django.db import models
from django.utils import timezone

#pip install Pillow 
# Create your models here.
TIPO_EVENTO = [
    ('', 'Seleccione un tipo de evento'),
    ('Evento', 'Evento'),
    ('Taller', 'Taller'),
    ('Campaña-Semestral', 'Campaña-Semestral'),
    ('Campaña-Mensual', 'Campaña-Mensual'),
]

MOTIVO = [
    ('', 'Seleccione el motivo'),
    ('Reclamo', 'Reclamo'),
    ('Consulta', 'Consulta'),
    ('Sugerencia', 'Sugerencia'),
    ('Felicitaciones', 'Felicitaciones'),
    ('Otro','Otro'),
]

class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='eventos/', blank=True)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_inicio = models.DateField()
    fecha_termino = models.DateField()
    descripcion = models.TextField(max_length=900,null=True, blank=True)
    tipo_evento = models.CharField(max_length=50, choices=TIPO_EVENTO)
    
    def __str__(self):
        return self.titulo

class Noticia(models.Model):
    titulo = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='noticias/', blank=True)
    descripcion = models.TextField(max_length=900,null=True, blank=True)
    evento_relacionado = models.ForeignKey(Evento, on_delete=models.CASCADE, null=True, blank=True)
    fecha_creacion = models.DateTimeField(default=timezone.now)

class Oirs(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField(max_length=100)
    motivo = models.CharField(max_length=50, choices=MOTIVO)
    mensaje = models.TextField(max_length=900)
    fecha_envio = models.DateTimeField(default=timezone.now)