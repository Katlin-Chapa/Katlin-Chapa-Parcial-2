from .models import *
from rest_framework import serializers

class ProfesorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profesor
        fields = ['celula', 'nombres', 'apellidos', 'genero']

class MascotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mascota
        fields = ['id_mascota', 'nombre', 'raza', 'genero', 'profesor']