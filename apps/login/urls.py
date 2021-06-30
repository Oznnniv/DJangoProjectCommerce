from django.urls import path
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from apps.login.views import ListadoUsuario

urlpatterns = [
    path('listado_usuarios/', login_required(ListadoUsuario.as_view()),{'parametro_extra': 'Hola!'}, name = 'listar_usuarios'),

]

#URLS DE VISTAS IMPLICITAS
urlpatterns += [
    path('inicio_usuarios/', login_required(
        TemplateView.as_view(
            template_name='login/listar_usuario.html'
        )
    ), name='inicio_usuario'),
]