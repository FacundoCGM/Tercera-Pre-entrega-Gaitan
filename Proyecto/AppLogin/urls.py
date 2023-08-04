from django.urls import path
from AppCoder import views
from django.contrib.auth.views import LogoutView
from . import views
from AppLogin.views import *

urlpatterns = [
    path('', views.inicio, name="Inicio"), 
    path('login', Login.as_view(), name="Login"),
    path('registrate', Registrate.as_view(), name="Registrate"),
    path('logout', LogoutView.as_view(template_name='AppLogin/logout.html'), name='Logout'),
    path('editarUsuario', EditarUsuario.as_view(), name='EditarUsuario'),
    path('perfil', views.perfil, name="Perfil"),
    path('editarContra', CambioPassword.as_view(), name='EditarContra'),
    path('edicionContraCorrecto' , views.edicionContraCorrecto, name='EdicionContraCorrecto'),
]