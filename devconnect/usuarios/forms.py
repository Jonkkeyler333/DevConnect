from django import forms
from .models import User


class RegisterForm(forms.ModelForm):
    USER_TYPE_CHOICES = [
        ('freelancer','Freelancer'),
        ('cliente','Cliente'),
    ]
    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES,widget=forms.Select(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=['first_name','last_name','email','password','user_type']
        widgets={
            'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre'}),
            'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Apellido'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}),
            'password':forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Contraseña'}),
            'profile_description':forms.TextInput(attrs={'class':'form-control','placeholder':'Descripcion de tu perfil'}),
            'profile_imag':forms.URLField(attrs={'class':'form-control','placeholder':'imagen_url'}),
        }
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}))