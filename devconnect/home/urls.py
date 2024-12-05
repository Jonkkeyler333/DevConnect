from django.urls import path
from .views import freelancer_home

urlpatterns=[
    path('freelancer_home/',freelancer_home,name='freelancer_home'),
]