from django import forms
from django.contrib.auth.models import User
from AppCoder.models import *

class FormularioNuevoBlog(forms.ModelForm):
    class Meta:
        model = NuevoBlog
        fields = ('usuario', 'titulo', 'tematica', 'texto', 'emailContacto', 'imagenBlog')

        widgets = {
            'usuario': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id':'usuario_id', 'type':'hidden'}),
            'titulo' : forms.TextInput(attrs={'class': 'form-control'}),
            'tematica' : forms.Select(attrs={'class': 'form-control'}),
            'texto' : forms.Textarea(attrs={'class': 'form-control'}),
            'emailContacto' : forms.TextInput(attrs={'class': 'form-control'}),
        }

class ActualizarBlog(forms.ModelForm):
    class Meta:
        model = NuevoBlog
        fields = ('titulo', 'tematica', 'texto', 'emailContacto', 'imagenBlog')


        widgets = {
            'titulo' : forms.TextInput(attrs={'class': 'form-control'}),
            'tematica' : forms.Select(attrs={'class': 'form-control'}),
            'texto' : forms.Textarea(attrs={'class': 'form-control'}),
            'emailContacto' : forms.TextInput(attrs={'class': 'form-control'}),
        }


