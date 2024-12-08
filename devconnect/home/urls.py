from django.urls import path
from .views import freelancer_home,cliente_home,agregar_proyecto,actualizar_proyecto,eliminar_proyecto,cerrar_sesion

urlpatterns=[
    path('freelancer_home/',freelancer_home,name='freelancer_home'),
    path('cliente_home/',cliente_home,name='cliente_home'),
    path('cerrar_sesion/',cerrar_sesion,name='cerrar_sesion'),
    path('agregar_proyecto/',agregar_proyecto,name='agregar_proyecto'),
    path('actualizar_proyecto/<int:proyecto_id>',actualizar_proyecto,name='actualizar_proyecto'),
    path('eliminar_proyecto/<int:proyecto_id>',eliminar_proyecto,name='eliminar_proyecto')
]