from django import forms
from .models import proyecto

class proyecto_form(forms.ModelForm):
    class Meta:
        model=proyecto
        fields=['titulo','categoria','descripcion','tiempo','sueldo','fecha_finalizacion']