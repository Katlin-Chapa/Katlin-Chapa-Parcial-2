from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Profesor, Mascota
from .forms import ProfesorForm, MascotaForm
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import ProfesorSerializer, MascotaSerializer
from django.core.paginator import Paginator

# Create your views here.

# Profesores
class ProfesorListView(LoginRequiredMixin, ListView):
    model = Profesor
    template_name = 'profesor/profesor_list.html'
    context_object_name = 'profesores'
    login_url = reverse_lazy('login')
    permission_required = 'Catalogo.view_profesor'

    def get_queryset(self):
        queryset = super().get_queryset().order_by('nombres')
        search_query = self.request.GET.get('search')
        if search_query:
            queryset = queryset.filter(nombres__icontains=search_query)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['can_add'] = self.request.user.has_perm('Catalogo.add_profesor')
        context['can_change'] = self.request.user.has_perm('Catalogo.change_profesor')
        context['can_delete'] = self.request.user.has_perm('Catalogo.delete_profesor')

        # Paginación
        paginator = Paginator(context['profesores'], 5)  
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['page_obj'] = page_obj
        
        # Total de páginas
        context['total_pages'] = paginator.num_pages
        return context
    
class ProfesorCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Profesor
    form_class = ProfesorForm
    template_name = 'profesor/profesor_form.html'
    success_url = reverse_lazy('profesor_list')
    login_url = reverse_lazy('login')
    permission_required = 'Catalogo.add_profesor'

class ProfesorUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Profesor
    form_class = ProfesorForm
    template_name = 'profesor/profesor_form.html'
    success_url = reverse_lazy('profesor_list')
    login_url = reverse_lazy('login')
    permission_required = 'Catalogo.change_profesor'

class ProfesorDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Profesor
    template_name = 'profesor/profesor_delete.html'
    success_url = reverse_lazy('profesor_list')
    login_url = reverse_lazy('login')
    permission_required = 'Catalogo.delete_profesor'

class ProfesorViewSet(viewsets.ModelViewSet):
    queryset = Profesor.objects.all()
    serializer_class = ProfesorSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

# Mascotas
class MascotaListView(LoginRequiredMixin, ListView):
    model = Mascota
    template_name = 'mascota/mascota_list.html'
    context_object_name = 'mascotas'
    login_url = reverse_lazy('login')
    permission_required = 'Catalogo.view_mascota'

    def get_queryset(self):
        queryset = super().get_queryset().order_by('profesor')
        search_query = self.request.GET.get('search')
        pais_id = self.request.GET.get('profesor')

        if search_query:
            queryset = queryset.filter(nombre__icontains=search_query)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profesor'] = Profesor.objects.all()
        context['can_add'] = self.request.user.has_perm('Catalogo.add_mascota')
        context['can_change'] = self.request.user.has_perm('Catalogo.change_mascota')
        context['can_delete'] = self.request.user.has_perm('Catalogo.delete_mascota')

        # Paginación
        paginator = Paginator(context['mascotas'], 5)  
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['page_obj'] = page_obj
        
        # Total de páginas
        context['total_pages'] = paginator.num_pages
        return context
    
class MascotaViewSet(viewsets.ModelViewSet):
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

class MascotaCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Mascota
    form_class = MascotaForm
    template_name = 'mascota/mascota_form.html'
    success_url = reverse_lazy('mascota_list')
    login_url = reverse_lazy('login')
    permission_required = 'Catalogo.add_mascota'

class MascotaUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Mascota
    form_class = MascotaForm
    template_name = 'mascota/mascota_form.html'
    success_url = reverse_lazy('mascota_list')
    login_url = reverse_lazy('login')
    permission_required = 'Catalogo.change_mascota'

class MascotaDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Mascota
    template_name = 'mascota/mascota_delete.html'
    success_url = reverse_lazy('mascota_list')
    login_url = reverse_lazy('login')
    permission_required = 'Catalogo.delete_mascota'
