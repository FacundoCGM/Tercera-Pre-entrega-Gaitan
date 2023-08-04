from django.shortcuts import render, redirect
from AppCoder.forms import *
from AppCoder.models import *
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic import TemplateView, ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView 
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm

# Create your views here.
def inicio(request):
    return render(request, 'AppCoder/inicio.html')

class Nuevo(LoginRequiredMixin, CreateView):
    model = NuevoBlog
    form_class = FormularioNuevoBlog
    success_url = reverse_lazy('Inicio')
    template_name = 'AppCoder/nuevo.html.'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(Nuevo, self).form_valid(form)

class Login(LoginView):
    template_name = 'AppCoder/login.html'
    fields = '__all__'
    redirect_autheticated_user = True
    success_url = reverse_lazy('Inicio')

    def get_success_url(self):
        return reverse_lazy('Inicio')

class Registrate(FormView):
    template_name = 'AppCoder/registrate.html'
    form_class = FormularioRegistrate
    redirect_autheticated_user = True
    success_url = reverse_lazy('Inicio')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(Registrate, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('Inicio')
        return super(Registrate, self).get(*args, **kwargs)
    
class EditarUsuario(UpdateView):
    form_class = FormularioEdicion
    template_name= 'AppCoder/editarUsuario.html'
    success_url = reverse_lazy('Inicio')

    def get_object(self):
        return self.request.user
    
def perfil(request):
    return render(request, 'AppCoder/perfil.html')

class CambioPassword(PasswordChangeView):
    form_class = FormularioEditarContra
    template_name = 'AppCoder/editarContra.html'
    success_url = reverse_lazy('EdicionContraCorrecto')

def edicionContraCorrecto(request):
    return render(request, 'AppCoder/edicionContraCorrecto.html', {})



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


