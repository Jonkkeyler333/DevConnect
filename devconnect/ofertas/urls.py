from django.urls import path
from .views import solicitudes_freelancer,realizar_oferta,aceptar_oferta,ver_ofertas,rechazar_oferta

urlpatterns=[
    path('solicitudes_freelancer',solicitudes_freelancer,name='solicitudes_freelancer'),
    path('realizar_oferta',realizar_oferta,name='realizar_oferta'),
    path('aceptar_oferta',aceptar_oferta,name='aceptar_oferta'),
    path('ver_ofertas',ver_ofertas,name='ver_ofertas'),
    path('rechazar_oferta',rechazar_oferta,name='rechazar_oferta'),
]