from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
import json
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.core.serializers import serialize
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from django.views.generic import CreateView, ListView, UpdateView, DeleteView,TemplateView
from .forms import FormularioLogin, FormularioUsuario
from .models import *

class Login(FormView):
    template_name = 'login.html'
    form_class = FormularioLogin
    success_url = reverse_lazy('inicio')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(Login, self).form_valid(form)


def logoutUsuario(request):
    logout(request)
    return HttpResponseRedirect('/login/')

class ListadoUsuario(ListView):
    model = Usuario

    def get_queryset(self):
        return self.model.objects.filter(usuario_activo=True)

    def get(self,request,*args,**kwargs):
        if request.is_ajax():
            print(self.args)
            return HttpResponse(serialize('json', self.get_queryset()), 'application/json')
        else:
            return redirect('login/inicio_usuario')

"""
class RegistrarUsuario(CreateView):
    model = Usuario
    form_class = FormularioUsuario
    template_name = 'login/crear_usuario.html'

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            form = self.form_class(request.POST)
            if form.is_valid():
                nuevo_usuario = Usuario(
                    email = form.cleaned_data.get('email'),
                    username = form.cleaned_data.get('username'),
                    nombres = form.cleaned_data.get('nombres'),
                    apellidos = form.cleaned_data.get('apellidos')
                )
                nuevo_usuario.set_password(form.cleaned_data.get('password1'))
                nuevo_usuario.save()
                mensaje = f'{self.model.__name__} registrado correctamente!'
                error = 'No hay error!'
                response = JsonResponse({'mensaje':mensaje,'error':error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se ha podido registrar!'
                error = form.errors
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 400
                return response
        else:
            return redirect('login/inicio_usuario')

def registrarUsuario(request):
    estado = False
    if request.method == 'POST':
        form = FormularioUsuario(request.POST)
        if form.is_valid():
            form.save()
            estado = True
            return redirect('inicio')
    else:
        form = FormularioUsuario()
    return render(request,'login/crear_usuario.html', {'form':form})
"""
