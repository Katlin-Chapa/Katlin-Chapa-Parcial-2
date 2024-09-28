from django.urls import path
from .views import LoginVista, LoginPersonalizado
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', LoginVista.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('api/login/', LoginPersonalizado.as_view(), name='custom_login'),
]
