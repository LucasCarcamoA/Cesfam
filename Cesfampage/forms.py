from django import forms
from .models import Noticia, Evento
from datetime import date

TIPO_EVENTO = [
    ('Evento', 'Evento'),
    ('Taller', 'Taller'),
    ('Campaña', 'Campaña'),
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
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Ingrese la descripción del evento'}),
            'tipo_evento': forms.Select(choices=TIPO_EVENTO, attrs={'class': 'form-select'}),
        }
    
    def __init__(self, *args, **kwargs):
        super(EventoForm, self).__init__(*args, **kwargs)
        self.fields['fecha_inicio'].widget.attrs['min'] = date.today().strftime('%Y-%m-%d')
        self.fields['fecha_termino'].widget.attrs['min'] = date.today().strftime('%Y-%m-%d')

class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ['titulo', 'imagen', 'descripcion', 'evento_relacionado']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el título de la noticia'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Ingrese la descripción de la noticia'}),
            'evento_relacionado': forms.Select(attrs={'class': 'form-select'})
        }