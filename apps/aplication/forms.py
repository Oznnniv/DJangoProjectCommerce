from django import forms
from apps.aplication.models import *
from apps.login.models import Usuario

class ProductoForm(forms.ModelForm):
	class Meta:
		model = Producto
		fields = [
			'name',
			'desc',
			'types',
			'cost',
			'stock',
			'img',
			#'cliente',
		]
		labels = {
			'name': 'Nombre',
			'desc': 'Descripción',
			'types': 'Tipo',
			'cost': 'Costo',
			'stock': 'Cantidad',
			'img': 'Imagen',
		}
		widgets = {
			'name': forms.TextInput(
				attrs = {
					'class':'form-control',
					'placeholder':'Ingresa el nombre del producto',
					'id': 'name'
				}
			),
			'desc': forms.TextInput(
				attrs = {
					'class':'form-control',
					'placeholder':'Ingresa una descripción del producto',
					'id': 'desc'
				}
			),
			'types': forms.TextInput(
				attrs = {
					'class':'form-control',
					'placeholder':'Ingresa el tipo de producto',
					'id': 'types'
				}
			),
			'cost': forms.TextInput(
				attrs = {
					'class':'form-control',
					'placeholder':'Ingresa el costo del producto',
					'id': 'cost'
				}
			),
			'stock': forms.TextInput(
				attrs = {
					'class':'form-control',
					'placeholder':'Ingresa la cantidad disponible del producto',
					'id': 'stock'
				}
			),
        }

class PedidoForm(forms.ModelForm):
	class Meta:
		model = Pedido
		fields = [
			#'ordered',
			'quantity',
			#'fecha',
			#'desc',
			'producto',
		]
		labels = {
			#'ordered': 'Orden',
			'quantity': 'Cantidad',
			#'desc': 'Descripción',
			'producto': 'Producto',
		}
		widgets = {
			'quantity': forms.NumberInput(
				attrs = {
					'id': 'stock',
					'value': '1',
					'min': '1',
					'max': '999'
				}
			),
		}
