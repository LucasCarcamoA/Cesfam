from django.db import models
from django.utils import timezone
# Importa CKEditor5Field de la librería django-ckeditor-5
from django_ckeditor_5.fields import CKEditor5Field

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

AREAS = [
    ('Medicina', 'Medicina'),
    ('Enfermería', 'Enfermería'),
    ('Administración', 'Administración'),
    ('Servicios Generales', 'Servicios Generales'),
    ('Otro', 'Otro'),
]

class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='eventos/', blank=True)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_inicio = models.DateField()
    fecha_termino = models.DateField()
    descripcion = CKEditor5Field('Text', config_name='extends', null=True, blank=True)
    #descripcion = models.TextField(max_length=900,null=True, blank=True)
    tipo_evento = models.CharField(max_length=50, choices=TIPO_EVENTO)
    
    def __str__(self):
        return self.titulo

class Noticia(models.Model):
    titulo = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='noticias/', blank=True)
    descripcion = CKEditor5Field('Text', config_name='extends', null=True, blank=True)
    #descripcion = models.TextField(max_length=900,null=True, blank=True)
    evento_relacionado = models.ForeignKey(Evento, on_delete=models.CASCADE, null=True, blank=True)
    fecha_creacion = models.DateTimeField(default=timezone.now)

class Oirs(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField(max_length=100)
    motivo = models.CharField(max_length=50, choices=MOTIVO)
    mensaje = models.TextField(max_length=900)
    fecha_envio = models.DateTimeField(default=timezone.now)

class TrabajaConNosotros(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    area_postulacion = models.CharField(max_length=50, choices=AREAS)
    curriculum = models.FileField(upload_to='curriculums/', null=True, blank=True)
    mensaje = models.TextField(max_length=300)
    fecha_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} - {self.area_postulacion}"