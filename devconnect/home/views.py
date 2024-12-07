from django.shortcuts import render
from django.http import HttpResponse
from .models import proyecto
from .forms import proyecto_form
from django.shortcuts import redirect

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
        formulario=proyecto_form(request.POST)
        if formulario.is_valid():
            proyecto_obj=formulario.save(commit=False)
            proyecto_obj.cliente=request.user
            proyecto_obj.save()
            return redirect('cliente_home')
    else:
        formulario=proyecto_form()
    return render(request,'cliente/agregar_proyecto.html',context={'form':formulario})