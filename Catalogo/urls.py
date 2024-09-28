from django.urls import path
from .views import *

urlpatterns = [
    path('profesores/', ProfesorListView.as_view(), name='profesor_list'),
    path('profesores/nuevo/', ProfesorCreateView.as_view(), name='profesor_create'),
    path('profesores/<int:pk>/', ProfesorUpdateView.as_view(), name='profesor_update'),
    path('profesores/<int:pk>/eliminar/', ProfesorDeleteView.as_view(), name='profesor_delete'),
    path('mascotas/', MascotaListView.as_view(), name='mascota_list'),
    path('mascotas/nuevo/', MascotaCreateView.as_view(), name='mascota_create'),
    path('mascotas/<int:pk>/', MascotaUpdateView.as_view(), name='mascota_update'),
    path('mascotas/<int:pk>/eliminar/', MascotaDeleteView.as_view(), name='mascota_delete'),
]
