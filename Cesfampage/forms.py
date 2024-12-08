from django import forms
from .models import Noticia, Evento, Oirs, TrabajaConNosotros
from datetime import date
# Importa el widget CKEditor5Widget de la librería django-ckeditor-5
from django_ckeditor_5.widgets import CKEditor5Widget

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
        super(EventoForm, self).__init__(*args, **kwargs)
        self.fields['fecha_inicio'].widget.attrs['min'] = date.today().strftime('%Y-%m-%d')
        self.fields['fecha_termino'].widget.attrs['min'] = date.today().strftime('%Y-%m-%d')
        self.fields["descripcion"].required = False
        
    def clean(self):
        cleaned_data = super().clean()
        fecha_inicio = cleaned_data.get("fecha_inicio")
        fecha_termino = cleaned_data.get("fecha_termino")

        if fecha_inicio and fecha_termino and fecha_termino < fecha_inicio:
            self.add_error('fecha_termino', "La fecha de término no puede ser anterior a la fecha de inicio.")
        
        return cleaned_data

class NoticiaForm(forms.ModelForm):
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
        super().__init__(*args, **kwargs)
        self.fields["descripcion"].required = False
        
class OirsForm(forms.ModelForm):
    class Meta:
        model = Oirs
        fields = ['nombre', 'apellido', 'correo', 'motivo', 'mensaje']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su nombre'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su apellido'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su correo electrónico'}),
            'motivo': forms.Select(choices=MOTIVO, attrs={'class': 'form-select'}),
            'mensaje': forms.Textarea(attrs={'class': 'form-control', 'rows': 6, 'placeholder': 'Ingrese su mensaje'}),
        }
class TrabajaConNosotrosForm(forms.ModelForm):
    class Meta:
        model = TrabajaConNosotros
        fields = ['nombre', 'correo', 'mensaje', 'area_postulacion', 'curriculum']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su nombre'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su correo electrónico'}),
            'mensaje': forms.Textarea(attrs={'class': 'form-control', 'rows': 6, 'placeholder': 'Ingrese su mensaje'}),
            'area_postulacion': forms.Select(choices=AREAS, attrs={'class': 'form-select'}),
            'curriculum': forms.FileInput(attrs={'class': 'form-control'}),
        }
