from django.shortcuts import render
from django.http import HttpResponse
from .models import proyecto

def freelancer_home(request):
    if request.user.user_type!='freelancer':
        return HttpResponse('You are not authorized to view this page')
    return render(request,'freelancer/freelancer_home.html',context={'user':request.user})

def cliente_home(request):
    if request.user.user_type!='cliente':
        return HttpResponse('You are not authorized to view this page')
    proyectos=proyecto.objects.filter(cliente=request.user)
    return render(request,'cliente/cliente_home.html',context={'user':request.user,'proyectos':proyectos})

def agregar_proyecto(request):
    if request.user.user_type!='cliente':
        return HttpResponse('You are not authorized to view this page')
    if request.method=='POST':
        titulo=request.POST['titulo']
        categoria=request.POST['categoria']
        descripcion=request.POST['descripcion']
        tiempo=request.POST['tiempo']
        sueldo=request.POST['sueldo']
        fecha_finalizacion=request.POST['fecha_finalizacion']
        proyecto.objects.create(titulo=titulo,categoria=categoria,descripcion=descripcion,tiempo=tiempo,sueldo=sueldo,cliente=request.user,fecha_finalizacion=fecha_finalizacion)
        return HttpResponse('Proyecto agregado exitosamente')
    return render(request,'dashboard/agregar_proyecto.html',context={'user':request.user})