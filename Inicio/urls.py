from django.urls import path
from .views import inicio_vista, SesionVista, AcercaVista

urlpatterns = [
    path('', inicio_vista, name='inicio'),  
    path('sesion/', SesionVista.as_view(), name='sesion'),  
    path('acerca/', AcercaVista.as_view(), name='acerca'),
]