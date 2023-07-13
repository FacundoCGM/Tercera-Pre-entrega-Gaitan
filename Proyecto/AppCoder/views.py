from django.shortcuts import render
from AppCoder.forms import *
from AppCoder.models import *

# Create your views here.
def inicio(request):
    return render(request, 'AppCoder/inicio.html')


def curso(request):

    if request.method == "POST":
        miFormulario = formularioCurso(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            curso = Curso(nombre = informacion['nombre'], camada = informacion['camada'])
            curso.save()
            return render(request, "AppCoder/inicio.html")
        
    else: 
        miFormulario = formularioCurso()

    return render(request, "AppCoder/curso.html", {"miFormulario": miFormulario})

def estudiante(request):

    if request.method == "POST":
        miFormulario = formularioEstudiante(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            estudiante = Estudiante(nombre = informacion['nombre'], apellido = informacion['apellido'], email = informacion['email'])
            estudiante.save()
            return render(request, "AppCoder/inicio.html")
        
    else: 
        miFormulario = formularioEstudiante()

    return render(request, "AppCoder/estudiante.html", {"miFormulario": miFormulario})

def profesor(request):

    if request.method == "POST":
        miFormulario = formularioProfesor(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            profesor = Profesor(nombre = informacion['nombre'], apellido = informacion['apellido'], email = informacion['email'], profesion = informacion['profesion'])
            profesor.save()
            return render(request, "AppCoder/inicio.html")
        
    else: 
        miFormulario = formularioProfesor()

    return render(request, "AppCoder/profesor.html", {"miFormulario": miFormulario})

def consultaAlumno(request):
    return render(request, 'AppCoder/consultaAlumno.html')

def buscar(request):
    if request.GET['apellido']:

        apellido = request.GET['apellido']    
        estudiantes = Estudiante.objects.filter(apellido__icontains = apellido)

        return render(request, 'AppCoder/inicio.html', {'nombre':estudiantes, 'apellido':apellido})
    
    else:
        respuesta = 'No enviaste datos.'

    return render(request, 'AppCoder/inicio.html', {'respuesta': respuesta})
