#from django.conf.urls import url
from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
	path('crear_prod/', login_required(crearProd), name = "crear_prod"),
	path('listar_prod/', login_required(listarProd), name = "listar_prod"),
	path('catal_prod/', catalProd, name = "catal_prod"),
	path('editar_prod/<id>/', login_required(editarProd), name = "editar_prod"),
	path('eliminar_prod/<id>/', login_required(eliminarProd), name = "eliminar_prod"),
	path('detalle_prod/<id>/', detalleProd, name = "detalle_prod"),

	path('listar_pedidos/', login_required(listarPedido), name = "listar_pedidos"),
]
"""urlpatterns = [
	url(r'^$', home, name = "index"),
	url(r'^crear_flor/', crearFlor, name = "crear_flor"),
]"""
