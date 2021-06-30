"""crud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from apps.login.views import Login, logoutUsuario, login
from apps.aplication.views import Inicio
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    #url('aplication/', include('apps.aplication.urls')),
    #path('usuarios/',include('apps.login.urls')),
    # path('usuarios/', include('apps.login.urls')),
    path('', include('apps.aplication.urls')),
    #path('usuarios/',include(('apps.libros.urls','usuarios'))),
    path('', login_required(Inicio.as_view()), name = 'inicio'),
    path('login/', Login.as_view(), name = 'login'),
    #path('accounts/login/', Login.as_view(), name = 'login'),
    #path('accounts/registrar_usuario/', registrarUsuario, name = 'registrar_usuario'),
    path('logout/', logoutUsuario, name = 'logout')
]
if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
