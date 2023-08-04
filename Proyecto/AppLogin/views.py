from django.shortcuts import render, redirect
from AppLogin.forms import *
from AppLogin.models import *
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic import TemplateView, ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView 
from django.contrib.auth.views import LoginView, PasswordChangeView

# Create your views here.

class Login(LoginView):
    template_name = 'AppLogin/login.html'
    fields = '__all__'
    redirect_autheticated_user = True
    success_url = reverse_lazy('Inicio')

    def get_success_url(self):
        return reverse_lazy('Inicio')
    
class Registrate(FormView):
    template_name = 'AppLogin/registrate.html'
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
    template_name= 'AppLogin/editarUsuario.html'
    success_url = reverse_lazy('Inicio')

    def get_object(self):
        return self.request.user
    
def perfil(request):
    return render(request, 'AppLogin/perfil.html')

class CambioPassword(PasswordChangeView):
    form_class = FormularioEditarContra
    template_name = 'AppLogin/editarContra.html'
    success_url = reverse_lazy('EdicionContraCorrecto')

def edicionContraCorrecto(request):
    return render(request, 'AppLogin/edicionContraCorrecto.html', {})

def inicio(request):
    return render(request, 'AppLogin/inicio.html')
