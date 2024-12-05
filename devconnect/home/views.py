from django.shortcuts import render
from django.http import HttpResponse

def freelancer_home(request):
    if request.user.user_type!='freelancer':
        return HttpResponse('You are not authorized to view this page')
    return render(request,'dashboard/freelancer_home.html',context={'user':request.user})
