from django.db import models

class oferta(models.Model):
    proyecto=models.ForeignKey('home.proyecto',on_delete=models.CASCADE)
    freelancer=models.ForeignKey('usuarios.User',on_delete=models.CASCADE)
    fecha_oferta=models.DateTimeField(auto_now_add=True)
    estado=models.CharField(max_length=100,choices=(('aceptada','aceptada'),('rechazada','rechazada'),('en espera','en espera')))