from django.db import models

# Create your models here.
class Profesor(models.Model):
    GENERO_CHOICES = [
        ('F', 'Femenino'),
        ('M', 'Masculino'),
    ]
    celula = models.CharField(max_length=20, primary_key=True)  
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    genero = models.CharField(max_length=1, choices=GENERO_CHOICES)  

    class Meta:
        verbose_name = 'Profesor'
        verbose_name_plural = 'Profesores'

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"


class Mascota(models.Model):
    id_mascota = models.AutoField(primary_key=True) 
    nombre = models.CharField(max_length=50)
    raza = models.CharField(max_length=50)
    genero = models.CharField(max_length=10)  
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)  

    class Meta:
        verbose_name = 'Mascota'
        verbose_name_plural = 'Mascotas'

    def __str__(self):
        return self.nombre