from django.urls import path
from .views import freelancer_home,cliente_home

urlpatterns=[
    path('freelancer_home/',freelancer_home,name='freelancer_home'),
    path('cliente_home/',cliente_home,name='cliente_home'),
]