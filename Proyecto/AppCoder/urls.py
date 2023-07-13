from django.urls import path
from AppCoder import views

urlpatterns = [
    path('', views.inicio, name="Inicio"), 
    path('curso', views.curso, name="Curso"),
    path('profesor', views.profesor, name="Profesor"),
    path('estudiante', views.estudiante, name="Estudiante"),
    path('consultaAlumno', views.consultaAlumno, name="ConsultarAlumno"),
    path('buscar/', views.buscar),
]