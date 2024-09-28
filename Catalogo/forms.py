from django import forms
from .models import Profesor, Mascota

class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = '__all__'

class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = '__all__'