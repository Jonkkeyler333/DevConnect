from django.http import HttpResponse
from .models import proyecto
from .forms import proyecto_form
from django.contrib.auth import logout
from django.shortcuts import redirect,render,get_object_or_404
import datetime

def freelancer_home(request):
    if request.user.user_type!='freelancer':
        return HttpResponse('You are not authorized to view this page')
    return render(request,'freelancer/freelancer_home.html',context={'user':request.user})

def cliente_home(request):
    if request.user.user_type!='cliente':
        return HttpResponse('You are not authorized to view this page')
    current_hour = datetime.datetime.now().hour
    if 5<=current_hour<12:
        saludo="Buenos días"
    elif 12<=current_hour<18:
        saludo="Buenas tardes"
    else:
        saludo="Buenas noches"
    proyectos=proyecto.objects.filter(cliente=request.user)
    return render(request,'cliente/cliente_home.html',context={'user':request.user,'proyectos':proyectos,'saludo':saludo})

def cerrar_sesion(request):
    logout(request)
    return redirect('home')

def agregar_proyecto(request):
    if request.user.user_type!='cliente':
        return HttpResponse('You are not authorized to view this page')
    if request.method=='POST':
        formulario=proyecto_form(request.POST)
        if formulario.is_valid():
            proyecto_obj=formulario.save(commit=False)
            proyecto_obj.cliente=request.user
            proyecto_obj.save()
            return redirect('cliente_home')
    else:
        formulario=proyecto_form()
    return render(request,'cliente/agregar_proyecto.html',context={'form':formulario})

def actualizar_proyecto(request,proyecto_id):
    proyecto_obj=get_object_or_404(proyecto,id=proyecto_id,cliente=request.user)
    if request.method=='POST':
        formulario=proyecto_form(request.POST,instance=proyecto_obj)
        if formulario.is_valid():
            formulario.save()
            return redirect('cliente_home')
    else:
        formulario=proyecto_form(instance=proyecto_obj)
    context={'proyecto':proyecto_obj,'form':formulario}
    return render(request,'cliente/actualizar_proyecto.html',context)

def eliminar_proyecto(request,proyecto_id):
    proyecto_obj=get_object_or_404(proyecto,id=proyecto_id,cliente=request.user)
    if request.method=='POST':
        proyecto_obj.delete()
        return redirect('cliente_home')
    return render(request,'cliente/eliminar_proyecto.html',context={'proyecto':proyecto_obj})