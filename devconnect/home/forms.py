from django import forms
from .models import proyecto

class proyecto_form(forms.ModelForm):
    class Meta:
        model = proyecto
        fields = ['titulo', 'categoria', 'descripcion', 'tiempo', 'sueldo', 'fecha_finalizacion']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el título'}),
            'categoria': forms.Select(attrs={'class': 'form-select'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Describa el proyecto'}),
            'tiempo': forms.Select(attrs={'class': 'form-select'}),
            'sueldo': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el sueldo'}),
            'fecha_finalizacion': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
