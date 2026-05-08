from django import forms
from .models import Estudiante, Carrera

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombre', 'appat', 'apmat', 'matricula', 'curp', 'fotografia', 'carrera']
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre'}),
            'appat': forms.TextInput(attrs={'placeholder': 'Apellido Paterno'}),
            'apmat': forms.TextInput(attrs={'placeholder': 'Apellido Materno'}),
            'matricula': forms.NumberInput(attrs={'placeholder': 'Matrícula'}),
            'curp': forms.TextInput(attrs={'placeholder': 'CURP'}),
            'fotografia': forms.ClearableFileInput(),
        }
        labels = {
            'nombre': 'Nombre',
            'appat': 'Apellido Paterno',
            'apmat': 'Apellido Materno',
            'matricula': 'Matrícula',
            'curp': 'CURP',
            'carrera': 'Carrera',
            'fotografia': 'Fotografía',
        }

class CarreraForm(forms.ModelForm):
    class Meta:
        model = Carrera
        fields = ['nombre', 'clave', 'modalidad']
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre de la Carrera'}),
            'clave': forms.TextInput(attrs={'placeholder': 'Clave'}),
            'modalidad': forms.Select(attrs={'placeholder': 'Modalidad'}),
        }
        labels = {
            'nombre': 'Nombre',
            'clave': 'Clave',
            'modalidad': 'Modalidad',
        }