from django import forms

class formularioCurso(forms.Form):
    nombre = forms.CharField()
    camada = forms.IntegerField()

class formularioEstudiante(forms.Form):
    nombre= forms.CharField()
    apellido= forms.CharField()
    email= forms.EmailField()

class formularioProfesor(forms.Form):
    nombre= forms.CharField()
    apellido= forms.CharField()
    email= forms.EmailField()
    profesion= forms.CharField()