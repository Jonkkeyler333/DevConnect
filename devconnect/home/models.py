from django.db import models
from usuarios.models import User

class proyecto(models.Model):
    titulo=models.CharField(max_length=100)
    categoria=models.CharField(max_length=100,choices=(('web','web'),('movil','movil'),('escritorio','escritorio'),('data science','data science'),('machine learning','machine learning'),('otros','otros')))
    descripcion=models.TextField()
    tiempo=models.CharField(max_length=100,choices=(('1 semana','1 semana'),('2 semanas','2 semanas'),('3 semanas','3 semanas'),('1 mes','1 mes'),('2 meses','2 meses'),('3 meses','3 meses'),('mas de 3 meses','mas de 3 meses'),('obra labor','obra labor')))
    sueldo=models.PositiveIntegerField()
    cliente=models.ForeignKey(User,on_delete=models.CASCADE)
    fecha_creacion=models.DateTimeField(auto_now_add=True)
    fecha_finalizacion=models.DateTimeField()
    freelancer_asignado=models.ForeignKey(User,on_delete=models.CASCADE,related_name='freelancer_asignado',null=True,blank=True)
    estado=models.CharField(max_length=100,choices=(('en espera','en espera'),('en progreso','en progreso'),('finalizado','finalizado')))
    def __str__(self):
        return self.titulo+' '+self.cliente.username+' '+self.estado