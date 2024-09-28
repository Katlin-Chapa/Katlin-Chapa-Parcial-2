from django import forms
from .models import Profesor, Mascota

class ProfesorForm(forms.ModelForm):
    GENERO_CHOICES = [
        ('F', 'Femenino'),
        ('M', 'Masculino'),
    ]
    
    genero = forms.ChoiceField(choices=GENERO_CHOICES, widget=forms.Select, label="Género")
    
    class Meta:
        model = Profesor
        fields = ['nombres', 'apellidos', 'celula', 'genero'] 

class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = '__all__'