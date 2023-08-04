from django.shortcuts import render, redirect
from AppCoder.forms import *
from AppCoder.models import *
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic import TemplateView, ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView 

# Create your views here.

class Nuevo(LoginRequiredMixin, CreateView):
    model = NuevoBlog
    form_class = FormularioNuevoBlog
    success_url = reverse_lazy('Inicio')
    template_name = 'AppCoder/nuevo.html.'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(Nuevo, self).form_valid(form)

class Blogs(ListView):
    context_object_name = 'blogs'
    queryset = NuevoBlog.objects.all()
    template_name = 'AppCoder/blogs.html'

class BlogDatos(LoginRequiredMixin, DetailView):
    model = NuevoBlog
    context_object_name = 'blog'
    template_name = 'AppCoder/blogDatos.html'

class BlogActualizar(LoginRequiredMixin, UpdateView):
    model = NuevoBlog
    form_class = ActualizarBlog
    success_url = reverse_lazy('Blogs')
    context_object_name = 'blog'
    template_name = 'AppCoder/blogActualizar.html'

class BlogBorrar(LoginRequiredMixin, DeleteView):
    model = NuevoBlog
    success_url = reverse_lazy('Blogs')
    context_object_name = 'blog'
    template_name = 'AppCoder/blogBorrar.html'

def aboutMe(request):
    return render(request, 'AppCoder/aboutMe.html')


