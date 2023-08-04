from django.urls import path
from AppCoder import views
from django.contrib.auth.views import LogoutView
from . import views
from AppCoder.views import *

urlpatterns = [

    path('blogs', Blogs.as_view(), name="Blogs"),
    path('nuevo', Nuevo.as_view(), name="Nuevo"),
    path('blogDatos/<int:pk>/', BlogDatos.as_view(), name='blog'),
    path('blogActualizar/<int:pk>/', BlogActualizar.as_view(), name='blogActualizar'),
    path('blogBorrar/<int:pk>/', BlogBorrar.as_view(), name='blogBorrar'),

    path('aboutMe', views.aboutMe, name="AboutMe"), 



]