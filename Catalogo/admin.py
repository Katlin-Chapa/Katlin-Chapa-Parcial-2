from django.contrib import admin
from .models import Profesor, Mascota

# Register your models here.
class ProfesorAdmin(admin.ModelAdmin):
    list_display = ['celula', 'nombres', 'apellidos', 'genero']
    search_fields = ['nombres', 'apellidos', 'celula']

class MascotaAdmin(admin.ModelAdmin):
    list_display = ['id_mascota', 'nombre', 'raza', 'genero', 'profesor']
    list_filter = ['raza', 'genero', 'profesor']
    search_fields = ['nombre', 'raza', 'profesor__nombres']

admin.site.register(Profesor, ProfesorAdmin)
admin.site.register(Mascota, MascotaAdmin)