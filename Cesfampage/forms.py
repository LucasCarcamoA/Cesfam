"""
Formularios personalizados para gestionar modelos del sistema.

Este módulo contiene formularios basados en `ModelForm` para interactuar con los modelos
`Evento`, `Noticia`, `Oirs`, y `TrabajaConNosotros`. Se configuran widgets y validaciones
específicas para facilitar la interacción del usuario final con el sistema.

Importaciones:
    - `forms.ModelForm`: Clase base para formularios basados en modelos.
    - `CKEditor5Widget`: Widget para campos de texto enriquecido con CKEditor5.
    - `CaptchaField`: Campo para implementar un captcha de validación.
    - `date`: Proporciona funcionalidad para trabajar con fechas.

Clases:
    - `EventoForm`: Gestiona la creación y validación de eventos.
    - `NoticiaForm`: Gestiona la creación y validación de noticias.
    - `OirsForm`: Gestiona la recepción y validación de mensajes OIRS.
    - `TrabajaConNosotrosForm`: Gestiona la recepción y validación de postulaciones laborales.

Constantes:
    - `TIPO_EVENTO`: Tipos disponibles para clasificar eventos.
    - `MOTIVO`: Razones disponibles para clasificar mensajes OIRS.
    - `AREAS`: Áreas disponibles para clasificar postulaciones laborales.
"""

from django import forms
from .models import Noticia, Evento, Oirs, TrabajaConNosotros
from datetime import date
from django_ckeditor_5.widgets import CKEditor5Widget
from captcha.fields import CaptchaField

TIPO_EVENTO = [
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
    ('', 'Seleccione el area'),
    ('Medicina', 'Medicina'),
    ('Enfermería', 'Enfermería'),
    ('Administración', 'Administración'),
    ('Servicios Generales', 'Servicios Generales'),
    ('Otro', 'Otro'),
]

class EventoForm(forms.ModelForm):
    
    """
    Formulario para gestionar eventos.

    Este formulario permite crear y validar eventos, asegurando que:
    - La fecha de término no sea anterior a la fecha de inicio.
    - Los campos personalizados usen widgets amigables.

    Campos:
        - titulo: Título del evento.
        - imagen: Imagen representativa del evento.
        - fecha_inicio: Fecha de inicio del evento.
        - fecha_termino: Fecha de término del evento.
        - descripcion: Descripción del evento en formato enriquecido.
        - tipo_evento: Tipo de evento seleccionado.

    Método:
        - clean: Valida que la fecha de término no sea anterior a la de inicio.
    """

    class Meta:
        model = Evento
        fields = ['titulo', 'imagen', 'fecha_inicio', 'fecha_termino', 'descripcion', 'tipo_evento']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el título del evento'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'fecha_inicio': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'min': date.today()}, format='%Y-%m-%d'),
            'fecha_termino': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'min': date.today()}, format='%Y-%m-%d'),
            'descripcion': CKEditor5Widget(attrs={'class': 'django_ckeditor_5', 'rows': 6, 'placeholder': 'Ingrese la descripción del evento'}, config_name='extends'),
            'tipo_evento': forms.Select(choices=TIPO_EVENTO, attrs={'class': 'form-select'}),
        }
    

    def __init__(self, *args, **kwargs):
        
        """
        Inicializa el formulario y establece validaciones dinámicas.
        """

        super(EventoForm, self).__init__(*args, **kwargs)
        self.fields['fecha_inicio'].widget.attrs['min'] = date.today().strftime('%Y-%m-%d')
        self.fields['fecha_termino'].widget.attrs['min'] = date.today().strftime('%Y-%m-%d')
        self.fields["descripcion"].required = False
        
    def clean(self):
        
        """
        Valida las fechas de inicio y término para evitar inconsistencias.
        """

        cleaned_data = super().clean()
        fecha_inicio = cleaned_data.get("fecha_inicio")
        fecha_termino = cleaned_data.get("fecha_termino")

        if fecha_inicio and fecha_termino and fecha_termino < fecha_inicio:
            self.add_error('fecha_termino', "La fecha de término no puede ser anterior a la fecha de inicio.")
        
        return cleaned_data

class NoticiaForm(forms.ModelForm):

    """
    Formulario para gestionar noticias.

    Este formulario permite crear y validar noticias, vinculándolas
    opcionalmente con un evento relacionado.

    Campos:
        - titulo: Título de la noticia.
        - imagen: Imagen ilustrativa de la noticia.
        - descripcion: Descripción en formato enriquecido.
        - evento_relacionado: Relación opcional con un evento.
    """
    
    class Meta:
        model = Noticia
        fields = ['titulo', 'imagen', 'descripcion', 'evento_relacionado']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el título de la noticia'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'descripcion': CKEditor5Widget(attrs={'class': 'django_ckeditor_5', 'rows': 6, 'placeholder': 'Ingrese la descripción de la noticia'}, config_name='extends'),
            #'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 6, 'placeholder': 'Ingrese la descripción de la noticia'}),
            'evento_relacionado': forms.Select(attrs={'class': 'form-select'})
        }
    def __init__(self, *args, **kwargs):

        """
        Inicializa el formulario, permitiendo descripciones opcionales.
        """

        super().__init__(*args, **kwargs)
        self.fields["descripcion"].required = False
        
class OirsForm(forms.ModelForm):
    
    """
    Formulario para gestionar mensajes OIRS.

    Este formulario recoge los datos necesarios para consultas, sugerencias,
    reclamos y otros mensajes, integrando un campo captcha para mayor seguridad.

    Campos:
        - nombre: Nombre del remitente.
        - apellido: Apellido del remitente.
        - correo: Correo electrónico del remitente (obligatorio).
        - motivo: Motivo del mensaje.
        - mensaje: Contenido del mensaje.
        - captcha: Verificación de seguridad.
    """
    
    captcha = CaptchaField()
    class Meta:
        model = Oirs
        fields = ['nombre', 'apellido', 'correo', 'motivo', 'mensaje', 'captcha']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su nombre'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su apellido'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su correo electrónico'}),
            'motivo': forms.Select(choices=MOTIVO, attrs={'class': 'form-select'}),
            'mensaje': forms.Textarea(attrs={'class': 'form-control', 'rows': 6, 'placeholder': 'Ingrese su mensaje'}),
        }
class TrabajaConNosotrosForm(forms.ModelForm):
    
    """
    Formulario para gestionar postulaciones laborales.

    Este formulario permite a los usuarios enviar información de contacto,
    el área de postulación, un archivo de CV y un mensaje adicional.

    Campos:
        - nombre: Nombre del postulante.
        - correo: Correo electrónico del postulante.
        - area_postulacion: Área a la que aplica.
        - curriculum: Archivo del currículum vitae.
        - mensaje: Mensaje adicional del postulante.
        - captcha: Verificación de seguridad.
    """

    captcha = CaptchaField()
    class Meta:
        model = TrabajaConNosotros
        fields = ['nombre', 'correo', 'mensaje', 'area_postulacion', 'curriculum', 'captcha']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su nombre'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su correo electrónico'}),
            'mensaje': forms.Textarea(attrs={'class': 'form-control', 'rows': 6, 'placeholder': 'Ingrese su mensaje'}),
            'area_postulacion': forms.Select(choices=AREAS, attrs={'class': 'form-select'}),
            'curriculum': forms.FileInput(attrs={'class': 'form-control'}),
        }
