from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

def inicio_vista(request):
    return render(request, 'inicio.html')

class SesionVista(LoginRequiredMixin, TemplateView):
    template_name = 'sesion.html'
    login_url = reverse_lazy('login')

class AcercaVista(TemplateView):
    template_name = 'acerca.html'