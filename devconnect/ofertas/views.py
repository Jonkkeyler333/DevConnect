from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import oferta
from django.contrib import messages

def solicitudes_freelancer(request):
    if request.user.user_type!='freelancer':
        return HttpResponse('You are not authorized to view this page')
    solicitudes=oferta.objects.filter(freelancer=request.user)
    return render(request,'freelancer/solicitudes_freelancer.html',context={'solicitudes':solicitudes})

def realizar_oferta(request):
    if request.user.user_type!='freelancer':
        return HttpResponse('You are not authorized to view this page')
    if request.method=='POST':
        proyecto_id=request.POST.get('proyecto_id')
        if oferta.objects.filter(proyecto_id=proyecto_id, freelancer=request.user).exists():
            messages.error(request, 'Ya has realizado una solicitud para este proyecto.')
            return redirect('freelancer_home')
        oferta_obj=oferta.objects.create(proyecto_id=proyecto_id,freelancer=request.user,estado='en espera')
        return redirect('freelancer_home')
    else:
        return HttpResponse('Invalid request')
    
def aceptar_oferta(request):
    if request.user.user_type!='cliente':
        return HttpResponse('You are not authorized to view this page')
    oferta_id=request.POST.get('oferta_id')
    oferta_obj=get_object_or_404(oferta,id=oferta_id)
    oferta_obj.estado='aceptada'
    oferta_obj.proyecto.estado='en progreso'
    oferta_obj.proyecto.freelancer_asignado=oferta_obj.freelancer
    oferta_obj.proyecto.save()
    oferta_obj.save()
    return redirect('cliente_home')

def ver_ofertas(request):
    if request.user.user_type!='cliente':
        return HttpResponse('You are not authorized to view this page')
    proyecto_id=request.POST.get('proyecto_id')
    ofertas=oferta.objects.filter(proyecto_id=proyecto_id)
    return render(request,'cliente/ver_ofertas.html',context={'ofertas':ofertas})

def rechazar_oferta(request):
    if request.user.user_type!='cliente':
        return HttpResponse('You are not authorized to view this page')
    oferta_id=request.POST.get('oferta_id')
    oferta_obj=get_object_or_404(oferta,id=oferta_id)
    oferta_obj.delete()
    return redirect('cliente_home')