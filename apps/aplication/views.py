from django.shortcuts import render, redirect
from .models import *
from .forms import ProductoForm, PedidoForm
from django.views.generic import View, TemplateView, ListView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from django.template import RequestContext

class Inicio(TemplateView):
	template_name = 'index.html'
"""
def home(request):
	return render(request, 'index.html')
"""
def carritoIndex(request):
	pedido = Pedido.objects.count()
	return render(request, 'index.html', pedido)

def crearProd(request):
	if request.method == 'POST':
		form = ProductoForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('/listar_prod')
		else:
			print('NO')
	else:
		form = ProductoForm()
	return render(request, 'aplication/crear_prod.html', {'form':form})

"""class CrearProd(SuccessMessageMixin, CreateView):
	model = Prod
	form_class = ProductoForm
	template_name = 'aplication/crear_prod.html'
	succes_url = reverse_lazy('/aplication/listar_prod.html')"""

def listarProd(request):
	prod = Producto.objects.all()
	context = {'prod':prod}
	return render(request, 'aplication/listar_prod.html', context)

def listarPedido(request):
	pedido = Pedido.objects.all()
	context = {'pedido':pedido}
	return render(request, 'pedidos/listar_pedidos.html', context)

def catalProd(request):
	prod = Producto.objects.all()
	context = {'prod':prod}
	return render(request, 'aplication/catal_prod.html', context)

def editarProd(request, id):
	prod = Producto.objects.get(id = id)
	if request.method == 'GET':
		form = ProductoForm(instance = prod)
	else:
		form = ProductoForm(request.POST, request.FILES, instance = prod)
		print(form)
		if form.is_valid():
			form.save()
		return redirect('/listar_prod')
	return render(request, 'aplication/editar_prod.html', {'form':form, 'prod':prod})

def detalleProd(request, id):
	prod = Producto.objects.get(id = id)
	if request.method == 'POST':
		form = PedidoForm(request.POST)
		print(form)
		if form.is_valid():
			form.save()
			return redirect('/catal_prod')
	else:
		form = PedidoForm()
	return render(request, 'aplication/detalle_prod.html', {'form':form, 'prod':prod})

def eliminarProd(request, id):
	prod = Producto.objects.get(id = id)
	if request.method == 'POST':
		prod.delete()
		return redirect('/listar_prod')
	return render(request, 'aplication/eliminar_prod.html', {'prod':prod})
