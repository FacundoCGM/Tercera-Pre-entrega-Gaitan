from django.urls import path
from AppCoder import views
from django.contrib.auth.views import LogoutView
from . import views
from AppCoder.views import *

urlpatterns = [
    path('', views.inicio, name="Inicio"), 
    path('login', Login.as_view(), name="Login"),
    path('registrate', Registrate.as_view(), name="Registrate"),
    path('logout', LogoutView.as_view(template_name='AppCoder/logout.html'), name='Logout'),
    path('editarUsuario', EditarUsuario.as_view(), name='EditarUsuario'),
    path('perfil', views.perfil, name="Perfil"),
    path('editarContra', CambioPassword.as_view(), name='EditarContra'),
    path('edicionContraCorrecto' , views.edicionContraCorrecto, name='EdicionContraCorrecto'),

    path('blogs', Blogs.as_view(), name="Blogs"),
    path('nuevo', Nuevo.as_view(), name="Nuevo"),
    path('blogDatos/<int:pk>/', BlogDatos.as_view(), name='blog'),
    path('blogActualizar/<int:pk>/', BlogActualizar.as_view(), name='blogActualizar'),
    path('blogBorrar/<int:pk>/', BlogBorrar.as_view(), name='blogBorrar'),

    path('aboutMe', views.aboutMe, name="AboutMe"), 



]