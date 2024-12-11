"""
Este módulo define los modelos para un sistema de eventos, noticias, y formularios de contacto. 
Utiliza el editor de texto enriquecido CKEditor5 para campos de texto personalizables.
"""

from django.db import models
from django.utils import timezone
from django_ckeditor_5.fields import CKEditor5Field

#pip install Pillow

# Opciones para el tipo de eventos
TIPO_EVENTO = [
    ('', 'Seleccione un tipo de evento'),
    ('Evento', 'Evento'),
    ('Taller', 'Taller'),
    ('Campaña-Semestral', 'Campaña-Semestral'),
    ('Campaña-Mensual', 'Campaña-Mensual'),
]

# Opciones para el motivo de contacto en OIRS
MOTIVO = [
    ('', 'Seleccione el motivo'),
    ('Reclamo', 'Reclamo'),
    ('Consulta', 'Consulta'),
    ('Sugerencia', 'Sugerencia'),
    ('Felicitaciones', 'Felicitaciones'),
    ('Otro','Otro'),
]

# Áreas disponibles para postulación
AREAS = [
    ('Medicina', 'Medicina'),
    ('Enfermería', 'Enfermería'),
    ('Administración', 'Administración'),
    ('Servicios Generales', 'Servicios Generales'),
    ('Otro', 'Otro'),
]


class Evento(models.Model):

    """
    Class Evento
    
    Representa un evento dentro del sistema.

    Atributos:
        titulo (str): El título del evento.

        imagen (ImageField): Imagen asociada al evento.
        
        fecha_creacion (datetime): Fecha de creación del evento.
        
        fecha_inicio (date): Fecha de inicio del evento.
        
        fecha_termino (date): Fecha de término del evento.
        
        descripcion (CKEditor5Field): Descripción detallada del evento.
        
        tipo_evento (str): Tipo del evento (Evento, Taller, Campaña, etc.).

    Método:

        __str__(self): retorna el titulo del evento

    """

    titulo = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='eventos/', blank=True)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_inicio = models.DateField()
    fecha_termino = models.DateField()
    descripcion = CKEditor5Field('Text', config_name='extends')
    tipo_evento = models.CharField(max_length=50, choices=TIPO_EVENTO)
    
    def __str__(self):
        return self.titulo

class Noticia(models.Model):

    """
    Representa una noticia publicada en el sistema.

    Atributos:
        titulo (str): El título de la noticia.
        
        imagen (ImageField): Imagen asociada a la noticia.

        descripcion (CKEditor5Field): Descripción detallada de la noticia.

        evento_relacionado (ForeignKey): Evento asociado con la noticia, si aplica.

        fecha_creacion (datetime): Fecha de creación de la noticia.

    """

    titulo = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='noticias/', blank=True)
    descripcion = CKEditor5Field('Text', config_name='extends')
    evento_relacionado = models.ForeignKey(Evento, on_delete=models.SET_NULL, null=True, blank=True)
    fecha_creacion = models.DateTimeField(default=timezone.now)

class Oirs(models.Model):
    
    """
    Representa un formulario de contacto de la OIRS.

    Atributos:
        nombre (str): Nombre del remitente.

        apellido (str): Apellido del remitente.
        
        correo (EmailField): Correo electrónico del remitente.
        
        motivo (str): Motivo del contacto (Reclamo, Consulta, etc.).
        
        mensaje (TextField): Mensaje enviado por el remitente.
        
        fecha_envio (datetime): Fecha de envío del formulario.
    """

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField(max_length=100)
    motivo = models.CharField(max_length=50, choices=MOTIVO)
    mensaje = models.TextField(max_length=500)
    fecha_envio = models.DateTimeField(default=timezone.now)

class TrabajaConNosotros(models.Model):

    """
    Representa una postulación al área de recursos humanos.

    Atributos:
        nombre (str): Nombre del postulante.

        correo (EmailField): Correo del postulante.
        
        area_postulacion (str): Área a la que postula el candidato.
        
        curriculum (FileField): Archivo del currículum adjunto.
        
        mensaje (TextField): Mensaje adicional del postulante.
        
        fecha_envio (datetime): Fecha de envío de la postulación.

    Métodos:

        __str__(self): retorna el nombre y el area seleccionada para 
        la postulación
    """

    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    area_postulacion = models.CharField(max_length=50, choices=AREAS)
    curriculum = models.FileField(upload_to='curriculums/', null=True, blank=True)
    mensaje = models.TextField(max_length=300)
    fecha_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} - {self.area_postulacion}"