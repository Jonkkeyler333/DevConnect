from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import RegisterForm,LoginForm
from django.http import HttpResponse

def register_view(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('login')
            return HttpResponse('Hola puto')
    else:
        form=RegisterForm()
    return render(request,'users/register.html',{'form':form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data.get('email')
            password=form.cleaned_data.get('password')
            user=authenticate(request,username=email,password=password)
            if user is not None:
                login(request,user)
                # return HttpResponse(f'Hola {request.user.first_name}')
                if user.user_type=='freelancer':
                    return redirect('freelancer_home')
                else:
                    return redirect('cliente_home')
            else:
                form.add_error(None,'Email o contraseña incorrectos')
    else:
        form=LoginForm()
    return render(request,'users/login.html',{'form': form})

def home_view(request):
    return render(request,'home_page/home_page.html')