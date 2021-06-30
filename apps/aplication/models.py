from django.db import models

# Create your models here.

"""class Cliente(models.Model):
	id = models.AutoField(primary_key = True)
	name = models.CharField(max_length = 200)
	lastn = models.CharField(max_length = 255)
	email  = models.EmailField(max_length = 255)
	number = models.IntegerField()"""

class Producto(models.Model):
	id = models.AutoField(primary_key = True)
	name = models.CharField(max_length = 200)
	desc = models.CharField(max_length = 255)
	types = models.CharField(max_length = 100)
	cost  = models.IntegerField()
	stock = models.IntegerField()
	#img = models.FileField(upload_to = 'images/')
	img = models.FileField(upload_to = 'images/')

	#Cliente = models.ForeignKey(Cliente, on_delete = models.CASCADE)
"""
class Pedido(models.Model):
	id = models.AutoField(primary_key = True)
	fecha = models.DateTimeField(auto_now = True, auto_now_add = False)
	desc = models.CharField(max_length = 255)
	order = models.ManyToManyField(PedidoProducto)
"""
class Pedido(models.Model):
	id = models.AutoField(primary_key = True)
	#ordered = models.BooleanField(default = True)
	quantity = models.IntegerField(default = 1)
	fecha = models.DateTimeField(auto_now = True, auto_now_add = False)
	#desc = models.CharField(max_length = 255)
	producto = models.ForeignKey(Producto, on_delete = models.CASCADE, default = True)
